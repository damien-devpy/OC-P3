'''
Contain class MacGyver. In charge of moving Mac and his attributes
Position and status, alive or not
'''

from configuration import UP, RIGHT, DOWN, LEFT


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
        self._position = self.decor_object.enter
        self._alive = True

    def _get_alive(self):
        return self._alive

    alive = property(_get_alive)

    def _get_position(self):
        return self._position

    position = property(_get_position)

    def _up(self):
        '''
        If the user choosing Mac going up, making him up
        '''
        self._position = (self._position[0], self._position[1]-1)

    def _right(self):
        '''
        If the user choosing Mac going right, making him right
        '''
        self._position = (self._position[0]+1, self._position[1])

    def _down(self):
        '''
        If the user choosing Mac going down, making him down
        '''
        self._position = (self._position[0], self._position[1]+1)

    def _left(self):
        '''
        If the user choosing Mac going left, making him left
        '''
        self._position = (self._position[0]-1, self._position[1])

    def movement(self, input_user, previous_position):
        '''
        Making move MacGyver and checking if he's going into a wall
        If so, going back to the previous_position
        '''
        if self.alive:
            if input_user in UP:
                self._up()
            elif input_user in RIGHT:
                self._right()
            elif input_user in DOWN:
                self._down()
            elif input_user in LEFT:
                self._left()

        # If we move into a wall, we going back
        if self.decor_object.is_not_hallways(self):
            self._position = previous_position

    def killing_mac(self):
        '''
        Mac has been killed by guard.
        '''
        self._alive = False
