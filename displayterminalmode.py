import configuration

class DisplayTerminalMode:
	'''
	Displaying the game in the terminal
	'''
	
	def __init__(self, 
		decor_object, 
		macgyver_object, 
		items_object, 
		guard_object
	):
	
		self.decor_object = decor_object
		self.macgyver_object = macgyver_object
		self.items_object = items_object
		self.guard_object = guard_object
		
	def refresh(self):
		'''
		Call to display_decor() at each move to refresh display
		'''
				
		self._display_decor()
		
	def _display_decor(self):
						
		'''
		Display decor considering position of MacGyver, items and guard
		'''
		for height in range(configuration.SIZE_MAZE):
			for length in range(configuration.SIZE_MAZE):
				
				if (((length, height) == self.macgyver_object.position)
					and self.macgyver_object.alive
					):
					#If coordinates matches MacGyver position, display him
					self._display_mac()
				elif (length, height) in self.items_object.positions:
					#If coordinates matches an item position, display it
					self._display_items(
						(length, height), 
						self.items_object.positions
					)
				elif (length, height) == self.guard_object.position:
					#If coordinates matches an guard position, display him
					self._display_guard()
				elif (length, height) in self.decor_object.walls:
					#Finally, if coordinates matches a wall, display it
					print(configuration.WALLS_TO_DISPLAY, end='')
				elif (length, height) in self.decor_object.hallways:
					#Or a hallway, display it
					print(configuration.HALLWAYS_TO_DISPLAY, end='')
				elif (length, height) == self.decor_object.enter:
					#If it's the enter of the maze, display it too.
					print(' ', end='')
			print()
		
	def _display_items(self, coordinates, items_positions):
		'''
		Display item key's dict that match actual coordinate in items_positions dict
		'''
		print(configuration.ITEMS_TO_PICKED[items_positions[coordinates]], end='')

		
	def _display_mac(self):
		print('.', end='')
		
	def _display_guard(self):
		print('x', end='')