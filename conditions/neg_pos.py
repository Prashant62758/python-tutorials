#user input a number 
ui = input("enter a number: ")
ui = float(ui) #converting  it to a floating point number

#if the number is greater then zero
# output positive
if ui > 0:
	print("positive number")
#if the number is less then zero 
#output negative
elif ui < 0:
	print("negative number")
#in all other case 
else:
	print("zero ")

