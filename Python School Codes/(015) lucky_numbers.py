n=int(input("Enter the number : "))
lst=list(range(1,n+1))
f=2

while (f<=len(lst)):
    for i in range(f-1,len(lst),f):
        lst[i]=0

    for j in lst:
        if (j==0):
            lst.remove(j)
            
    f+=1

print(f"Lucky numbers from 1 to {n} are :",end=" ")
for i in lst:print(i,end=" ")