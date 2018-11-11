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
		self.tiles = []#41 tiles in here boiis -1 to 39 Read (3a)

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
		self.status_pos = -1#Has no place in status list
	def __repr__(self):
		return str(self.status_pos) + " " +str(self.position)+ " " +str(self.id) + " " + str(self.name) + " " + str(self.price) + " " + str(self.group) + " " + str(self.price) + " " + str(self.housecost) + " " + str(self.rent) + " " +str(self.status_pos) +"\n"
def build_board(gamestate,path):
	property_types = []
	js = json.load(open(path))
	for tile in js['properties']:
		price = tile['price'] if 'price' in tile else -1
		housecost = tile['housecost'] if 'housecost' in tile else -1
		multpliedrent = tile['multpliedrent'] if 'multpliedrent' in tile else []
		property_types.append(tile['group'])
		obj = Tile(tile['id'],tile['name'],price,tile['position']-1,tile['group'],housecost,multpliedrent)
		gamestate.tiles.append(obj)
	gamestate.tiles.sort(key=lambda x:x.position)

	print(set(property_types))
	count = 0
	for each_tile in gamestate.tiles:
		if each_tile.group != "Special":
			each_tile.status_pos = count
			count+=1


if __name__ == '__main__':
	gs = GameState()
	build_board(gs,"./properties.json")
	for i in gs.tiles:
		print(i)
	# gs.status[0] = -1
	# gs.status[1] = 2
	# gs.status[2] = 7
	# gs.status[27] = -7
	# gs.calculateNetWealth()
	# print(gs.p1_net_wealth)
	# print(gs.p2_net_wealth)
