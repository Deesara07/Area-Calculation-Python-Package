import Select.selection as selct
import  os
import Objects.objects as obje


area = 0

def objectselect():
    object_selection = selct.get_input()
    if(object_selection == 1):
        os.system('cls')
        area = obje.cube_area()
        return area
    elif(object_selection == 2):
        os.system('cls')
        area = obje.sphere_area()
        return area
    elif(object_selection == 3):
        os.system('cls')
        area= obje.cylinder_area()
        return area
    elif(object_selection == 4):
        os.system('cls')
        area = obje.cone_area()
        return area
    elif(object_selection == 5):
        os.system('cls')
        area = obje.cuboid_area()
        return area