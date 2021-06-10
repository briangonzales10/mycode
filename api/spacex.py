#!usr/bin/python3
'''
Import space X capsule data from SpaceX API , saves as a .csv file and displays formatted data with Panda
Author: Brian G
'''

import requests
import pandas as pd
import time

def getCapsule():
    capsules = requests.get("https://api.spacexdata.com/v3/capsules").json()
    #example how to get capsule serial number for 1st object in list
    #print(capsules[0]["capsule_serial"])
   
    outfile = open("capsule_data.csv", "a")
    #print the header
    print("capsule_serial;capsule_id;status;original_launch;original_launch_unix;missions;landings;type;details;reuse_count", file=outfile)
    #iterate through
    for cap in capsules:
        serial = cap.get("capsule_serial")
        capid = cap.get("capsule_id")
        status = cap.get("status")
        launch = cap.get("original_launch")
        launchu = cap.get("original_launch_unix")
        missions = cap.get("missions") #missions giving me errors...
        land = cap.get("landings")
        typecap = cap.get("type")
        details = cap.get("details")
        resuse = cap.get("resuse_count")

        print(f"{serial};{capid};{status};{launch};{launchu};{missions};{land};{typecap};{details};{resuse}",file=outfile )  
          
def readCapsule():
    #read our newly created csv file
    capdata = pd.read_csv("capsule_data.csv",sep=";",header=0,index_col=0)

    print(capdata)
    print(capdata.shape)
    
def main():
    getCapsule()
    time.sleep(2)
    readCapsule()

if __name__ == "__main__":
    main()
