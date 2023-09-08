n = int(input("Enter no. of terms : "))
lst = [0,1]
for i in range(1,(2*n)+1) : lst.append(lst[i]+lst[i-1])
for i in lst[2::2] : print(i,end=" ")

# OR

# n = int(input("Enter no. of terms : "))
# a = 0
# b = 1
# for i in range(n):
#     c = a+b
#     a = c
#     b += c
#     print(c,end=" ")