import random

bob = random.randint(1,100)

turn = 1
turnsleft = 7

name = input("What is your superhero name? ")

while True:
	print(f'{name.title()}, this is turn {turn}, you have {turnsleft} turns left')
	turn += 1
	turnsleft -=1
	
	fred = input("Please pick a number from 1-100 ")
	fred = int(fred)

	if bob == fred:
		print("You win! You guessed the number!")
		break
	elif bob > fred:
		print("Higher")
	else:
		print("Lower")	

	if turn == 8:
		print("You ran out of turns")
		break


print('''


   ___                   ___              _ 
  / __|__ _ _ __  ___   / _ \__ _____ _ _| |
 | (_ / _` | '  \/ -_) | (_) \ V / -_) '_|_|
  \___\__,_|_|_|_\___|  \___/ \_/\___|_| (_)
                                            


''')

print("The winning number was",bob)
