#!/usr/local/bin/python3.6

t = (1, 2, [31, 32], 4)
t2 = t

print(t, id(t))
print(t2, id(t2))

del t

try:
    print(t, id(t))
except NameError as e:
    print(e)
print(t2, id(t2))

del t2

# removes the last reference to the tupel so the garbage collector has a green light to collect it
