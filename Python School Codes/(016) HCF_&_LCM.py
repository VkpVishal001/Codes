num1 = int(input("num1 = "))
num2 = int(input("num2 = "))
num3 = int(input("num3 = "))

hcf = 0
lcm = 0

for i in range(min(num1,num2,num3),0,-1):
    if ((num1%i) == (num2%i) == (num3%i) == 0):
        hcf = i
        break

print(f"HCF of {num1}, {num2}, and {num3} is {hcf}")

for i in range(max(num1,num2,num3),(num1*num2*num3)+1):
    if ((i%num1) == (i%num2) == (i%num3) == 0):
        lcm = i
        break

print(f"LCM of {num1}, {num2}, and {num3} is {lcm}")