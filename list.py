#list : list is a collection which is ordered and changeable. Allows duplicate members
#tuple : Tuple a is collection which is ordered and unchangeable. Allows duplicate members
#set : Set is a collection which is unordered and unindexed. No duplicate members
#dictionary: Dictionary is a collecation which is unordered, 
# changeable and indexed . no duplicate 

#LIST
#create a list
li = ['hello','hello2','world','world2','python','python2']
print(li)
# remember that the first item has index 0
print(li[1]) #print the second of the list
#negative indexing
#negative indexing means begining from the end -1 refers to the last .-2refers to the second last.
print(li[-1])#print the last item of the list 

#RANGE OF INDEX
# you can specify a range of index by specifying where to start and where to end  the range
#when specifying range> the return value will be a new list with the specifyied items
print(li[1:5]) # return the second, third, fourt,fifth items

#note : The search will start at index at 1(included) and end at index 5(not included)

#Range of NEgative Indexes
#Specify negative indexes the item from indexes if you want to start the search from the end of the list
print(li[-3:-1])


#Change Item Value 
#To change the value of a specific item, refer to indes numbers

li[4]='python1' #change the fifth items
print(li)

#loop Through a List
# for loop
# you can loop through the list items by using a for loop 
for x in li:
    print(x) #print all items in the list. one by one


#Check if item exists
# to determine if a specified items is present in a list use the (in) keyword
if 'hello' in li: #check if item is present in list
    print('item is in the list ')
else:
    print('item is not in list')
    
#LIST LENGTH
#to determine how many items a list has, use the len() function:
length_item = len(li)  #print the number of items in the list
print(length_item)

#Add Items

#to add an item to the end of the list, use the append() method:
li.append('python3') #append method to append an item
print(li)
#insert method
li.insert(1,'gello') #insert item as the second position
print(li)
#remove method
li.remove('hello') #remove item as the specified items
print(li)

#pop method
#the popmethod removes the specified index. (or the last item if index is not specfied)
li.pop()
print(li)

# del method 
# del keyword removes the specified indexdatetime A combination of a date and a time. Attributes: ()
del li[0]
print(li)

#clear method 
#clear method empities the the list
# li.clear()
# print(li)


#copy a list 
copy_li = li.copy()
print(copy_li)

#another way to makeacopy is to use the built-in method list()
new_li = list(li) #make a copy of a listwith the list() method
print(new_li)


#Join two list
l2 = [1,2,3,4]
l3 = li + l2
print(l3)

#another way to join two lists are by appending all the items from l2 int li ,one by one
for x in l2:
    li.append(x)  #append l2 into li
print(li) 

#or use the extend method , which purpose is to element from one to another list 

li.extend(l2) # add l2 at the end of li
print(li)

#the list constructor 
# it also possible to use the list() constructor to make a new list 
lis = (1,2,3,4)
list_constructor = list(lis)
print(list_constructor)

# list method
#python has set of built-in methods thaT you can use on lists

#append()method : Adds an element at the end of the list
#clear() :removes all the elements from the list
#copy() : Return a copy of the list
#count() : Returns the number of elements with the specified value
#extend() : Add the elements of a list (or any iterable), to the end of the current list
#index() : Return the index of the first element with the specified value
#insert() : Add an element at the specified value
#pop() : Removes the element at the specified

#reverse(): reverse the order of the list
l = [1,2,3,4,53,4,34,54,38]
l.reverse()
print(l)#[38, 54, 34, 4, 53, 4, 3, 2, 1]
#remove(): removes the element at the specified position

#sort(): Sort the list alphabetically
l.sort()
print(l) #[1, 2, 3, 4, 4, 34, 38, 53, 54]