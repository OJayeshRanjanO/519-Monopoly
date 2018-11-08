Roll
MultiBMST
jailDecision = None

trueFree = True
playerFree = True
if(player is jail):
	trueFree = False
	MultiBMST
	playerFree = False
	jailDecision = player.jailDecision
	switch(jailDecision):
		case getOutFree():
			removeCard
			playerFree = True
			trueFree = True
		case roll():
			if doubles: playerFree = True
		case nothing():
			if(waitCount >= 3): playerFree = True
		case pay():
			updateWealth(-50)
			playerFree = True


if(PlayerFree):
	Move Player
	while(not mainLogic());

	if(trueFree and double and count < 3):
		current player is fixed
	else:
		current player is chagned

	if(count >= 3):
		move previous player to jail
	else 
		updateWaitCount
else:
	player is changed

def mainLogic() <-- Returns True/False for final state reached
	Check type of tile landed
	if(property and unowned):
		MultiBMST
		bought = pCurrent.buy()
		owner = pCurrent
		if(not bought):
			MultiBMST
			aucPrice1 = p1.auction()
			aucPrice2 = p2.auction()
			owner = resolveAuction(aucPrice1, aucPrice2, otherPlayer)
		updateProperty(property, owner)

	costToPlayer = 0
	costToOthers = 0
	if(property and owned):
		costToPlayer = GameState.rent(property)
	if(costTile):
		costToPLayer = costTile.getCost()
	if(deck):
		card = pullDeck(decktype)
		cardType = card.type()
		playerPos = currentPlayer.pos()
		switch(cardType):
		F|	case fixedJump:
		F|	case relativeJump:
		F|	case relativeFixedJump:
			case getFreeCard:
			case moneyFromPlayers:
			case moneyToPlayers:
			case moneyToBank:
			case moneyFromBank:

		if(playerPos != currentPlayer.pos()):
		movePlayer(currentPlayer, pos)

	MultiBMST


Game(object):
	def roll():
		d1 = randint(1,6)
		d2 = randint(1,6)
		return d1 + d2