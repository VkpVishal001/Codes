var1 = input("Enter 1st word : ")
var2 = input("Enter 2nd word : ")

var3 = list(tuple(var1))
var4 = list(tuple(var2))

var3.sort()
var4.sort()

if (var3 == var4):
	print(f"{var1} and {var2} are anagrams .")
else:
	print(f"{var1} and {var2} are not anagrams .")