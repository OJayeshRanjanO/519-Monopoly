import json

def loadGameConfigurations(location):
	gameJson = None
	with open(location, "r") as fp:
		gameJson = json.load(fp)

	groups = gameJson["groups"]
	properties = gameJson["properties"]
	for prop in properties:
		prop["group_id"] = groups.index(prop["group"].lower())

	properties = sorted(properties, key=lambda p: p["position"])
	
	return properties, groups
