# program that prints out all colors from color_list_1 that are not present in color_list_2.

def finder(l1, l2):
    result = []
    for color in l1:
        if color not in l2:
            result.append(color)
    return result

color_list_1 = ["Red", "Green", "White", "Black"]
color_list_2 = ["Red", "Green", "White"]
result = finder(color_list_1, color_list_2)
print("The colors that are in color_list_1 but not in color_list_2 are:", result)

        
