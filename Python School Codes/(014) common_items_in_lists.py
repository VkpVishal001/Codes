l1 = list(eval(input("List 1 : ")))
l2 = list(eval(input("List 2 : ")))

# n1=int(input("Enter length of l1 : "))
# l1=[]

# for i in range(n1):
#     e1=int(input("Enter element of l1 : "))
#     l1.append(e1)

# n2=int(input("Enter length of l2 : "))
# l2=[]

# for i in range(n2):
#     e2=int(input("Enter element of l2 : "))
#     l2.append(e2)

print("Common elements in both lists :",end=" ")

for x in l1:
    for y in l2:
        if (x==y):
            print(x,end=" ")