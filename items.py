import configuration
import random

class Items:
	'''
	About items in the maze, being dropped, position and picked update
	'''

	def __init__(self, decor_object):
		self.decor_object = decor_object
		self.positions = self._dropping_items()
		self.items_carried = list()
		
		
	def _dropping_items(self):
		'''
		Choose (number of items) random position in decor_object.hallways
		for dropping them in the maze
		'''
		list_of_items = (item for item in configuration.ITEMS_TO_PICKED.keys())
		hallways_copy = self.decor_object.hallways.copy()
		hallways_copy.discard(self.decor_object.enter)
		hallways_copy.discard(self.decor_object.exit_maze)
		items_positions = dict()
		
		#For each items to dropped	
		for i in configuration.ITEMS_TO_PICKED:
			#Choosing one hallway cell randomly
			random_position = random.sample(hallways_copy, 1)[0]
			#Removing choosed position, avoiding choising the same more then once
			hallways_copy.discard(random_position) 
			#Assigning our item the position choosen
			items_positions[random_position] = next(list_of_items)
			
		return items_positions
			
		
	def picked_up_items(self, coordinates):
		'''
		Counting items carried an taking care off removing them from display
		'''
		self.items_carried.append(self.positions[coordinates])
		del self.positions[coordinates]