class Concluded_maze:
	total_moves = 0
	steps = 0
	distancia_ao_final = (0,0)
	
	def __init__(self, total_moves, steps, distancia_ao_final):
		self.total_moves = total_moves
		self.steps = steps
		self.distancia_ao_final = distancia_ao_final

def make_concluded_maze(total_moves,steps, distancia_ao_final):
    concluded_maze = Concluded_maze(total_moves,steps, distancia_ao_final)
    return concluded_maze


