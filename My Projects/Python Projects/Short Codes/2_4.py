var = input("Enter word : ")
var1 = list(var)
for i in range(-1,-1*len(var1)-1,-1):
	var1[i] = var[i+1]
var2 = "".join(var1)
print(var2)