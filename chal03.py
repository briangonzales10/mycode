#!usr/bin/env python3
char_name = input("Which character do you want to know about? (wolverine, Harry Potter, Captain America) \n >")
char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)\n > ")

heroes=  {
"wolverine":
    {"real name": "James Howlett",
    "powers": "regeneration",
    "archenemy": "Sabertooth",},
"harry potter":
    {"real name": "Harry Potter",
    "powers": "magic",
    "archenemy": "Voldemort",},
"captain america":
    {"real name": "Steve Rogers",
    "powers": "frisbee shield",
    "archenemy": "Hydra",}
        }


lowername = char_name.lower()
lowerstat = char_stat.lower() 
stat = heroes[lowername][lowerstat]
name = char_name.title()

print(f"{name}'s {char_stat} is: {stat}")


