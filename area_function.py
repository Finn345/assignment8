import math

def area_calc():
    length = float(input("Enter the length of the house in feet: "))
    width = float(input("Enter the width of your house in feet: "))
    if length and width:
        area = round(length*width, 3)
        print("Your house is " + str(area) + " square feet")
    break
area_calc()