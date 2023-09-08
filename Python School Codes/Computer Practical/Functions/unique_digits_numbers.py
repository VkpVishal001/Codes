# Question

"""

"""

# Answer :

def unique(variable):
    is_unique = True
    list_1 = []

    while (variable > 0):
        remainder = variable % 10
        variable //= 10
        if remainder not in list_1:
            list_1.append(remainder)
        else:
            is_unique = False
            break

    if is_unique == True:
        return True
    else:
        return False

length = int(input("Enter the length of the list : "))
list_2 = []
for i in range(length):
    element = int(input("Enter the number to be added : "))
    list_2.append(element)

for j in list_2:
    value = unique(j)
    if value == True:
        print(j, end=" ")
    else:
        pass

# Variable Description :

"""
1. variable :
2. is_unique :
3. list_1 :
4. remainder : 
5. length :
6. list_2 : 
7. i :
8. element :
9. j :
10. value : 
"""

# Output :

"""

"""