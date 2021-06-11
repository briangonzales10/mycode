#!/usr/bin/python3
'''
Space launch RPG by Brian
'''

def showInstructions():
  #print a main menu and the commands
  print('''
Space Launch RPG
==============
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are at the ' + currentRoom +"\n")
  print(rooms[currentRoom]['description'] + "\n")
  #Find direction options:
  print("Direction Options:")
  for options in rooms[currentRoom]:
      if options != 'item' and options != 'description':
          print(options)
  print('-----------------')
  
  
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Observatory' : {
                  'east'  : 'Winding Mountain',
                  'item'  : 'Observation Notes',
                  'description' : 'A gentle dome with a telescope peaking out observing the universe.'
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
                  'description' : 'A simple pad with a simple rocket almost ready for launch.  Just waiting for you, her sole crewmember'
               },
            'Control Room' : {
                  'north' : 'Lounge',
                  'south' : 'Launch Pad',
                  'description' : 'Just a bunch of laptops overlooking the launch pad.  You can set your launch destination here'
               },
            'Lounge' : {
                'east' : 'Fuel Storage',
                'west' : 'Quarters',
                'item' : 'whiskey',
                'description' : 'Nothing much here but a bunch of chairs and tables. Oh is that Janus in the corner?'
             },
            'Fuel Storage' : {
                'west' : 'Lounge',
                'item' : 'fusion core',
                'description' : 'A dumpy looking room lined with fusion cores.  This is how we store our fuel?'
             },
            'Quarters' : {
                'east' : 'Lounge',
                'west' : 'Training Room',
                'description' : 'Just a well made twin bed and a desk with a lamp turned off.  Now is no time for napping though.'
             },
            'Training Room' : {
                'east' : 'Quarters',
                'item' : 'training books',
                'description' : 'The training room has a simulator in the corner for how to maneuver your ship.  You should probably brush up and take some reference materials with you'
             },
         }

## Create Commands based on current Room!
## Create Room descriptions based off current

## Only add item to inventory if room command is executed

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
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and 'cookie' in inventory:
      print('Gave the monster a cookie and it ran away')
      del rooms[currentRoom]['item']
  
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break