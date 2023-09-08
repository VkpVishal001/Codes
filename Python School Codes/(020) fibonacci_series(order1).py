n = int(input("Enter no. of terms : "))
a = 0
b = 1
print(a,end=" ")
print(b,end=" ")
for i in range(n-2):
    c = a+b
    a = b
    b = c
    print(c,end=" ")

# OR :

# n = int(input("Enter no. of terms : "))
# lst = [0,1]
# for i in range(1,n-1) : lst.append(lst[i]+lst[i-1])
# for i in lst : print(i,end=" ")