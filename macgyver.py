import configuration

class MacGyver:
	'''
	Managing MacGyver : PV, position and moving it
	'''

	def __init__(self, decor_object):
		'''
		Initializing MacGyver attributes
		position and a attribute containing Decor() instance
		'''
		self.decor_object = decor_object
		self.position = self.decor_object.enter
		
		
	def _up(self):
		'''
		If the user choosing Mac going up, making him up
		'''
		self.position = (
			self.position[0], 
			self.position[1]-1,
		)
		
	def _right(self):
		'''
		If the user choosing Mac going right, making him right
		'''
		self.position = (
			self.position[0]+1,
			self.position[1],
		)
		
	def _down(self):
		'''
		If the user choosing Mac going down, making him down
		'''
		self.position = (
			self.position[0],
			self.position[1]+1,
		)
		
	def _left(self):
		'''
		If the user choosing Mac going left, making him left
		'''
		self.position = (
			self.position[0]-1,
			self.position[1],
		)
		
	def movement(self, input_user, previous_position):
		'''
		Making move MacGyver and checking if he's going into a wall
		If so, going to previous_position
		'''
		if input_user == configuration.UP:
			self._up()
		elif input_user == configuration.RIGHT:
			self._right()
		elif input_user == configuration.DOWN:
			self._down()
		elif input_user == configuration.LEFT:
			self._left()

		#If we move into a wall, we going back
		if self.decor_object.is_not_hallways(self):
			self.position = previous_position
			
	def killing_mac(self):
		'''
		Mac has been killed by guard. Deleting his position
		'''
		self.position = 0
		
	
		
