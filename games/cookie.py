import urllib.request
import json
import time

while True:

  url = 'https://api.adviceslip.com/advice'
  response = urllib.request.urlopen(url)
  result = json.loads(response.read())

  print('\n\nYou go out for dinner')
  time.sleep(2)
  print('When you are done, you get a fortune cookie')
  time.sleep(2)
  choice = input('Do you want to see what it says? y/n ')
 
  if choice == 'y':
    print(result['slip']['advice'])
    print('\n\n\n')
  else:
    print('You decide not to risk it')
    break  