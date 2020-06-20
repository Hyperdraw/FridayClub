import time
import random

print('''

  _    _ _____    ______ _  __   _      _  __     
 | |  | |  __ \  |  ____| |/ _| | |    (_)/ _|    
 | |__| | |__) | | |__  | | |_  | |     _| |_ ___ 
 |  __  |  ___/  |  __| | |  _| | |    | |  _/ _ \
 | |  | | |      | |____| | |   | |____| | ||  __/
 |_|  |_|_|      |______|_|_|   |______|_|_| \___|
                                                  
                                                  

''')

name = input('Hello student! What is your name? ')


def intro():
	print("Welcome to the world of HP Elf Life!")
	
	

	print(f'Welcome {name}, welcome to Hogwarts!\n')

	choice = input("Are you prepared for adventure? yes or no ")

	if choice == 'yes' or 'y':
		print('Welcome to the adventure')
		choice = input("Please choose your adventure, one or two ")
			
		if choice == 'one':
			pet_story()
		elif choice == 'two':
			colordemontor()
		else:
			intro()
	else:
		print("You are a squib")
		print("Game over")				
 


def pet_story():
	print('\n\nYou have been invited to attend Hogwarts')
	time.sleep(2)
	print('\nA big car lands and you can see a little elf inside')
	time.sleep(2)
	print('\nYou hop in and the elf flies you to Hogwarts')
	time.sleep(2)
	print('\nYou arrive at Hogwarts and can choose a [C]at, an [O]wl, or a [T]oad.')
	time.sleep(2)
	choice = input('What do you choose? ')
	
	if choice == 'C' or 'Cat' or 'cat':
		print('They give you a cat and you are bitten in the face!!!!\n')
		time.sleep(2)
		print('You are next going to the sorting hat')
		time.sleep(2)
		sortinghat()
	elif choice == 'O' or 'Owl' or 	'owl':
		print('You got an owl and he wants to eat a mouse.')
		print('You are not a mouse, but he still tried to eat you!')
		print('You are next going to the sorting hat')
		time.sleep(2)
		sortinghat()
	else:
		print('you picked toad, who is also magic. Problem, he wants to transform you into a frog')
		time.sleep(2)
		print('too bad you have to get sorted looking all green')
		time.sleep(2)
		print('You are next going to the sorting hat')
		time.sleep(2)
		sortinghat()	

def sortinghat():
	print('''	
	 _____            _   _             _    _       _   _ 
	  / ____|          | | (_)           | |  | |     | | | |
	 | (___   ___  _ __| |_ _ _ __   __ _| |__| | __ _| |_| |
	  \___ \ / _ \| '__| __| | '_ \ / _` |  __  |/ _` | __| |
	  ____) | (_) | |  | |_| | | | | (_| | |  | | (_| | |_|_|
	 |_____/ \___/|_|   \__|_|_| |_|\__, |_|  |_|\__,_|\__(_)
	                                 __/ |                   
	                                |___/                    
	''')
	
	name = input("Hello student, what is your name? ")
	
	gryffindor = 0
	ravenclaw = 0
	slytherin = 0 
	hufflepuff = 0 
	
	print(f"{name.title()}, here are the houses: [G]ryffindor, [R]avenclaw, [S]lytherin, or [H]ufflepuff")
	
	q1 = input('Which house to you like more? ')
	
	if q1 == "G":
		gryffindor += 1
	elif q1 == "R":
		ravenclaw += 1
	elif q1 == "S":
		slytherin += 1
	else:
		hufflepuff += 1
		
		
	q2 = input(f"{name.title()}, are you He Who Shall Not be Named? y/n ")
	
	if q2 == 'y':
		slytherin += 20
		print("Uh, we know who you are now...")	
		
	q3 = input(f"{name.title()}, which color do you prefer? [R]ed, [Y]ellow, [B]lue, [Green] ")	
	
	if q3 == "R":
		gryffindor += 1
	elif q3 == "B":
		ravenclaw += 1
	elif q3 == "G":
		slytherin += 1
	else:
		hufflepuff += 1
	
	q4 = input(f"{name.title()}, are you brave? y/n ")
	
	if q4 == "y":
		gryffindor += 1
		hufflepuff += 1
	
	q5 = input(f"{name.title()}, do you like eating breakfast with dementors? y/n ")
	
	if q5 == "y":
		slytherin += 2
	else:
		gryffindor += 1
		hufflepuff += 1
		ravenclaw += 1
			
	q6 = input(f'What is your favourite animal? [L]ion, [S]nake, [B]adger, [E]agle ')
	
	if q6 == "L":
		gryffindor += 1
	elif q6 == "E":
		ravenclaw += 1
	elif q6 == "S":
		slytherin += 1
	else:
		hufflepuff += 1
		
	
			
		
	print("G",gryffindor)
	print("R",ravenclaw)
	print("S",slytherin)
	print("H",hufflepuff)			


def colordemontor():
	print('What is your favourite color? Yellow Red Green Blue')


def fish():
	print('''The Anaphelous Maximus Scalos, also known as the great fish of the deep, 
	is quite the unusual sort. It eats anything relatively poisonous, such as Venomus 
	Tentacula and Devil's Snare, and fancy dress robes. it is your job to feed it, but you 
	only have, 1 an (pet) 2 school robes 3 yourself and 4 your spellbook. what will you feed him?
	''')


while True:
	intro()
