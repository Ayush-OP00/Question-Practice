# program that concatenates all elements in a list into a string and returns it.

def concat(list):
    
    result = ""
    for element in list:
        result += str(element)  # Convert each element to a string and concatenate it to the result.
    return result 

# this can take the any input into the list and concatenate it into a sring
number = input("Enter a list of numbers (separated by spaces): ").split()
# The line below converts all the input into a list of numberrs
# number = [int(x) for x in input("Enter a list of numbers (separated by spaces): ").split()]
result = concat(number)
print("Concatenated string:", result)