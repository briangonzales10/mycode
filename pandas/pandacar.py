#!usr/bin/python3

import pandas
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt


def main():
    #read csv first   
    df = pandas.read_csv("carsdata.csv", sep=";")
    #export to excel
    df.to_excel("carsdata.xlsx")
    
    #sort by Horsepower and export to bargraph
    cars  = pandas.read_csv("carsdata.csv", sep=";", index_col=0)
    sort_by_hp = cars.sort_values(["Horsepower"], ascending=True)
    print(sort_by_hp)
    
    #bar graph
    sort_by_hp['Horsepower'].head(20).plot(kind="barh")
    plt.savefig("/home/student/static/carbar22.png", bbox_inches='tight')

if __name__ == "__main__":
    main()
