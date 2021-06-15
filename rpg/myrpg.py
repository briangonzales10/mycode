#!/usr/bin/python3
'''
Space launch RPG by Brian
'''
import os
import requests
import random

#API endpoint for random APOD
API = "https://api.nasa.gov/planetary/apod?count=1"

def returnKey():
  """Returns API key from key.txt"""
  with open("./key.txt", "r") as mykey:
    nasakey = mykey.read()
  nasakey = "&api_key="+ nasakey
  return nasakey

def showInstructions():
  #print a main menu and the commands
  print('''
Space Launch RPG
==============
Commands:
  go [direction]
  get [item]
  use [object]
''')

def showStatus():
  #print the player's current status
  os.system("clear")
  
  print(lastAction)
  print('---------------------------')
  print('You are at the ' + currentRoom +"!" +"\n")
  print(rooms[currentRoom]['description'] + "\n")
  #Find direction options:
  print("Direction Options:")
  for options in rooms[currentRoom]:
      if options != 'item' and options != 'description' and options != 'use':
          print(options)
  print('-----------------')
  
  
  #print the current inventory
  print('Inventory : ' + str(inventory))
  print('-----------------')
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
    print('-----------------')
  #print use options per room
  if "use" in rooms[currentRoom]:
        print('You can USE the following objects: ' + rooms[currentRoom]['use'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []
#other flags
lastAction = ""
simcount = 0

#Super win flag is if telescope is used
telescopeUsed = False
navigationSet = False
rocketUsed = False

# A dictionary linking a room to other rooms
rooms = {

            'Observatory' : {
                  'east'  : 'Winding Mountain',
                  'item'  : 'notes',
                  'description' : 'A gentle dome with a telescope peaking out observing the universe.',
                  'use' : 'telescope'
                },

            'Winding Mountain' : {
                  'north' : 'Launch Pad',
                  'west'  : 'Observatory',
                  'east' : 'Winding Mountain',
                  'south' : 'Winding Mountain',
                  'description' : 'A winding mountain trail with rough terrain.  It looks confusing, but you can see the observatory at the top and launch pad at the bottom',                
                },
            'Launch Pad' : {
                  'north' : 'Control Room',
                  'south': 'Winding Mountain',
                  'description' : 'A simple pad with a simple rocket almost ready for launch.  Just waiting for you, her sole crewmember',
                  'use' : 'rocket',
               },
            'Control Room' : {
                  'north' : 'Lounge',
                  'south' : 'Launch Pad',
                  'description' : 'Just a bunch of laptops overlooking the launch pad.  You can set your launch destination here',
                  'use' : 'computer'
               },
            'Lounge' : {
                'east' : 'Fuel Storage',
                'west' : 'Quarters',
                'south' : 'Control Room',
                'item' : 'whiskey',
                'description' : 'Nothing much here but a bunch of chairs and tables. Oh is that Janus in the corner?',
                'use' : 'janus'
             },
            'Fuel Storage' : {
                'west' : 'Lounge',
                'item' : 'fuel',
                'description' : 'A dumpy looking room lined with fusion cores.  This is how we store our fuel?'
             },
            'Quarters' : {
                'east' : 'Lounge',
                'west' : 'Training Room',
                'description' : 'Just a well made twin bed and a desk with a lamp turned off.  Now is no time for napping though.'
                
             },
            'Training Room' : {
                'east' : 'Quarters',
                'item' : 'books',
                'description' : 'The training room has a simulator in the corner for how to maneuver your ship.  You should probably brush up and take some reference materials with you',
                'use' : 'simulator'
             },
         }
#Janus Words
janusWords = ['Hello, are you ready for your journey?', 'Remember to pick up the navigation notes from the observatory!', 'Did you try out the new simulator in the training room? It\'s great!', 'Be careful when getting the fuel from the fuel depot..', 'Don\'t you dare try to launch the rocket before you\'re ready!']



#start the player in the Hall
currentRoom = 'Launch Pad'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go' and move[1] != 'item' and move[1] != 'description' and move[1] != 'use':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
      lastAction = ""
    #there is no door (link) to the new room
    else:
        lastAction = 'You can\'t go that way!'

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      lastAction = f'{move[1]} recieved!'
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
       lastAction = f"Can't get{move[1]}!"
  
  #define USE for objects in game
  if move[0] == 'use':
        
    #Just for fun
    if move[1] == 'whiskey' and 'whiskey' in inventory:
            lastAction = "You've passed out drunk from too much whiskey!"
            inventory.remove('whiskey') 
            currentRoom = "Quarters"
            
    if "use" in rooms[currentRoom] and move[1] in rooms[currentRoom]['use']:
      lastAction = f"You have used the {rooms[currentRoom]['use']}!"
      
      #define specific objects

      #Observatory telescope
      if rooms[currentRoom]['use'] == 'telescope':
            mynasakey = returnKey()
            res = requests.get(API + mynasakey)
            apod = res.json()
            lastAction = ""
            lastAction = f'''You start observing the stars with the telescope and spot {apod[0]["title"]}.
                            The computer prints out the following description:
                            {apod[0]["explanation"]}
            '''
            telescopeUsed = True
            
      #Navigation computer in control room
      if rooms[currentRoom]['use'] == 'computer' and 'notes' not in inventory:
            lastAction = "You need the observatory notes first before you can set a destination"
      if rooms[currentRoom]['use'] == 'computer' and 'notes' in inventory:
            navigationSet = True
            lastAction = "You have set the navigation destination for your rocket!"
      
      #Talk to Janus
      if rooms[currentRoom]['use'] == 'janus':
  
            randInd = random.randint(1,len(janusWords))
            print(randInd)
            lastAction = f"Janus: {janusWords[randInd]}"

      ##Launch Pad actions            
      if rooms[currentRoom]['use'] == 'rocket' and 'fuel' not in inventory:
            lastAction = 'You need to fuel the rocket first.. Please visit the fuel depot'
      elif rooms[currentRoom]['use'] == 'rocket' and 'fuel' in inventory:
            rocketUsed = True
      
      #Training Room
      if rooms[currentRoom]['use'] == 'simulator':
            simcount += 1
            lastAction = f"You've used the simulator for {simcount} hours!"
            

  ## Define how a player can launch rocket & win or lose 

  #Win
  if currentRoom == 'Launch Pad' and rocketUsed == True and 'fuel' in inventory and 'training books' in inventory and telescopeUsed == True:
        print("With your obersvations from the telescope, you've uncovered the secrets of the universe.  Launch successful, congratulations!") 
  #partial Win         
  elif currentRoom == 'Launch Pad' and rocketUsed == True and 'fuel' in inventory and navigationSet == False:
    print('You have taken off!  God speed on your journey! However you forgot to set a destination so you will forever drift aimlessly among the stars')
    break
  #Win
  elif currentRoom == 'Launch Pad' and rocketUsed == True and 'fuel' in inventory and navigationSet == True:
    print('You have taken off!  God speed on your journey! However you forgot to set a destination so you will forever drift aimlessly among the stars')
    break
  #super win
  elif currentRoom == 'Launch Pad' and rocketUsed == True and 'fuel' in inventory and 'notes' in inventory and navigationSet == True:
    print('You have taken off!  God speed on your journey! However you forgot to set a destination so you will forever drift aimlessly among the stars')
    break
  #lose
  elif currentRoom == 'Launch Pad' and rocketUsed == True and 'fuel' in inventory:
    print('You took off but forgot to set the destination in the control room....*rocket explodes*')
    break