def fibonacci(a,b,num):
    if (num==0):
        return a
    else:
        print(a)
        return fibonacci(b,a+b,num-1)
    
value = int(input("Enter the number : "))
k = fibonacci(0,1,value-1)
print(k)