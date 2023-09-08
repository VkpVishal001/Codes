num = int(input("Enter the number : "))
m = num
n = 0
sum = 0

while (m>0):
    r = m%10
    n += r
    m //= 10

while (n>0):
    r = n%10
    sum += r
    n //= 10

if (sum==1):
    print(f"{num} is a magic number")
else:
    print(f"{num} is not a magic number")