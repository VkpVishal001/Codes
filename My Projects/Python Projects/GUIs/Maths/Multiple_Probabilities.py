import math


def C(x,y):
    difference = x-y

    def factorial(num):
        for i in range(1,num):
            num *= i
        return num

    var1 = factorial(x)
    var2 = factorial(y)
    var3 = factorial(difference)

    a = var2 * var3
    hcf = math.gcd(a,var1)

    result = f'{int(a / hcf)} / {int(var1 / hcf)}'

    return result


while True:
    x = int(input("Total no. of possibilities : "))
    y = int(input("No. of favourable outcomes : "))

    print(f"Probability of getting the desired outcome : {C(x,y)}")
