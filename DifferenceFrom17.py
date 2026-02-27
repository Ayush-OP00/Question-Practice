#Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.

def difference(n):

    if n > 17:
        return (17 - n) * 2
    else:
        return (17 - n)
    
number = int(input("Enter a number: "))
result = difference(number)

print("The result is:", result)