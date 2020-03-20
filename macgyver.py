""" -tc- Ajouter une docstring."""

import configuration

class MacGyver:
	'''
	Managing MacGyver : PV, position and moving it
	'''

	def __init__(self, decor_object):
		""" -tc- Ajouter une docstring."""
		# -tc- stocker decor_object également en attribut
		self.position = decor_object.enter
		self.life = 50 # -tc- Mieux d'ajouter un compteur d'objet ou une liste dans laquelle accumuler les objets. Ici, le concept de vie n'a pas vraiment de sens
		
		
	def _up(self):
		""" -tc- Ajouter une docstring."""
		#Changing Mac attribute position for getting him up
		self.position = (
			self.position[0]-1, 
			self.position[1],
		)
		
	def _right(self):
		""" -tc- Ajouter une docstring."""
		#... getting him right
		self.position = (
			self.position[0],
			self.position[1]+1,
		)
		
	def _down(self):
		""" -tc- Ajouter une docstring."""
		#... getting him down
		self.position = (
			self.position[0]+1,
			self.position[1],
		)
		
	def _left(self):
		""" -tc- Ajouter une docstring."""
		#... getting him left
		self.position = (
			self.position[0],
			self.position[1]-1,
		)
		
	def movement(self, input_user):
		""" -tc- Ajouter une docstring."""
		#Moving MacGyver
		# -tc- attention, tu dois vérifier que la position est autorisée avant de bouger. Ou bouger, comme tu le fais, mais 
		# -tc- revenir en arrière si la nouvelle position n'est pas un hallway.
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
		
	
		
