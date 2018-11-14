import random
from gamestate import GameState
import library

class Adjudicator(object):
	def __init__(self, playerModel1, playerModel2, config=None):
		# Add agents to the game
		self.players = (playerModel1, playerModel2)
		# Error Flag -- automatic game over
		self.error = False
		# Set some constants
		self.maxTurns = 100
		# Initialize game state
		self.turn = 0		
		self.gamestate = GameState()
		self.gamestateHistory = []
		# Initialize the lookup table
		self.properties, self.cmnty_chest, self.chance = library.loadLookup("./properties.json")
		# Randomize a current deck for community chest and chance
		self.cmnty_chest_deck = sorted(list(range(len(self.cmnty_chest))))
		self.chance_deck = sorted(list(range(len(self.chance))))
		# Declare random dice rolls
		self.rolls = [(random.randint(0,5), random.randint(0,5)) for i in range(self.maxTurns)]

		# If configuration is provided, set the start state accordingly
		if(config):
			# If a history is provided, initailze that state entirely
			if("from_history" in config):
				loadedHistory = library.HistoricState_fromDict(config["from_history"])			
				self.cmnty_chest_deck = loadedHistory.cards.community_chest
				self.chance_deck = loadedHistory.cards.chance
				self.gamestate = loadedHistory.gamestate
				self.error = loadedHistory.error
				self.rolls[0] = loadedHistory.diceRoll
			
			# Now we can use sub combinations of state backup
			else:			
				# If there are a specific dice roll layout required, let this be the start
				if("dice_rolls" in config):
					self.rolls = config["dice_rolls"]
				# If a specific order of community_chest cards, let this be the original configuartion
				if("community_chest_order" in config):
					self.cmnt_chance_deck = config["community_chest_order"]
				# If there is a specific chance configuration, let it be so
				if("chance_order"):
					self.chance_deck = config["chance_order"]



	def diceRoll(self):
		return self.rolls[self.turn]

	def gameFinished(self):
		# Increase the number of turns
		turnsReached = self.turn >= self.maxTurns
		# Check if any player has a negative balance
		noMoney = any([m < 0.0 for m in self.gamestate.liquid_cash])
		return turnsReached or noMoney

	def buildGamestate(self):
		# Builds a deep copy of gamestate so models can use
		return self.gamestate.deepcopy()

	def playerOwnsTile(self, current_player, tile_status):
		p_sign = (-1)**(current_player)
		same_sign = lambda x,y: (x < 0 and y < 0) or (x > 0 and y > 0)
		return same_sign(tile_status, p_sign)

	def multiBMST(self):
		turn = self.gamestate.current_player
		responses = [None, None]
		concensus = False
		while not concensus:
			gs = self.buildGamestate()
			model = self.players[turn]
			resp = model.getBMSTDecision(gs)

			self.respondToBMSTDecision(turn, resp)

			if(type(resp) == TradeDecision):
				gs = self.buildGamestate()
				self.player[(turn+1)%2].respondTrade(gs)
			
			responses[turn] = resp
			concensus = responses[0] is None and responses[1] is None
			turn = (turn + 1) % 2

	def same_group(self, property_one, property_two):
		return property_one["group_id"] == property_two["group_id"]

	def respondToBMSTDecision(self, player_index, response):
			invalid_move = False
			if(response):
				if(response[0] == 0): # This is the BMS
					b, m, s = response[1:]

					buildGS = self.buildGamestate()

					p_sign = (-1)**(player_index)
					same_sign = lambda x,y: (x < 0 and y < 0) or (x > 0 and y > 0)
					same_group = lambda x,y: x["group_id"] == y["group_id"]
					prop_lookup = lambda x: buildGS.status[x["position"]]

					if(not all([same_sign(buildGS.status[s], p_sign) for s in b+m+s])):
						invalid_move = True
						return invalid_move

					for p in s:
						prop = self.properties[p]
						status = buildGS.status[p]					
						if(abs(status) > 1 and abs(status) < 7):
							buildGS.liquid_cash[player_index] += (prop["houseprice"] // 2)
							buildGS.status[p] -= p_sign
							if(abs(status) == 6):
								buildGS.houses_left -= 4
								buildGS.hotels_left += 1
							else:
								buildGS.houses_left += 1
						else:
							invalid_move = True
							break

					for p in m:
						prop = self.properties[p]
						status = buildGS.status[p]
						if(abs(status) == 1):
							buildGS.liquid_cash[player_index] += (prop["price"] // 2)
							buildGS.status[p] = p_sign*7
						else:
							invalid_move = True
							break

					for p in b:
						prop = self.properties[p]
						status = buildGS.status[p]
						group = prop["group_id"]

						has_monopoly = buildGS.monopolies[group] == player_index
						can_build = group < 8 and abs(status) < 6

						if(can_build and has_monopoly):
							buildGS.liquid_cash[player_index] -= prop["houseprice"]
							buildGS.status[p] += p_sign
							if(status == 5):
								buildGS.hotels_left -= 1
								buildGS.houses_left += 4
							else:	
								buildGS.houses_left -= 1
						else:
							invalid_move = True
							break

					for p in s+b:
						prop = self.properties[p]
						status = buildGS.status[p]					
						p_group = [prop_lookup(adj) for adj in self.properties if same_group(prop, adj)]
						if(any([abs(status-((adj_s!=7)*adj_s)) > 1 for adj_s in p_group])):
							invalid_move = True
							break

					invalid_move = invalid_move or buildGS.houses_left < 0
					invalid_move = invalid_move or buildGS.hotels_left < 0
					invalid_move = invalid_move or buildGS.liquid_cash[player_index] < 0
					
					if(not invalid_move):
						self.gamestate = buildGS

			return not invalid_move
			
	def updateWealth(self, player_index, wealth):
		self.gamestate.liquid_cash[player_index] += wealth

	def getCurrentPlayerAndModel(self):
		playerIndex = self.gamestate.current_player
		playerModel = self.players[playerIndex]
		return (playerIndex, playerModel)

	def getOtherPlayerAndModel(self):
		player_index = self.players[(self.turn + 1)%2]
		player_model = self.players[player_index]
		return (player_index, player_model)

	def inJail(self, player_index):
		return self.gamestate.jailed[player_index]
	
	def movePlayer(self, player_index, move, fixed=False, get_go=False):
		previous_pos = self.gamestate.position[player_index]
		current_pos = previous_pos
		if(fixed):
			current_pos = move
		else:
			current_pos = previous_pos + move
		updated_pos = updated_pos % 40
		if(updated_pos < current_pos and get_go): 
			self.updateWealth(current_pos, 200)


	def hasJailCard(which_deck, player_index):
		jail_cards = self.gamestate.jail_free_card[player_index]
		#first index represents a chance get out of jail card
		#second index represents a community chest get of jail card
		chance_card = jail_cards[0]
		community_card = jail_cards[1]
		return_val = -1

		if(chance_card >= 1 and which_deck == 28):
			return_val = 0
		elif (community_card >= 1 and which_deck == 29):
			return_val = 1

		return return_val


	def resolveAuction(self, floor_price, current_player_price, other_player_price):
		maxBet = int(max(current_player_price, other_player_price))
		if(maxBet < floor_price):
			return -1
		else:
			if(maxBet == int(other_player_price)):
				return 1
			else:
				return 0
				
	#Pass in a negative 1 to remove and positve 1 to add
	def updateJailCards(amount, which_deck, player_index):
		jail_cards = self.gamestate.jail_free_card[player_index]
		chance_card = jail_cards[0]
		community_card = jail_cards[1]

		if(which_deck == 28):
			chance_card = chance_card + amount
		else:
			community_card = community_card + amount

		self.gamestate.jail_free_card[player_index] = [chance_card, community_card]

	def updateWaitCount(self):
		current_player, current_model = self.getCurrentPlayerAndModel()
		current_wait = self.gamestate.wait_count[current_player]
		self.gamestate.wait_count[current_player] = current_wait + 1 

	# Plays the game, returns a csv
	def play(self):
		current_player, current_model = self.getCurrentPlayerAndModel()
		if(not self.gameFinished()):
			die1, die2 = self.diceRoll()
			double = die1 == die2
			roll = die1 + die2

			double_count = self.GameState.double_count[current_player]
			jail_decision = None
			true_free = True
			is_jailed = self.inJail(current_player)

			if(is_jailed[current_player] == True):
				trueFree = False

				self.multiBMST()
				player_free = False

				temp_state = self.buildGamestate()
				jail_decision = player_model.jailDecision(temp_state)
				wait_count = self.gamestate.wait_count[current_player]
				
				valid = 1
				if jail_decision[0] == 'C':
					num_jail_free = hasJailCard(jail_decision[1], current_player)

					if has_jail_free > 0:
						#Update the player's jail cards
						self.updateJailCards(-1, jail_decision[1], current_player)
						self.updateDeck()
						player_free = True
						true_free = True
					else:
						self.error = True
						return
				elif jail_decision[0] == 'R':
					if(double):
							player_free = True
					else:
						self.updateWaitCount(current_player)
				elif jail_decision[0] == 'N':
					if(wait_count >= 3):
						player_free = True
					else:
						self.updateWaitCount(current_player)
				else:
					self.updateWealth(current_player, -50)
					player_free = True

			if(player_free):
				while(not self.mainLogic(roll)):
					pass

				player_pos = self.gamestate.position[current_player]
				if(true_free and double and (double_count + 1) < 3):
					#Need to send in the mapping for jail
					self.movePlayer(player_pos, 10, True, False)
					self.incDoubleCount(current_player)
				elif(true_free and double and (double_count + 1) >= 3):
					self.movePlayer(current_player, 10, True, False)
				else:
					self.movePlayer(player_pos, roll)

			self.buildGamestate(self)

		self.turn = self.turn + 1
		return self.gameFinished()

	def updateJailWaitCount(current_player):
		jail_wait_count = self.gamestate.wait_count[current_player]
		jail_wait_count = jail_wait_count + 1
		self.gamestate.wait_count[current_player] = jail_wait_count


	def incDoubleCount(current_player):
		self.double_count[current_player] = self.double_count[current_player] + 1

	def mainLogic(self, dice_roll):
		current_player, current_model = self.getCurrentPlayerAndModel()
		other_player, other_model = self.getOtherPlayerAndModel()
		player_pos = self.position[current_player]
		tile_group_id = self.getTileGroupId(player_pos) 

		#Property
		if(tile_group_id <= 9):
			self.resolveProperty(current_player, player_pos, tile_group_id, dice_roll)
		#Cost tile, luxury and income tax
		elif(tile_group_id == 10):
			self.damagePlayer(current_player, player_pos)
		#Deck card
		elif(tile_group_id >= 11 and tile_group_id <= 12):
			self.pullDeckCard(current_player, player_pos, tile_group_id)
		#Special don't remember what this is.
		elif(tile_status == 14):
			self.processSpecialSnowflake(current_player, player_pos)
		#Going on a one way trip to jail
		else:
			self.movePlayer(player_pos, 10, True, False)

		#Let the players decided what to do next gien the updated board state.
		self.multiBMST()


	def processSpecialSnowflake(self, current_player, player_pos):
		#This means they landed on go.
		if(player_pos == 0):
			self.updateWealth(current_player, 200)
		#Free parking and just visitting spaces don't have any side
		else:
			pass

	def damagePlayer(self, current_player, player_pos):
		#Income tax, according to the document, we pay a flat $200
		if(player_pos == 4):
			self.updateWealth(current_player, -200)
		else:
			self.updateWealth(current_player, -75)


	def resolveProperty(self, current_player, tile_index, tile_group_id, dice_roll):
		#player landed on an unowned property
		prop = self.properties[tile_index]
		tile_status = self.getTileStatus(tile_index)

		if(tile_status == 0):
			self.multiBMST()
			current_gamestate = self.buildGamestate()
			gonna_buy = player_model.buyProperty(current_gamestate)
			owner = -1
			if(not gonna_buy):
				self.multiBMST()
				#phase info needs to be updated here before model call 
				auc_price_current = current_model.auctionProperty(current_gamestate)
				auc_price_other =  other_model.auctionProperty(current_gamestate)
				#As of now the base price for a property will be set to 0, this will
				#be updated when the property objects are fully implemented

			if(owner != -1):
				self.updateProperty(player_pos, owner)
		else:
			other_player, other_model = getOtherPlayerAndModel()
			rent = self.calculateRent(tile_group_id, tile_status, dice_roll)
			self.updateWealth(current_player, -rent)
			self.updateWealth(other_player, rent)

	def calculateRent(tile_group_id, tile_status, dice_roll):
		same_owner = self.playerOwnsTile(current_player, tile_status)
		rent = 0
		other_player, other_model = self.getOtherPlayerAndModel()

		if(not same_owner):	
			#Railroad
			railroad_rent = [25, 50, 100, 200]
			if(group_id == 8):
				num_railroads_owned = self.numRailsUtilsOwned(other_player, 0)
				rent = railroad_rent[numRailroadsOwned - 1]
			#Utilities
			elif(group_id == 9):
				num_utilities_owned = self.numRailsUtilsOwned(other_player, 1)
				if(num_utilities_owned > 1):
					rent = 4 * dice_roll
				else:
					rent = 10 * dice_roll
			else:
				temp = abs(tile_status) - 2
				if(temp < 0):
					rent = prop["rent"]
				else:
					rent_var = prop["multpliedrent"]
					rent = rent_var[temp]
		else:
			rent = 0

	def numRailsUtilsOwned(player, util_or_rail):
		signs = []
		tile_pos = [5, 5, 10, 12, 28, 14]
		which = []
		#Check for railroads
		if(rail_or_util == 0):
			which = tile_pos[0:3]
		#Check for utils
		else:
			which = tile_pos[3:]
		
		for x in range(which):
			signs.append(self.getTileStatus(x))

		owned = map(self.playerOwnsTile(player, signs))
		return owned.count(1)



	def resolveCardModifiers(card_id, current_player):
		pass

	def pullChanceCard(self):
		pass

	def pullCommunityChestCard(self):
		pass

	def getTileStatus(self, tile_index):
		tile = self.properties[player_pos]
		return self.status[tile]

	def getTileGroupId(self, tile_index):
		prop = self.properties[tile_index]
		return prop["group_id"]


	def updateGameHistory(self):
		current_reflection = self.buildGamestate(self)
		self.gamestateHistory.append(current_reflection)

	def updateProperty(self, player_pos, owner):
		new_status = -1 if owner else 0
		self.gamestate.status[player_pos] = new_status

		

