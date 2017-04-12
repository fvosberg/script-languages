#!/usr/local/bin/python3.6

def isSchaltjahr(year):
    result = False
    if year % 400 == 0:
        result = True
    elif year % 100 == 0:
        result = False
    elif year % 4 == 0:
        result = True
    else:
        result = False
    return result

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
        print("Korrekt: ", year, "ist", "ein" if isSchaltjahr(year) else "kein", "Schaltjahr")
        break
