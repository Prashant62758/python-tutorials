#user input
ui = input("enter number to check wheter odd or even : ")
#converting it ti integer type
ui = int(ui)
#the % operator  return the residue of division
if ui % 2 == 0:
	print("even number")
else:
	print("odd number")
