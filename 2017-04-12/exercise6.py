#!/usr/local/bin/python3.6

t = (1, 2, [31, 32], 4)
t2 = t

print(t, id(t))
print(t2, id(t2))

try:
    t[0] = 'X'
except TypeError as e:
    print(e)

t[2][0] = 'X'

print(t, id(t))
print(t2, id(t2))

# tupels are immutable
