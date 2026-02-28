#Count the number of occurrences in a list

def count_num(nums):

    count = 0

    for num in nums:
        if num == 4:
            count = count+1
    return count  
#return has to be put outside the for loop else it will return The count = 1 as soon as it hits the first 4
    
numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
#for x in ...: This is part of a List Comprehension. It loops through each item (the strings '10', '20', etc.) created by the split. 
# The int(x) converts each of those strings into an integer, and the resulting integers are collected into a list assigned to the variable numbers.
result = count_num(numbers)
print("The number of occurrences of 4 is:", result)

