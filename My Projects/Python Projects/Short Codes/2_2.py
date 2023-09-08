words = input("Enter sentence(s) : ")
alnum = 0

lst = []
for i in words:
	lst.append(i)
	
lst2 = words.split()
for i in lst2:
	if i.isalnum() == False:
		lst2.remove(i)
		
for i in lst:
	if i.isalnum() == True:
		alnum += 1
alnum *= 100

print("Number of words in the given sentence(s) is :",len(lst2))
print("Number of characters in the given sentence(s) is :",len(lst))
print("Percentage of alpha-numeric characters in the given sentence(s) is :",round((alnum/len(lst)),2))