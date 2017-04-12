#!/usr/local/bin/python3.6

t = (1, 2, [31, 32], 4)
t2 = t

print(t, id(t))
print(t2, id(t2))

t += 5,

print(t, id(t))
print(t2, id(t2))

# a tupel is copied while trying to manipulate it
