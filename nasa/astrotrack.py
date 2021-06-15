#!/usr/bin/python3
"""
Astronaut Tracker! Check to see who's currently in space
Author: Brian
"""
import requests
import json

def getAstronauts():
    """Get list of astronauts"""
    res = requests.get("http://api.open-notify.org/astros.json")
    tracker = res.json()
    print(f"People in Space: {tracker['number']}")
    
    for astronaut in tracker["people"]:
        print(f"{astronaut['name']} is on the {astronaut['craft']}!")
        #print(astronaut)
    

def main():
    getAstronauts()

if __name__ == "__main__":
    main()
