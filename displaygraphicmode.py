import pygame
import configuration

class DisplayGraphicMode:
	
	pygame.init()
	
	def __init__(self, decor_object, macgyver_object, items_object, guard_object):
	
		self.screen = pygame.display.set_mode((configuration.TOTAL_SIZE, 
												configuration.TOTAL_SIZE+35
												)
			)
			
		self.decor_object = decor_object
		self.macgyver_object = macgyver_object
		self.items_object = items_object
		self.guard_object = guard_object
		
		self.macgyver_pict = self._loading_pict('MacGyver.png', True)
		self.dead_macgyver_pict = self._loading_pict('blood.png', True)
		self.guard_pict = self._loading_pict('Gardien.png', True)
		self.items_pict = {item:self._loading_pict(item, True) 
							for item in configuration.ITEMS_TO_PICKED.keys()
							}
		self.tile = self._loading_pict('tile.jpg')
		self.wall = self._loading_pict('wall.png')
		
		self._making_map(525)
	
	def refresh(self):
		self._display_map()
		pygame.display.update()
		
	def input_user(self):
	
		continuer = True
		input_made = False
		choice = None
		
		while not input_made:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						continuer = False
						input_made = True
					if event.key == pygame.K_UP:
						choice = 'up'
						input_made = True
					elif event.key == pygame.K_RIGHT:
						choice = 'right'
						input_made = True
					elif event.key == pygame.K_DOWN:
						choice = 'down'
						input_made = True
					elif event.key == pygame.K_LEFT:
						choice = 'left'
						input_made = True
					
					
		return continuer, choice
		
	def counter(self):
		for i, item in enumerate(self.items_object.items_carried):
			self.screen.blit(self.items_pict[item], (i*35, configuration.TOTAL_SIZE))
		pygame.display.update()
		
	def display_text(self, text):
		font = pygame.font.Font(None, 20)
		text_to_display = font.render(text, 1, (250, 250, 250))
		self.screen.blit(text_to_display, (250, 535))
		pygame.display.update()
		
	def repeat(self, delay, interval):
		pygame.key.set_repeat(delay, interval)	
		
	def _display_map(self):
		self.map.blit(self.background, (0, 0))
		self._display_items()
		self._display_guard()
		self._display_macgyver()
		self.screen.blit(self.map, (0, 0))
	
	def _display_macgyver(self):
		if self.macgyver_object.alive:
			column, height = self.macgyver_object.position
			self.map.blit(self.macgyver_pict, (column*35, height*35))
		else:
			column, height = self.macgyver_object.position
			self.map.blit(self.dead_macgyver_pict, ((column-1)*35, height*35))
		
	
	def _display_items(self):
		for key, value in self.items_object.positions.items():
			column, height = key
			self.map.blit(self.items_pict[value], (column*35, height*35))
			
	def _display_guard(self):
		if self.guard_object.position:
			column, height = self.guard_object.position
			self.map.blit(self.guard_pict, (column*35, height*35))
			
	def _loading_pict(self, name, alpha=False):
		if alpha:
			return pygame.image.load(f'ressource/{name}').convert_alpha()
		else:
			return pygame.image.load(f'ressource/{name}').convert()
		
	def _making_map(self, size_map):
		
		self.background = pygame.Surface((size_map, size_map))
		self.map = pygame.Surface((size_map, size_map))
		
		for height in range(configuration.SIZE_MAZE):
			for length in range(configuration.SIZE_MAZE):
				if (length, height) in self.decor_object.walls:
					self.background.blit(self.wall, (length*35, height*35))
					self.map.blit(self.wall, (length*35, height*35))
				elif (length, height) in self.decor_object.hallways:
					self.background.blit(self.tile, (length*35, height*35))
					self.map.blit(self.wall, (length*35, height*35))
					
