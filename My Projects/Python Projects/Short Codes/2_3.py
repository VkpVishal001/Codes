lst1 = list(eval(input("Enter list 1 : ")))
lst2 = list(eval(input("Enter list 2 : ")))
lst3 = []

for i in range(max(len(lst1),len(lst2))):
	value = lst1[i]+lst2[i]
	lst3.append(value)
	
print("The sum of list1 and list2 is :",lst3)

