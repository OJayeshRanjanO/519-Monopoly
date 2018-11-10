import random
from gamestate import GameState

class Adjudicator(object):
	def __init__(self, playerModel1, playerModel2):
		self.players = (playerModel1, playerModel2)

		# Error Flag -- automatic game over
		self.error = -1
		
		# Set some constants
		self.maxTurns = 100

		#Initialize game state
		self.turn = 0		
		self.gamestate = new GameState()
		self.gamestateHistory = []

	def diceRoll(self):
		return (random.randint(0,5), random.randint(0,5))

	def gameFinished(self):
		# Increase the number of turns
		self.turn = self.turn+1
		return self.turn >= self.maxTurns

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

	def respondToBMSTDecision(self, player_index, response):
			success = False
			if(response):
				if(response[0] == 0): # This is the BMS
					b, m, s = response[1:]
					
					for p in s:
						pass
														
					for p in b:
						pass

					for p in m:
						pass
				
			return success

			
	def updateWealth(self, player_index, wealth):
		self.gamestate.liquid_cash[player_index] += wealth

	def getCurrentPlayerAndModel(self):
		playerIndex = self.gamestate.current_player
		playerModel = self.players[playerIndex]
		return (playerIndex, playerModel)

	def inJail(self, player_index):
		return self.gamestate.jailed[player_index]

	def hasJailCard(which_deck):
		jail_cards = self.gamestate.jail_free_card[current_player]
		#first index represents a chance get out of jail card
		#second index represents a community chest get of jail card
		chance_card = jail_cards[0]
		community_card = jail_cards[1]
		return_val = -1

		if(chance_card >= 1 && which_deck == 28):
			return_val = 0
		else if(community_card >= 1 && which_deck == 29):
			return_val = 1

		return return_val


	#Pass in a negative 1 to remove and positve 1 to add
	def updateJailCards(amount, which_deck):
		jail_cards = self.gamestate.jail_free_card[current_player]
		chance_card = jail_cards[0]
		community_card = jail_cards[1]

		if(which_deck == 28):
			chance_card = chance_card + amount
		else:
			community_card = community_card + amount

		self.gamestate.jail_free_card[current_player] = [chance_card, community_card]



	def updateWaitCount(self):
		current_player, current_model = self.getCurrentPlayerAndModel()
		current_wait = self.gamestate.wait_count[current_player]
		self.gamestate.wait_count[current_player] = current_wait + 1 

	# Plays the game, returns a csv
	def play(self):
		current_player, current_model = self.getCurrentPlayerAndModel()
		while not self.gameFinished():
			die1, die2 = self.diceRoll()
			double = die1 == die2
			roll = die1 + die2

			jail_decision = None
			true_free = True
			is_jailed = self.inJail(current_player)

			if(is_jailed == True)
				trueFree = False

				##### Signature will change when the function is committed #####
				multiBMST()
				player_free = False

				temp_state = self.buildGamestate()
				jail_decision = player_model.jailDecision(temp_state)
				wait_count = self.gamestate.wait_count[current_player]
				
				valid = 1
				if arg_in[0] == 'C':
					num_jail_free = hasJailCard(arg_in[1])

					if has_jail_free > 0:
						#Update the player's jail cards
						updateJailCards(-1, arg_in[1])
						updateDeck()
						player_free = True
						true_free = True
					else
						valid = 0
				else if arg_in[0] == 'R':
					if(double):
							player_free = True
						else:
							updateWaitCount()
				else if arg_in[0] == 'N':
					if(wait_count >= 3):
						player_free = True
				else:
					self.updateWealth(current_player, -50)
					player_free = True

			if(player_free):
				movePlayer()
				while(not mainLogic());


		self.buildGamestate(self)



	def mainLogic():
		#### Need to check the tile type here ####
		current_player, current_model = self.getCurrentPlayerAndModel()
		player_pos = self.position[current_player]
		tile_status = self.board[player_pos]
		#player landed on an unowned property

		if(tile_status == 0):
			self.multiBMST()
			current_gamestate = self.buildGamestate(self)
			gonna_buy = player_model.buyProperty(current_gamestate)
		


	def updateGameHistory(self):
		current_reflection = self.buildGamestate(self)
		self.gamestateHistory.append(current_reflection)

			
		
	
	
