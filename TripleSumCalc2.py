#Sum of three given integers. However, if two values are equal sum will be zero


def tri_sum(a, b, c):
    if a == b or b == c or c == a:
        return 0
    else:
        return a+b+c
    
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

result = tri_sum(num1, num2, num3)
print(result)
 