#!/usr/local/bin/python3.6

eingabe = input("Bitte etwas eingeben\n")
if len(eingabe) < 3:
    print("Ich will mehr!")
else:
    print("Yes, 3 oder mehr")

print("Das waren", len(eingabe), "Zeichen")
