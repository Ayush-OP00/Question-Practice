sample=(input("Enter comma separated numbers: "))

list1 = sample.split(",") # Split the 'values' of sample into a list using commas as separators and store it in the 'list1' variable
tuple1 = tuple(list1)

print("List: ", list1)
print("Tuple: ", tuple1)