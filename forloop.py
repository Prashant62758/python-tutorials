#python for loop
# a for loop is used for iterating over a sequence(that is either a list , a tuple, a dictionary, a set or a string)
#with the for loop we can execute a set of statements once for each item in a list ,tuple etc

#print each cars in a cars list
cars = ['bmw','honda','suzuki']
for x in cars:
    print(x)

#the for loop does not require an indexing variable to set beforehand

#looping Through a String
#even  string are iterable objects the contain a sequence of characters

for x in 'honda':
    print(x) 

#The Break Statement
#with the break statement we can stop the loop before it has looped through all the items

#exit the loop when x is 'honda'
for x in cars:
    print(x)
    if x == 'honda':
        break
#exit the loop when x is 'honda'. but this time the break comes before the print

for x in cars:
    if x == 'honda':
        break
    print(x)

#The Continue Statement

#with the continue statement we can stop the current iteration of the loop and continue with the next
for x in cars:
    if x == 'honda':
        continue
    print(x)


#The Range() Function
#to loop through a set of code a specified number of time we can use the range() function
#the rangefunction returns a sequence of numbers starting from 0
#by default and increment by 1 (by defualt ). and end at a specified number
for x in range(6):
    print(x)


#note that range(6) is not the values of 0 to 6 but the value 0 to 5

#the range() function defualt to 0 as a starting values however it is possible to specified 
#the starting value by adding a parameter range(1,5), which means value from 1 to 5(but not including 5)
for x in range(1,5):
    print(x)

#the range() function defaults to increment the sequence by 1 however it is possible to specify the 
#increment value by adding a third parameter range(2,30,3)
for x in range(3, 30, 3):
    print(x)

# else in for loop
#the else keyword in a for loop specifirs a block of code to be executed when the loop is finished
for x in range(10):
    print(x)
else:
    print('finished')

#print all the number from 0 t0 9 and print a message when the loop has ended

#Nested loops
#a nested loo is a loop inside a loop
#the inner loop will be execute one time for each iteration of the outer loop

lo = ['black','red','green']
f = ['apple','ball','cat']
for x in lo:
    for y in f:
        print(x,y)

#the pass statement
#for loops cannot be empty but if you for some reason have a for loop with no content
#  put in the pass statements to avoid getting an error

for x in [0,1,2]:
    pass
# having an empty for loop like this would raise an error without the pass statement