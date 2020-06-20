import random
import time

print('''
#####################################
#                                   #
#       A BAD DAY AT HOGWARTS!      #
#            by Tom Riddle          #
#                                   #
#####################################
''')

def intro():
	
	name = input("Welcome! What is your name? ")
	
	print(f'''
	
	{name}, Welcome to Hogwarts!
	
	These are the spells you can choose:
	
	avada kedavra - kills people
	locomotor - hoists you up like Lucy
	oblivio - wipes your enemies memory
	reducto - blows something up BOOM
	expelliarmius - disarms opponent
	''')
	
	
	spells = ['avada kedavra','locomotor','oblivio','reducto','expelliarmius']
	time.sleep(3)
	print(f"{name}, you go to Hogwarts and youre having a bad day")
	time.sleep(3)
	print(f'It seems like you made an enemy on the first day, and now is seems Draco is mad.')
	time.sleep(3)
	print(f'All you wanted to do is eat some chocolate snitches and have a pumpkin juice...')
	time.sleep(3)
	print(f'Now youre worried about getting some terrible hex put on you\n\n')
	time.sleep(3)
		
	fight_choice = input("Do you want to [fight] or hear the [story]? ")
	
	if fight_choice == 'fight':
		fight()
	elif fight_choice == 'story':
		story()
	else:
		intro()	
	

def fight():
	print("\n")
	our_spell = input("Which spell do you choose? ")
	
	time.sleep(3)
	
	spells = ['avada kedavra','locomotor','oblivio','reducto','expelliarmius']
	
	#draco = random.choice(spells)
	#draco = 'avada kedavra'
	draco = 'oblivio' #this forces draco to pick oblivio
	
	print(f'Draco looks at you, and pulls out his wand and...')
	time.sleep(2)
	print("\n\n")
	
	print(draco)
	print("\n\n")
	time.sleep(2)
	print("\n\n")
	
	if draco == 'avada kedavra' and our_spell == 'avada kedavra':
		print('Draco used an unforgivable curse, and kills you.')
		time.sleep(2)
		print('You are frying like an old piece of bacon on the sidewalk a hot day')
		time.sleep(2)
		print('You realize that challanging Draco was not a good idea')
		time.sleep(2)
		print('Draco gets expelled, but....')
		time.sleep(2)
		print('You are dead.... Draco is also dead... Game over')
		time.sleep(2)
		print('Both of your corpses are expelled from Hogwarts')
		time.sleep(2)
		dead()
	elif draco == 'locomotor' and our_spell == 'locomotor':
		print('You both float in the air and are hoised up')
		time.sleep(2)
		print('Its like an invisible rope is holding you up by your ankles')
		time.sleep(2)
		print('You float but you get ready to cast a spell of your own...')
		time.sleep(2)
		print('You are now stuck on the ceiling and need to call for help')
	elif draco == 'oblivio' and our_spell == 'oblivio':
		print('What just happened? Who am I? Who is this guy?')
		time.sleep(2)
		print('You cant remember anything, but this you may be a sponge or a block of cheese')
		time.sleep(2)
		print('Unsure of who you are or where you are, you are sent to St. Mungos for treatment')
		time.sleep(2)
		print('You both have no idea who you are and go to St. Mungos forever')
		time.sleep(4)
		
		symbollist = ['1','0','1','0','1','0','   oblivio   ']
		for i in range(1,100):
			print(f'{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}')
			time.sleep(0.1)
		
		mungo()
	elif draco == 'reducto' and our_spell == 'reducto':
		redu = random.randint(1,2)
		if redu == 1:
			print("Draco misses")
			time.sleep(2)
			fight()
		else:
			print("You get knocked back into the wall")
			time.sleep(2)
			fight()
	else:
		print("You are disarmed, and now have no wand")
		time.sleep(2)
		print("Perhaps challanging someone with such a great hair cut was a terrible idea")
		time.sleep(2)
		print("You really regret your choices and decide to go home and try another way")
		time.sleep(2)
		intro()			
		
	
def story():
	print('You go to Diagon Ally to get your school suplys and you see Voldemort!!!')
	print('You have three choices:')
	print('''
	         [A] run away and come back later 
	         [B] ask him what he is doing there
	         [C] ask him if you can be a death eater
	         \n''')
	time.sleep(3)
	choice = input("Pick an option... ")
	if choice == 'A':
		time.sleep(3)
		print('return later get your school suplys and go to Hogworts')
	elif choice == 'B':
		time.sleep(3)
		print('he looks at you laughs and says “Avada Kedabra” and you die')
		dead()
	else:
		time.sleep(3)
		print('He considers it then says “finish your magical education first then I will see… ')
		time.sleep(3)
		print('you will also need to be sorted into Slytherin.”')
		time.sleep(3)
		print('You nod and leave (after you get all your school suplys of course)')
		time.sleep(3)
	
	intro()	
		
	
def dead():
	print("Sadly, you are dead, game over")
	time.sleep(3)
	
	symbollist = [' wand ',' potato ',' 2 ','2','2']
	for i in range(1,100):
		print(f'{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}{random.choice(symbollist)}')
		time.sleep(0.1)
	again()
	
def mungo():
	print("You are hospitalized")
	again()


def again():
	choice = input("Do you want to play again? y/n ")
	
	if choice -- 'y':
		intro()	
	
	
intro()		
 
