# import gamestate as gs
import random
class Agent:	
	def getBMSTDecision(self,state):
		#args: GameState Object
		#rtype: Action Object
		#Definition: 
		return None

	def auctionProperty(self,state):
		#args: GameState Object
		#rtype: Action
		current_player = state.current_player#Get the current player (0,1)
		property = state.properties[state.phase_info]#Get the property tuple using the phase info index
		property_price = property[0]#Get the price of the property
		return random.randrange(0,property_price)

	def buyProperty(self,state):
		#args: GameState Object
		#rtype: Action
		#Check a player's liquid assets
		current_player = state.current_player#Get the current player (0,1)
		property = state.properties[state.phase_info]#Get the property tuple using the phase info index
		property_price = property[0]#Get the price of the property
		if property_price < state.liquid_cash[current_player]:
			return True
		return False
	def jailDecision(self,state):
		#args: GameState Object
		#rtype: Action
		current_player = state.current_player
		opponent_player = 0 if current_player == 1 else 1
		owership = -1 if current_player == 1 else 1#Player 2's properties are negative, Player 1's are positive
		player_money = state.liquid_cash[current_player]

		#JAIL CARD STATUS
		jail_card_1 = state.status[28]#Chance
		jail_card_2 = state.status[29]#Community chest
		if jail_card_1 == owership or jail_card_2 == owership:#If player owns any of the card 
			if jail_card_2 == owership and jail_card_1 == owership:#Both owened by the same player
				return ("C",28)#Return the first card
			else:
				return ("C",28) if jail_card_1 == owership else ("C",29)
		#If the percentage of property owned by opponent is over 25% then stay in jail
		elif state.percent_own_buildings[opponent_player] > 0.25:
			return ("W",-1)

		#Only pay if the player has over $50
		if player_money >= 50: 
			if random.random() > 0.5:
				return ("C",-1)
			else:
				return ("R",-1)
		#Player doesn't have enough money, the player can either wait or choose to roll dice
		else:
			return ("W",-1) if random.random() > 0.5 else ("R",-1)

	def respondTrade(self,state):
		#args: GameState Object
		#rtype: Action
		return False #Always return false, because any trade will increase other player's advantage