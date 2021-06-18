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
        
        #from planets.json file        
        #with open("planets.json") as planetDB:
        #    planets = json.load(planetDB)
        with open("planets.csv", "r") as planetList:
            planets = csv.reader(planetList)
        
            for planet in planets:
                if planet[6] != None:
                    self.year.append(planet[6]) #discovery year
                else:
                    self.year.append("None")
                if planet[27] != None:
                    self.mass.append(planet[27]) #mass in Earth mass
                else:
                    self.mass.append(0) #append 0 mass if unknown

def getPlanets():
    """returns our data from Planet Class"""
    return Planets()


def main():
    planet = getPlanets()
    print(len(planet.year))
    print(len(planet.mass))
    
    
    xp = np.array(planet.year) # xp for planet discovery year
    xp = np.sort(xp)
    
    xm = np.array(planet.mass) #xm for planet mass
    xm = np.sort(xm)
    
    y = len(planet.year) #y-axes will be for # of planets on both
    
    data = (xp, xm)
    #print(data)
    colors = ("blue", "red")
    groups = ("discovery year", "mass in E")
    
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    for data, color, group in zip(data, colors, groups):
        x, y = data
        ax.scatter(x,y, alpha=0.8, c=color, label=group, edgecolors='none', s=30)
        
    plt.title('Exoplanets discovered by year and mass')
    plt.xlabel('Discovery Year')
    plt.xticks(rotation=70)
    plt.legend(loc=2)
    plt.show()
    
if __name__ == "__main__":
    main()
