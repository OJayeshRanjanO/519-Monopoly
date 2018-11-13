import json

class GameState(object):
	def __init__(self):
		self.turn = 0
		self.current_player = 0
		self.jailed = [False, False]
		self.status = [0 for i in range(42)]
		self.position = [0,0]
		#-1 empty tile, -2 income tax tile, -3 luxury tax, -4 chance, -5 community chest, -6 go to jail
		#>=0 will be a property
		self.liquid_cash = [0,0]#Cash in hand
		self.total_wealth = [0,0]#Cash + Buildings + Face value of property
		self.liquid_assets= [0,0]#Cash + Face value of prop
		self.phase = None#Phase when the game begins, this will be changed later
		self.phase_info = None
		self.debt = 0
		self.previous_states = []
		self.card_history=[]		
		self.percent_own_buildings=[0.0,0.0]#[addons_p1, addons_p2]
		self.percent_own_money =[0, 0]
		self.total_transacted_wealth = [0.0, 0.0]
		self.trades_p1 = []#[([properties], price, accepted)]
		self.trades_p2 = []#[([properties], price, accepted)]
		self.trades_attempmted=[0, 0] 
		self.hotels_left = 12
		self.houses_left = 32
		self.monopolies_held = [0 for i in range(10)]
		self.wait_count = [0, 0]

class HistoricState(object):
	def __init__(self, gameState, community_chest, chance, diceRoll, error_flag):
		self.gamestate = gameState
		self.cards = {
			"community_chest": community_chest,
			"chance": chance
		}
		self.diceRoll = diceRoll
		self.error_flag = error_flag

class History(object):
	def __init__(self):
		self.history = []

	def add_history(self, historicState):
		self.history.append(historicState)

