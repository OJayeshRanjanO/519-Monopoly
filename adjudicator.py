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

	def diceRoll(self):
		# Get two random ints to make it closer to the regular dist.
		die1 = random.randint(0,5)
		die2 = random.randint(0,5)
		return die1 + die2

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
		while not self.gameFinished():
			roll = self.diceRoll()
			
		
	
		
