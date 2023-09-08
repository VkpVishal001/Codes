var = input("Enter some words ( separated by a comma ) : ")
lst = var.split(",")
lst2=[]
for i in range(len(lst)):
	lst2.append(len(lst[i]))
print(lst[lst2.index(max(lst2))])