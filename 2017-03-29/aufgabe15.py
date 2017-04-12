#!/usr/local/bin/python3.6

l = []

for i in range(3):
    print("Bitte", i, ". Zahl eingeben:")
    x = int(input())
    if x < 0:
        print("No negatives")
        break
    l += x,
else:
    for i in l:
        print(i, i**2, sep=":")
