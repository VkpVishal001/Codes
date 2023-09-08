# Question

"""

"""

# Answer :

def BubbleSort(l):
    for i in range(1,len(l)):
        for j in range(1,len(l)):
            if (l[j-1] < l[j]):
                l[j-1],l[j] = l[j],l[j-1]
    return l

def display(s):
    print(f"Before sorting , the list was : {s}")

    a = BubbleSort(s)
    print(f"After sorting , the list is : {a}")

n = int(input("Enter the length of the list : "))
lst = []
for i in range(n):
    e = int(input("Enter the element : "))
    lst.append(e)

display(lst)

# Variable Description :

"""
 
"""

# Output :

"""

"""