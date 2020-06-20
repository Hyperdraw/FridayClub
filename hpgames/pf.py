import time
from random import choice as c #random choice
from random import randint as r #random number

points = 0


print(f"""
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
          __            __  _______   _         _____     _____     __      __    _______
          \ \    __    / / |  _____| | |       / ____\   / ___ \   |  \    /  |  |  _____|
           \ \  /  \  / /  | |___    | |      | |       | /   \ |  | \ \  / / |  | |___
            \ \/ /\ \/ /   |  ___|   | |      | |       | |   | |  | |\ \/ /| |  |  ___|
             \  /  \  /    | |_____  | |_____ | |____   | \___/ |  | | \__/ | |  | |_____
              \/    \/     |_______| |_______| \_____/   \_____/   |_|      |_|  |_______|

        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ """)

print(f"To the patronus test! ")


print(f"Would you like to take the test? y/n ")
choice = input (">>> ")
if choice == 'n':
    print(f"So you don't want want to find out what your patronous is, huh? ")
    time.sleep(1)
    print("\n... ")
    time.sleep(1)
    print("\nToo bad you're still taking the test!😜 ")
else:
    print("Great! Let's get started! ")

print("    ")
time.sleep(1)
print("Think happy thoughts... ")

time.sleep(2)
print("    ")
time.sleep(2)

q1 = input('Q1: [a]Dusk or [b]Dawn? ')

if q1 == 'Dusk':
    points += 1
elif q1 == 'a':
    points += 1
elif q1 == 'Dawn':
    points += 2
elif q1 == 'b':
    points += 2

time.sleep(.5)
print("    ")
time.sleep(.5)

q2 = input('Q2: [a]Blood or [b]Bone? ')

if q2 == 'Blood':
    points += 1
elif q2 == 'a':
    points += 1
elif q2 == 'Bone':
    points += 2
elif q2 == 'b':
    points += 2

print("    ")
time.sleep(.5)
print(f"Interesting... ")
time.sleep(.5)
print("    ")

q3 = input('Q3: [a]Sun, [b]Moon, or [c]Stars? ')

if q3 == 'Sun':
    points += 1
elif q3 == 'a':
    points += 1
elif q3 == 'Moon':
    points += 2
elif q3 == 'b':
    points += 2
elif q3 == 'Stars':
    points += 3
elif q3 == 'c':
    points += 3

time.sleep(1)
print("    ")
time.sleep(1)

q4 = input("Q4: [a]Fire, [b]Water, [c]Earth, or [d]Air? ")

if q4 == 'Fire':
    points += 1
elif q4 == 'a':
    points += 1
elif q4 == 'Water':
    points += 2
elif q4 == 'b':
    points += 2
elif q4 == 'Earth':
    points += 3
elif q4 == 'c':
    points += 3
elif q4 == 'Air':
    points += 4
elif q4 == 'd':
    points += 4

print("    ")
time.sleep(1)
print(f"Great answer! ")
time.sleep(1)
print("    ")

q5 = input("Q5: [a]Beach or [b]Savannah? ")

if q5 == 'Beach':
    points += 2
elif q5 == 'a':
    points += 2
elif q5 == 'Savannah':
    points += 3
elif q5 == 'b':
    points += 3

time.sleep(1)
print("    ")

q6 = input("Q6: [a]Blue, [b]Yellow, [c]Green, or [d]Red? ")

if q6 == 'Blue':
    points += 1
elif q6 == 'a':
    points += 1
elif q6 == 'Yellow':
    points += 2
elif q6 == 'b':
    points += 2
elif q6 == 'Green':
    points += 3
elif q6 == 'c':
    points += 3
elif q6 == 'Red':
    points += 4
elif q6 == 'd':
    points += 4

print("    ")
time.sleep(1)
print(f"Difficult, very difficult... ")
time.sleep(1)
print("    ")

q7 = input("Q7: Are you more [a]Benevolent, [b]Knavish, [c]Dauntless, or [d]Intellectual? ")

if q7 == 'Knavish':
    points += 3
elif q7 == 'b':
    points += 3
elif q7 == 'Dauntless':
    points += 4
elif q7 == 'c':
    points += 4
elif q7 == 'Intellectual':
    points += 5
elif q7 == 'd':
    points += 5
elif q7 == 'Benevolent':
    points += 6
elif q7 == 'a':
    points += 6

time.sleep(1)
print("    ")
time.sleep(1)

q8 = input("Q8: [a]Owl, [b]Dog, [c]Cat, or [d]Rabbit? ")

if q8 == 'Owl':
    points += 2
elif q8 == 'a':
    points += 2
elif q8 == 'Dog':
    points += 3
elif q8 == 'b':
    points += 3
elif q8 == 'Cat':
    points += 4
elif q8 == 'c':
    points += 4
elif q8 == 'Rabbit':
    points += 5
elif q8 == 'd':
    points += 5

print("    ")
time.sleep(1)
print(f"Well that changes things! ")
time.sleep(1)
print("    ")

q9 = input("Q9: Are you most afraid of [a]Heights, [b]Spiders, [c]The Dark, or [d]Small Spaces? ")

if q9 == 'Spiders':
    points += 3
elif q9 == 'b':
    points += 3
elif q9 == 'Heights':
    points += 4
elif q9 == 'a':
    points += 4
elif q9 == 'Small Spaces':
    points += 5
elif q9 == 'd':
    points += 5
elif q9 == 'The Dark':
    points += 6
elif q9 == 'c':
    points += 6

time.sleep(1)
print("    ")
time.sleep(1)

q10 = input("Q10: [a]Chocolate or [b]Vanilla? ")

if q10 == 'Chocolate':
    points += 1
elif q10 == 'a':
    points += 1
elif q10 == 'Vanilla':
    points += 2
elif q10 == 'b':

 time.sleep (1)
print("    ")
time.sleep(1)
print(f"I sure hope you weren't lying! ")
time.sleep(1)
print("    ")

q11 = input("Q11: [a]Thunder or [b]Lightning? ")

if q11 == 'Lightning':
    points += 3
elif q11 == 'b':
    points += 3
elif q11 == 'Thunder':
    points += 4
elif q11 == 'a':
    points += 4

time.sleep(1)
print("    ")
time.sleep(1)

q12 = input("Q12: [a]Buckbeak or [b]Norbert? ")

if q12 == 'Norbert':
    points += 5
elif q12 == 'b':
    points += 5
elif q12 == 'Buckbeak':
    points += 4
elif q12 == 'a':
    points += 4

print("    ")
time.sleep(1)
print("Are you thinking about a happy thought? ")
time.sleep(1)
print("    ")

q13 = input("Q13: [a]Winter, [b]Spring, [c]Summer, or [d]Fall? ")

if q13 == 'Winter':
    points += 3
elif q13 == 'a':
    points += 3
elif q13 == 'Spring':
    points += 4
elif q13 == 'b':
    points += 4
elif q13 == 'Summer':
    points += 5
elif q13 == 'c':
    points += 5
elif q13 == 'Fall':
    points += 6
elif q13 == 'd':
    points += 6

time.sleep(1)
print("    ")
time.sleep(1)

q14 = input("Q14: [a]Transfiguration or [b]Charms? ")

if q14 == 'Transfiguration':
    points += 3
elif q14 == 'a':
    points += 3
elif q14 == 'Charms':
    points += 4
elif q14 == 'b':
    points += 4

print("    ")
time.sleep(1)
print("Look! You're getting it! ")
time.sleep(1)
print("    ")

q15 = input("Q15: [a]Invisibility Cloak, [b]Philosopher's Stone, [c]Elder Wand, or [d]Golden Snitch? ")

if q15 == 'Invisibility Cloak':
    points += 3
elif q15 == 'a':
    points += 3
elif q15 == "Philosopher's Stone":
    points += 4
elif q15 == "b":
    points += 4
elif q15 == 'Elder Wand':
    points += 5
elif q15 == 'c':
    points += 5
elif q15 == 'Golden Snitch':
    points += 2
elif q15 == 'd':
    points += 2

time.sleep(1)
print("    ")
time.sleep(1)

q16 = input("Q16: If a fight broke out, would you [a]Join It, [b]Stop It, or [c]Do Nothing? ")

if q16 == 'Join It':
    points += 2
elif q16 == 'a':
    points += 2
elif q16 == 'Stop It':
    points += 4
elif q16 == 'b':
    points += 4
elif q16 == 'Do Nothing':
    points += 3
elif q16 == 'c':
    points += 3

print("    ")
time.sleep(1)
print("Concentrate really hard! ")
time.sleep(1)
print("    ")

q17 = input("Q17: [a]Mountains or [b]Forest? ")

if q17 == 'Mountains':
    points += 2
elif q17 == 'a':
    points += 2
elif q17 == 'Forest':
    points += 3
elif q17 == 'b':
    points += 3

time.sleep(1)
print("    ")
time.sleep(1)

q18 = input("Q18: [a]Wizard Chess or [b]Quidditch? ")

if q18 == 'Wizard Chess':
    points += 3
elif q18 == 'a':
    points += 3
elif q18 == 'Quidditch':
    points += 2
elif q18 == 'b':
    points += 2

print("    ")
time.sleep(1)
print("Here's some butterbeer... for after you finish the quiz! 🍺 ")
time.sleep(1)
print("    ")

q19 = input("Q19: [a]Bertie Botts' Beans or [b]Fizzing Whizbees? ")

if q19 == 'Bertie Botts Beans':
    points += 2
elif q19 == "a":
    points += 2
elif q19 == 'Fizzing Whizbees':
    points += 2
elif q19 == 'b':
    points += 2

time.sleep(1)
print("    ")
time.sleep(1)

q20 = input("Q20: Would you rather battle [a]a Basilisk or [b]Voldemort? ")

if q20 == 'Basilisk':
    points += 5
elif q20 == 'a':
    points += 5
elif q20 == 'Voldemort':
    points += 4
elif q20 == 'b':
    points += 4

print("    ")
time.sleep(1)
print("Last question! ")
time.sleep(1)
print("    ")

q21 = input("Q21: [a]Banshee or [b]Mermaid? ")

if q21 == 'Banshee':
    points += 3
elif q21 == 'a':
    points += 3
elif q21 == 'Mermaid':
    points += 3
elif q21 == 'b':
    points += 3

time.sleep(1)
print("    ")
time.sleep(1)

animals = ['seal','polar bear','arctic fox','arctic hare','walrus','reindeer','narwal','canada lynx','penguin','puffin','snowy owl','beluga whale','orca','moose','wolf','red fox','brown bear','black bear','caribou','beaver','racoon','skunk','porcupine','otter','wolverine','great horned owl','deer','blue whale','octopus','tiger shark','sea turtle','dolphin','humpback whale','stingray','clownfish','pelican','great white shark','pufferfish','rhino','lion','elephant','gazelle','giraffe','zebra','hyena','meerkat','crocodile','ostrich','cheetah','hippo','flamingo','wildebeast','warthog','cow','pig','crow','sheep','chicken','rooster','goat','duck','horse','llama','donkey','turkey','barn owl','black panther','chimpanzee','tucan','parrot','macaw','capybara','mountain gorilla','sloth','jaguar','poison dart frog','anaconda','kangaroo','koala','dingo','wombat','tasmanian devil','platypus','kookoobura','armadillo']

print(f"""
            ____                                      _           _
           / ___\                                    | |         | |
          | |      ___  __ ___    ____ __ __   ____  | |_  ___   | |
          | |     / _ \ ||/__ \  / _  |||/__\ / _  \ | __|/ __|  | |
          | |___ | (_) || /  \ || (_) || /   | (_)  || |_ \__ \  |_|
           \____/ \___/ |_|  |_| \___ ||_|    \___/|| \__||___/  (_)
                                  __/ |
                                 |___/   """)

print("    ")
time.sleep(1)
print("Your patronus is a... ")

if points > 49:
    print("    ")
    time.sleep(2)
    print( {c(animals).title()}, '!!! ')
else:
    print("    ")
    time.sleep(1)
    print(f'You did not get enough points to produce a patronus. Come back soon and try again! ')

print("Points", points)
