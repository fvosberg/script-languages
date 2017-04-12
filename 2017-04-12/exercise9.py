#!/usr/local/bin/python3.6

x = 5
y = 'y'

try:
    z = x + y
except TypeError as e:
    print(e)
    print("Because python is strongly typed")
