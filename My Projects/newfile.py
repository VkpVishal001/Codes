def prime_number(n):
    for i in range(2,n//2-1):
        if (n%i==0):
            return False
    return True
    
k = prime_number(33)
print(k)

