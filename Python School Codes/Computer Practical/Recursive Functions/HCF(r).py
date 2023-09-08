def HCF(a,b,i):
    if (a%i==0) and (b%i==0):
        return i
    else:
        return HCF(a,b,i-1)
    
a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : ")) 
k = HCF(a,b,min(a,b))
print(k)