n = 1
x = int(input("No. of lines : "))
for i in range(x): # When x : no. of lines (and not 5 , as in question) ...
	for j in range(i+1):
		print(i+j+n,end=" ")
		n += (x-2)-j # we use x-2 instead of 3
	print()
	n = 1