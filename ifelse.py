#Python Conditions and if statements
#python support the usual logical conditions from mathematics
# equals a == b
# not equal a != b 
# less then a < b
# greater then a > b
# less then or equal to : a <= b
# greater then or equal to : a >= b

#there is a condition can be used in several ways most commonly in "iff statements " and loops

#if statement
a = 5
b = 4
if a > b :
    print('a is greater then b')

#elif
#th elif keyword is pythons way of saying 
#if the previous conditions were not true then try this condition

a = 3
b = 3
if a > b:
    print('a is greater then b')
elif a == b:
    print(' a is equal to b')

#else 
#the else keyword catches anything which isn't caught by the preceding condition
x = 2
y = 3
if x > y:
    print('x is greater then y')
elif x == y:
    print('x is equal to y')
else:
    print('y is greater then x')

#short hand If
#if you have only one statement to execute you can put it on same line 
#as the if statement

#x = 2, y = 3
if x < y: print('x is less then y')

#dhort hand if else 
#if you have only one statement to execute one for if and one for else
#you can out it all on the same line
print('x is greater then y') if x > y else print('y is greater then y')
#you can also have multiple  else statement on the same line

print(' less then y') if x < y else print('equal') if x == y else print('less then x')
#And , OR , 
#the and keyword is a logical operator and is used to combine conditional statements.

a = 10
b = 15
c = 5
if a > c and c < b:
    print('condition are true')
if a > c or c < b:
    print('at least one of the condition is true')
#at least one of the condition is true

#nested if
#you can have if statemets inside if statements this is called nested if statements
x = 25
if x > 18:
    print('above 18+')
    if x > 23:
        print('above 20')
    else:
        print('not above 25')

#the pass statements
#if statements cannot be empty but if you for some reason have an if statements
#with no content put in the pass statement to avoid getting an error.

x = 22
y = 34
if a > b :
    pass
#having an empty if statement like this would raise an error without the pass statement