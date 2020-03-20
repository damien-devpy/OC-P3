import configuration

class MacGyver:
	'''
	Managing MacGyver : PV, position and moving it
	'''

	def __init__(self, decor_object):
		self.position = decor_object.enter
		self.life = 50
		
		
	def _up(self):
		#Changing Mac attribute position for getting him up
		self.position = (
			self.position[0]-1, 
			self.position[1],
		)
		
	def _right(self):
		#... getting him right
		self.position = (
			self.position[0],
			self.position[1]+1,
		)
		
	def _down(self):
		#... getting him down
		self.position = (
			self.position[0]+1,
			self.position[1],
		)
		
	def _left(self):
		#... getting him left
		self.position = (
			self.position[0],
			self.position[1]-1,
		)
		
	def movement(self, input_user):
		#Moving MacGyver
		if input_user == configuration.UP:
			self._up()
		elif input_user == configuration.RIGHT:
			self._right()
		elif input_user == configuration.DOWN:
			self._down()
		elif input_user == configuration.LEFT:
			self._left()	
			
	def killing_mac(self):
		self.life = 0
		self.position = 0
		
	
		