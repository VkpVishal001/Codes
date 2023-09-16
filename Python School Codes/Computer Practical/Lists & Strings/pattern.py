"""
INDIAIDNI
 NDIAIDN
  DIAID
   IAI
    A
"""

a = input("Enter the word : ")
print()
k = len(a)
for i in range(k):
    for j in range(0,i):
        print(" ",end=" ")
    for j in range(i,k):
        print(a[j],end=" ")
    for j in range(k,((2*k)-1)-i):
        print(a[((2*k)-2)-j],end=" ")
    print()