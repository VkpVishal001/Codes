def LCM(a,b,i):
    if (i%a==0) and (i%b==0):
        return i
    else:
        return LCM(a,b,i+1)
    
a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : ")) 
k = LCM(a,b,max(a,b))
print()