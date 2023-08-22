import Display.main_view as view
import Select.selection as selct
import  os
import Combined.objects as obj



def view():
    print("1. For Calulate Area of Cube")
    print("2. For Calulate Area of Sphere")
    print("3. For Calulate Area of Cylinder")
    print("4. For Calulate Area of Cone")
    print("5. For Calulate Area of Cuboid\n")


area = 0

def object_select():
    object_selection = selct.get_input()
    if(object_selection == 1):
        os.system('cls')
        area = obj.cube_area()
    elif(object_selection == 2):
        os.system('cls')
        area = obj.sphere_area()
    elif(object_selection == 3):
        os.system('cls')
        area= obj.cylinder_area()
    elif(object_selection == 4):
        os.system('cls')
        area = obj.cone_area()
    elif(object_selection == 5):
        os.system('cls')
        area = obj.cuboid_area()
    return area