from flask import Flask, request, render_template
import pdb
import os
import queue
import threading
import worker

app = Flask(__name__, static_url_path='')

gameLookup = {}
gameStartQueue = queue.Queue()
gameActiveQueue = queue.Queue()

@app.route('/')
def root():
	return app.send_static_file('index.html')

@app.route('/upload', methods = ['POST'])
def upload_file():
	zipFile = request.files.get('file')
	team = request.form['teamName']
	game = request.form['gameName']
	
	if(game in gameLookup and len(gameLookup[game]) == 2):
		return "Game Already Begun."
	else:
		over_dir = "./games/%s" % (game)
		if(not os.path.isdir(over_dir)):
			os.mkdir(over_dir)
			gameLookup[game] = []

		over_dir = over_dir + "/%s" % (team)	
		if(not os.path.isdir(over_dir)):
			os.mkdir(over_dir)
			gameLookup[game].append(team)
			
		zipFile.save(over_dir + "/upload.zip")

		if(len(gameLookup[game]) == 2):
			print("Game Ready")
			gameStartQueue.put((game, gameLookup[game]))

	return root()
	
def main():
	sThread = threading.Thread(target=worker.startMonopoly, args = (gameStartQueue, gameActiveQueue))
	sThread.start()
	gameStartQueue.put(('asdf', ['asdf', '124124']))
	app.run()

if __name__ == '__main__':
	main()
