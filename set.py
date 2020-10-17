#Set 

#a set is a collection which is unorderd
#  and unindexed in python sets are written with curly bracket

#create a set
s = {1,2,3,4,5,6,7}
print(s) 
#Note : SETS ARE UNORDERED SO YOU CANNOT BE SURE IN WHICH ITEMS WILL APPEAr


#loop through the set

for x in s:
    print(x)
#CHECK IF item is in the set

if 2 in s:
    print("item is peresent in the set")

#change item

#once a set is created you cannot change its value but  you can add new list

#ADD items 
# to add one item to a set use the add() method

s.add('222')
print(s)
# to add  more then one item to a set use the update() method

s.update([11,21,34,23])
print(s)

#get the length of a set 
# to determine how many  items a set has use the len() method

print(len(s)) #get the number of items in a set 

#remove item
#to remove item in a set use the remove() or the discard()method

s.remove(34)
print(s)

#note : if the item to remove does not exist remove() will raise an error

#remove 11 by using discard method

s.discard(11)
print(s)

#note : if the item to remove does not exist discard() will not raise an error

#you can also use the pop() method to remove an item but this method will remove the last item
# remember that sets are unordered so you ill not know what items that gets removed
s_p = s.pop() 
print(s_p) #remove item
print(s) # the set after removal
#note : set sre unordered so when using the pop() method you will not know which item that gets removed

#clear method
# the clear Method empities the set 
# s.clear()
# print(s)

#del keyword will delete the set completely

# del s
# print(s)

#JOIN TWO SETS 
# there are several way to join two or more set in python 
#you can use the union() method that returns a new set 
# containing all items from both sets or 
# the update() method that  inserts all the items from one set into another.

#the union method returns a new set with all items from both sets
set1 = {'a','b'}
set2 = {1,2}
set3 = set1.union(set2)
print(set3)

#the update()method insert the item in set2 into set1

set1.update(set2)
print(set1)

# note : both union() and update() will exclude any duplicate item


#SET METHODS

#add() : add an element to set
#clear : remove all the item from the set 
#copy(): return a copy of the set
#difference() : return a set contining the diference between two or more sets
x = {'apple', 'ball', 'cat'}
y = {'apple', 'bat', 'car'}
z = x.difference(y)
#return a set that contains the items that only exist x and not in set y
print(z)
# difference_update() : removes the items in this set that are also included in another specified set
x.difference_update(y) 
#remove the items that exist in both sets
print(x)

#discard() : remove the specified item
#intersection() : return the set that is the intersection of two other sets
# to intersection first comment both difference and difference_update methods
z = x.intersection(y)
print(z)


#intersection_update(): remove the items in this set that are not present in other specified sets(s)
x.intersection_update(y)
print(x)

# isdisjoint() : returns whether tWO set haVe a interaction or not
z = x.isdisjoint(y)
print(z)
#issuperset(): return wether this set contain another set or not
# pop(): remove an element from the set
#remove() : remove the specified element
# symmetric_difference() : return a set with th symmetric difference a two set
#symmetric_fifference_update() : inserts the symmetric difference from this set and another 
#union(): return a set containing the union of sets
#update() : update the set with the union of this set and other 
