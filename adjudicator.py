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

	def multiBMST(self):
		currentTurn = self.gamestate.current_player
		

	# Plays the game, returns a csv
	def play(self):
		while not self.gameFinished():
			roll = self.diceRoll()
			
		
	
		
