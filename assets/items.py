'''
Contain Items class. In charge of dropping items in random position and
deleting their positions if picked up
'''

from random import sample
from configuration import ITEMS_TO_PICKED


class Items:
    '''
    About items in the maze, being dropped, position and picked update
    '''

    def __init__(self, decor_object):
        self.decor_object = decor_object
        self._positions = self._dropping_items()
        self._items_carried = list()

    def _get_positions(self):
        return self._positions

    positions = property(_get_positions)

    def _get_items_carried(self):
        return self._items_carried

    items_carried = property(_get_items_carried)

    def _dropping_items(self):
        '''
        Choose (number of items) random position in decor_object.hallways
        for dropping them in the maze
        '''
        hallways_copy = self.decor_object.hallways.copy()
        # We don't want items dropped into enter/exit
        # removing there position from the hallways set
        hallways_copy.discard(self.decor_object.enter)
        hallways_copy.discard(self.decor_object.exit_maze)
        items_positions = dict()

        # For each items to dropped
        for item in ITEMS_TO_PICKED:
            # Choosing one hallway cell randomly
            random_position = sample(hallways_copy, 1)[0]
            # Removing choosed position,
            # avoiding choising the same more then once
            hallways_copy.discard(random_position)
            # Assigning our item the position choosen
            items_positions[random_position] = item

        return items_positions

    def picked_up_items(self, coordinates):
        '''
        Counting items carried an taking care off removing them from display
        '''
        self._items_carried.append(self.positions[coordinates])
        del self._positions[coordinates]
