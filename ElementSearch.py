#program that checks whether a specified value is contained within a group of values.

def search_num(num, group):

    if num in group:
        return "True"
    else:
        return "False"
    
number = [int(x) for x in input("Enter the group of numbers: ").split()] 
#taking input in the form of list of integers from the user and storing it in the variable 'number'
num = int(input("Enter the number to search: "))
result = search_num(num, number)

print("Is the number in the group?", result)
