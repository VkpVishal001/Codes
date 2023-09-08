n = int(input("Enter the length of the list : "))
lst = []
for i in range(n):
    e = input("Enter the element : ")
    lst.append(e)

lst.sort()
x = 1

for i in range(1,len(lst)):
    if (lst[i-1] == lst[i]):
        x += 1
    else:
        print(f"{lst[i-1]} is present {x} times")
        x = 1

print(f"{lst[i]} is present {x} times")