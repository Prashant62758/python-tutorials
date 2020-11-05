year = input("enter year for check whether leap or usual : ")
year = int(year)

if year%4 != 0:
	print("usual year")
elif year%100 == 0:
	if year %400 == 0:
		print("leap year")
	else:
		print("usual year")
else:
	print("leap year")
