# import gamestate as gs
class Agent:	
	def getBMSTDecision(self,state):
		#args: GameState Object
		#rtype: Action Object
		#Definition: 
		return None

	def auctionProperty(self,state):
		#args: GameState Object
		#rtype: Action
		return None

	def buyProperty(self,state):
		#args: GameState Object
		#rtype: Action
		#Check a player's liquid assets
		current_player = state.current_player
		property_price = (state.phase_info)[0]
		if state.properties[property_price] < state.liquid_cash[current_player]:
			return True
		return False
	def jailDecision(self,state):
		#args: GameState Object
		#rtype: Action
		return None

	def respondTrade(self,state):
		#args: GameState Object
		#rtype: Action
		return None
	def recieveState(self,state):

		return None