#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        
        #need another API request for pov books titles
        povbooknames = []
        
        for bookname in got_dj["povBooks"]:
            povBooknameReq = requests.get(bookname)
            res = povBooknameReq.json()
            povbooknames.append(res["name"])
        
        #API request for book titles
        booknames = []

        for bookname in got_dj["books"]:
            booknameReq = requests.get(bookname)
            res = booknameReq.json()
            povbooknames.append(res["name"])
        
        #API req for Allegiances
        allegience = []
        for ally in got_dj["allegiances"]:
            allyReq = requests.get(ally)
            res = allyReq.json()
            allegience.append(res["name"])

        #print(povbooknames)

        #update our dict
        got_dj.update(povBooks = povbooknames)
        got_dj.update(books = booknames)
        got_dj.update(allegiances = allegience)
        
        #pretty print response
        pprint.pprint(got_dj)

if __name__ == "__main__":
        main()
