import matplotlib.pyplot as plt
import math

while True:
    input1 = input("Enter the type of graph ( sin , cos or quit ) : ")

    if input1.lower() == "quit":
        print("Closing ...")
        break

    input2 = int(input("Enter the maximum angle ( starting from nil ) : "))

    def graph():     
        theta = list(range(input2+1))

        plt.plot(theta,value)
        plt.plot([-1*input2,input2],[0,0])
        plt.plot([0,0],[-1,1])
        plt.show()
        print()

    if input1.lower() == "sin" or input1.lower() == "sine":
        value = [math.sin(math.radians(x)) for x in range(input2+1)]
        graph()

    elif input1.lower() == "cos" or input1.lower() == "cosine":
        value = [math.cos(math.radians(x)) for x in range(input2+1)]
        graph()

    else:
        print("Invalid command , re-starting the program ...\n\n")