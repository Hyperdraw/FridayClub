import login
import utils

def main_menu(name):
  while True:
    choice = utils.choice('Main Menu', [
      'Games',
      'Harry Potter Games',
      'Programs',
      'Run Your Own Python Code'
    ], 'What do you want to do?')

    if choice == 0:
      games(name)
    elif choice == 1:
      hpgames(name)
    elif choice == 2:
      programs(name)
    elif choice == 3:
      print('===== Python Runner =====')
      print('Enter your Python code below. Leave blank to end.\n')
      code = ''

      while True:
        line = input('> ')

        if line == '':
          break
        else:
          code += line + '\n'
      
      print('\nRunning This:')
      print(code)
      print('-----')
      exec(code)

def games(name):
  rooms = [
    'this','planet.main','games.swr1r','games.sw2e','games.sw2eJD','games.spacetrails','games.jd','games.sugar1','games.sugar2','games.dog2','games.trivia','games.rhyme','games.walker','games.cookie','games.murder','games.translator','games.orc','games.cataclone1','games.hangman'
  ]

  choice = utils.choice('Games', [
    '[Back]',
    'Zen of Python',
    'Planet Selector',
    'Space Wars 1 - Retirement',
    'Space Wars 2 - Escape (MAXs Version)',
    'Space Wars 2 - Escape (JDs Version)',
    'Space Trails',
    'Star Wars Quiz',
    'Sugar Bank 1',
    'Sugar Bank 2',
    'Dog Adventure 2',
    'Trivia',
    'Rhyme Adventure',
    'Time Travel',
    'Fortune Cookie',
    'Murder Mystery',
    'Translator',
    'Orc',
    'Cataclone',
    'Hangman',
    'Guess the Number'
  ], 'What do you want to do?')

  if choice == 0: return
  exec('import ' + rooms[choice - 1])


def hpgames(name):
  rooms = ['this','hpgames.selection','hpgames.hp_game','hpgames.mm','hpgames.story','hpgames.hpapi','hpgames.elflife','hpgames.pf'
  ]

  choice = utils.choice('Games', [
    '[Back]',
    'Zen of Python',
    'House Selection',
    'Journey of Options',
    'Muggle Madness',
    'Madlibs Story',
    'HP Trivia Game',
    'HP Elf Life',
    'Patronus Finder'
  ], 'What do you want to do?')

  if choice == 0: return
  exec('import ' + rooms[choice - 1])

def programs(name):
  rooms = ['this']

  choice = utils.choice('Games', ['[Back]', 'Zen of Python'], 'What do you want to do?')

  if choice == 0: return
  exec('import ' + rooms[choice - 1])