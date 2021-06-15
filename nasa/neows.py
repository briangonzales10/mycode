#!/usr/bin/python3
import requests

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/mycode/nasa/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()
    
    ## update the date below, if you like
    inputStart = input("Please input a start date YYYY-MM-DD\n>")
    inputEnd = input("Please input end date YYYY-MM-DD otherwise hit enter\n>")
    
    if inputEnd == "":
        daterange = inputStart
    else: 
        daterange = inputStart + " & " + inputEnd

    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    neowrequest = requests.get(NEOURL + daterange + "&" + nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()
    #print(type(neodata))
    
    ## display NASAs NEOW data
    #print(neodata)
    
    neoTotal = neodata["element_count"]
    neoHazards = 0

    #iterate through and count how many hazards
    for days in neodata["near_earth_objects"]:
        for neo in neodata["near_earth_objects"][days]:
            if neo["is_potentially_hazardous_asteroid"] == True:
                neoHazards += 1
    
        
    print(f"Near Earth Asteroids: {neoTotal}")
    print(f"Hazardous Asteroids in date range: {neoHazards}")

if __name__ == "__main__":
    main()

