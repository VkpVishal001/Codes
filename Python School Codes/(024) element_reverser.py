n = int(input("Enter the length of list : "))
lst = []
for i in range(n):
    e = int(input("Enter the element (number) : "))
    lst.append(e)

result = []
reverse = 0

for i in lst:
    m = i
    while (m>0):
        r = (m%10)
        reverse = (reverse*10)+r
        m //= 10
    result.append(reverse)
    reverse = 0

print(result)