a = [1,2,3,4,5]
b = [4,5,6,7,8]

def listDifference(list1, list2):
	for element in list2:
		if(element in list1):
			list1 = [x for x in list1 if x != element]
	return list1

def listUnion(list1, list2):
	list1 = listDifference(list1, list2)
	for element in list2:
		list1.append(element)
	return list1

print("List 1:", a)
print("List 2:", b)

print("Difference:", listDifference(a,b))
print("Union:", listUnion(a,b))
