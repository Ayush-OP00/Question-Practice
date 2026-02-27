#program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".

def add_is(s):
    if s.startswith("Is"): 
        # The 'startswith' method is used to check if the string 's' starts with the substring "Is". If it does, the function returns the original string 's' unchanged.
        return s
    else:
        return "Is " + s
    
string = input("Enter a string: ")
result = add_is(string)
print (result)