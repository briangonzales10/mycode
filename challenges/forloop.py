#!/usr/bin/python3

width = 1


for i in range (1,11):
    char = '*' * width
    print(char)
    width += 1
    if width == 6:
        while width <= 6 and width > 0:
            width -= 1
            print(char)

