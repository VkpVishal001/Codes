def digits(num,c):
    if (num==0):
        return c
    else:
        return digits(num//10,c+1)
    
value = int(input("Enter the number : "))
k = digits(value,0)
print(k)