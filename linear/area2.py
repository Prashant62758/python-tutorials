import math
r = input("Radius : ")
#string is converted to a float number 

r = float(r)

#the length of circumference is 2 * pi * r

ln = 2 * math.pi * r

# the area of circle is p*r*r
area = math.pi * math.pow(r,2)

#Note :  in python  rise to power using the ** operator 
#then area = math.pi*r**r

print("length = %.2f" %ln)
print("area = %.2f" % area)
