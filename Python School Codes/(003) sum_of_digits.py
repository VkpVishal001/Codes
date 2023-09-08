s=0
x=int(input("Enter the number : "))
while (x>0):
    d=x%10
    s+=d
    x//=10
print(f"Sum of digits of {x} is {s}")