#Python loops
#python have two primitive loop commands
#while loops
#for loops

# the while loops
#with the while loop we can execute a set of statements as long as a condition is true

i = 1
while i < 6: #print i as long as i is less then 6
    print(i)
    i += 1

#note : remember to increment i, or else the loop will continue forever

#the while loop requires relevant variables to be ready in this example we need to define
#ab indexing variable i which we set to 1

#The Break Statement
#with the break statement we can stop the loop even if the while conditionis true

#exit the loop when i is 4

i = 1
while i < 10:
    print(i)
    if i == 4:
        break
    i += 1

#The Continue Statement
#with the continue statement we can stop the current iteration and continue with thw next

i = 0
while i < 10:
    i += 1
    if i == 4: #note that number 4 is missig in the result         
        continue
    print(i) 

#The Else Statement 
# with the else statement we can run a block of code once when the condition no longer is true
#print a message once the condition is false 
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print('i is no longer less then 5')