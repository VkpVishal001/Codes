def factorial(num):
    if (num==0):
        return 1
    else:
        return (num * factorial(num-1))
    
value = int(input("Enter the number : "))
k = factorial(value)
print(k)