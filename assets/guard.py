'''
Contain class Guard, getting his position and status, alive or dead
'''


class Guard:
    '''
    Getting coordinates of the exit of the maze for guard position
    '''

    def __init__(self, decor_object):
        '''
        Assigning to the guard his position, given decor.object.exit_maze
        '''
        self.decor_object = decor_object
        self._position = self.decor_object.exit_maze

    def _get_position(self):
        return self._position

    position = property(_get_position)

    def killing_guard(self):
        '''
        Guard has been killed by Mac, deleting his position
        '''
        self._position = 0
