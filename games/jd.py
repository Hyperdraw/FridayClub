from time import sleep
points = 0

print('''
  _____ _______       _____   __          __     _____   _____    ____  _    _ _____ ______
 / ____|__   __|/\   |  __ \  \ \        / /\   |  __ \ / ____|  / __ \| |  | |_   _|___  /
| (___    | |  /  \  | |__) |  \ \  /\  / /  \  | |__) | (___   | |  | | |  | | | |    / / 
 \___ \   | | / /\ \ |  _  /    \ \/  \/ / /\ \ |  _  / \___ \  | |  | | |  | | | |   / /  
 ____) |  | |/ ____ \| | \ \     \  /\  / ____ \| | \ \ ____) | | |__| | |__| |_| |_ / /__ 
|_____/   |_/_/    \_\_|  \_\     \/  \/_/    \_\_|  \_\_____/   \___\_\\____/|_____/_____|''')
sleep(2)
print("    You will be tested on how well you know STAR WARS")
sleep(2)
print("    We will start easy with multiple choice questions")
sleep(2)
print("    Then we will move on to open answer questions")
sleep(2)
print("    There will be a total of twenty questions")
sleep(2)
print("    Note: Answer in uppercase")
sleep(2)
print("    Let us begin")
sleep(2)

while True:
    choice = input('''
    1. What species is Jabba?
    A. Ithorian
    B. Jawa
    C. Jenet
    D. Hutt
    ''')

    if choice == 'D':
        sleep(1)
        print("    Correct")
        sleep(2)
        points += 1
        print(f"    You have {points} points")
        sleep(2)

    else:
        sleep(1)
        print("    Incorrect")
        sleep(2)
        print("    The correct answer is the Hutts")
        sleep(2)
        print(f"    You have {points} points")
        sleep(2)

    lol = input('''
    2. Which order brought about the death of the Jedi?
    A. Order 55
    B. Order 47
    C. Order 66
    D. None of the above
    ''')

    if lol == 'C':
        sleep(1)
        print("    Correct")
        sleep(2)
        points += 1
        print(f"    You have {points} points")
        sleep(2)

    else:
        sleep(1)
        print("    Incorrect")
        sleep(2)
        print("    The correct answer is Order 66")
        sleep(2)
        print(f"    You have {points} points")
        sleep(2)

    kil = input('''
    3. Who played Princess Leia
    A. Gillian Anderson
    B. Sigourney Weaver
    C. Carrie Fisher
    D. Linda Hamilton
    ''')

    if kil == 'C':
        sleep(1)
        print("    Correct")
        sleep(2)
        points += 1
        print(f"    You have {points} points")
        sleep(2)

    else:
        sleep(1)
        print("    Incorrect")
        sleep(2)
        print("    The correct answer is Carrie Fisher")
        sleep(2)
        print(f"    You have {points} points")
        sleep(2)

    lil = input('''
    4. Who are the only two characters who appear in every Star Wars movie?
    A. C-3PO and R2-D2
    B. Luke and Leia
    C. Han and Chewbacca
    D. Darth Vader and Emperor Palpatine
    ''')

    if lil == 'A':
        sleep(1)
        print("    Correct")
        sleep(2)
        points += 1
        print(f"    You have {points} points")
        sleep(2)

    else:
        sleep(1)
        print("    Incorrect")
        sleep(2)
        print("    The correct answer is C-3PO and R2-D2")
        sleep(2)
        print(f"    You have {points} points")
        sleep(2)

    lid = input('''
    5. On which planet do we first meet Rey in The Force Awakens?
    A. Farlax
    B. Tatooine
    C. Dantooine
    D. Jakku
    ''')

    if lid == 'D':
        sleep(1)
        print("    Correct")
        sleep(2)
        points += 1
        print(f"    You have {points} points")
        sleep(2)

    else:
        sleep(1)
        print("    Incorrect")
        sleep(2)
        print("    The correct answer is Jakku")
        sleep(2)
        print(f"    You have {points} points")
        sleep(2)

    liw = input('''
    6. Which furry species lives on the forest moon of Endor?
    A. Ewoks
    B. Wookiees
    C. Hutts
    D. Jawas
    ''')

    if liw == 'A':
        sleep(1)
        print("    Correct")
        sleep(2)
        points += 1
        print(f"    You have {points} points")
        sleep(2)

    else:
        sleep(1)
        print("    Incorrect")
        sleep(2)
        print("    The correct answer is Ewoks")
        sleep(2)
        print(f"    You have {points} points")
        sleep(2)

    lic = input(
    '''
    7. What is the name of Poe Dameron’s astromech droid?
    A. AA-7
    B. BB-8
    C. CC-9
    D. DD-10
    ''')

    if lic == 'B':
        sleep(1)
        print("    Correct")
        sleep(2)
        points += 1
        print(f"    You have {points} points")
        sleep(2)

    else:
        sleep(1)
        print("    Incorrect")
        sleep(2)
        print("    The correct answer is BB-8")
        sleep(2)
        print(f"    You have {points} points")
        sleep(2)

    lik = input('''
    8. Who originally played Han Solo?
    A. Mel Gibson
    B. Harrison Ford
    C. Sylvester Stallone
    D. James Brolin
    ''')

    if lik == 'B':
        sleep(1)
        print("    Correct")
        sleep(2)
        points += 1
        print(f"    You have {points} points")
        sleep(2)

    else:
        sleep(1)
        print("    Incorrect")
        sleep(2)
        print("    The correct answer is Harrison Ford")
        sleep(2)
        print(f"    You have {points} points")
        sleep(2)

    viv = input('''
    9. Who is Boba Fett’s father?
    A. Bat Man
    B. Bob Ross
    C. Jango Fett
    D. Darth Vader
    ''')

    if viv == 'C':
        sleep(1)
        print("    Correct")
        sleep(2)
        points += 1
        print(f"    You have {points} points")
        sleep(2)

    else:
        sleep(1)
        print("    Incorrect")
        sleep(2)
        print("    The correct answer is Jango Fett")
        sleep(2)
        print(f"    You have {points} points")
        sleep(2)

    vib = input('''
    10. Which of these movies is the one where Luke finds out Vader is his father?
    A. Return of the Jedi
    B. The Empire Strikes Back
    C. The Force Awakens
    D. Attack of the Clones
    ''')

    if vib == 'B':
        sleep(1)
        print("    Correct")
        sleep(2)
        points += 1
        print(f"    You have {points} points")
        sleep(2)

    else:
        sleep(1)
        print("    Incorrect")
        sleep(2)
        print("    The correct answer is The Empire Strikes Back")
        sleep(2)
        print(f"    You have {points} points")
        sleep(2)

    print('''
    You're  half way there, keep it up''')
    sleep(2)

    vin = input('''
    11. What is Kylo Ren’s real name?
    A. Tom Solo
    B. Ben Solo
    C. Rick Solo
    D. Frank Solo
    ''')

    if vin == 'B':
        sleep(1)
        print("    Correct")
        sleep(2)
        points += 1
        print(f"    You have {points} points")
        sleep(2)

    else:
        sleep(1)
        print("    Incorrect")
        sleep(2)
        print("    The correct answer is Ben Solo")
        sleep(2)
        print(f"    You have {points} points")
        sleep(2)

    vim = input('''
    12. Who built C-3PO?
    A. Luke
    B. Obi-Wan
    C. Anakin
    D. Yoda
    ''')

    if vim == 'C':
        sleep(1)
        print("    Correct")
        sleep(2)
        points += 1
        print(f"    You have {points} points")
        sleep(2)

    else:
        sleep(1)
        print("    Incorrect")
        sleep(2)
        print("    The correct answer is Anakin")
        sleep(2)
        print(f"    You have {points} points")
        sleep(2)

    vix = input('''
    13. Who plays Rey?
    A. Emma Watson
    B. Daisy Ridley
    C. Anna Paquin
    D. Brianna Hildebrand
    ''')

    if vix == 'B':
        sleep(1)
        print("    Correct")
        sleep(2)
        points += 1
        print(f"    You have {points} points")
        sleep(2)

    else:
        sleep(1)
        print("    Incorrect")
        sleep(2)
        print("    The correct answer is Daisy Ridley")
        sleep(2)
        print(f"    You have {points} points")
        sleep(2)

    viz = input('''
    14. How many parsecs did Han Solo make the Kessel Run in?
    A. 8
    B. 10
    C. 12
    D. 14
    ''')

    if viz == 'C':
        sleep(1)
        print("    Correct")
        sleep(2)
        points += 1
        print(f"    You have {points} points")
        sleep(2)

    else:
        sleep(1)
        print("    Incorrect")
        sleep(2)
        print("    The correct answer is 12")
        sleep(2)
        print(f"    You have {points} points")
        sleep(2)

    vil = input('''
    15. What did Luke cut off the Wampa with his Lightsaber?
    A. Arm
    B. Leg
    C. Head
    D. Tail
    ''')

    if vil == 'A':
        sleep(1)
        print("    Correct")
        sleep(2)
        points += 1
        print(f"    You have {points} points")
        sleep(2)

    else:
        sleep(1)
        print("    Incorrect")
        sleep(2)
        print("    The correct answer is the Wampa's Arm")
        sleep(2)
        print(f"    You have {points} points")
        sleep(2)

    print('''
    That was the last multiple choice question''')
    sleep(2)
    print("    From now on there is only open answer questions")
    sleep(2)

    vik = input('''
    16. How old was Yoda when he died?
    ''')

    if vik == '900':
        sleep(1)
        print("    Correct")
        sleep(2)
        points += 1
        print(f"    You have {points} points")
        sleep(2)

    else:
        sleep(1)
        print("    Incorrect")
        sleep(2)
        print("    The correct answer is the 900 years old")
        sleep(2)
        print(f"    You have {points} points")
        sleep(2)

    vij = input('''
    17. Who did Finn call “Chromedome”?
    ''')

    if vij == 'Captain Phasma':
        sleep(1)
        print("    Correct")
        sleep(2)
        points += 1
        print(f"    You have {points} points")
        sleep(2)

    else:
        sleep(1)
        print("    Incorrect")
        sleep(2)
        print("    The correct answer is Captain Phasma")
        sleep(2)
        print(f"    You have {points} points")
        sleep(2)

    vih = input('''
    18. Who played Mace Windu?
    ''')

    if vih == 'Samuel L. Jackson':
        sleep(1)
        print("    Correct")
        sleep(2)
        points += 1
        print(f"    You have {points} points")
        sleep(2)

    else:
        sleep(1)
        print("    Incorrect")
        sleep(2)
        print("    The correct answer is the Samuel L. Jackson")
        sleep(2)
        print(f"    You have {points} points")
        sleep(2)

    vig = input('''
    19. Who killed Qui-Gon Jinn?
    ''')

    if vig == 'Darth Maul':
        sleep(1)
        print("    Correct")
        sleep(2)
        points += 1
        print(f"    You have {points} points")
        sleep(2)

    else:
        sleep(1)
        print("    Incorrect")
        sleep(2)
        print("    The correct answer is the Darth Maul")
        sleep(2)
        print(f"    You have {points} points")
        sleep(2)

    vif = input('''
    20. Where do Luke and Obi-Wan meet Han and Chewie?
    ''')

    if vif == 'Mos Eisley':
        sleep(1)
        print("    Correct")
        sleep(2)
        points += 1
        print(f"    You have {points} points")
        sleep(2)

    else:
        sleep(1)
        print("    Incorrect")
        sleep(2)
        print("    The correct answer is the Mos Eisley")
        sleep(2)
        print(f"    You have {points} points")
        sleep(2)

    print("    Congratulations, you finished the quiz")
    sleep(2)

    kis = input("    Would you like to see your score? y/n")

    if kis == 'y':
       sleep(1)
       print(f"    You got {points} out of 20")
       if points < 20:
           print("    Keep trying, practice makes perfect")
           sleep(2)
       else:
           print("    You are the ultimate Star Wars Fan!")
           sleep(2)

    if kis == 'n':
        print("OK")
        sleep(2)

    vis = input("    Would you like to play again? y/n")

    if vis == 'y':
        sleep(2)
        points = 0

    else:
        break