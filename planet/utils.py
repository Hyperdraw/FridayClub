# Yes/No Choice Function
# Call with a question parameter
# Asks the user the question and returns a boolean of whether they answered yes or no
# Use this! Don't make a yes/no prompt yourself!
def yessno(message):
  choice = input(message + ' [y/n]: ')

  while choice not in ('y', 'n'):
    print('Not a valid input.')
    choice = input(message + ' [y/n]: ')
  
  return choice == 'y'

# Multiple Choice Function
# Call with a title message, a list of options, and a question message
# Asks the user to choose and returns the option they chose
# Use this! Don't make a multiple choice prompt yourself!
def choice(message, options, question):
  print(message + '\n')

  for i in range(len(options)):
    print(str(i + 1) + '. ' + options[i])
  
  print('\n')

  while True:
    choice = input(question + ' ')

    try:
      i = int(choice)

      if i < 1 or i > len(options):
        print("That's not a valid option. Try again.")
      else:
        return i - 1
    except ValueError:
      print("That's not even a number! Try again.")