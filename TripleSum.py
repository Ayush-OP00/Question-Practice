#Python program to sum three given integers. However, if two values are equal, the sum will be zero.

def sum_q(x, y, z):
    
    if x==y or y==z or z==x:
        sum_three = 0
        
    else:
        sum_three = x + y + z
    return sum_three

inp = ( input("enter three number separated by commas= ").split(','))
x, y, z = map(float, inp) #this line maps the entries taken in inp to x,y,z and wrap them into float
result = sum_q(x, y, z)
print (result)


