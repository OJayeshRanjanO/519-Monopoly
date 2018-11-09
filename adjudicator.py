import random
from gamestate import GameState

class Adjudicator(object):
	def __init__(self, playerModel1, playerModel2):
		self.players = (playerModel1, playerModel2)
		
		# Set some constants
		self.maxTurns = 100

		#Initialize game state
		self.turn = 0		
		self.gamestate = new GameState()
		self.gamestateHistory = []
		self.game

	def diceRoll(self):
		# Get two random ints to make it closer to the regular dist.
		die1 = random.randint(0,5)
		die2 = random.randint(0,5)
		return (die1 + die2, die1, die2)

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
			
		

	# Plays the game, returns a csv
	def play(self):
		current_player = self.gamestateHistory.current_player
		while not self.gameFinished():
			roll = self.diceRoll()
			jail_decision = None
			true_free = True
			is_jailed = self.jailed[current_player]
			if(is_jailed == True)
				trueFree = False

				##### Signature will change when the function is committed #####
				MultiBMST()
				player_free = False

				temp_state = self.buildGamestate()
				jail_decision = player_obj.jailDecision(temp_state)
				
				valid = 1
				if arg_in == 'GETOUTFREE':
					current_player = self.gamestateHistory.current_player
					player_obj = self.players[current_player] 

					if player_obj.jaiL_free_card > 0:
						player_obj.jaiL_free_card - 1
						player_free = True
						true_free = True
					else
						valid = 0
				else if arg_in == 'ROLL':
					if(roll[1] == roll[2]):
							player_free = True
						else:
							player_obj.wait_count = player_obj.wait_count + 1 
				else if arg_in == 'NOTHING':
					if(player_obj.wait_count >= 3):
						player_free = True
				else:
					updateWealth(-50)
					player_free = True

			if(player_free):
				movePlayer()
				while(not mailLogic());


		self.buildGamestate(self)



	def mainLogic():
		#### Need to check the tile type here ####
		current_player = self.current_player
		player_obj = self.players[current_player]
		player_pos = self.position[current_player]
		tile_status = self.board[player_pos]
		#player landed on an unowned property

		if(tile_status == 0):
			self.multiBMST()
			current_gamestate = self.buildGamestate(self)
			gonna_buy = player_obj.buyProperty(current_gamestate)
		els
		


	def updateGameHistory(self):

			
		
	
		
