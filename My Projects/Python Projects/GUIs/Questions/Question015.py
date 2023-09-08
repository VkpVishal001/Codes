while True:
    user_input = int(input("Enter the number : "))
    list1 = []

    for i in range(1,user_input):
        if user_input % i == 0:
            list1.append(i)

    result = sum(list1)

    if result > user_input:
        print(f"{user_input} is an abundant number .")

    elif result == user_input:
        print(f"{user_input} is a perfect number .")

    else:
        print(f"{user_input} is neither an abundant number nor a perfect number .")