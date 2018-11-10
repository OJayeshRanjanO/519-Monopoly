import json
class GameState(object):
	def __init__(self):
		self.turn = 0
		self.current_player = 0
		self.jailed = [False, False]
		self.status = [0 for i in range(30)]
		self.position = [0,0]
		#-1 empty tile, -2 income tax tile, -3 luxury tax, -4 chance, -5 community chest, -6 go to jail
		#>=0 will be a property
		self.tile_lookup = [0 for i in range(40)]
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
		self.p1_net_wealth = 0
		self.wait_count = [0, 0]
		self.p2_net_wealth = 0
		self.properties = []
		# self.properties = [
		# (60,50),#"Mediterranean Avenue"
		# (60,50),#"Baltic Avenue"
		# (100,50),#"Oriental Avenue"
		# (200,0),# "Reading Railroad"
		# (100,50),#"Vermont Avenue"
		# (120,50),#"Connecticut Avenue"
		# (140,100),#"St. Charles Place"
		# (150,0),#"Electric Company"
		# (140,100),#"States Avenue"
		# (160,100),#"Virginia Avenue"
		# (200,0),#"Pennsylvania Railroad"
		# (180,100),#"St. James Place"
		# (180,100),#"Tennessee Avenue"
		# (200,100),#"New York Avenue"
		# (220,150),#"Kentucky Avenue"
		# (220,150),#"Indiana Avenue"
		# (240,150),#"Illinois Avenue"
		# (200,0),#"B. & O. Railroad"
		# (260,150),#"Atlantic Avenue"
		# (260,150),#"Ventnor Avenue"
		# (150,0),#"Water Works"
		# (280,150),#"Marvin Gardens"
		# (300,200),#"Pacific Avenue"
		# (300,200),#"North Carolina Avenue"
		# (320,200),#"Pennsylvania Avenue"
		# (200,0),#"Short Line Railroad"
		# (350,200),#"Park Place"
		# (400,200),#"Boardwalk"
		# (50,0),#Get Out of Jail Free 1
		# (50,0)#Get Out of Jail Free 2
		# ]
		self.properties = []
	def build_board(self):
		js = json.load(open("./properties.json"))
		for tile in js['properties']:
			price = tile['price'] if 'price' in tile else -1
			housecost = tile['housecost'] if 'housecost' in tile else -1
			multpliedrent = tile['multpliedrent'] if 'multpliedrent' in tile else []
			obj = Tile(tile['id'],tile['name'],price,tile['position']-1,tile['group'],housecost,multpliedrent)
			print(obj)
			self.properties.append(obj)
		return None
class Tile:
	def __init__(self,id,name,price,position,group,housecost,multpliedrent):
		self.id = id
		self.name = name
		self.price = price
		self.position = position
		self.group = group
		self.price = price
		self.housecost = housecost
		self.rent = multpliedrent
	def __repr__(self):
		return str(self.id) + " " + str(self.name) + " " + str(self.price) + " " + str(self.position) + " " + str(self.group) + " " + str(self.price) + " " + str(self.housecost) + " " + str(self.rent) +"\n"

if __name__ == '__main__':
	gs = GameState()
	gs.build_board()
	# gs.status[0] = -1
	# gs.status[1] = 2
	# gs.status[2] = 7
	# gs.status[27] = -7
	# gs.calculateNetWealth()
	# print(gs.p1_net_wealth)
	# print(gs.p2_net_wealth)
