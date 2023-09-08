def power(num,exp):
    if (exp==0):
        return 1
    else:
        return (num*power(num,exp-1))
    
value1 = int(input("Enter the base : "))
value2 = int(input("Enter the power : "))
k = power(value1,value2)
print(k)