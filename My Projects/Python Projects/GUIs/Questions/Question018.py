import matplotlib
import matplotlib.pyplot as plt

while True:
    user_input1 = int(input("No. of fibonacci numbers needed in the list : "))
    user_input2 = int(input("Max. no. of fibonacci numbers to be in list : "))

    fibonacci = [0,1]

    for i in range(2,user_input2):
        value = fibonacci[i-1] + fibonacci[i-2]
        fibonacci.append(value)

    fibonacci[:user_input1].pop()

    ordinate = []

    for i in range(user_input1,user_input2):
        ordinate.append(fibonacci[i] / fibonacci[i-1])

    print(ordinate)

    plt.plot(list(range(user_input2-user_input1)),ordinate)
    plt.show()