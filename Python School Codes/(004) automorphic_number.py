n=int(input("Enter the number : "))
m=n
d=1
while (m>0):
    d*=10
    m//=10
m=n*n
r=m%d
if (r==n):
    print(f"{n} is an automorphic number")
else:
    print(f"{n} is not an automorphic number")