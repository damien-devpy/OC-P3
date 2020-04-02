'''
Contain class DisplayGraphicMode. Allow to display the game in the terminal
Get instances of Decor(), MacGyver(), Items() and Guard() classes for
displaying
'''

import pygame
from configuration import SIZE_MAZE, TOTAL_SIZE, ITEMS_TO_PICKED, SIZE_SPRITES


class DisplayGraphicMode:
    '''
    Display the game in a window with sprites
    '''

    def __init__(self,
                 decor_object,
                 macgyver_object,
                 items_object,
                 guard_object,):
        '''
        Initializing pygame, and creating attributes
        '''
        pygame.init()

        # Open up pygame window
        self.screen = pygame.display.set_mode((TOTAL_SIZE, TOTAL_SIZE+35))

        self.decor_object = decor_object
        self.macgyver_object = macgyver_object
        self.items_object = items_object
        self.guard_object = guard_object

        # Loading all picts we need to display the maze
        self.macgyver_pict = self._loading_pict('MacGyver.png', True)
        self.dead_macgyver_pict = self._loading_pict('blood.png', True)
        self.guard_pict = self._loading_pict('Gardien.png', True)
        self.items_pict = {item: self._loading_pict(item, True)
                           for item in ITEMS_TO_PICKED}
        self.tile = self._loading_pict('tile.jpg')
        self.wall = self._loading_pict('wall.png')

        self._making_map(TOTAL_SIZE)

    def refresh(self):
        '''
        Call to _display_map() at each move to refresh display
        '''
        self._display_map()
        pygame.display.update()

    def input_user(self):
        '''
        Getting input user for moving MacGyver
        '''
        continuer = True  # If the user want to quit
        input_made = False  # If input has occured
        choice = None  # Choice made

        while not input_made:
            for event in pygame.event.get():
                # The user want to quit
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    continuer = False
                    input_made = True
                # The user moves up
                elif pygame.key.get_pressed()[pygame.K_UP]:
                    choice = 'up'
                    input_made = True
                # The user moves right
                elif pygame.key.get_pressed()[pygame.K_RIGHT]:
                    choice = 'right'
                    input_made = True
                # The user moves down
                elif pygame.key.get_pressed()[pygame.K_DOWN]:
                    choice = 'down'
                    input_made = True
                # The user moves left
                elif pygame.key.get_pressed()[pygame.K_LEFT]:
                    choice = 'left'
                    input_made = True

        return continuer, choice

    def counter(self):
        '''
        Displaying every items picked up under the maze
        '''
        for i, item in enumerate(self.items_object.items_carried):
            self.screen.blit(
                self.items_pict[item], (i*35, TOTAL_SIZE)
            )
        pygame.display.update()

    def display_text(self, text):
        '''
        Displaying win or loose message
        '''
        # Getting lenght of the counter to display the text on a right place
        counter_size = (len(ITEMS_TO_PICKED)
                        * SIZE_SPRITES
                        + SIZE_SPRITES)

        font = pygame.font.Font(None, 20)
        text_to_display = font.render(text, 1, (250, 250, 250))
        self.screen.blit(
            text_to_display,
            (counter_size, TOTAL_SIZE+10)
        )

        pygame.display.update()

    def repeat(self, delay, interval):
        '''
        Detect if a key stay pressed
        '''
        pygame.key.set_repeat(delay, interval)

    def _display_map(self):
        '''
        Display decor considering position of MacGyver, items and guard
        '''
        self.map.blit(self.background, (0, 0))
        self._display_items()
        self._display_guard()
        self._display_macgyver()
        self.screen.blit(self.map, (0, 0))

    def _display_macgyver(self):
        '''
        Display MacGyve, if is alive, else blood spread
        '''
        if self.macgyver_object.alive:
            column, height = self.macgyver_object.position
            self.map.blit(
                self.macgyver_pict, (column*35, height*35)
            )
        else:
            column, height = self.macgyver_object.position
            self.map.blit(
                self.dead_macgyver_pict, ((column-1)*35, height*35)
            )

    def _display_items(self):
        '''
        Display each items considering his position
        '''
        # For each {coordinates:item} in Items.positions attribute
        for key, value in self.items_object.positions.items():
            # Getting coordinates
            column, height = key
            # Bliting the item
            self.map.blit(
                self.items_pict[value], (column*35, height*35)
            )

    def _display_guard(self):
        '''
        Display guard
        '''
        if self.guard_object.position:
            column, height = self.guard_object.position
            self.map.blit(
                self.guard_pict, (column*35, height*35)
            )

    def _loading_pict(self, name, alpha=False):
        '''
        Loading sprites
        '''
        if alpha:
            return pygame.image.load(f'ressources/{name}').convert_alpha()
        else:
            return pygame.image.load(f'ressources/{name}').convert()

    def _making_map(self, size_map):
        '''
        Building background and map objects
        regarding walls and hallways coordinates
        '''
        self.background = pygame.Surface((size_map, size_map))
        self.map = pygame.Surface((size_map, size_map))

        for height in range(SIZE_MAZE):
            for length in range(SIZE_MAZE):

                if (length, height) in self.decor_object.walls:
                    self.background.blit(self.wall, (length*35, height*35))
                    self.map.blit(self.wall, (length*35, height*35))

                elif (length, height) in self.decor_object.hallways:
                    self.background.blit(self.tile, (length*35, height*35))
                    self.map.blit(self.wall, (length*35, height*35))
