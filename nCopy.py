# n (non-negative integer) copies of the first 2 characters of a given string

def copy_str(text, n):
    
    f_len = len(text) 
    #len() function is used to get the length of the string, which is stored in the variable f_len. This is done to check if the string has less than 2 characters.
    if f_len < 2:
        return text * n
    else:
        return text[:2] * n  #we have used the technique of slicing to get the first 2 characters of the string 

string = input("Enter a string: ")
number = int(input("Enter a non-negative integer: "))

result = copy_str(string, number)
print("Result:", result)