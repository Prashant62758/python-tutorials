#Tuples : A tuple is a collection which is ordered and unchangeable.
#  In python tuple are written with round brackets.

#to create tuple with only one item you have add a comma after the item
#  unless python will not recognize variable as tuple 
tpl = ('hello')#not a tuple 
print(type(tpl))
tpl = ('hello',)
print(type(tpl))

#create a tuple
tple = ('hello','hello2','world','world2','python','python2')
print(type(tple))

#Access tuple items
#you can access tuple items by referring to the index number, inside square brackets:

print(tple[1])# print the second item in the tuple

#negative indexing
#negative indexing means beginning from the end, -1 refers to the last items
  
print(tple[-1])# PRINT THE LAST ITEM IN THE TUPLE

#RANGE OF INDEX
# you can specify a range of  index by specifying where to start and  where to end the range
# WHEN  SPECIFYING RANGE THE RETURN VALUE WILL BE A NEW LIST WITH THE SPECIFYIED ITEMS 
print(tple[1:3])
#note : the search will start at 1 first index(included) and end at 3 last index(not included)
#remember that the first item has  index 0

#range of negartive indexs
#specify negative indexs if you want to start  the search from the end of the tuple
print(tple[-4:-2]) 
#Negative indexing means starting from the end of the tuple
#this example returns the items from index -4 (included) to index -2(excluded)
#remember that the last item has the index -1

#change the tuple value
#once a tuple is create. You cannot change its value .
#  Tuples are unchangeable or immutable as it also is called
#but there is a workaround. You  can convert 
# the tuple into a list change the list and convert the list into a tuple

lis = list(tple)
lis[1] = 'hello22'
tple = tuple(lis)
print(tple)

#loop through a tuple
#you can loop through the tuple item by using a for loop

for x in tple:
    print(x)

#check if item exists
# to determine if a specified items is present in a tuple us the in keyword
if 'hello' in tple:
    print("item is in the tuple")

#tuple length
#To determine how many item a tuple has use the len() method 
print(len(tple))

#remove item 
#cannot remove item in a tuple

#join two tuple 
t1 = ('brown','black')
t2 = ('green','yellow')
t = t1 + t2
print(t)
