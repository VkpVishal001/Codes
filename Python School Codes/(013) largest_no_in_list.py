L=[]

for i in range(10):
    x=int(input("Enter the number : "))
    L.append(x)

max=L[0]

for i in range(1,10):
    if L[i]>max:
        max=L[i]

print("\n",L,"\n")
print(f"The largest number is {max}")