"""
INDIAIDNI
 NDIAIDN
  DIAID
   IAI
    A
"""

a = "INDIA"
for i in range(5):
    for j in range(0,i):
        print(" ",end=" ")
    for j in range(i,5):
        print(a[j],end=" ")
    for j in range(5,9-i):
        print(a[8-j],end=" ")
    print()