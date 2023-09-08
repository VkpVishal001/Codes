def factorial(var):
    for i in range(2,var):
        var *= i
    return var


n = int(input("n = "))
r = int(input("r = "))

a = factorial(n)
b = factorial(r)
c = factorial(n-r)

result = int(a/(b*c))
print(f"C({n},{r}) = {result}")