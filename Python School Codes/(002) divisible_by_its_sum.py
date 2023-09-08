var=int(input("Enter the number : "))

quo=var//10
rem=var%10
sum=quo+rem

if (var%sum==0):
    print(f"{var} is divisible by the sum of it's digits")
    
else:
    print(f"{var} is not divisible by the sum of it's digits")