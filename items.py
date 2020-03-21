import configuration
import random

class Items:
	'''
	About items in the maze, being dropped, position and picked update
	'''

	def __init__(self, decor_object):
		self.positions = self._dropping_items(decor_object.hallways)
		self.items_carried = 0
		
		
	def _dropping_items(self, hallways):
		'''
		Choose (number of items) random position in decor_object.hallways
		for dropping them in the maze
		'''
		list_of_items = (item for item in configuration.ITEMS_TO_PICKED.keys())
		hallways_copy = hallways.copy()
		items_positions = dict()
		
		for i in configuration.ITEMS_TO_PICKED:
			#For each items to dropped
			random_position = random.sample(hallways_copy, 1)[0]
			#Choosing one hallway cell randomly
			hallways_copy.discard(random_position) 
			#Removing choosed position, avoiding choising the same more then once
			items_positions[random_position] = next(list_of_items)
			#Assigning our item the position choosen
		return items_positions
			
		
	def picked_up_items(self, coordinates):
		#Item picked up, changing is coordinates to 0
		del self.positions[coordinates]
		self.items_carried += 1