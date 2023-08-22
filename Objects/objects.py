import math
import os

def cube_area():
    print("Enter the length of the cube: ")
    length = float(input())
    area = length * 6 ** 2
    return area
    
def sphere_area():
    print("Enter the radius of the sphere: ")
    radius = float(input())
    area = 4 * math.pi * radius ** 2
    return area

def cylinder_area():
    print("Enter the radius of the cylinder: ")
    radius = float(input())
    print("Enter the height of the cylinder: ")
    height = float(input())
    area = math.pi * radius ** 2 * height
    return area
    
def cone_area():
    print("Enter the radius of the cone: ")
    radius = float(input())
    print("Enter the height of the cone: ")
    height = float(input())
    area = math.pi * radius ** 2 * height / 2
    return area
    
def cuboid_area():
    print("Enter the length of the cuboid: ")
    length = float(input())
    print("Enter the width of the cuboid: ")
    width = float(input())
    print("Enter the height of the cuboid: ")
    height = float(input())
    area = length * width * height
    return area




""" 
def cube_area():
    print("Enter the length of the cube: ")
    length = float(input())
    area = length * 6 ** 2
    print("\nThe area of the cube is: ", area)
    
def sphere_area():
    print("Enter the radius of the sphere: ")
    radius = float(input())
    area = 4 * math.pi * radius ** 2
    print("\nThe area of the sphere is: ", area)

def cylinder_area():
    print("Enter the radius of the cylinder: ")
    radius = float(input())
    print("Enter the height of the cylinder: ")
    height = float(input())
    area = math.pi * radius ** 2 * height
    print("\nThe area of the cylinder is: ", area)
    
def cone_area():
    print("Enter the radius of the cone: ")
    radius = float(input())
    print("Enter the height of the cone: ")
    height = float(input())
    area = math.pi * radius ** 2 * height / 2
    print("\nThe area of the cone is: ", area)
    
def cuboid_area():
    print("Enter the length of the cuboid: ")
    length = float(input())
    print("Enter the width of the cuboid: ")
    width = float(input())
    print("Enter the height of the cuboid: ")
    height = float(input())
    area = length * width * height
    print("\nThe area of the cuboid is: ", area) """
