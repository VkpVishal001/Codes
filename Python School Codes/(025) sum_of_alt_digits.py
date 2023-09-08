x = int(input("Enter the number : "))
m,y = x,x
n = 0
sum = 0

while (m>0):
    n += 1
    m //= 10

if (n%2==0):
    x //= 10

while (x>0):
    r = x%10
    sum += r
    x //= 100

print(f"Sum of alternate digits from beginning of {y} is {sum}")