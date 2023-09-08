def sum_of_digits(num):
    if (num==0):
        return 0
    else:
        return (num%10 + sum_of_digits(num//10))

value = int(input("Enter the number : "))
k = sum_of_digits(value)
print(k)