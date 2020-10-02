#import the constant pi from the math module
from math import pi 

#cylinder height 
h = input("h : ")

#cylinder base radius
r = input("r : ")

#string are conveted to float number
h = float(h)
r = float(r)

#a cylinder has two base  area of each 
#is pi * r * r

circle = 2 * (pi * r ** 2)
 # the area of the side surface of a
#cylinder is 2 * pi * r * h

side = 2 * pi * r * h

area = circle + side 
print('area = ', round(area,2))
