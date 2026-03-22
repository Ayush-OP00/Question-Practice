#program to find the least common multiple (LCM) of two positive integers.

def lcm(x, y):

    if x > y:
        z = x
    else:
        z = y

    while True:
        
        if (z % x == 0) and (z % y == 0):
            lcm = z
        break

        z += 1

    return lcm

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
calc = lcm(a,b)
print("LCM of above two numbers is:  ",calc)



