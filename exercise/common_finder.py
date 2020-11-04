def common_finder(l1,l2):
	output = []
	for i in l1:
		if i in l2:
			output.append(i)
	return output

list1 = [1,2,3,4,5,6]
list2 = [2,3,4,6]
print(f"list1 = {list1} and list2 = {list2}")
common = common_finder(list1,list2)
print("common: " ,common)
