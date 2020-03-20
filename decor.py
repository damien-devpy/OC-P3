""" -tc- Ajouter une docstring."""

import configuration

class Decor:
	'''
	In charge of decor. Managing walls, hallways, enter and exit
	'''

	def __init__(self, maze_file):
		""" -tc- Ajouter une docstring."""
		
		# -tc- Pas nécessaire que _get_structure_of_maze renvoie les infos.
		# -tc- Elle peut directement créer les attributs
		(self.walls, 
			self.hallways, 
			self.enter, 
			self.exit_maze,
		) = self._get_structure_of_maze(maze_file)
		
	def _get_structure_of_maze(self, maze_file):
		""" -tc- Ajouter une docstring."""
		#Recovering structure of maze from the file
		# -tc- Utiliser directement self.walls, self.hallways, etc.
		walls = set()
		hallways = set()
		enter = tuple() # Utiliser None plutôt qu'un tuple vide, plus idiomatique
		exit_maze = tuple()
		
		# -tc- éviter la variable file est réservée en python. 
		with open(maze_file, 'r') as file:
			file = file.read().split('\n') # -tc- Inutile
			
			for i in range(configuration.SIZE_MAZE): # -tc- plus pythonique: for i, line in enumerate(file)
				for j in range(configuration.SIZE_MAZE): # -tc- plus pythonique for j, letter in enumerate(line)
					if file[i][j] == configuration.WALLS: # -tc- avec le code plus haut: if letter == configuration.WALLS
						#Building walls in a set
						walls.add((i, j)) # -tc- La convention euclidienne, utilisée en python, est (j, i), c'est à dire (colonne, ligne)
					elif file[i][j] == configuration.HALLWAYS:
						#Building hallways in a set
						hallways.add((i, j))
					elif file[i][j] == configuration.ENTER:
						#Creating enter
						enter = (i, j)
					elif file[i][j] == configuration.EXIT_MAZE:
						#Creating exit
						exit_maze = (i, j)
		
		# -tc- inutile si tu manipules directement self.walls, etc., après tout, c'est une méthode de ta classe
		return walls, hallways, enter, exit_maze
	
	def is_hallways(self, macgyver_object):
		""" -tc- Ajouter une docstring."""
		#Checking if coordinates wanted by user
		#are an hallway... or walls.
		# -tc- ou simplement return macgyver_object.position in self.hallways
		if macgyver_object.position in self.hallways:
			return True
