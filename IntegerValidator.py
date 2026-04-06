#a Python program to add two objects if both objects are integers.
def validator(x, y):
    if isinstance(x, int) and isinstance(y, int):
        return x+y
    else:
        print("the numbers are not integer type")

x, y = map(int, input("Enter two number separated by space: ").split())
print (validator(x, y))
