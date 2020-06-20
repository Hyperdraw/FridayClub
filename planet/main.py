import json
from re import sub
import urllib.request
import random
from utils import yessno
import time
import sys

def PS(Input):
  for x in Input:    
    sys.stdout.write(x) 
    sys.stdout.flush()   
    time.sleep(.025)
  sys.stdout.write('\n')
  time.sleep(2)
  
oxygen_tank=5
radiation_suit=5
gravity_generator=5
thermostat=5
shields=5
emergency_booster=5
credits=1000
cargo_bay=[]

with open('planets_final_final.json', 'r') as myfile:
    data = myfile.read()

# parse file
obj = json.loads('\n'.join([sub(r'^\s*#.*$', '', line) for line in data.splitlines()]))
fil = open('ports.json', "r")
f = fil.read()
obj2 = json.loads('\n'.join([sub(r'^\s*#.*$', '', line) for line in f.splitlines()]))

with open('merchandise.json', 'r') as myfile:
    data_three=myfile.read()

obj4=json.loads(data_three)
# show values
def show_planet(num):
  num = int(num)
  #print(obj[num])

  print("Welcome to Galaxy",str(obj[num]['galaxy']) + "! You are at planet",obj[num]["number"],"which is named",obj[num]["name"])
  if obj[num]["oxygen"] == 0:
     print("There is nothing to breathe")
  else:
    print("There is a good amount of oxygen")
  print(f'''
  =====================================================
                    SECTOR INFO                      
    Name: {obj[num]["name"]}. Annoying Factor {obj[num]["annoyance_factor"]}
    Planet #{obj[num]["number"]} in Galaxy {obj[num]["galaxy"]} Solar System {obj[num]["solar_system"]}
    Oxygen {obj[num]["oxygen"]}   Gravity {obj[num]["gravity"]}  Heat {obj[num]["heat"]}
    Air Pressure {obj[num]["air_pressure"]}   Air Quality {obj[num]["air_quality"]}
    Radioactivity {obj[num]["radioactivity"]} Surface {obj[num]["surface"]} Population {obj[num]["population"]}
    Port Status {obj[num]["port_status"]} 
  ''')


  
  print(f"{obj[num]['nature_factor']}% is how much land is taken up by nature")
  print("A person who lives at this planet their whole life has an average life span of", obj[num]['average_life_span'])
  nn = 0
  if obj[num]['port_status'] == 1:
    nn = 0
    for make in obj:
      if make['port_status'] == 1:
          nn += 1
          if obj[num]['name'] == make['name']:
              main_merch_num=obj[num]["imports"]-1
              print(f'Port Stats:')
              print(f"Port Name: {obj2[nn]['name'].title()}")
              print(f'Main Merchandise: {obj4[main_merch_num]["merchandise_name"].title()}')
              print(f"Main Trader: {obj2[nn]['trader']}")
              print(f"Assistant Trader: {obj2[nn]['assistant']}")
              print(f"Limit of ships: {obj2[nn]['number_limit']}")
              break
          else:
            continue
        
      else:
        continue
  planet=obj[num]
  return planet
  #what this code does is put obj[num] into a single variable, making it easier to type
    
    
def trader_talk(num, num2, num3, num4, num5, credits, oxygen_tank, radiation_suit, gravity_generator, thermostat,shields, emergency_booster):
  num=int(num)
  port_name=obj2[num]["name"]
  port_name=port_name.title()
  PS(f'Hello there! Welcome to the trading port {port_name}')
  PS(f'My name is {obj2[num]["trader"]}, my assistants name is {obj2[num]["assistant"]}, and we are here to help fulfill your intergalactic shopping needs.')
  
  if obj[num]["barter_or_currency"]==0:
    PS("This planet uses a bartering system, which means you trade for goods with other goods, as opposed to currency.")
    PS("Here is a catalog of our merchandise.")
    print(f'''
    ==================================================
                        MERCHANDISE
        Merchandise Name          
        1. Oxygen Tanks           
        2. Radiation Suits        
        3. Gravity Generators     
        4. Nucleoid Thermostats   
        5. Shield Generators      
        6. Emergency Booster      
        7. {obj4[num2]["merchandise_name"].title()}      
    ==================================================
    
    ''')
    time.sleep(2)
    PS("So, what would you like to offer?")
    PS(f"You have {cargo_bay} in your cargo bay, pick the corresponding item number to select it.")
    PS(f"In addition to the items in your cargo bay, you also have {oxygen_tank} oxygen tanks, {radiation_suit} radiation suits, {gravity_generator} gravity generators, {thermostat} nucleiod thermostats, {shields} shield generators and {emergency_booster} emergency boosters that you can sell.")
    PS("Type O for oxygen tank, R for radiation suit,G for gravity generators, T for nucleoid thermostats,S for shield generators and B for emergency boosters.")
    thing_sold=input()
    print("Ok, what would you like to obtain?")
    thing_traded=input()
    if thing_sold=='O' or thing_sold=="o" or thing_sold=='R' or thing_sold=='r' or thing_sold=='G' or thing_sold=='g' or thing_sold=='T' or thing_sold=="t" or thing_sold=='S' or thing_sold=='s' or thing_sold=='b' or thing_sold=='B':
      if thing_traded=='1' or thing_traded=='2' or thing_traded=='3' or thing_traded=='4' or thing_traded=='5' or thing_traded=='6':
        print("That is a good deal!")
        print("Are you sure you want to trade this? Y/N")
        yay_or_nay=input()
        if yay_or_nay=='y' or yay_or_nay=='Y':
          print("Splendid!")
          if thing_sold=='o' or 'O':
            oxygen_tank-=1
          elif thing_sold=='R' or 'r':
            radiation_suit-=1
          elif thing_sold=='G' or 'g':
            gravity_generator-=1
          elif thing_sold=='T' or "t":
            thermostat-=1
          elif thing_sold=='S' or 's':
            shields-=1
          elif thing_sold=='b' or 'B':
            emergency_booster-=1
          if thing_traded=='1':
            oxygen_tank+=1
            print("You have gained one oxygen tank!")
          elif thing_traded=='2':
            radiation_suit+=1
            print("You have gained one radiation suit!")
          elif thing_traded=='3':
            gravity_generator+=1
            print("You have gained one gravity generator!")
          elif thing_traded=='4':
            thermostat+=1
            print("You have gained one nucleoid thermostat!")
          elif thing_traded=='5':
            shields+=1
            print("You have gained one shield generator!")
          elif thing_traded=='6':
            emergency_booster+=1
            print("You have gained one emergency booster!")
      elif thing_traded=='7':
        if obj4[num2]["value"]<=100:
          print("That's a good deal!")
          print("Are you sure you want to do this trade? Y/N")
          trade_or_nah=input()
          if trade_or_nah=='Y' or trade_or_nah=='y':         
            print("Splendid!")
            print(f'You have gained one {obj4[num2]["merchandise_name"]}!')
            cargo_bay.append(obj4[num2]["merchandise_name"])
            if thing_sold=='o' or 'O':
              oxygen_tank-=1
            elif thing_sold=='R' or 'r':
              radiation_suit-=1
            elif thing_sold=='G' or 'g':
              gravity_generator-=1
            elif thing_sold=='T' or "t":                
              thermostat-=1
            elif thing_sold=='S' or 's':                 
              shields-=1
            elif thing_sold=='b' or 'B':
            
              emergency_booster-=1
        else:
          print("That's a terrible deal.")
    else:
      thing_sold_cargo=int(thing_sold)
      thing_sold_cargo-=1
      num_counter=0
      while num_counter!=74:
        if obj4[num_counter]["merchandise_name"]==cargo_bay[thing_sold_cargo]:
          thing_sold_price=obj4[num_counter]["value"]
          break
        else:
          num_counter+=1
      if cargo_bay[thing_sold_cargo]==obj4[num3-1]["merchandise_name"]:
        print(f'Woah, are you offering to sell {obj4[num3-1]["merchandise_name"]}? I will pay extra for that!')
        thing_sold_price=thing_sold_price*1.5
      elif cargo_bay[thing_sold_cargo]==obj4[num4-1]["merchandise_name"]:
        print(f'Woah, are you offering to sell {obj4[num4-1]["merchandise_name"]}? I will pay extra for that!')
        thing_sold_price=thing_sold_price*2
      elif cargo_bay[thing_sold_cargo]==obj4[num5-1]["merchandise_name"]:
        print(f'Woah, are you offering to sell {obj4[num5-1]["merchandise_name"]}? I will pay extra for that!')
        thing_sold_price=thing_sold_price*2.5
      
      if thing_traded=='1' or '2' or '3' or '4' or '5' or '6':
        if thing_sold_price>=100:
          print("That's a very good deal. Are you sure you want to do that? Y/N")
          trade_or_nah=input()
          if trade_or_nah=='y' or trade_or_nah=='Y':
            print("Splendid!")
            cargo_bay.remove(cargo_bay[thing_sold_cargo])
            if thing_traded=='1':
              oxygen_tank+=1
              print("You have gained one oxygen tank!")
            elif thing_traded=='2':
              radiation_suit+=1
              print("You have gained one radiation suit!")
            elif thing_traded=='3':
              gravity_generator+=1
              print("You have gained one gravity generator!")
            elif thing_traded=='4':
              thermostat+=1
              print("You have gained one nucleoid thermostat!")
            elif thing_traded=='5':
              shields+=1
              print("You have gained one shield generator!")
            elif thing_traded=='6':
              emergency_booster+=1
              print("You have gained one emergency booster!")
        else:
          print("That's a terrible deal")      
      elif thing_traded=='7':
          if obj4[num2]["value"]<=thing_sold_price:
            print("That's a good deal!")
            print("Are you sure you want to do this trade? Y/N")
            trade_or_nah=input()
            if trade_or_nah=='Y' or trade_or_nah=='y':
              print("Splendid!")
              print(f'You have gained one {obj4[num2]["merchandise_name"]}!')
              cargo_bay.append(obj4[num2]["merchandise_name"])
              cargo_bay.remove(cargo_bay[thing_sold_cargo])
          
          else:
            print("That's a terrible deal.")

    
  else:
    PS("This planet uses currency, so we will be accepting and paying you with Galactic Credits.")
    if obj4[num2]["value"]==100:
      thangy=", of course"
    else:
      thangy=" (Finally not 100 credits!)"
    PS("Here is a catalog of our merchandise.")
    print(f'''
    ==================================================
                        MERCHANDISE
        Merchandise Name          Price
        1. Oxygen Tanks           100 credits
        2. Radiation Suits        100 credits
        3. Gravity Generators     100 credits again
        4. Nucleoid Thermostats   Yet again, 100 credits
        5. Shield Generators      You guessed it, 100 credits
        6. Emergency Booster      Who would've thought? 100 credits
        7. {obj4[num2]["merchandise_name"].title()}      {obj4[num2]["value"]} credits{thangy}
    ==================================================
                                                           
    ''')
    time.sleep(2)
    PS(f'Unfortunately for us, we have run low on these three resources: {obj4[num3-1]["merchandise_name"]}, {obj4[num4-1]["merchandise_name"]}, and {obj4[num5-1]["merchandise_name"]}. We will pay extra for these specific commodities')
    PS("So, are you here to buy (1), or sell (2)?")
    buy_or_sell=int(input())
    if buy_or_sell==1:
      print("Great! What would you like to buy? I'll tell you our offers again.")
      print(f'Besides the neccessary essentials for space travel, such as oxygen tanks (1), radiation suits (2), gravity generators (3), nucleoid thermostats (4), shield generators (5) and emergency boosters (6), we also specialize in selling {obj4[num2]["merchandise_name"]} (7).')
      thing_bought=int(input())
      if thing_bought==1:
        print("So you want to buy an oxygen tank? That will cost 100 credits.")
        print("Are you sure you want to buy it? Y/N")
        buy_or_nah=input()
        if buy_or_nah=='Y' or 'y':
          print("Ok, that will cost 100 credits")
          if credits<100:
            print("Oh no! It appears you don't have enough credits to buy this!")
          else:
            print("You have bought an oxygen tank!")
            oxygen_tank+=1
            credits-=100
            print(f"You have {credits} credits.")
        else:
          print("Ok then.")
      elif thing_bought==2:
        print("So you want to buy a radiation suit? That will cost 100 credits.")
        print("Are you sure you want to buy it? Y/N")
        buy_or_nah=input()
        if buy_or_nah=='Y' or 'y':
          print("Ok, that will cost 100 credits")
          if credits<100:
            print("Oh no! It appears you don't have enough credits to buy this!")
          else:
            print("You have bought a radiation suit!")
            radiation_suit+=1
            credits-=100
            print(f"You have {credits} credits.")
        else:
          print("Ok then.")
      elif thing_bought==3:
        print("So you want to buy an gravity generator? That will cost 100 credits.")
        print("Are you sure you want to buy it? Y/N")
        buy_or_nah=input()
        if buy_or_nah=='Y' or 'y':
          print("Ok, that will cost 100 credits")
          if credits<100:
            print("Oh no! It appears you don't have enough credits to buy this!")
          else:
            print("You have bought a gravity generator!")
            gravity_generator+=1
            credits-=100
            print(f"You have {credits} credits.")
        else:
          print("Ok then.")     
      elif thing_bought==4:
        print("So you want to buy a nucleoid thermostat? That will cost 100 credits.")
        print("Are you sure you want to buy it? Y/N")
        buy_or_nah=input()
        if buy_or_nah=='Y' or 'y':
          print("Ok, that will cost 100 credits")
          if credits<100:
            print("Oh no! It appears you don't have enough credits to buy this!")
          else:
            print("You have bought a nucleoid thermostat!")
            thermostat+=1
            credits-=100
            print(f"You have {credits} credits.")
        else:
          print("Ok then.")
      elif thing_bought==5:
        print("So you want to buy a shield generator? That will cost 100 credits.")
        print("Are you sure you want to buy it? Y/N")
        buy_or_nah=input()
        if buy_or_nah=='Y' or 'y':
          print("Ok, that will cost 100 credits")
          if credits<100:
            print("Oh no! It appears you don't have enough credits to buy this!")
          else:
            print("You have bought a shield generator!")
            shields+=1
            credits-=100
            print(f"You have {credits} credits.")
        else:
          print("Ok then.")
      elif thing_bought==6:
        print("So you want to buy an emergency booster? That will cost 100 credits.")
        print("Are you sure you want to buy it? Y/N")
        buy_or_nah=input()
        if buy_or_nah=='Y' or 'y':
          print("Ok, that will cost 100 credits")
          if credits<100:
            print("Oh no! It appears you don't have enough credits to buy this!")
          else:
            print("You have bought an emergency booster!")
            shields+=1
            credits-=100
            print(f"You have {credits} credits.")
        else:
          print("Ok then.")
      elif thing_bought==7:
        print(f'So you want to buy a {obj4[num2]["merchandise_name"]}? That will cost {obj4[num2]["value"]} credits.')
        print("Are you sure you want to buy it? Y/N")
        buy_or_nah=input()
        if buy_or_nah=='Y' or 'y':
          print(f'Ok, that will cost {obj4[num2]["value"]} credits')
          if credits<obj4[num2]["value"]:
            print("Oh no! It appears you don't have enough credits to buy this!")
          else:
            print(f'You have bought a {obj4[num2]["merchandise_name"]}!')
            cargo_bay.append(obj4[num2]["merchandise_name"])
            credits-=obj4[num2]["value"]
            print(f"You have {credits} credits.")
        else:
          print("Ok then.")
    if buy_or_sell==2:
      print("Ok, what would you like to sell?")
      print(f"You have {cargo_bay} in your cargo bay, pick the corresponding item number to select it.")
      print(f"In addition to the items in your cargo bay, you also have {oxygen_tank} oxygen tanks, {radiation_suit} radiation suits, {gravity_generator} gravity generators, {thermostat} nucleiod thermostats, {shields} shield generators and {emergency_booster} emergency boosters that you can sell.")
      print("Type O for oxygen tank, R for radiation suit,G for gravity generators, T for nucleoid thermostats,S for shield generators and B for emergency boosters.")
      thing_sold=input()
      if thing_sold=='O' or thing_sold=="o" or thing_sold=='R' or thing_sold=='r' or thing_sold=='G' or thing_sold=='g' or thing_sold=='T' or thing_sold=="t" or thing_sold=='S' or thing_sold=='s' or thing_sold=='b' or thing_sold=='B':
        print("You want to sell this item? You will earn 80 credits. Y/N")
        sell_or_nah=input()
        if sell_or_nah=='Y' or 'y':
          print("Ok, pleasure doing business with you!")
          print("You have earned 80 credits!")
          credits+=80
          print(f'You now have {credits} credits!')
          if thing_sold=='o' or 'O':
            oxygen_tank-=1
          elif thing_sold=='R' or 'r':
            radiation_suit-=1
          elif thing_sold=='G' or 'g':
            gravity_generator-=1
          elif thing_sold=='T' or "t":
            thermostat-=1
          elif thing_sold=='S' or 's':
            shields-=1
          elif thing_sold=='b' or 'B':
            emergency_booster-=1
        else:
          print("Ok then")
      elif thing_sold!='O' and thing_sold!="o" and thing_sold!='R' and thing_sold!='r' and thing_sold!='G' and thing_sold!='g' and thing_sold!='T' and thing_sold!="t" and thing_sold!='S' and thing_sold!='s' and thing_sold!='b' and thing_sold!='B':
        
        thing_sold_cargo=int(thing_sold)
        thing_sold_cargo-=1
        num_counter=0
        while num_counter!=74:
          if obj4[num_counter]["merchandise_name"]==cargo_bay[thing_sold_cargo]:
            thing_sold_price=obj4[num_counter]["value"]
            break
          else:
            num_counter+=1
        if cargo_bay[thing_sold_cargo]==obj4[num3-1]["merchandise_name"]:
          print(f'Woah, are you offering to sell {obj4[num3-1]["merchandise_name"]}? I will pay extra for that!')
          thing_sold_price=thing_sold_price*1.5
        elif cargo_bay[thing_sold_cargo]==obj4[num4-1]["merchandise_name"]:
          print(f'Woah, are you offering to sell {obj4[num4-1]["merchandise_name"]}? I will pay extra for that!')
          thing_sold_price=thing_sold_price*2
        elif cargo_bay[thing_sold_cargo]==obj4[num5-1]["merchandise_name"]:
          print(f'Woah, are you offering to sell {obj4[num5-1]["merchandise_name"]}? I will pay extra for that!')
          thing_sold_price=thing_sold_price*2.5
        print(f'Are you sure you want to sell {cargo_bay[thing_sold_cargo]}? You will earn {thing_sold_price} credits. Y/N')
        sell_cargo=input()
        if sell_cargo=='y' or sell_cargo=='Y':
          print(f"Great! You earned {thing_sold_price} credits!")
          credits+=thing_sold_price
          cargo_bay.remove(cargo_bay[thing_sold_cargo])
          print(f"You now have {credits} credits!")
          print(f"You now have {cargo_bay} in your cargo bay.")
        else:
          print("Ok then")
        

  PS("Would you like to try another transaction? Y/N")    
  purchase_or_nah=input()  
  if purchase_or_nah=='Y' or purchase_or_nah=='y':      
    PS("Splendid! You got me so worked up, I'm going to introduce myself, my products and the way this port works all over again!")
    trader_talk(num, num2, num3, num4, num5, credits, oxygen_tank, radiation_suit, gravity_generator, thermostat,shields, emergency_booster)
  elif purchase_or_nah=='n' or purchase_or_nah=='N':
    PS("Ok then. Off you go!")


planet = show_planet(random.randint(0, 1000))
travel = yessno("Would you like to travel to this planet?")
if travel:
  if planet['radioactivity'] == 1:
    print("WARNING: This planet contains a high radioactivity.")
    if radiation_suit==0:
      print('Oh no! You are out of radiation suits! Your entire crew has died of radiation sickness.')
      print("GAME OVER")
      sys.exit()
    else:
      print("You have used one of your radiation suits.")
      radiation_suit-=1
      print(f"You have {radiation_suit} suits left.")
      
  if planet['explosion_factor'] > 90:
    print("WARNING: This planet has a high explosion factor.")
  if planet['heat'] > 108:
    print("WARNING: This planet has an unlivable temperature")
    if thermostat==0:
      print("Oh no! You are out of nucleoid thermostats!")
      print("Your entire crew has died of heat stroke.")
      print("GAME OVER")
      sys.exit()
    else:
      print("You have used up a nucleoid thermostat")
      thermostat-=1
      print(f"You have {thermostat} nucleoid thermostats left")
  if planet['heat'] < -90:
    print("WARNING: This planet's temperature is extremely low.")
    if thermostat==0:
      print("Oh no! You are out of nucleoid thermostats!")
      print("Your entire crew has died of hypothermia.")
      print("GAME OVER")
      sys.exit()
    else:
      print("You have used up a nucleoid thermostat")
      thermostat-=1
      print(f"You have {thermostat} nucleoid thermostats left")
  if planet['oxygen'] == 0:
    print("WARNING: This planet has no oxygen")
    if oxygen_tank==0:
      print("Oh no! You have run out of oxygen tanks!")
      print("Your entire crew has died of asphxiation")
      print("GAME OVER")
      sys.exit()
    else:
      print("You have used up one of your oxygen tanks")
      oxygen_tank-=1
      print(f"You have {oxygen_tank} oxygen tanks left.")
  if planet['active_war'] > 65:
    print("WARNING: This planet has a high chance of war.")
  if planet["gravity"]==1:
    print("WARNING: The gravity on this planet is far too weak!")
    if gravity_generator==0:
      print("Oh no! You have run out of gravity generators!")
      print("Your entire crew has floated off into space")
      print("GAME OVER")
      sys.exit()
    else:
      print("You have used up one of your gravity generators")
      gravity_generator-=1
      print(f"You have {gravity_generator} gravity generators left")
  elif planet["gravity"]==2:
    print("The gravity here is weaker than you're used to")
    print("However, it is not so weak that you require a gravity generator")
  elif planet["gravity"]==3:
    print("The gravity here is perfect!")
  elif planet["gravity"]==4:
    print("The gravity here is stronger than your used to")
    print("However, it is not so strong that you require a gravity generator")
  elif planet["gravity"]==5:
    print("WARNING: The gravity on this planet is far too strong!")
    if gravity_generator==0:
      print("Oh no! You have run out of gravity generators!")
      print("Your entire crew has been compressed to a pancake on the face of the planet")
      print("GAME OVER")
      sys.exit()
    else:
      print("You have used up one of your gravity generators")
      gravity_generator-=1
      print(f"You have {gravity_generator} gravity generators left")

  if planet['port_status']==1:
    trade=yessno("This planet has a port! Would you like to trade?")
  
    if trade:
      print("Ok, you go to the port and talk to the trader.")
      num2=planet["imports"]
      num3=planet["exports"]
      num4=planet["exports2"]
      num5=planet["exports3"]
      trader_num=random.randint(1,502)
      trader_talk(trader_num, num2, num3, num4, num5, credits, oxygen_tank, radiation_suit, gravity_generator, thermostat,shields, emergency_booster)
    else:
      print("Ok then.")