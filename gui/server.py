from flask import Flask, request, render_template
import pdb
import os
import queue
import threading
import json
import worker
import shutil

app = Flask(__name__, static_url_path='')

gameLookup = {}
gameStartQueue = queue.Queue()
gameActiveQueue = queue.Queue()
lock = threading.Lock()

@app.route('/')
def root():
	return app.send_static_file('index.html')

@app.route('/start', methods = ['POST'])
def start_game():
	game = request.form["gameName"]
	returnForm = ""
	with lock:
		if(game in gameLookup):
			if(len(gameLookup[game][1])==2):
				if(not gameLookup[game][0]):
					gameLookup[game][0] = True
					gameStartQueue.put((game, gameLookup[game][1]))
					returnForm = root()
				else:
					returnForm = "Game already started"
			else:
				returnForm = "Not enough players to start."
		else:
			returnForm = "Game does not exist"
	return returnForm

@app.route('/config', methods = ['POST'])
def upload_config():
	game = request.form['gameName']
	config = request.files.get('file')
	if("numGames" in request.form):
		nums = request.form["numGames"]
	else:
		nums = None
	pathDir = "./games/%s/" % game
	pathFile = pathDir + "config.json"
	pathNums = pathDir + "num_runs.txt"

	resp = ""

	with lock:
		if(not(game in gameLookup and gameLookup[game][0])):
			if(not os.path.isdir(pathDir)):
				os.mkdir(pathDir)
				gameLookup[game] = [False, []]
			if(config):
				config.save(pathFile)
			if(nums):
				with open(pathNums, "w") as fp:
					json.dump(nums, fp)
				
			resp = root()
		else:
			resp = "Game already Running"	

	return resp
		

@app.route('/upload', methods = ['POST'])
def upload_file():
	zipFile = request.files.get('file')
	team = request.form['teamName']
	game = request.form['gameName']
	
	responseForm = ""
	
	with lock:
		if(game in gameLookup and len(gameLookup[game][1]) == 2):
			responseForm =  "Game Already Begun."
		else:
			over_dir = "./games/%s" % (game)
			if(not os.path.isdir(over_dir)):
				os.mkdir(over_dir)
				gameLookup[game] = [False, []]
	
			over_dir = over_dir + "/%s" % (team)	
			if(not os.path.isdir(over_dir)):
				os.mkdir(over_dir)
				gameLookup[game][1].append(team)
				
			zipFile.save(over_dir + "/upload.zip")
	
			responseForm = root()

	return responseForm
	
def main():
  shutil.rmtree("./games", ignore_errors=True)
  os.mkdir("./games")

	tTargets = [worker.startMonopoly, worker.activeMonopoly]
	tArgs = [(gameStartQueue, gameActiveQueue), (gameActiveQueue, None)]
	for target, args in zip(tTargets, tArgs):
		thread = threading.Thread(target=target, args=args)
		thread.start()
	app.run()

if __name__ == '__main__':
	main()
