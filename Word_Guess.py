import random
from time import sleep as s
STAR_WARS = []
loop = 0
counter = 0
JD = 0
lol = 0
Number = 5
print('''
Welcome to WORD GUESS
''')
s(3)
mil = input("""
DIRECTIONS (PRESS ENTER TO CONTINUE)
1. Pick a difficulty
2. Enter 5 words that the computer can pick from
3. Wait while the computer picks a random word from the list of words
4. The computer will ask you to guess a letter from the random word 
   (You get more or less guesses depending on the difficulty you pick)
5. You will attempt to guess the word the computer picked
   (You can also quit there by pressing enter)
""")
list1 = []
Kelly = input("""Select a difficulty
[E]asy
[M]edium
[H]ard
""")

if Kelly == 'E':
  s(1)
  print("You are playing Easy difficulty")
  JD += 8

if Kelly == 'M':
  s(1)
  print("You are playing Medium difficulty")
  JD += 5

if Kelly == 'H':
  s(1)
  print("You are playing Hard difficulty")
  JD += 3

s(2)
while True:
  Molly = input(f'''
  Enter {Number} more words (One at a time): ''')
  list1.append(Molly)
  counter += 1
  Number -= 1
  if counter == 5:
    break

word = random.choice(list1)

for letter in correct:
  STAR_WARS.append(letter.lower())
  STAR_WARS.append(letter.upper())

while True:
  choice = input('''
  Guess a letter: ''')
  if choice in STAR_WARS:
    print("CORRECT")
    loop += 1
    if loop == JD:
      break

  else:
    print("INCORRECT")
    loop += 1
    if loop == JD:
      break

Alyssa = input("""
Try to guess the word 
(Press enter to quit)""")

if Alyssa == correct:
  s(1)
  print("You are Correct")
  s(1)
  lol += 1

if Alyssa == '':
  s(2)

if lol == 0:
  print(f"Incorrect, the correct answer is {correct}")
  s(2)

print('''
  _______ _                 _          ______           _____  _             _             
 |__   __| |               | |        |  ____|         |  __ \| |           (_)            
    | |  | |__   __ _ _ __ | | _____  | |__ ___  _ __  | |__) | | __ _ _   _ _ _ __   __ _ 
    | |  | '_ \ / _` | '_ \| |/ / __| |  __/ _ \| '__| |  ___/| |/ _` | | | | | '_ \ / _` |
    | |  | | | | (_| | | | |   <\__ \ | | | (_) | |    | |    | | (_| | |_| | | | | | (_| |
    |_|  |_| |_|\__,_|_| |_|_|\_\___/ |_|  \___/|_|    |_|    |_|\__,_|\__, |_|_| |_|\__, |
                                                                        __/ |         __/ |
                                                                       |___/         |___/ ''')