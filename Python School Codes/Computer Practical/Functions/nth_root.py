def nth_root(x,n=2):
    x_root_n = x**(1/n)
    return x_root_n

num = int(input("Enter the base : "))
exp = int(input("Enter its power : "))

result = nth_root(num,exp)
print(f"The {exp}th root of {num} is {round(result,2)}")