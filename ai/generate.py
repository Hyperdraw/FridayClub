from json import loads, dumps
from os.path import exists

print('=====')
print('This tool will help you ceate an NPC JSON file.')
print('You will be continuously asked for questions and responses until you press stop.')
print('=====')
npc_path = input('Enter the name of a file to edit or create. (Should end in .json): ')

if exists(npc_path):
  with open(npc_path, 'r') as npc_file:
    npc = loads(npc_file.read())
else:
  npc = []

print()

while True:
  print('Add Rule #' + str(len(npc)))
  print('-----')
  print('Begin entering patterns (messages similar to what the user will enter to trigger this rule).')
  matches = []

  while True:
    match = input('Enter a pattern or leave blank to end: ')

    if len(match.strip()) == 0:
      break
    else:
      matches.append(match.strip().casefold())
  
  print()
  print('Begin entering possible responses. (The bot will choose a random response from this list when this rule is triggered.)')
  responses = []

  while True:
    response = input('Enter a response or leave blank to end: ')

    if len(response.strip()) == 0:
      break
    else:
      responses.append(response.strip().casefold())
  
  npc.append({"match": matches, "responses": responses})

  with open(npc_path, 'w+') as npc_file:
    npc_file.write(dumps(npc))
  
  print('-----')
  print()