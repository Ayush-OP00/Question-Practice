file_name=input("Enter the file name = ")
print(file_name)

extension = file_name.split('.')
print("The extension of the file is: ", extension[-1]) # The last element of the list will be the extension of the file