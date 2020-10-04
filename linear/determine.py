# any lowercase letter should be entered
c = input("letter(a - z): ")

#the ord() function rertunt the ordinal
#number of character is the symbol table

c = ord(c)

#the code of the first letter of the alphabet 
a = ord('a')

#since the letter follow i order by subtracting 
# the character code

n = c - a

#since it is necesery to find not the distance ,
#but the ordinal number of the 	letter in the alphabet 
#we add 1

n = n + 1
print("its number is %d " % n)

