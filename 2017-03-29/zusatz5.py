#!/usr/local/bin/python3.6

def multi(x, y):
    if len(x) != len(y):
        raise ValueError("The length of the both lists aren't the same")
    for n,e in enumerate(x):
        if e * y[n] > 100:
            return str(e) + " * " + str(y[n]) + " = " + str(e * y[n])
    else:
        return "There is no product over 100"

x = [1,3,2,6,8]
y = [4,2,7,9,4]
print(multi(x,y))

x = [1,3,20,6,8]
y = [4,2,7,9,4]
print(multi(x,y))

try:
    x = [1,3,20,6]
    y = [4,2,7,9,4]
    print(multi(x,y))
except ValueError as e:
    print(e)
