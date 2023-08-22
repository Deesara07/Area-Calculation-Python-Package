import Display.main_view as view
import Shapes.shapes as shapes
import Select.selection as selct
import Objects.objects as obj

import Combined.selection as cs
import Combined.shapes as comshape
import os



total_area = 0
view.start_view()        
user_input = selct.get_input()

if(user_input == 1):
    os.system('cls')
    view.shape_view()
    shape_selection = selct.get_input()
    if(shape_selection == 1):
        os.system('cls')
        shapes.circle_area()
    elif(shape_selection == 2):
        os.system('cls')
        shapes.rectangle_area()
    elif(shape_selection == 3):
        os.system('cls')
        shapes.triangle_area()
    elif(shape_selection == 4):
        os.system('cls')
        shapes.square_area()
elif(user_input == 2):
    view.object_view()
    object_selection = selct.get_input()
    if(object_selection == 1):
        os.system('cls')
        obj.cube_area()
    elif(object_selection == 2):
        os.system('cls')
        obj.sphere_area()
    elif(object_selection == 3):
        os.system('cls')
        obj.cylinder_area()
    elif(object_selection == 4):
        os.system('cls')
        obj.cone_area()
    elif(object_selection == 5):
        os.system('cls')
        obj.cuboid_area()
        
elif (user_input == 3):
    print('1. for Combined Objects area calculation')
    print('2. for Combined Shapes area calculation')
    
    shape_selection = selct.get_input()
            
    if (shape_selection == 1):
        print('How many objects do you want to combine? ')
        num_objects = selct.get_input()
        total_area = 0
        
        while (num_objects > 0):
            print('Select the Object to combine')
            area = cs.objectselect()
            total_area = total_area + area
            num_objects -= 1
            area = 0

        print(f"The total area of objects is: {total_area}")
    elif shape_selection == 2:
        pass

        
