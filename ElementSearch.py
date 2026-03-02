#program that checks whether a specified value is contained within a group of values.

def search_num(num, group):

    if num in group:
        return "True"
    else:
        return "False"
    
#Little touch to determine the occurence of the particular number in group of numbers.

def count(num, group):
    count = 0

    for n in group:
         if n == num:
            count = count + 1
    return count
    
    
number = [int(x) for x in input("Enter the group of numbers: ").split()] 
#taking input in the form of list of integers from the user and storing it in the variable 'number'
num = int(input("Enter the number to search: "))
result = search_num(num, number)
occurence = count(num, number)

print("The number of occurrences of", num, "is:", occurence)
print("Is the number in the group?", result)

