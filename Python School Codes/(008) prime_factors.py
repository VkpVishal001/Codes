num=int(input("Enter the number : "))
m=num
print(f"Prime factors of {num} are :",end=" ")

while (m>1):
    for i in range(2,m+1):
        if (m%i==0):
            print(i,end=" ")
            m//=i
            break