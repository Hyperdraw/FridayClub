import urllib.request
import json
import random

#https://hp-api.herokuapp.com/

url = 'http://hp-api.herokuapp.com/api/characters'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
'''
#print(result)
#{'name': 'Argus Filch', 'species': 'human', 'gender': 'male', 'house': '', 'dateOfBirth': '', 'yearOfBirth': '', 'ancestry': 'squib', 'eyeColour': '', 'hairColour': 'grey', 'wand': {'wood': '', 'core': '', 'length': ''}, 'patronus': '', 'hogwartsStudent': False, 'hogwartsStaff': True, 'actor': 'David Bradley', 'alive': True, 'image': 'http://hp-api.herokuapp.com/images/filch.jpg'}]

for person in result[0:-1]:
	print(person['name'])

print(result[5]['name'],"is played by",result[5]['actor'])
print(result[6]['name'],"is played by",result[6]['actor'])
print(result[7]['name'],"is played by",result[7]['actor'])
print(result[0]['name'],"is played by",result[0]['actor'])

'''


choice = input(f"Do you know who plays {result[0]['name']}?")

if choice == result[0]['actor']:
	print("You are right!")
else:
	print("The right answer is",result[0]['actor'])	
	
choice = input(f"Do you know who plays {result[1]['name']}?")	

if choice == result[1]['actor']:
	print("You are right!")
else:
	print("The right answer is",result[1]['actor'])	

number = random.randint(1,10)

choice = input(f"Do you know who plays {result[number]['name']}?")

if choice == result[number]['actor']:
	print("You are right!")
else:
	print("The right answer is",result[number]['actor'])	
	
number = random.randint(1,10)

choice = input(f"Do you know who plays {result[number]['name']}?")

if choice == result[number]['actor']:
	print("You are right!")
else:
	print("The right answer is",result[number]['actor'])	


number = random.randint(1,10)

choice = input(f"Do you know who plays {result[number]['name']}?")

if choice == result[number]['actor']:
	print("You are right!")
else:
	print("The right answer is",result[number]['actor'])	
	
number = random.randint(1,10)

choice = input(f"Do you know who plays {result[number]['name']}?")

if choice == result[number]['actor']:
	print("You are right!")
else:
	print("The right answer is",result[number]['actor'])	
	
number = random.randint(1,10)

choice = input(f"Do you know who plays {result[number]['name']}?")

if choice == result[number]['actor']:
	print("You are right!")
else:
	print("The right answer is",result[number]['actor'])	

number = random.randint(1,10)

choice = input(f"Do you know who plays {result[number]['name']}?")

if choice == result[number]['actor']:
	print("You are right!")
else:
	print("The right answer is",result[number]['actor'])						
