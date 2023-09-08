num=int(input("Enter the number : "))

tp=True
rev=0

for i in range(2,num):
    if (num%i==0):
        tp=False

if (tp==True):
    m=num

    while (m>0):
        r=m%10
        rev=(rev*10)+r
        m//=10

    for i in range(2,rev):
        if (rev%i==0):
            tp=False

if (tp==True):
    print(f"{num} is a twisted prime")
else:
    print(f"{num} is not a twisted prime")