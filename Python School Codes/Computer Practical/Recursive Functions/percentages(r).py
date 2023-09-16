def p(n,r):
    if (r==100):
        return n
    else:
        k = round((r/100)*n,2)
        print(k)
        return p(n,r+1)
    
num = int(input("Enter the number : "))
x = p(num,1)
print(x)