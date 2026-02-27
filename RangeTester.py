#Write a Python program to test whether a number is within 100 of 1000 or 2000.

# Define a function named "near_thousand" that takes an integer parameter "n"
def near_thousand(n):
    # Check if the absolute difference between 1000 and n is less than or equal to 100
    # OR check if the absolute difference between 2000 and n is less than or equal to 100
    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))

number = int(input("Enter a number: "))
result = near_thousand(number)
print("Is the number within 100 of 1000 or 2000?", result)
