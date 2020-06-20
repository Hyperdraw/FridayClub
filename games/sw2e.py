from time import sleep
import sys
import random
credits = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000
item = []
Jedi_Skill = 0
Trust = 0
print(" Made by Max(xXFireShadow700Xx) and JD")
sleep(5)
print('''
 _____ ____   ____    __    ___      __    __   ____  ____    _____
 / ___/|    \ /    |  /  ]  /  _]    |  |__|  | /    ||    \  / ___/
(   \_ |  o  )  o  | /  /  /  [_     |  |  |  ||  o  ||  D  )(   \_ 
 \__  ||   _/|     |/  /  |    _]    |  |  |  ||     ||    /  \__  |
 /  \ ||  |  |  _  /   \_ |   [_     |  `  '  ||  _  ||    \  /  \ |
 \    ||  |  |  |  \     ||     |     \      / |  |  ||  .  \ \    |
  \___||__|  |__|__|\____||_____|      \_/\_/  |__|__||__|\_|  \___|         2
                                                                    
 
  ______                          
 |  ____|                         
 | |__   ___  ___ __ _ _ __   ___ 
 |  __| / __|/ __/ _` | '_ \ / _ \

 | |____\__ \ (_| (_| | |_) |  __/
 |______|___/\___\__,_| .__/ \___|
                      | |         
                      |_|                   
''')
print(" As you cruise along in space with me(your humble BB unit) you relax, settling down into your seat.")
sleep(2)
print("Then, all of a sudden, a Star Destroyer comes out of hyperspace.")
sleep(2)
print("wait...")
sleep(5)
print("A STAR DESTROYER?!?!? NANI?!?!")

print('''
      .            .                     .
                  (o)       .                          .            (
                    
                            .        O      .          ()
                                               .
  .        ____.--^.
   .      /:  /    |                               +           .         .
         /:  `--=--'   .                                                .
  LS    /: __[\==`-.___          *           .
       /__|\ _~~~~~~   ~~--..__            .             .
       \   \|::::|-----.....___|~--.                                 .
        \ _\_~~~~~-----:|:::______//---...___
    .   [\  \  __  --     \       ~  \_      ~~~===------==-...____
        [============================================================-
        /         __/__   --  /__    --       /____....----````~~~~      .
  *    /  /   ==           ____....=---=```~~~~ .
      /____....--=-```:~~~~                     .                .
      .       ~--~                               ^     
                     .                        i  A  i
                                              I I_I I         .           .
                          .                         .             +
        .     +              .                                       <=>
                                               .                .      .
   .                 *                 .                *                ` -
''')
sleep(5)
print("The Star Destroyer launched thousands of Tie Daggers...")
sleep(2)
print("It must be a remnant of the Final Order!")
sleep(2)
answers = random.randint(1,2)

if answers <1:
  print("You destroy a couple, along with me, but the overwhelming amount of ties destroy us. HelPmEfZzZz")
  sleep(2)
  print('''
   _____          __  __ ______    ______      ________ _____  
  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ 
 | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |
 | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / 
 | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ 
  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\
  ''')
  sys.exit()
else:
  print("You don't immediately get overwhelmed,")
  sleep(2)
  print("But you get pulled in by their tractor beam")
  sleep(2)
  print("They take away your unlimited credits and your lightsaber")
  credits -= 1000000000
  sleep(2)

print("By some chance you get put into the same cell as Ezra Bridger, along with me.")
sleep(2)
print("Ezra Bridger and his small group of rebels")
sleep(2)
print("Liberated Lothal all by themselves!...")
sleep(2)
print("But he has been missing for years.")
sleep(2)
print("This was the perfect chance to escape!")
sleep(2)
print("You think you have a plan to escape with Ezra?")
sleep(2)
dol = input('''
Do you want to know the plan? y/n''')

if dol == 'y':
  print('''
    The plan is for Ezra to use the force to open the door.
  Then 2BB7(me) will hack into a console and find out
  troop movements so you avoid them.
  Then you will move to the hangar get a ship and escape.''')
  sleep(7)
  print(" Now the game shall continue")
  sleep(2)

if dol == 'n':
  sleep(1)
  print(" Now the game shall continue")
  sleep(2)

print("You are still playing as the pilot")
sleep(2)
STAR_WARS = input('''
  What do you tell him?
[1] I'm with the resistance
[2] I have a plan to escape
''')
if STAR_WARS == '1':
  sleep(1)
  print(" 'What is the resistance?' He asks you.")
  sleep(2)
  print("You realize he wouldn't know what the resistance is")
  sleep(2)
  lol = input('''
    What do you tell him now?
  [1] Explain what the Resistance is
  [2] Tell him your escape plan
  [3] Say nothing
  ''')

  if lol == '1':
    sleep(1)
    print(" He believes you")
    Trust += 1
    sleep(2)
    print(f"Your Trust with Ezra is now level {Trust}!")
    sleep(2)
    dil = input('''
      What do you tell him now?
    [1] Tell him your plan 
    [2] Say nothing
    ''')

    if dil == '1':
      sleep(1)
      print(" He agrees with the plan")
      Trust += 1
      print(f"Your trust level with Ezra is now {Trust}")
    
    if dil == '2':
      sleep(2)
      print(" You miss your opportunity to escape")
      sleep(2)
      print('''
   _____          __  __ ______    ______      ________ _____  
  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ 
 | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |
 | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / 
 | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ 
  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\
    ''')
      sys.exit


  if lol == '2':
    sleep(1)
    print(" He is skeptical, but he agrees with the plan")
  
  if lol == '3':
    sleep(1)
    print(" He now thinks you not trust worthy ")
    sleep(2)
    print("You are now stuck in prison forever")
    sleep(2)
    print('''
     _____          __  __ ______    ______      ________ _____  
    / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ 
   | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |
   | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / 
   | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ 
    \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\ ''')
    sys.exit()

if STAR_WARS =='2':
  sleep(1)
  print(" Why should I trust you")
  sleep(2)
  print("Tip: Explain to him why he should trust you")
  sleep(2)
  lil = input('''
    What do you say to him now?
  [1] Tell him your with the resistance
  [2] It doesn't matter
  [3] Say nothing
  ''')

  if lil == '1':
    sleep(1)
    print(" He asks you  what the restistance is")
    sleep(2)
    print("You tell him it's like the Rebel Alliance")
    sleep(2)
    print("He now agrees to your plan")
    Trust += 1
    print(f"Your Trust with Ezra is now level {Trust}!")

  if lil == '2':
    sleep(1)
    print(" He is skeptical but agrees")
  
  if lil == '3':
    sleep(1)
    print(" He decides you are not trust worthy")
    sleep(2) 
    print("You are stuck in prison forever")
    sleep(2)
    print('''
       _____          __  __ ______    ______      ________ _____  
      / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ 
     | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |
     | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / 
     | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ 
      \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\                                                         
    ''')
    sys.exit()

sleep(2)
print(" Ezra uses the force to open the door.")
sleep(2)
print("I hack into the Scomp link. I will try to help you guys escape.")
sleep(2)
print(" I discovered where the troops move are patrolling next.")
sleep(2)
print("Wait... what's this?")
sleep(3)
print('''_______ _ _ _ __ __ __  _ ___ _   __  ___  __ __  __  _  ___ _ _  __ _______
%=x%=x% | |V| |_)|_ |_) | |_| |   |_) |_| (_  |_  |_) |  |_| |\| (_  %=x%=x%
~~~~~~~ | | | |  |_ | \ | | | |_  |_) | | __) |_  |   |_ | | | | __) ~~~~~~~
 LS
                 .-. .-.
               .=========.         E x t e r i o r ,   A e r i a l   V i e w
               ||.-.7.-.||         -----------------------------------------
               ||`-' `-'||
               `========='
                `-'| |`-'8               1 .............. Sensor Suite Tower
          ______   |9|   ______          2 ... Heavy Twin Turbolaser Turrets
         /     /\__| |__/\     \         3 ............. Heavy Laser Turrets
        /  \_ / /  |_|  \ \ _/  \        4 ....... TIE Fighter Launch Chutes
       /___(\\\/         \///)___\       5 ............... Heavy Blast Doors
       \____\\`==========='//____/       6 .................... Guard towers
       /     '/ .-------. \\     \       7 ........ Shuttle Landing Platform
    __/     //. \`+---+'/ .\\     \__    8 ........... AT-AT Docking Station
   /\ \    ///x`.\|___|/.'x\\\    / /\   9 ................. Connecting Ramp
  /  \ \  //`-._//|   |\\_.2'\\  / /  \
 /  _.-==='_____//.-=-.\\_____`===-._  \
 
 \   `-===.\-.  \ `-=1' /  .-/.===-' 3 / The pre-fabricated,  multi-function
  \  / /  \\\ \  \.===./  /4///  \ \  /  Imperial garrison base is the back-
   \/_/    \\\ | /.---.\ | ///    \_\/   bone of the  Empire's  occupational
      \     \\\|/ |_m_| \|///     /      forces. These heavily-armoured for-
       \_____\=============/_____/       tresses have  walls up to 10 meters
       /____///    ___    \\\____\       thick  to  guard   against   ground
       \   (_//\__|||||__/\\_)   /       assaults,  and  powerful  deflector
        \  /  \|,,|||||,,|/  \  /        shields  protect  them  for  air or
         \_____|  | 5 | 6|_____/         space attacks.
               `--'   `--'
____________________________________________________________________________
%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                           U           E x t e r i o r ,   S i d e   V i e w
                          /_\          -------------------------------------
                       1 [___]
                         :`:':           1 .............. Sensor Suite Tower
                         `:::'           2 ... Heavy Twin Turbolaser Turrets
                  _       :_:       _    3 ............. Heavy Laser Turrets
                =[ ]2     [%]      [ ]=  4 ....... Tie Fighter Launch Chutes
                 :=:      :=:      :=:   5 ............... Heavy Blast Doors
                _|_|_   __| |__   _|_|_  6 .................... Guard Towers
               / /XX|\ /__|_|__\ /|XX\ \
         3    /4/XXX| | _/___\_ | |XXX\ \             7 ....... AT-AT Walker
    --===____/--===X|_|/_______\|_|X===--\____===--   8 ........ AT-ST Scout
     /__| |     /l_\\             //_|\     |_|__\
    /~~.' |    /:'  \\   _____   //  `:\    | `.  \
   /   | .'   / |    \\==|||||==//    | \   `. |   \   7    8
  /   .' |   / .'     |  ||5|| 6|     `. \   | `.   \  xx=   _
 /____|__|__/__|______l__|||||__l______|__\__|__|____\ ll   <~

____________________________________________________________________________
%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                                                 O u t e r   D e f e n s e s
            |                      |             ---------------------------
         ^_[]_^                 ^_[]_^
         |----|               5 |----|        1 ... High Voltage Death Fence
 ________`-..-'________4________`-..-'______  2 ....... Perimeter Gate House
 ===========================================  3 ........ Powered Force Field
          `||'                   `||'         4 .......... Fortified Catwalk
           ||     ^==^   ^==^     ||          5 .......... Observation tower
 ___.____._ll_._1_|--|   |--|___._ll_.____.____
 XXX|XXXX|XIIX|XXX|--| 3 |--|XXX|XIIX|XXXX|XXXX
 XXX|XXXX|XIIX|XXX| 2|   |  |XXX|XIIX|XXXX|XXXX

 The outer perimeter is  marked  by a  high-voltage  "death fence."  Powered
 force fields  placed at regular intervals along the fence may be turned off
 to permit entry and exit.  Observation towers,  connected by fortified cat-
 walks,  are set back from the fence and constantly manned by stormtroopers.
 Other outer  defenses  include energy mine fields,  modified patrol Droids,
 and AT-ST Scout Walkers.

____________________________________________________________________________
%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
             _
            /|                               L a n d i n g   P l a t f o r m
          -==+                               -------------------------------
            :
         [__________]               Up to two Lambda-class shuttles and four
         `' ||  ||`-'               AT-AT  Walkers can dock at the platform.
           ========  =xx            A loading  ramp  leads directly from the
            ||  ||    ll            platform into the garrison complex.
     ~~~~~~~~~~~~~~~~~~~~~~
____________________________________________________________________________
%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                                     I n t e r i o r ,   L e v e l s   1 - 5
                                     ---------------------------------------

          ______         ______      The first 5 levels of the garrison com-
         / ____ \_______/ ____ \     plex are of identical layout, construc-
        / /    \_________/    \ \    ted  around  a  level-spanning  surface
       / /      |   3   |  5   \ \   vehicle bay.  Refer to the key below to
       \ \       \_____/_______/ /   determine what each level contains.
       / /    o   |o o|   o    \ \
    __/ /  2    .' o4o `.    6  \ \__    1 ... Storage Gallery (levels 1-2),
   / __/      .' ._o_o_. `.      \__ \         Armory (levels 3-4), Training
  / /  `-.  .' .'  10   `. `.  .-'  \ \        Facilities   and   Recreation
 / /      ~' .'`-._____.-'`. `~      \ \       Rooms (level 5)
 \ \     o  <  C  | | |  D  >  o  7  / / 2 ... Stormtrooper Barracks (levels
  \ \__      \    ' ' '    /      __/ /        1-3),    Security    Barracks
   \__ \  1  |----  9  ----|~-._ / __/         (levels 4-5)
      \ \    |====    B====|    Y /      3 ...... Base Security (levels 1-5)
       \ \   |----     ----|   / /       4 ......... Turbolifts (levels 1-6)
       / /   |__A_     _ __| 8 \ \       5 .... Detention Block (levels 1-5)
       \ \      | |   | |      / /       6 ... Technical and Service Person-
        \ \_____| |   | |_____/ /              nel Barracks (levels 1-5)
         \_____ `o|   |o' _____/         7 ... Technical Shops (levels 1-2),
               `--'   `--'                     Medical   Bay    (level   3),
                                               Science Labs (levels 4-5)
                8 ... Storage Gallery (levels 1-2), Droid Shops (levels 3-5)
                9 ...................... Surface Vehicle  Bay  (levels 1-5):
                A .................................. AT-ST Scout Walker Bays
                B ........................................ AT-AT Walker Bays
                C ...................... Vehicle Maintenance and Repair Deck
                D ........................................ Speeder Bike Deck
                10 ........................... Miscellaneous Vehicle Parking

____________________________________________________________________________
%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                                           I n t e r i o r ,   L e v e l   6
                                           ---------------------------------
         ____           ____
        / __ \_________/ __ \        Base command personnel,  control rooms,
       / /  \___________/  \ \       trade mission,  and  diplomatic offices
       \ \ o     oo      o / /       are located on this level.
       / /       oo----.   \ \
      / /   8  __oo     `.1 \ \      1 ....... Sensor Monitors, Tractor Beam
   __/ /\    .~  ||   2   \  \ \__                       and Shield Controls
  / __/  \ .' 9.-'`-.      | /\__ \  2 ....................... Computer Room
 / /   o  \|__:   o  :_____|/ o  \ \ 3 ....................... Meeting Rooms
 \ \__  7 .---: 10   :------.3 __/ / 4 ...... Officers' and Pilots' Quarters
  \__ \  /     `-..-'        \/ __/  5 ... Trade Mission, Diplomatic Offices
     \ \/\   5   ||          / /     6 ........... Base Commander's Quarters
      \ \ `.     ||    4    / /                                  and offices
       \ \ o~`---||      o / /       7 ............ Officer Recreation Rooms
       / /6  ____||_____   \ \       8 ............................. Offices
       \ \__/ _________ \__/ /       9 ................... Base Control Room
        \____/         \____/        10 ..................... Reception Area


____________________________________________________________________________
%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                                           I n t e r i o r ,   L e v e l   7
                                           ---------------------------------
        __             __
       /_]\           /[_\        The TIE Fighter  Hanger  Deck  houses  the
       \ \,===========./ /        garrison's TIE fighters in standard-design
       //:o-----------o:\\        ceiling racks.  Bases are usually equipped
      /// X  X X X X  X \\\       with  30 TIE fighters and five TIE bombers
     /// X X  X_X_X  X X \\\      (a single  bomber  takes  up the same rack
  __/// X X   [___]   X X \\\__   space as two fighters).  Five  to 15 ships
 /\_/o X X  1 &/3\&    X X o\_/\  are on constant  patrol,  depending on the
 \]_\\ X X   <\\_//>       //_[/  base's readiness level.
    \\\ X X   \>&</2  X []///
     \\\ X X   []    X []///      1 .............. TIE Fighter Ceiling Racks
      \\\ X   [] []     ///                           (holds up to 40 craft)
       \\:o-----------o://        2 ............. Lift Platforms, to Level 8
       /_/`==========='\_\        3 .................. Flight Control Center
       \_]/           \[_/        X ............................ TIE Fighter
                                  [] ............................ TIE Bomber

____________________________________________________________________________
%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                                           I n t e r i o r ,   L e v e l   8
                                           ---------------------------------
                                                      (not shown)

  The Flight Deck contains the  tractor beam  generators which catapult out-
  going craft into the open sky and reel in landing ships. Pilots relinquish
  control of  their ships during take off and landing because of the limited
  maneuvering area within the chutes.

____________________________________________________________________________
%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%=x%
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                               S u b - L e v e l   I n s t a l l a t i o n s
                               ---------------------------------------------
                                                (not shown)

  A large underground section of the base  houses the main power and back-up
  generators, the tractor beam and deflector shield generators, the environ-
  ment  control  station,  and  the  waste  disposal and refuse units.  Some
  storage facilities are also located here.

''')
sleep(30)
print("I tasered a officer. I copied the keycard, so if you and Ezra can retrieve your lightsaber. ")
sleep(2)
print(" That would be great. I'm hoping we don't run into any worker personel on this battle station.")
sleep(2)
print("WAIT! I realized a flaw in the plan!")
sleep(2)
print('''There is no way we
can get a ship in the hangar without 
being shot down.''')
sleep(5)
print(''' You two tell you to find out
where the Barracks are.''')
sleep(4)
print(" I searched the Scomp link.")
sleep(5)
print("loading...")
sleep(5)
print("loading...")
sleep(5)
print("loading...")
sleep(2)
print("download complete!")
sleep(2)
print("I presented you the map I found earlier to get there.")
sleep(2)
print("We approach the entance to the barracks")
sleep(2)
print(" We burst into the barracks.")
sleep(2)
print('''The Sith troopers are taken by suprise.
This gives Ezra the chance to attack them.''')

answer = random.randint(1,20)

if answer < 2:
  sleep(2)
  print(" A lucky shot from a sith trooper kills you")
  sleep(2)
  print('''
       _____          __  __ ______    ______      ________ _____  
      / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ 
     | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |
     | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / 
     | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ 
      \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\  ''')
  sys.exit()

if answer > 2:
  sleep(2)
  print(" You take out (well mostly Ezra) the sith troopers")
  sleep(2)
  print("You take the ST-W48 blasters that are on the racks")
  sleep(2)
  print("You are now ready to assault the hangar")

sleep(2)
print(''' You are on your way to the hanger when you hear 
footsteps nearby''')

answe = random.randint(1,2)

if answe == 1:
  sleep(2)
  print(''' The foot steps turn around and head in the 
  opposite direction''')
  sleep(2)
  print("You easily take down the Sith Trooper")
  
  if answe == 2:
    sleep(2)
    print("An stray shot from the Sith Trooper kills you")
    sleep(2)
    print('''
         _____          __  __ ______    ______      ________ _____  
        / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ 
       | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |
       | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / 
       | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ 
        \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\ ''')
    sys.exit
if answe == 2:
  print("The footsteps continues in your direction")
  sleep(2)
  print("A Sith Trooper turns around the corner")
  sleep(2)
  print("The Sith Trooper starts firing at you")

  ans = random.randint(1,2)

  if ans == 1:
    sleep(2)
    print("You easily take down the Sith Trooper")
  ans = random.randint(3,4)
  if ans ==2:
    sleep(2)
    print("An stray shot from the Sith Trooper kills you")
    sleep(2)
    print('''
         _____          __  __ ______    ______      ________ _____  
        / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ 
       | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |
       | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / 
       | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ 
        \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\ ''')
    sys.exit
  if ans == 3: 
    print("You evade the shots with ease")
    sleep(2)
    print("So you make the jump to hyperspace")
    sleep(2)

  if ans == 4:
    sleep(1)
    print("You go over to fly in the Special Forces TIE FIGHTER with Ezra")
    sleep(2)
    print("He asks you if you want to fly or if you'll let him fly")
    sleep(2)
    kil = input("Do you let him fly? y/n")

    if kil == 'y':
      sleep(1)
      print("You decide it would be best to let a jedi fly instead of you")
      sleep(4)
      print("You get in the Special Forces TIE FIGHTER")
      sleep(2)
      print("It was a little hard to get 2BB7 in the Special Forces TIE FIGHTER but you manage")
      sleep(5)
      print("Ezra flies you out of the hanger")
      sleep(2)
      print("Then the Star Destoyers Turbo batteries open fire on your ship")
      sleep(2)
      print("But Ezra evades the shots with ease")
      sleep(2)
      print("You tell Ezra make the jump to hyperspace")
      sleep(2)
      print("And he does")

sleep(2)
print("You arrive in the Bespin system")
sleep(2)
print("Now that you are out of harms way you can go wherever you want")
sleep(4)

def planets():
  dad = input("Where do you want to go?\n 1. Naboo      2. Eadu     3. Kashyyyk   4. Geonosis   5. Kamino  6. Dagobah\n    7. Jedha    8. Hoth       9. Endor      10. Chandrilla 11. Mustafar   12. Jakku\n   13. Scarif    14. Coruscant 15. Yavin 16. Tatooine   17. Wobani  18. Mygeeto\n   19. D`qar     20. Christophsis 21. Felucia    22. Utapau  23. Crait     24. Lah’mu \n   25. Takodana 26. Cantonica  27. Bespin  28. Anaxes    29. Dantooine 30. Batuu\n Just saying, you're probably screwed if you visit the other planets") 
  return dad
dad = planets()
def Batuu():
  print(" you fly into the Resistance hangar on Batuu and greet the Resistance troopers.")
  a = input(f'''
  Welcome, weary traveler. Bright Suns.
        You have many credits,I recall...[7] Have some more.  
                                         [m] 
	   How can I help on this amazing day?
     Press [B] to buy and [S] to sell''')
  if a == 'B':
    print('''
    You can buy four things here
      1. Custom Lightsaber- 50,000 credits
	    2. dual WESTAR-35 blasters and a Mandalorian jetpack - 700 credits
      3. a Sith Holocron - 5000 credits
      4. A talking space potato - 2 credits
      ''')
    choice = input("What do you want to buy? 0 to quit ")
    choice = int(choice)
    if choice == 1:
      print("You buy a bunch of parts and choose a blue kyber crystal, which calls to you. Found in the icy caves and caverns of Hoth, this crystal is powerful and serene. YOu take a bantha leather grip and install it. your ignition button is a red circle, and you choose two emmiters- because you have a DOUBLE lightsaber. You ignite the lightsaber, as its cold, crisp,serene coolness flashes in the air. you clip it to your belt.")
      sleep(2)
      print(f'You now have  a lightsaber and too many credits, which is ${credits*0.5}')
      sleep(2)
    if (choice == 2):
      print("You buy the mandalorian package, you gained 2 WESTAR-35 blasters and a mandalorian jetpack.sith troopers burst through the door as you fly up and blast them to bits. Refreshed by the new beskar's scent, you continue on your adventure.")
      sleep(2)
      print(f'You now have  a lightsaber and too many credits, which is ${credits*0.5}')
    if (choice == 3): 
      print("You buy a Sith Holocron")
      print("You play the message and break the holocron with your lightsaber, pulling a black kyber crystal.")
      print(f'You now have  a lightsaber and too many credits, which is ${credits*0.5}')
    print("You buy a talking potato. His name is Bill, and he is a potato. He is very annoying and screams all the time")
    sleep(2)
    print("You scream things like'Do you want to be a baked potato'? and Quiet or I mash you.")
    sleep(2)
    print("But it does not seem to help and the screaming continues. 2-BB7- angrily uses his tool bay to torch the potato, baking it.")
    sleep(2)
  print("You then walk to a milk stand.") 
  sleep(2)
  print(" Welcome to the milk stand. you can buy two items here-blue milk and green milk.The blue milk is from a Bantha and the green milk is from a Thala Siren.")
  requested_toppings = []
  while True:
	  choice = input("What would you like today? ")
	  requested_toppings.append(choice)
	
	  choice = input("Would you like another item? y/n ")
	  if choice == 'n':
	  	break
	
  available_toppings = ['blue milk','green milk']

  for topping in requested_toppings:
	  if topping in available_toppings:
		  print(f'Adding {topping} to your order! that will be 4 credits!')
  print("Thank you for your order")	
  sleep(7)
  print("you then go to the creature stall, and you are greeted by Bina ")
  sleep(5)
  print(''' Welcome to the creature stall! You can buy four things here
    1.  Porg- a cute bird.................................................. 10 credits
	  2. Kowakian monkey lizard-talks........................................ 50 credits
    3. Fire raccoon- can firebend in the cutest ways....................... 200 credits
    4. baby rathlar-dont tell anyone about this black market deal.......... 5000 credits
    5. Tooka cat-cute as hecc.............................................. 150 credits
      ''')
  choice = input("What do you want to buy? 0 to quit ")
  choice = int(choice)
  if choice == 1:
    print("awww. you carry the cage back to your X-wing, and it stares at yew wib the cwoootest eyes evah. ")
    sleep(2)
    print(f'You now have  a porg. And still too many credits.')
    sleep(2)
  if (choice == 2):
    print("You buy the kowakian monkey lizard. it hits me and shoves em across the room, so I kill it.")
    sleep(2)
    print(f'You now have a hole in your savings and somehow too many credits, which is a lot')
  if (choice == 3): 
    print("The fire racoon climbs onto your shoulder, securing itself beside your helmet. he looks at the dunderhead shooting at you, and the poor man is engulfed in a fiery wave of paw slashes.")
    sleep(3)
    print(f'You now have a panda-like guardian. I approve. (and expendable credits, which is a hecc ton.)')
  if (choice == 4):
    print(" you just bought a baby rathlar. it proceeds to try to eat me, but you shove it back in the cage.") 
    sleep(7)
    print(" and you lost all your credits. WHICH WAS EATEN BY THE LITTLE CREATURE.")
  if (choice == 5):
    print(" the owner sells it to you for free. awwww.")
    sleep(2)
    print(" wow! you have a lot of credits!")
 sleep(5)  
  print(" You go back to the Resistance base, talk to Hondo, and fly away.")

if dad == '1':
 Naboo()

if dad == '2':
  Eadu()

if dad == '3':
  Kashyyyk()

if dad == '4':
  Geonosis()

if dad == '5':
  Kamino()

if dad == '6':
  Dagobah()

if dad == '7':
  Jedha()
  
if dad == '8':
  Christophsis()
  
if dad == ' 9':
  Endor()

if dad == '10':
  Chandrilla()

if dad == '11':
  Mustafar()  

if dad == '12':
  Jakku()

if dad == '13':
  Scarif()

if dad == '14':
  Coruscant()

if dad == '15':
  Yavin()

if dad == '16':
  Tatooine()

if dad == '17':
  Wobani()

if dad == '18':
  Mygeeto()
  
if dad == '19':
  Hoth()
  
if dad == '20':
  Dqar()

if dad == '21':
  Felucia()

if dad == '22':
  Utapu()

if dad == '23':
  Crait()

if dad == '24':
  Lahmu()

if dad == '25':
  Takodana()

if dad == '26':
  Cantonica()

if dad == '27':
  Bespin()

if dad == '28':
  Anaxes()

if dad == '29':
  Dantooine()

if dad == '30':
  Batuu()


