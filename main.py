import configuration
from decor import Decor
from macgyver import MacGyver
from items import Items
from guard import Guard
from displayterminalmode import DisplayTerminalMode
from displaygraphicmode import DisplayGraphicMode
import os
	
def terminal_mode():
	
	structure = Decor(configuration.FILE)
	hero = MacGyver(structure)
	stuff = Items(structure)
	pnj = Guard(structure)
	displaying = DisplayTerminalMode(structure, hero, stuff, pnj)
	
	while True:
		
		if hero.position in stuff.positions:
		#If Mac coordinates matches with an item
			stuff.picked_up_items(hero.position)
			#Picking up this one
		displaying.refresh()
		print(f'Items carried: {len(stuff.items_carried)}')
		#Displaying decor
		
		choice = input()
		print()
		#Asking user wiche way he want to drive MacGyver
		
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
	
	os.system('pause')
	
def graphic_mode():

	structure = Decor(configuration.FILE)
	hero = MacGyver(structure)
	stuff = Items(structure)
	pnj = Guard(structure)
	displaying = DisplayGraphicMode(structure, hero, stuff, pnj)
	continuer = True
	
	displaying.repeat(150, 50)
	
	while continuer:
		input_made = False
		if hero.position in stuff.positions:
			stuff.picked_up_items(hero.position)
			displaying.counter()
			
		displaying.refresh()
		
		continuer, choice = displaying.input_user()
			
		previous_position = hero.position
		hero.movement(choice, previous_position)
		
		if hero.position == pnj.position:
			if len(stuff.items_carried) == len(configuration.ITEMS_TO_PICKED):
				pnj.killing_guard()
				displaying.refresh()
				displaying.display_text(configuration.WIN)
			else:
				hero.killing_mac()
				displaying.refresh()
				displaying.display_text(configuration.LOOSE)
	
terminal_mode()	


	