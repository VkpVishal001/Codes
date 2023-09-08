def insert_original(e,l):
    if e in l:
        pass
    else:
        l.append(e)


lst = eval(input("List : "))

add_on = input("Enter value to be added : ")
insert_original(add_on,lst)
print(lst)