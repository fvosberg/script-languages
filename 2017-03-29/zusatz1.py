#!/usr/local/bin/python3.6

eingabe = input("Bitte Monat eingeben")

if eingabe in ["Januar", "Februar", "März"]:
    print("1. Quartal")
elif eingabe in ["April", "Mai", "Juni"]:
    print("2. Quartal")
elif eingabe in ["Juli", "August", "September"]:
    print("3. Quartal")
elif eingabe in ["Oktober", "November", "Dezember"]:
    print("4. Quartal")
else:
    print("Bitte einen validen Monat eingeben")
