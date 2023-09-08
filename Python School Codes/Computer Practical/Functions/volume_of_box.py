def volume(l=1,b=1,h=1):
    v = l*b*h
    return v

length = int(input("Enter the length of box : "))
width = int(input("Enter the width of box : "))
height = int(input("Enter the height of box : "))

result = volume(length,width,height)
print(result)