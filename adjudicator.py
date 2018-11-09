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
		self.gamestate.liquid_cash[player_index] -= wealth

	def getCurrentPlayerAndModel(self):
		playerIndex = self.gamestate.current_player
		playerModel = self.players[playerIndex]
		return (playerIndex, playerModel)

	def inJail(self, player_index):
		return self.gamestate.jailed[player_index]


	# Plays the game, returns a csv
	def play(self):
		current_player, current_model = self.getCurrentPlayerAndModel()
		while not self.gameFinished():
			die1, die2 = self.diceRoll()
			roll = die1 + die2
			jail_decision = None
			true_free = True
			if(self.inJail(current_player))
				trueFree = False

				##### Signature will change when the function is committed #####
				MultiBMST()
				player_free = False

				temp_state = self.buildGamestate()
				jail_decision = player_model.jailDecision(temp_state)
				
				valid = 1
				if arg_in == 'GETOUTFREE':
					if player_model.jaiL_free_card > 0:
						player_model.jaiL_free_card - 1
						player_free = True
						true_free = True
					else
						valid = 0
				else if arg_in == 'ROLL':
					if(roll[1] == roll[2]):
							player_free = True
						else:
							player_model.wait_count = player_model.wait_count + 1 
				else if arg_in == 'NOTHING':
					if(player_model.wait_count >= 3):
						player_free = True
				else:
					updateWealth(-50)
					player_free = True

			if(player_free):
				movePlayer()
				while(not mainLogic());


		self.buildGamestate(self)



	def mainLogic():
		#### Need to check the tile type here ####
		current_player = self.current_player
		player_model = self.players[current_player]
		player_pos = self.position[current_player]
		tile_status = self.board[player_pos]
		#player landed on an unowned property

		if(tile_status == 0):
			self.multiBMST()
			current_gamestate = self.buildGamestate(self)
			gonna_buy = player_model.buyProperty(current_gamestate)
		


	def updateGameHistory(self):

			
		
	
		
