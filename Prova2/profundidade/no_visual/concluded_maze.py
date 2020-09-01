class Concluded_maze:
	total_moves = 0
	steps = 0
	
	def __init__(self, total_moves, steps):
		self.total_moves = total_moves
		self.steps = steps

def make_concluded_maze(total_moves,steps):
    concluded_maze = Concluded_maze(total_moves,steps)
    return concluded_maze


