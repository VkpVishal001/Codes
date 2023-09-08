def digits_sum(var1):
    sum = 0

    while (var1>0):
        r = var1%10
        sum += r
        var1 //= 10
    
    return sum


def primes_digits_sum(var2):
    lst = []
    sum = 0

    while (var2>1):
        for i in range(2,var2+1):
            if (var2%i==0):
                lst.append(i)
                var2//=i
                break

    for i in lst:
        a = digits_sum(i)
        sum += a

    return sum

num = int(input("Enter the number : "))

x = digits_sum(num)
y = primes_digits_sum(num)

if (x==y):
    print(f"{num} is a Smith's number")
else:
    print(f"{num} is not a Smith's number")