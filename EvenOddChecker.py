# program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.

def checker(num):
    if num % 2 == 0:
        return "The number is even."
    else:
        return "The number is odd."
    
number = int(input("Enter a number: "))
result = checker(number)
print(result)