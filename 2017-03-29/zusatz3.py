#!/usr/local/bin/python3.6

def quartalFor(monat):
    if monat in ["Januar", "Februar", "März"]:
        return "1. Quartal"
    elif monat in ["April", "Mai", "Juni"]:
        return "2. Quartal"
    elif monat in ["Juli", "August", "September"]:
        return "3. Quartal"
    elif monat in ["Oktober", "November", "Dezember"]:
        return "4. Quartal"
    else:
        return "Invalider Monat"

months = ["Mai", "MMärz", "April", "Januar"]

print(*map(quartalFor, months))

months = ["Mai", "März", "April", "Januar"]

// TODO what does * mean?
print(*map(quartalFor, months))
print(*map(lambda x: quartalFor(x), months))
