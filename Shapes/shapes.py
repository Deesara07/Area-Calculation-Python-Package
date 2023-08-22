import math

def circle_area():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius ** 2
    print("\nThe area of the circle is", area)
    
def rectangle_area():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print("\nThe area of the rectangle is", area)

def square_area():
    length = float(input("Enter the length of the square: "))
    area = length ** 2
    print("\nThe area of the square is", area)
    
def triangle_area():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = (base * height) / 2
    print("\nThe area of the triangle is", area)
