#program to test whether a passed letter is a vowel or not.

def vowel_tester(letter):

    if letter in 'aeioeAEIOU': # Check if the letter is in the string of vowels (both lowercase and uppercase)
        return "The letter is a vowel."
    else:
        return "The letter is not a vowel."

letter = input("Enter a letter: ")
result = vowel_tester(letter)
print(result)
                 
                 
                 
