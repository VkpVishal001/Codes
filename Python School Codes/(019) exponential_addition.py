x = int(input("Enter the number : "))
n = int(input("Enter number of terms : "))
result = 0

for i in range(1,n+1):
	factorial = 1
	for j in range(1,i+1):
		factorial *= j
	result += (x**i)/factorial
	
print(result)