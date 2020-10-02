from random import random
#when the is multipled by 900 a random
#number is obtained from 0 to 899(9)
#if add 100 to it

#get a number from 100 to 99.
n = random() * 900 + 100

#the fractional pard is discribed the number is displayed

n = int(n)
print(n)

#the first digit the most significant of the 
#number is extracted by dividing is by 100
a = n // 100

#the last digit of the number is deleted
# by dividing by 10 whole then
#finding the reminder when dividing by 10 extract 
#the last digit which in the original 
#number was in the middle
b = (n // 10) % 10

#the last digit the lowest digit
# of the number is extracted by 
#finding the remainder by dividing 10
c = n % 10

#the sum of digits is caculated and displayed on the screen

print(a+b+c)
