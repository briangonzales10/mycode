#!/usr/bin/env python3
'''
Pokemon Picker by Brian.

Creates a file from pokedex.txt based on user chosen pokemon.
'''
import csv

def printPokemon(id, name, t1, t2, total, hp, atk, defense, spatk, spd, speed, gen, leg, list):
    # function to create data for txt files
                        print(f'''
                        PokeID: {id}
                        Name: {name}
                        Type1: {t1}
                        Type2: {t2}
                        Total: {total}
                        HP: {hp}
                        Attack: {atk}
                        Defense: {defense}
                        Sp. Atk: {spatk}
                        Sp. Def: {spd}
                        Speed: {speed}
                        Generation: {gen}
                        Legendary:{leg}\n
                        ------------------------------
                          ''', file=list)

def legendary():
    #function to print out list of legendary pokemon
    with open("pokedex.txt", "r") as pokelist:
        
        with open('legendary.txt', "w") as list:
            for pokemon in csv.reader(pokelist):
                
                if pokemon[12] == 'True': #checking the Legendary status of each pokemon
                    printPokemon(pokemon[0],pokemon[1],pokemon[2],pokemon[3],pokemon[4],pokemon[5],pokemon[6],pokemon[7],pokemon[8],pokemon[9],pokemon[10],pokemon[11],pokemon[12],list)
                    
def pickaPokemon():
    #function to print out a pokemon by ID
    pokeID = input("Choose a pokemon by ID: ")
    
    
    with open("pokedex.txt", "r") as pokelist:
        with open('pickamon.txt', "w") as list:
            for pokemon in csv.reader(pokelist):
                if pokemon[0] == pokeID:
                    printPokemon(pokemon[0],pokemon[1],pokemon[2],pokemon[3],pokemon[4],pokemon[5],pokemon[6],pokemon[7],pokemon[8],pokemon[9],pokemon[10],pokemon[11],pokemon[12],list)

                    
def main():
    while True:
        selection = input('''
                        1. Pick Pokemon by ID
                        2. List all Legendary
                        
                        ''')
        
        if selection == '1':
            pickaPokemon()
            break
        
        if selection == '2':
            legendary()
            break
        else:
            print('Please make a valid selection!\n')
            continue
    

if __name__ == '__main__':
    main()