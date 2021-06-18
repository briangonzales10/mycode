#!/usr/bin/env python3
"""
Uses a cached database from NASA APIs at https://exoplanetarchive.ipac.caltech.edu/. 
The script plots all the discovered explanets based on year discovered using matplotlib.

Author: Brian
"""
#import json
import csv
import numpy as np
import matplotlib.pyplot as plt

class Planets:
    """Gets our planet data from csv file"""
    def __init__(self):
        self.year = []
        self.mass = []
        self.name = []
        
        #from planets.json file        
        #with open("planets.json") as planetDB:
        #    planets = json.load(planetDB)
        with open("planets.csv", "r") as planetList:
            planets = csv.reader(planetList)

            for planet in planets:
                
        
                if planet[0] not in self.name:#filters out repeated data
                    if planet[6] != None: 
                        self.year.append(planet[6]) #discovery year
                    else:
                        self.year.append("None")
                    if planet[27] != None:
                        self.mass.append(planet[27]) #mass in Earth mass
                    else:
                        self.mass.append(0.0) #append 0 mass if unknown
                    self.name.append(planet[0])## add name to our list to filte
def getPlanets():
    """returns our data from Planet Class"""
    return Planets()


def main():
    """Plots planet count vs year discovered"""
    planet = getPlanets() #Gives us our raw data
    print(len(planet.year))
    print(len(planet.mass))
    
    x = sorted(set(planet.year)) #x-axis is years
    y = [] # count frequency for the Y-Axis
    freq = {}
    
    for year in x: #Map our years we discovered planets
        freq[year] = 0
        
    for count in planet.year: #count how many planets we discovered year year
        for year in freq:
            if count == year:
                freq[year] += 1
    
    for count in freq.values():
        y.append(count)
    
    print(y)

    #x = np.array(planet.year) # X-axis is our discovery year
    #x = np.sort(x)
    #y = np.array(planet.mass) #y-axis is our mass in Earth Mass
    #y = np.sort(y)
    
    colors = "blue"

    plt.scatter(x, y, color=colors, alpha=0.5, s=10)
    plt.title('Exoplanets discovered by year')
    plt.xlabel('Discovery Year')
    plt.xticks(rotation=70)
    plt.ylabel('# of planets discovered')
    y_ticks = np.arange(0, max(y), 50)
    plt.yticks(y_ticks)
    plt.show()
    
if __name__ == "__main__":
    main()
