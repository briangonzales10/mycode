#!usr/bin/python3

import pandas as pd

def main():
    
    
    capdata = pd.read_csv("capsule_data.csv",index_col=0)

    print(capdata)
    print(capdata.shape)

if __name__ == "__main__":
    main()
