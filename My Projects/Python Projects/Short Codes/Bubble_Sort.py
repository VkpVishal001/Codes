lst = [15,12,7,19,4]
for i in range(len(lst)):
	for j in range(len(lst)-1):
		if lst[j]>lst[j+1]:
			lst[j],lst[j+1] = lst[j+1],lst[j]
print(lst)