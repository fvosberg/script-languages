#!/usr/local/bin/python3.6

m = ['a', 'b', 'd', 'e', 'f']

print(m, id(m))

m[0] = 'A'

print(m, id(m))

# a list is mutable
