
def intro():
	
	print("This is the intro")
	print("Where do you want to go?")
	
	choice = input("You can go to room [1] or room [2] ")
	
	if choice == '1':
		room1()
	else:
		room2()	
	
def room1():
	print("This is room 1")
	
	choice = input("Do you want to play again? y/n ")
	if choice == 'y':
		intro()

def room2():
	print("This is room 2")
	
	choice = input("Do you want to play again? y/n ")
	if choice == 'y':
		intro()
	
	
	
	
	
	
intro()	


print("game over")
