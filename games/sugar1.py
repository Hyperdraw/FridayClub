
print("This is a story about an ant")

sugar = 0

def intro(sugar):
	print("You are an aunt, and also an ant")
	print(f'Your sugar balance is {sugar}')	
	
	choice = input("How much sugar would you like?")
	
	choice = int(choice)
	
	sugar += choice

	sugarbank(sugar)
	
def sugarbank(sugar):	
	print(f'Your sugar balance is {sugar}')	
	print('''
	Welcome to the sugar bank!
	Would you like to make a deposit or a withdrawl?
	Type CAT for deposit
	Type SNAKEFACE for withdrawl
	Type HAMSTER to rob the bank
	Type MANGO to light your sugar on fire
	''')

	choice = input("Please pick an option")
	
	if choice == 'CAT':
		print("You add five sugars")
		sugar -= 5
	if choice == 'HAMSTER':
		print("You rob the bank")
		sugar += 500000000	
	if choice == 'MANGO':
		print("You light your sugar on fire")
		sugar = 0	
	else:
		print("You take five sugars")
		sugar += 5
		
		
	print(f'Your sugar balance is {sugar}')	
	
	choice = input("Do you want to play again? y/n ")
	
	if choice == 'y':
		intro(sugar)


intro(sugar)

print("Thanks for playing, game over")
