import random
from gamestate import GameState
import library

class Adjudicator(object):
	def __init__(self, playerModel1, playerModel2):
		# Add agents to the game
		self.players = (playerModel1, playerModel2)
		# Error Flag -- automatic game over
		self.error = -1
		# Set some constants
		self.maxTurns = 100
		# Initialize game state
		self.turn = 0		
		self.gamestate = GameState()
		self.gamestateHistory = []
		# Initialize the lookup table
		self.properties = library.loadGameConfigurations("./properties.json")

	def diceRoll(self):
		return (random.randint(0,5), random.randint(0,5))

	def gameFinished(self):
		# Increase the number of turns
		turnsReached = self.turn >= self.maxTurns
		# Check if any player has a negative balance
		noMoney = any([m < 0.0 for m in self.gamestate.liquid_cash])
		return turnsReached or noMoney

	def buildGamestate(self):
		# Builds a deep copy of gamestate so models can use
		return self.gamestate

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

	def updateProperty(self, player_index, property_id):
		pass

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
						#They tried to use a card that they didn't have.
						#TODO handle
						pass
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
		#### Need to check the tile type here ####
		current_player, current_model = self.getCurrentPlayerAndModel()
		other_player, other_model = self.getOtherPlayerAndModel()
		player_pos = self.position[current_player]
		tile_status = self.lookupSpace(current_player)

		#player landed on an unowned property
		if(tile_status == 0):
			self.multiBMST()
			current_gamestate = self.buildGamestate(self)
			gonna_buy = player_model.buyProperty(current_gamestate)
			owner = -1
			if(not gonna_buy):
				self.multiBMST()
				#phase info needs to be updated here before model call 
				auc_price_current = current_model.auctionProperty(current_gamestate)
				auc_price_other =  other_model.auctionProperty(current_gamestate)
				#As of now the base price for a property will be set to 0, this will
				#be updated when the property objects are fully implemented
				winner = self.resolveAuction(auc_price_current, auc_price_other, 0)
				if(winner != -1):
					owner = winner

			self.updateProperty(player_pos, owner)

		cost_to_player = 0
		cost_to_others = 0

		#Every other tile status indicates various degrees of ownership
		#TODO PARSE OUT TO FUNCTION
		if(tile_status != 0):
			#Need to calculate the rent 
			cost_to_player = self.resolveRent(player_pos)
		#If there is a cost associated with the spot e.g. income tax or luxury tax
		if(tile_status == -2 or tile_status == -3):
			cost_to_player = self.resolveRent(property_index)
		#Chance or community chest
		if(tile_status == -4 or tile_status == -5):
			card = None
			if((tile_status % 2) == 0):
				card = self.pullChanceCard()
			else:
				card = self.pullCommunityChestCard()

			self.resolveCardModifiers(card, current_player)

		self.multiBMST()


	def resolveCardModifiers(card_id, current_player):
		pass

	def pullChanceCard(self):
		pass

	def pullCommunityChestCard(self):
		pass

	def lookupSpace(self, current_player):
		pass


	def updateGameHistory(self):
		current_reflection = self.buildGamestate(self)
		self.gamestateHistory.append(current_reflection)

	def updateProperty(self, player_pos, owner):
		pass

	def resolveRent(self, property_index):
		pass

