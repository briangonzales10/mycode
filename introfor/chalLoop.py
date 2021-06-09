#!usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

def NEAnimals():
    for farm in farms:
        if farm["name"] == "NE Farm":
            print(farm["name"] + "Animals:")
            for animal in farm["agriculture"]:
                print(animal)

NEAnimals()

def chooseFarm():
    farmname = input("Choose a farm ('NE Farm', 'W Farm', 'SE Farm' \n >")
    for farm in farms:
        if farm["name"] == farmname:
            print(farm["name"] + " Agriculture: ")
            for ag in farm["agriculture"]:
                print(ag)

chooseFarm() 

def chooseAnimalFarm():
    farmlist = []
    for farm in farms:
        farmlist.append(farm["name"])

    animalsList = ["sheep", "cows", "pigs", "chickens", "ducks", "cats", "goats", "dogs", "llamas"]

    farmInput = input(f"Choose a farm to see the animals: {farmlist} \n > ")
    for farm in farms:
        if farm["name"] == farmInput:
            print(farm["name"] + " Animals: ")
            for ag in farm["agriculture"]:
                for animal in animalsList:
                    if ag == animal:
                        print(animal)

chooseAnimalFarm()
