#!/usr/local/bin/python3.6

m = ['a', 'b', 'd', 'e', 'f']
m2 = m

print(m, id(m))
print(m2, id(m2))

m += 'g',

print(m, id(m))
print(m2, id(m2))

# a list is always a refrence
