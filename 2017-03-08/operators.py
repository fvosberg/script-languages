print("Hello World")

def test(t):
    print()
    try:
        print(t)
        print(eval(t))
    except:
        print("Error at ", t)

test("type(1)")

test("5-3")


#t = '"5"-"3"'
#print()
#print(t)
#print(eval(t))

#t = "5"-3
#print()
#print(t)
#print(eval(t))
print("FAIL")


test('"5"*3')


t = '"5"/3'
print()
print(t)
#print(eval(t))
print("FAIL")

test("5//2")
test("5%2")
test("5**2")
test("15**2")
test("3**2")

test("~2")
test("~3")

test("2<<3")
test("2**64")
test("2**64+1")

test("3<<1")
test("3>>1")

def greet():
    print("evaled")

test("True or greet()")
test("True || greet()")

test("10 | -7")
test("[1,2,3]")
test("[1,2,3][1]")
test("[1,2,3,4,5][1:2]")
