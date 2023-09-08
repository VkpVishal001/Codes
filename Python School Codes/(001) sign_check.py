var=float(input("Enter the number : "))

if (var>0):
    print("The number is (+ve) and is equal to",var)
elif (var<0):
    print("The number is (-ve) and it's (+ve) value is equal to",(-1)*var)
else:
    print("The number is zero")