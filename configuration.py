'''
Contain useful information for running MacGyver maze
Such as maze size, items to display, control keys, ...
'''

# File to load
FILE = 'structure.maze'

# File configuration
WALLS = '#'  # How walls are define in maze file
HALLWAYS = ' '  # How walls are define in maze file
ENTER = 'E'
EXIT_MAZE = 'X'
# This value can be changed to display another maze from another file
SIZE_MAZE = 15

# User controls
UP = ('up', 'z')
RIGHT = ('right', 'd')
DOWN = ('down', 's')
LEFT = ('left', 'q')

# Display configuration
WALLS_TO_DISPLAY = '#'  # Choosing how we want to display walls
HALLWAYS_TO_DISPLAY = ' '  # Choosing how we want to display hallways

ITEMS_TO_PICKED = {
    'syringe.png': '>',
    'pipe.png': '-',
    'ether.png': 'o',
}

SIZE_SPRITES = 35

TOTAL_SIZE = SIZE_MAZE * SIZE_SPRITES

WIN = "Congratulations, you win !"
LOOSE = "The guard killed you, pick up more stuff!"
