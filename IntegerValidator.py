#a Python program to add two objects if both objects are integers.
def add_numbers(a, b):
    # Check if both 'a' and 'b' are integers using the 'isinstance' function.
    if not (isinstance(a, int) and isinstance(b, int)):
        # If either 'a' or 'b' is not an integer, return an error message.
        return "Inputs must be integers!"
    # If both 'a' and 'b' are integers, return their sum.
    return a + b

print(add_numbers(10, 20))    
print(add_numbers(10, 20.23))