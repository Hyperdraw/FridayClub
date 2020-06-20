def intro():
  print('=== Time Travel ===')
  print('...Everything goes black, and after a few long minutes, you hear a deep voice...')
  print('"Welcome to the Origin. This is the place from which all of the Universe began, and the source of all matter and energy lies here. You have been sent here because the Universe you were in has been destroyed. It is now up to you to travel back in time and stop this disaster, or you will be forced to live in another Universe."')

  again = True

  while again:
    choice = input("Do you want to try to save your Universe? (If you don't, you must live in anothe Universe forever.) [y/n]: ")

    if choice == 'y':
      pass
    elif choice == 'n':
      print('You hear the booming voice say, "Well, then, if that is your choice, then you may go." Everything goes black, and then you wake up in another Universe, and you must live there forever.')

      travel_again = True

      while travel_again:
        travel = input("Time travel back and make a different choice? (If you don't, the game will end.) [y/n]: ")

        if travel == 'y':
          again = False
          intro()
        elif travel == 'n':
          again = False
          return
        else:
          print('The instructions were very clear: answer "y" or "n"! Try again.')
    else:
      print('The instructions were very clear: answer "y" or "n"! Try again.')

intro()