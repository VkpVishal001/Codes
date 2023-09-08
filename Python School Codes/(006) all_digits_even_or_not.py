x=int(input("Enter the number : "))
n=x
a=True
while (n>0):
    d=n%10
    if (d%2!=0):
        a=False
        break
    n//=10
if a==True:
    print(f"All digits of {x} are even")
else:
    print(f"All digits of {x} are not even")