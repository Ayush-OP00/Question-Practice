#Python program that will accept the base and height of a triangle and compute its area.

def area_triangle (base, hheight):
    area = 0.5 * base * hheight
    return area

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

result = area_triangle(base, height)
print("The area of the triangle is:", result)
