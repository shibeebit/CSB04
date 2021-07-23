import math

def area_of_circle(radius):
    return math.pi * (radius ** 2)

def perimeter_of_circle(radius):
    return math.pi * 2 * radius

def area_of_rectangle(w, l):
    return w * l

def perimeter_of_rectangle(w, l):
    return 2 * (w+l)

def volume_of_sphere(radius):
    return 4/3 * math.pi * (radius ** 3)

def volume_of_rec_prism(l, w, h):
    return l * w * h
        
def main_func():
    while True:
        try:
            user_choice = str(input("1.What do u want to calculate (volume/area/perimeter): ")).lower()
            if user_choice == "quit": 
                break
            elif user_choice == "area" or user_choice == "perimeter" or user_choice == "volume":
                user_shape = str(input("What shape do u want to calculate (circle/rectangle/sphere/rectangle prism): ")).lower()
                if user_shape == "quit": 
                    break
                elif user_shape == "circle":
                    radius = float(input("Input radius: "))
                    if user_choice == "area":
                        print(area_of_circle(radius))
                    elif user_choice == "perimeter":
                        print(perimeter_of_circle(radius))
                    else:
                        print("Invalid")
                elif user_shape == "rectangle":
                    l = float(input("Input length: "))
                    w = float(input("Input width: "))
                    if user_choice == "area":
                        print(area_of_rectangle(w, l))
                    elif user_choice == "perimeter":
                        print(perimeter_of_rectangle(w, l))
                    else:
                        print("Invalid")
                elif user_shape == "sphere":
                    if user_choice == "volume":
                        radius = float(input("Input radius: "))
                        print(volume_of_sphere(radius))
                    else:
                        print("Invalid")
                elif user_shape == "rectangular prism":
                    if user_choice == "volume":
                        l = float(input("Input length: "))
                        w = float(input("Input width: "))
                        h = float(input("Input height: "))
                        print(volume_of_rec_prism(l, w, h))
                    else:
                        print("Invalid")
        except ValueError:
            continue

main_func()