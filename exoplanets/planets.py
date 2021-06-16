#!/usr/bin/env python3
"""
Uses a cached database from NASA APIs at https://exoplanetarchive.ipac.caltech.edu/. 
The script plots all the discovered explanets based on year discovered using matplotlib.

Author: Brian
"""
import json

class Planets:
    """Gets our planet data from json file"""
    def __init__(self):
        self.year = []
        self.mass = []
        
        with open("planets.json") as planetDB:
            planets = json.load(planetDB)
        
        for planet in planets:
            self.year.append(planet.get("disc_year")) #discovery year
            self.mass.append(planet.get("pl_masse")) #mass in Earth mass

def getPlanets():
    """returns our data from Planet Class"""
    return Planets()


def main():
    planet = getPlanets()
    print(planet.year)
    print(planet.mass)
    
if __name__ == "__main__":
    main()
