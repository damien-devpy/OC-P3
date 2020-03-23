import configuration

class Guard:
	'''
	Getting coordinates of the exit of the maze for guard position
	'''
	
	def __init__(self, decor_object):
		'''
		Assigning to the guard his position, given decor.object.exit_maze
		'''
		self.position = decor_object.exit_maze
		
	def killing_guard(self):
		'''
		Guard has been killed by Mac, deleting his position
		'''
		self.position = 0
	