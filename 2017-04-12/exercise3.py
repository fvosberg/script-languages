#!/usr/local/bin/python3.6

s = "Hallo"
s2 = s

print(id(s), id(s2))

s += " Welt!"

print(id(s), id(s2))

# one string has one id and is passed by reference. If you try to modify it you get a copy
