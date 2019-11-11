# python lambda 
# a lambda function is a small anonymous function
# a lambda function can take any number of arguments but can only have one expression

x = lambda a : a + 10
print(x(3))


#a lambda function that multiplies  argument a with argument to and pass the result

x = lambda a, b : a * b
print(x(2,4)) 

x = lambda a, b, c : a + b + c
print(x(4,5,2))

#use that function definition to make a function that always double the number you send in

def myfun(number):
    return lambda a : a * number
doubler = myfun(2)
print(doubler(15))

def myfun(number):
    return lambda a : a * number
tripler = myfun(3)
print(tripler(15))

#or you can use 
def myfun(number):
   return lambda a : a * number
d = myfun(2)
t = myfun(3)
print(d(10))
print(t(20))

#use lambda function when an anonymous function is required for a short period of time