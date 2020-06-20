import intro
import pickle
import menu

print("Welcome...")

def login():
  welcome = input("Do you have an acount? y/n: ")
  if welcome == "n":
      while True:
          username  = input("Enter a username: ")
          password  = input("Enter a password: ")
          password1 = input("Confirm password: ")
          if password == password1:
            file = open('users/' + username + ".txt", "wb")
            pickle.dump({'username': username, 'password': password}, file)
            file.close()
            welcome = "y"
            break
          print("Passwords do NOT match!")
          login()

  if welcome == "y":
      while True:
          login1 = input("Login: ")
          login2 = input("Password: ")
          try:
            with open('users/' + login1 + ".txt", "rb") as file:
              data = pickle.load(file)
            
            if data['username'] == login1 and data['password'] == login2:
              name = login1
              file = open("currentaccount.txt", "wb")
              pickle.dump({'Account': name}, file)
              file.close()
              menu.main_menu(name)
              break
            else:
              print("Incorrect username or password.")
              login()
          except FileNotFoundError:
            print('Your account is not found, please try again')
            login()

login()