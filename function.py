#Function
#function is a block of code which only runs when it called
#you can pass data known as parameters into a function 
#a function can return data as a result

#creating a function
#in python a function is defined using the def keyword

def my_fun():
    print('hello world')

my_fun() # calling a function 

#Parameters
#information can be passed to function as parameter
#parameter are specified after the function name inside the parentheses.
# you can also add many parameters as you want, just separate them with a comma

def myfun(color):
    print(color + 'colour')
myfun('green') 
myfun('blue') 
myfun('pink') 

#default parameter value
#if we call the function without parameter it use default value
def my_fun(like = 'fruits'):
    print('i like ' + like)
my_fun('vagetables')
my_fun('guitar')
my_fun('music')
my_fun()

#Passing a list as a parameter
#you can send any data types of parameter to a function
#(string, number, list, dictionary) and it will be treated as the same data types inside the function
def myfun(like):
    for i in like:
         print('i likes ' + i)
likes = ['music','game','dance','friuts']
myfun(likes)

#return value
#to let a function return a value use the return statement

def myfun(x):
    return 2 * x

print(myfun(4))
print(myfun(8))
print(myfun(5))

#keyword arguments 
#you can also send argument with the key = value syntax
def myfun(c1,c2,c3):
    print('first colour ' + c1)
myfun(c1='green', c2 = 'red', c3 = 'black')

#the pharse keyword argument are often shortened to kwargs in python
#if you dont know how many arguments that will be passed into your function 
#add a * before the parameter name in the function definition
def myfun(*args):
    print('first student is ' + args[1])

myfun('rajesh','rakesh','hari')
