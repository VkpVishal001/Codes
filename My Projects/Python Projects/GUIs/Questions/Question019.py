import math

while True:
    velocity = float(input("Enter initial velocity : "))
    angle = float(input("Enter angle of projection : "))

    g = 9.8

    angle1 = math.radians(angle)
    angle2 = math.radians(2*angle)

    sine = round(math.sin(angle1), 2)
    sine2 = round(math.sin(angle2), 2)

    time = round((2*velocity*sine) / g, 2)
    height = round(((velocity**2) * (sine**2)) / (2*g), 2)
    distance = round(((velocity**2) * sine2) / g, 2)

    print(f"Time of flight = {time}\nMaximum height = {height}\nHorizontal Range = {distance} \n\n")
