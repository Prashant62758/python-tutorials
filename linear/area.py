#the math module containing various math function is imported
import math

#the input() function retun a string

x = input("length of the first leg: ")
y = input("length of the second leg: ")

#string are converted to real number
x = float(x)
y = float(y)

#find the hypotenuse by the  Pythagorean theorem
#the sum of the squre of the hypotenuse
#the sqrt() function of the math module  extracts a square root
#operator ** raises a number to a power
z = math.sqrt(x ** 2 + y ** 2)

#the area oa a right triangle is equal to half the area 
# of the corresponding  rectangle 
s = (x * y)/ 2

#perimeter is the sum of all sides 
p = x + y + z
print("Area of the triangle : %.2f" % s)
print("Perimeter of the triangle: %.2f" % p)
