#[Arthmetic operators]
#addition
x = 2
y = 5
z = x + y
print(z)

#subtraction
x = 7
y = 5
z = x + y
print(z)

#multiplication

x = 2
y = 3
z = x * y
print(z)

#division

x = 8
y = 2
z = x / y
print(z)

#modules

x = 7
y = 3
z = x / y
print(z)

#exponentiation
x = 2
y = 3
z = x ** y #2*2*2
print(z)

#floor division 

x = 5
y = 2
z = x // y
print(z)

#[Assignment Operators]

#Assignment operators are used to  assign values to variables


# [=] : [x = 5] : [x = 5]

x = 3
print(x)

# [+=]: [x+= 5] : [x = x + 5]
x = 4
x += 5 
print(x)
# [-=]: [x-= 5] : [x = x - 5]
x = 4
x -= 2 
print(x)
# [*=]: [x*= 5] : [x = x * 5]
x = 4
x *= 2 
print(x)
# [/=]: [x/= 5] : [x = x / 5]
x = 10
x /= 2 
print(x)

x = 5
x %= 3
print(x)

x = 5
x //= 3
print(x)

x = 6
x **= 3
print(x)

x = 14
x &= 7
print(x)


# Python Comparison Operators

#Comparison operators are used to compare two value

x = 6
y = 5
print(x == y) # equall to 

x = 7
y = 6
print(x != y) # not equal to

x = 6
y = 7
print(x > y) #greater then 

x = 9
y = 10
print(x < y)  # less then

x = 3 
y = 4
print(x <= y)# less then or equal to

x = 8
y = 7
print(x >= y) # greater then or equal to

#Python Logical Operators

#Logical operators are used to combine conditional statements.


# And Opertors
# return true if both statement are true

x = 4
print(x > 6 and x < 5) #return false because 4 is less then 6 AND 4 is less then 5

#Or Operators
# return true if one ot the statement is true

x = 5
print(x > 4 or x < 3)
 # return true because one of the conditions are true 5 is grater then 4 
 # OR  5 is not less then 3

#NOT Operators
#Reverse the result, return false if the result is true
x = 10
print(not(x > 7 and x < 15))

#Python Identity Operators

#Identity operators are used to the object , not if they are equal,
#  but if they are actually the same object, with the same memory location  

# is Operators 
#Return true if both variables are the same object

x = [1,2,3]
y = [1,2,3]
z = x

print(x is y)
# return False because x is not the same object as y, even if they have same content 

print(x is z)
#return True because z is the same object as x

print(x == y)
#to demonsatrate the different between "is" and  "==" :
#  this comparison return True because x is equal to y

#IS NOT Operators 
# return true if both variables are not the same object

x = [1,2,3]
y = [1,2,3]
z = x

print(x is not z)
#return false because z is the same object as z

print(x is not y)
#return true because x is not the same object as y, even they have the same contrnt

print(x!=y)
# to demonstrate The difference between "is not" and "!=" :
# This comparison return false because x is equal to y

#Python membership Operators
#membership operators are used to test if a sequence is presented in an object
#In Operators
# return True if a sequence with the specified value is present in the object
x = [1,2,3]
print( 1 in x)
#return true because a sequence with the value 1 is in the list

#NOT IN Operators 
#return true if a sequence with the specified values is not present in the object 

x = [1,2,3]
print(not(6 in x))
