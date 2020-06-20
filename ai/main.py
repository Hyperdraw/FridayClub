choice = input('Do you want to create or edit a bot or run one? (Type "edit" to create or edit one or "run" to run one.): ')

while choice not in ('edit', 'run'):
  print('Not a valid response.')
  choice = input('Do you want to create or edit a bot or run one? (Type "edit" to create or edit one or "run" to run one.): ')

if choice == 'edit':
  import generate

from json import loads
from random import choice

def chat(npc_path, message):
  with open(npc_path, 'r') as npc_file:
    npc = loads(npc_file.read())
  
  matches = {}

  for i in range(len(npc)):
    rule = npc[i]

    for tag in rule['match']:
      for length in range(1, len(message) + 1):
        for j in range(len(message) - length):
          if message.casefold()[j:j + length] in tag:
            if i not in matches.keys():
              matches[i] = 1
            else:
              matches[i] += 1

  biggest = 0

  for match in matches.keys():
    if matches[match] > matches[biggest]:
      biggest = match
  
  return choice(npc[biggest]["responses"])

npc_path = input('Enter the name of the NPC file to run. (Should end in .json.): ')

while True:
  print(chat(npc_path, input('> ')))