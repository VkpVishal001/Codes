import random

def choose_one(x,y):
    num = random.randint(x,y)
    return num

def choose_three(x,y):
    lst = list(range(x,y+1))
    lst2 = []
    for i in range(3):
        nums = random.choice(lst)
        print(nums)
        lst2.append(nums)
        lst.remove(nums)
    return lst2

lower_limit = int(input("Enter the lower limit of the number : "))
upper_limit = int(input("Enter the upper limit of the number : "))

return_one = choose_one(lower_limit,upper_limit)
return_three = choose_three(lower_limit,upper_limit)

print(f"One number between {lower_limit} and {upper_limit} is {return_one}")
print(f"Three number between {lower_limit} and {upper_limit} are {return_three}")