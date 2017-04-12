#!/usr/local/bin/python3.6
year = 0
while True:
    year = int(input("Bitte Geburtsjahr eingeben\n"))
    if year < 1582 or year > 2015:
        print("Das Jahr muss zwischen 1582 und 2015 liegen")
    else:
        break

print("Korrekt: ", year)
