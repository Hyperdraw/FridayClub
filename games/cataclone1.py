import random
from time import sleep as s 


print("¯\_(ツ)_/¯")

choice = input("Welcome to the cat cloning machine, How many cats do you want?")
choice = int(choice)
s(2)

if choice >= 5:
	print("I am sorry, unless you want to pay for computer repairs, don't go over 5 cats")
	choice = 5
elif choice == 1:
	print("Thank you for ordering one cat")
else:
	print("Thank you for your cat order")

s(2)		
choice2 = input("How many DNA tubes should we use?")
choice2 = int(choice2)

if choice2 > 10:
	
	if choice2 >= 100:
		choice2 = 100
	s(2)
	print("You decide to order more than 10 tubes, and the lab may now explode!")
	s(2)
	boom = random.randint(1,100)
	
	if choice2 > boom:
		print("The lab explodes, GAME OVER")
		s(2)
	elif choice2 == boom:
		print("The lab does not explode")
		print("Your order is on the way")
		s(2)		
	
		print(f"Your order of {choice} cats combined with {choice2} DNA tubes is being processed")	
		s(2)

		cat_factor = random.randint(1,10000)

		print(f'The lab has made you {choice * choice2 * cat_factor} cats!')
		s(2)
	else:
		print("You came close, but the lab is able to process your order")
		s(2)
		print("Your order is on the way")
		s(2)		
		print(f"Your order of {choice} cats combined with {choice2} DNA tubes is being processed")	
		s(2)
		cat_factor = random.randint(1,10000)
		s(2)
		print(f'The lab has made you {choice * choice2 * cat_factor} cats!')
	
else:
	print("Your order is on the way")
	s(2)		
	

	print(f"Your order of {choice} cats combined with {choice2} DNA tubes is being processed")	
	s(2)

	cat_factor = random.randint(1,10000)

	s(2)
	print(f'The lab has made you {choice * choice2 * cat_factor} cats!')
