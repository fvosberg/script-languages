#!/usr/local/bin/python3.6

eingabe = input("Bitte etwas eingeben\n")
umfang = "lang" if len(eingabe) > 10 else "kurz"
print(umfang)
