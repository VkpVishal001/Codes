n=int(input("Enter number : "))
sum=0

if (n!=0):
	for i in range(int(n),int((2**n))+1,1):
		sum+=i
		
if (n==0):
		sum=1
		
print("Sum of numbers between n and 2^n is :",sum)


		