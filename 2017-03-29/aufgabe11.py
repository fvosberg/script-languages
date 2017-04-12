#!/usr/local/bin/python3.6
year = 0
print("Bitte Geburtsjahr eingeben")
while True:
    year = int(input())
    if year == 0:
        print("Null geht wirklich gar nicht")
        break
    elif year == 1:
        continue
    elif year < 1582 or year > 2015:
        print("Das Jahr muss zwischen 1582 und 2015 liegen")
    else:
        print("Korrekt: ", year)
        break
