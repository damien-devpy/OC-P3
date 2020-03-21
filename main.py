import configuration
from decor import Decor
from macgyver import MacGyver
from items import Items
from guard import Guard
from displayterminalmode import DisplayTerminalMode
import os
	
def terminal_mode():
	
	structure = Decor(configuration.FILE)
	hero = MacGyver(structure)
	stuff = Items(structure)
	pnj = Guard(structure)
	displaying = DisplayTerminalMode()
	
	while True:
		
		if hero.position in stuff.positions:
		#If Mac coordinates matches with an item
			stuff.picked_up_items(hero.position)
			#Picking up this one
		displaying.refresh(structure, hero, stuff, pnj)
		print(f'Items carried: {stuff.items_carried}')
		#Displaying decor
		
		choice = input()
		print()
		#Asking user wiche way he want to drive MacGyver
		
		previous_position = hero.position
		#Storing current position of Mac, in case user drive into a wall
		
		hero.movement(choice, previous_position)
		#Applying user input to MacGyver
		
		if hero.position == pnj.position:
			if stuff.items_carried == 3:
				pnj.killing_guard()
				displaying.refresh(structure, hero, stuff, pnj)
				print('Congratulations, you won!\n')
				break
			else:
				hero.killing_mac()
				displaying.refresh(structure, hero, stuff, pnj)
				print('The guard killed you, pick up more stuff\n')
				break
	
	os.system('pause')
	
terminal_mode()	


	