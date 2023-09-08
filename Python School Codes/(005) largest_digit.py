x=int(input("Enter the number : "))
n=x
l=0
while (n>0):
    s=n%10
    if (s>l):
        l=s
    n//=10
print(f"Largest digit of {x} is {l}")