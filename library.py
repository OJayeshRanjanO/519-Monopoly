import json

def loadGameJson(location):
	gameJson = None
	with open(location, "r") as fp:
		gameJson = json.load(fp)
	return gameJson

def loadGameProperties(gameJson):
	groups = gameJson["groups"]
	properties = gameJson["properties"]
	for prop in properties:
		prop["group_id"] = groups.index(prop["group"].lower())
	properties = sorted(properties, key=lambda p: p["position"])
	return properties

def loadGameCards_CmntyChest(gameJson):
	return gameJson["cards"]["community_chest"]

def loadGameCards_Chance(gameJson):
	return gameJson["cards"]["chance"]

def loadLookup(location):
	gameJson = loadGameJson(location)
	properties = loadGameProperties(gameJson)
	community_chest = loadGameCards_CmntyChest(gameJson)
	chance = loadGameCards_Chance(gameJson)

	return properties, community_chest, chance
		
