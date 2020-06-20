import sys
import subprocess

def switch(): 
  if len(sys.argv) == 1:
    main()
  elif sys.argv[1] == "inp":
    print(input(''))
  else:
    print("Wrong arguments:", sys.argv[1:])

def main():
  passw = input_timed('You have 10 seconds to enter password:', timeout=10)
  if passw is None: 
    print("Time's out! You explode!")
  elif passw == "PasswordShmashword":
    print("H-h-how did you know you h-h-hacker")
  else:
    print("I spare your life because you at least tried")


def input_timed(*args, timeout, **kwargs):
  """
  Print a message and await user input - return None if timedout
  :param args: positional arguments passed to print()
  :param timeout: number of seconds to wait before returning None
  :param kwargs: keyword arguments passed to print()
  :return: user input or None if timed out
  """
  print(*args, **kwargs)
  try:
    out: bytes = subprocess.run(["python", sys.argv[0], "inp"], capture_output=True, timeout=timeout).stdout
  except subprocess.TimeoutExpired:
    return None
  return out.decode('utf8').splitlines()[0]

switch()