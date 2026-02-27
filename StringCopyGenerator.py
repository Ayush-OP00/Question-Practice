#program that returns a string that is n (non-negative integer) copies of a given string.

def copy_str(s, n):
    return (s + "\n")* n 
#add strings to the new line and multiply it by n to get n copies of the string, each on a new line

string = input("Enter a string: ")
number = int(input("Enter a non-negative integer: "))
result = copy_str(string, number)
print(result)
