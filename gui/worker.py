import os
import sys
import zipfile
import importlib.util
import pdb
#import Adjudicator

# A function which resolves the relative directory of a team within a game
def genDirPath(game, team):
	return "./games/%s/%s/" % (game, team)

# A function which resolves the uploaded zipfile for a specific team in a game
def genZipPath(game, team):
	return genDirPath(game, team) + "/upload.zip"

# A function which resolves the agent file for a specific team in a game
def genBotPath(game, team):
	return genDirPath(game, team) + "/agent.py"

# A worker thread which unzips team files and extracts their agent classes
def startMonopoly(startQueue, activeQueue):
	# Print a success message that the thread has started
	print("Start Monopoly Thread Initiated!")
	# Run forever
	while True:
		# Wait for a new game to need to start
		(game_name, teams) = startQueue.get()
		models = []
		# Iterate through each team
		for team in teams:
			# Get the current directory fo the team
			dirPath = genDirPath(game_name, team)
			# Get the current file that the team uploaded
			zipPath = genZipPath(game_name, team)
			zip_ref = zipfile.ZipFile(zipPath, 'r')
			# Unzip the the uploaded file into the team's directory
			zip_ref.extractall(dirPath)
	
			# Resolve the path of the extracted agent
			botPath = genBotPath(game_name, team)

			# Dynamically load the agent.py into the game
			spec = importlib.util.spec_from_file_location("agent", botPath)
			agentModule = importlib.util.module_from_spec(spec)
			spec.loader.exec_module(agentModule)
			# Instantiate the agent from the team's uplaoded files
			model = agentModule.Agent()
			# Append the agent to the list of models
			models.append(model)

		# Add the extracted models and adjudicator to the running queue
		activeQueue.put(models)

def activeMonopoly(activeQueue, finishedQueue):
	print("Active Monopoly Thread Initiated!")
	while True:
		adjudicator = activeQueue.get()
		adjudicator[0].function2()
		adjudicator[1].function2()
