#Dictionary 
#a dictionary is a collection which is unordered, changeable and indexed.
#in python dictionares are written in curly brakets and the have key and values

#create a dictionary

dic = {
    'name' : 'Rajendra kumar',
    'class' : 'two',
    'age' : 23
}
print(dic)

#Access items
#you cam access the items of a dictionary by reffering to its key name.
#  inside square brackets

x = dic['name'] #get the value of the 'name' key
print(x)

#there is also method called get() that will give you the  same  result.

x = dic.get('class')#get the value of he class key
print(x) 

#change values
#you can change the value of a specified item by reffering to its key name

dic['age'] = 6
print(dic)

#loop through a dictionary
#you can loop through a dictionary by using a for loop
#when looping through a dictionary the return values are key of the dictionary 
#but there are methods to return the values as well

for x in dic: #print all key names in the dictionary one by one
    print(x)

for x in dic: #print all values in the dictionary one by one
    print(dic[x])

#you can also use the values() function to return values of a dictionary
for x in dic.values():
    print(x)

#loop through both key and values, by using the items() function
for x, y in dic.items():
    print(x,' : ', y)

#check if key exists
#to determine if a specified key is present in a dictionary 
#use in keyword

if 'name' in dic:
    print('key is present in dictionary..')

#to determine how many items (key - value pairs)
#a dictionary has use the len() method
print(len(dic))

#adding item

dic['color'] = 'green'
print(dic)

#Nested Dictionary
member = {
    'child1' : {
        'name' : 'Akash',
        'school' : 'high school',
        'year' : 2002
    },
    'child2' : {
        'name' : 'bijay',
        'school' : 'high school',
        'year' : 2004
    },
    'child3' : {
        'name' : 'ajay',
        'school' : 'high school',
        'year' : 2007
    }
}

for c, v in member.items():
    print(c , '   : ' ,v)


#dictionary methods
# clear() : remove all the elements from the dictionary
#copy() : return copy of the dictionary
#fromkey(): return a dictionary with the specified keys and values
x = ('key1','key2','key3')
y = 0
di = dict.fromkeys(x,y)
print(di)
#keys : required an iterable specifying the keys of the new dictionary
#values : optional. the value for all the keys. defaut value is none

#get() : return the value of the specified key
#items() : returns a list containing a tuple for each key value pair

z = dic.items()
print(z)

#keys() : return a list containing the dictionary's keys

z = dic.keys()
print(z)

#pop() : remove the elements with the specified key
#popitems() : removes the last inserted key value paIR
#setdefault(): return the value of thE specified key.
#  if the code does not exist : insert the key with the specified value
x = dic.setdefault('name','Akash')
print(x)

#update(): update the dictionay with the soecified key value pairs
dic.update({'year' : 2011})

for x , y in dic.items():
    print(x,'  : ',y)

#values() : return a list of all the values in the dictionary
x = dic.values()
print(x)