import configuration
from decor import Decor
from macgyver import MacGyver
from items import Items
from guard import Guard
from displayterminalmode import DisplayTerminalMode
from displaygraphicmode import DisplayGraphicMode
	
def terminal_mode():
	'''
	Display in the terminal, by using class DisplayTerminalMode()
	'''
	
	structure = Decor(configuration.FILE)
	hero = MacGyver(structure)
	stuff = Items(structure)
	pnj = Guard(structure)
	displaying = DisplayTerminalMode(structure, hero, stuff, pnj)
	continuer = True
	
	while continuer:
		
		#If Mac coordinates matches with an item
		if hero.position in stuff.positions:
			#Picking up this one
			stuff.picked_up_items(hero.position)
			
		#Displaying decor
		displaying.refresh()
		print(f'Items carried: {len(stuff.items_carried)}')
		
		#Asking user wiche way he want to drive MacGyver
		choice = input()
		print()
		
		#If user want to quit
		if choice == 'exit':
			continuer = False

		previous_position = hero.position
		#Storing current position of Mac, in case user drive into a wall
		
		hero.movement(choice, previous_position)
		#Applying user input to MacGyver
		
		if hero.position == pnj.position:
			if len(stuff.items_carried) == len(configuration.ITEMS_TO_PICKED):
				pnj.killing_guard()
				displaying.refresh()
				print(f'{configuration.WIN}\n')
				break
			else:
				hero.killing_mac()
				displaying.refresh()
				print(f'{configuration.LOOSE}\n')
				break
	
def graphic_mode():
	'''
	Display in a window with sprites, by using class DisplayGraphicMode()
	'''

	structure = Decor(configuration.FILE)
	hero = MacGyver(structure)
	stuff = Items(structure)
	pnj = Guard(structure)
	displaying = DisplayGraphicMode(structure, hero, stuff, pnj)
	continuer = True
	
	#Delay and interval we want to watch over key pressed
	displaying.repeat(150, 50)
	
	while continuer:
		#If MacGyver is on an item, picking it up
		if hero.position in stuff.positions:
			stuff.picked_up_items(hero.position)
			displaying.counter()
			
		#After each move, we refreshin the display
		displaying.refresh()
		
		#Waiting for input user
		continuer, choice = displaying.input_user()
			
		#Moving MacGyver according user choice
		previous_position = hero.position
		hero.movement(choice, previous_position)
		
		#If Mac reach the end of maze
		if hero.position == pnj.position:
			#And picked all items, user wins
			if len(stuff.items_carried) == len(configuration.ITEMS_TO_PICKED):
				pnj.killing_guard()
				displaying.refresh()
				displaying.display_text(configuration.WIN)
			#Else, Mac die
			else:
				hero.killing_mac()
				displaying.refresh()
				displaying.display_text(configuration.LOOSE)
	
def main():
	print("\n0: Terminal mode (Use ZQSD keys + ENTER to move, 'exit' to quit)")
	print("1: Graphic mode (Use arrow keys to move, ESCAPE to quit)\n")
	
	
	input_ok = False
	
	while not input_ok:
		try:
			input_user = int(input('In wich mode do you want to play ?\n'))
			print()
			input_ok = True
		except ValueError:
			print("\n0: Terminal mode (Use ZQSD keys + ENTER to move, 'exit' to quit)")
			print("1: Graphic mode (Use arrow keys to move, ESCAPE to quit)\n")
			
	if input_user:
		graphic_mode()
	else:
		terminal_mode()

if __name__ == '__main__':
	main()
	