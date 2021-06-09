"""
Movie recommendation App by Brian
"""
import random
recommend = 'y'
genreLoop = True
ageLoop = True
fameLoop = True

movies= {
    "comedy" : {
                "classic" : {"blockbuster": ["Dumb & Dumber", "The Big Lebowski", "Fargo"],
                            "underrated": ["Wet Hot American Summer", "Kingpin","LA Story"]
                            },
                "modern": {"blockbuster": ["Hot Fuzz", "Step Brothers", "Zombieland"],
                            "underrated": ["Role Models", "Idiocracy","Eurovision"]} 
                },

    "drama" : {
                "classic" : {"blockbuster": ["Citizen Kane", "Seven Samurai", "The Godfather"],
                            "underrated": ["Twelve o Clock High", "Vanila Sky","Brick"]
                            },
                "modern": {"blockbuster": ["Parasite", "Knives Out", "Logan"],
                            "underrated": ["In Bruges", "The Babadook", "Doubt"]} 
                },

    "action" : {
                "classic" : {"blockbuster": ["Die Hard", "Enter the Dragon", "The Terminator"],
                            "underrated": ["Last Action Hero","Demolition Man","Lionheart"]
                            },
                "modern": {"blockbuster": ["The Dark Knight", "Mad Max: Fury Road", "Avengers: End Game"],
                            "underrated": ["47 Ronin","Smokin Aces","Dredd"]} 
                },

    "scifi" : {
                "classic" : {"blockbuster": ["The Matrix", "Moon", "Alien"],
                            "underrated": ["Close Encounters of the 3rd Kind","Bladerunner","Galaxy Quest"]
                            },
                "modern": {"blockbuster": ["Star Wars: The Force Awakens", "Interstellar", "The Martian"],
                            "underrated": ["Synchronic", "Bliss", "Underwater"]} 
                },
    }
while recommend == 'y':

    #Random Int for movie currently only up to 3 movies in a category
    randInd = random.randint(0,2)
    #Ask what kind of genre do you want to watch? Comedy/Drama/Action/Romance/SciFi

    while genreLoop:
        genre = input("What genre are you in the mood for?\n ('comedy' 'drama' 'action' or 'scifi')\n>").lower()
        if genre != 'comedy' and genre != 'drama' and genre != 'action' and genre != 'scifi':
            print("Please enter a valid input: 'comedy' 'drama' 'action' or 'scifi'")
        else:
            genreLoop = False

        #Ask what era of movie old/classic or modern?
    while ageLoop:
        age = input("'Classic' movie or 'modern'?\n>").lower()
        if age != 'classic' and age != 'modern':
            print("Please enter a valid input: 'classic' or 'modern'")
        else:
            ageLoop = False

        #Famous Blockbuster or underrated gem?
    while fameLoop:
        fame = input("'blockbuster' or 'underrated'?\n >")
        if fame != 'blockbuster' and fame != 'underrated':
            print("Please enter a valid input: 'blockbuster' or 'underrated'")
        else:
            fameLoop = False

    print(f"Your recommendation is {movies[genre][age][fame][randInd]}!")
    
    next = input("Would you like another recommendation (y or no)?\n>").lower()
    if next == 'n':
        recommend = 'n'