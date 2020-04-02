'''
Contain Decor class. In charge of getting structure of maze from a maze file
'''

from configuration import WALLS, HALLWAYS, ENTER, EXIT_MAZE


class Decor:
    '''
    In charge of decor. Managing walls, hallways, enter and exit
    '''

    def __init__(self, maze_file):
        '''
        Calling private method that recovering structure of maze
        and initializing suitable attributes
        '''

        self._get_structure_of_maze(maze_file)

    def _get_structure_of_maze(self, maze_file):
        '''
        Recovering structure of maze from the file
        '''
        self._walls = set()
        self._hallways = set()
        self._enter = None
        self._exit_maze = None

        with open(maze_file, 'r') as f:
            for i, line in enumerate(f):
                for j, letter in enumerate(line):
                    if letter == WALLS:
                        # Building walls in a set
                        self._walls.add((j, i))
                    elif letter == HALLWAYS:
                        # Building hallways in a set
                        self._hallways.add((j, i))
                    elif letter == ENTER:
                        # Creating enter
                        self._enter = (j, i)
                        self._hallways.add((j, i))
                    elif letter == EXIT_MAZE:
                        # Creating exit
                        self._exit_maze = (j, i)
                        self._hallways.add((j, i))

    def _get_walls(self):
        return self._walls

    walls = property(_get_walls)

    def _get_hallways(self):
        return self._hallways

    hallways = property(_get_hallways)

    def _get_enter(self):
        return self._enter

    enter = property(_get_enter)

    def _get_exit_maze(self):
        return self._exit_maze

    exit_maze = property(_get_exit_maze)

    def is_not_hallways(self, macgyver_object):
        '''
        Checking if coordinates wanted by user are an hallway or walls.
        '''
        return macgyver_object.position not in self._hallways
