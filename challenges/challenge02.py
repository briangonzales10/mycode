#!/usr/bin/env python3
import random

icecream= ["flavors", "salty"]
tlgclass= ["Brian","Clint","Damian","Dan","David","Jelani","Jerad","Jon","Jun","Mark","Max"]
icecream.append(99)

nameInd = random.randint(0,10)
print(f"{icecream[2]} {icecream[0]}, and {tlgclass[nameInd]} chooses to be {icecream[1]}")


