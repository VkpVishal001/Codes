def product_of_all(l,i):
    if (i==len(l)):
        return 1
    else:
        return (l[i] * product_of_all(l,i+1))
    
k = eval(input("Enter the list of numbers : "))
result = product_of_all(k,0)
print(result)