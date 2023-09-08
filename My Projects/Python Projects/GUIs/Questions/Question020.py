import matplotlib
import matplotlib.pyplot as plt
import math

while True:
    velocity = float(input("Enter initial velocity : "))
    angle = float(input("Enter angle of projection : "))

    g = 9.8

    angle1 = math.radians(angle)
    angle2 = math.radians(2*angle)

    sine = round(math.sin(angle1), 2)
    sine2 = round(math.sin(angle2), 2)
    cosine = round(math.cos(angle1), 2)

    time = int(2*velocity*sine / g)
    height = round((g*(time**2)) / 8, 2)
    distance = round(height * 4 * (cosine/sine), 2)

    distances = []
    heights = []

    height1 = 0
    distance1 = 0

    for i in range(100):
        time1 = round(time / 100, 2)
        velocity1 = round(velocity / 100, 2)

        if i<50:
            height1 += (g*(((time1 / 2) * (50-i)) ** 2)) / 8
        elif i>49:
            height1 -= (g*(((time1 / 2) * (i-49)) ** 2)) / 8

        distance1 += velocity1 * cosine * time

        distances.append(distance1)
        heights.append(height1)

        with open("observation.txt", "a") as writ:
            writ.write(f"Time : {time1*i} , Height : {height1} , Range : {distance1}\n")

    plt.xlim(0,math.ceil(distance1))
    plt.ylim(0,math.ceil(distance1))

    plt.plot(distances,heights)
    plt.show()