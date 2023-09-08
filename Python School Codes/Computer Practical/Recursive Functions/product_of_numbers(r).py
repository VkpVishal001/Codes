def product(x,y,n):
    if (n==x):
        return 0
    else:
        return (y + product(x,y,n+1))
    
a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
k = product(min(a,b),max(a,b),0)
print(k)