import random

lower = int(input("Enter the lower limit : "))
upper = int(input("Enter the upper limit : "))
length = int(input("Enter length of limit : "))

numbers = set([])

while len(numbers)<length:
	element = random.randint(lower,upper)
	numbers.add(element)
	
print("\nNumbers :",numbers)