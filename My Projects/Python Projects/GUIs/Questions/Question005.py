# Question  : How to make all possible pairs of a list ?

# Program : Creating a function which will create all possible pairs of a list ( order of element matters )

while True:
    grand_list = input("Enter the elements of the list ( separated by a comma ) : ").split(",")

    elements_no = len(grand_list)

    final_list = []

    for i in range(elements_no):
        for j in range(elements_no):
            final_list.append([grand_list[i], grand_list[j]])

    for i in final_list:
        if i[0] == i[1]:
            final_list.remove(i)

    print(final_list)