def cube(s=2):
    c = s**3
    return c

def char_checker(char1,char2):
    if (char1 == char2):
        return True
    else:
        return False
    
side = int(input("Enter side length of cube : "))
result1 = cube(side)
print(f"Cube of {side} is {result1}\n")

character1 = input("Enter the first character : ")
character2 = input("Enter the second character : ")
result2 = char_checker(character1,character2)
print(f"The fact that {character1} and {character2} are the same , is {result2}")
