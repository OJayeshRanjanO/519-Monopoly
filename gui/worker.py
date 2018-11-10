import zipfile

def genDirPath(game, team):
	return "./games/%s/%s/" % (game, team)

def genZipPath(game, team):
	return genDirPath(game, team) + "/upload.zip"

def startMonopoly(startQueue, activeQueue):
	print("Start Monopoly Thread Initiated!")
	while True:
		(game_name, teams) = startQueue.get()
		for team in teams:
			dirPath = genDirPath(game_name, team)
			zipPath = genZipPath(game_name, team)
			zip_ref = zipfile.ZipFile(zipPath, 'r')
			zip_ref.extractall(dirPath)
		
