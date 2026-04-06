#Python program that returns true if the two given integer values are equal or their sum or difference is 5.
# def equality_checker(x, y):
#     if x == y  or abs(x + y) == 5 or abs(x - y) == 5:
#         return True
#     else:
#         print("not the expected input")

# x, y = map(int, input("Enter two no. separated by space:").split())
# result = equality_checker(x, y)
# print(result)

x, y = map(int, input("Enter two numbers: ").split())
print(x == y or abs(x + y) == 5 or abs(x - y) == 5)