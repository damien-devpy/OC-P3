import configuration

class Decor:
	'''
	In charge of decor. Managing walls, hallways, enter and exit
	'''
	
	def __init__(self, maze_file):
		'''
		Calling private method that recovering structure of maze
		and initializing suitable attributes
		'''
		
		self._get_structure_of_maze(maze_file)
		
	def _get_structure_of_maze(self, maze_file):
		'''
		Recovering structure of maze from the file
		'''
		self.walls = set()
		self.hallways = set()
		self.enter = None
		self.exit_maze = None
		
		with open(maze_file, 'r') as maze_file:
			for i, line in enumerate(maze_file):
				for j, letter in enumerate(line):
					if letter == configuration.WALLS:
						#Building walls in a set
						self.walls.add((j, i))
					elif letter == configuration.HALLWAYS:
						#Building hallways in a set
						self.hallways.add((j, i))
					elif letter == configuration.ENTER:
						#Creating enter
						self.enter = (j, i)
						self.hallways.add((j, i))
					elif letter == configuration.EXIT_MAZE:
						#Creating exit
						self.exit_maze = (j, i)
						self.hallways.add((j, i))
	
	def is_not_hallways(self, macgyver_object):
		'''
		Checking if coordinates wanted by user are an hallway or walls.
		Return True for hallway
		'''
		return macgyver_object.position not in self.hallways
