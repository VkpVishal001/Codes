def GP(a,r,n,sum):
    if (n==0):
        return [a,sum]
    else:
        k=a*r
        return GP(k,r,n-1,sum+k)
    
a,r,n = 3,3,5
k = GP(a,r,n-1,a)
print(k)