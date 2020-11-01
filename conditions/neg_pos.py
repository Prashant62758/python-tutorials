#user input a number 
ui = input("enter a number: ")
ui = float(ui) #converting  it to a floating point number

if ui > 0:
	print("positive number")
elif ui < 0:
	print("negetive number")
else:
	print("zero ")
