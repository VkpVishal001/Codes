def reverse(num,r):
    if (num==0):
        return r
    else:
        return reverse(num//10, r*10+(num%10))
    
value = int(input("Enter the number : "))
k = reverse(value,0)
print(k)