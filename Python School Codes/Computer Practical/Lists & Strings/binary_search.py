lst = []
num = int(input("Enter the number : "))
for i in range(num):
    e = int(input("Enter the element : "))
    lst.append(e)
lst.sort()

s = int(input("Enter the number : "))
f = 0
l = num-1
p = False

while (f<=l):
    mid = (f+l)//2
    if (lst[mid]<s):
        f = mid+1
    elif (lst[mid]>s):
        l = mid-1
    elif (lst[mid]==s):
        p = True
        break

if (p==True):
    print(f"The element '{s}', in the sorted list, is in position '{mid}'")
else:
    print(f"{s} is not found")