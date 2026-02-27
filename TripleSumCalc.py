#to calculate the sum of three given numbers. If the values are equal, return three times their sum.

def triple_sum(a,b,c):
    if a == b == c:
        return 3 * (a + b + c)
    else:
        return a + b + c
    
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

result = triple_sum(num1, num2, num3)
print(result)