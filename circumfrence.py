import math
from math import pi

def circumfrence():

    radius = float(input("Enter your circle's radius: "))
    if radius:
        circum = round(2 * pi * radius, 3)
        print("The circumfrence of the circle is " + str(circum) + " units.")
        break

circumfrence()