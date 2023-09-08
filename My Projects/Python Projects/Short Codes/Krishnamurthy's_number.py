def factorial(int):
    for i in range(2,int):
        int *= i
    return int


num = int(input("Enter the number : "))
m = num
sum = 0

while (m>0):
    r = m%10
    a = factorial(r)
    sum += a
    m //= 10

if (sum == num):
    print(f"{num} is a Krishnamurthy's number")
else:
    print(f"{num} is not a Krishnamurthy's number")