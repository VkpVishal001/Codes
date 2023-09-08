import tabulate

print("Open it in full-screen mode to fully view the table . Do as recommended .\n\n")

while True:
    user_input = int(input("How many rows you want in your pascal's triangle (Recommended : less than 22) ? : "))

    l = []

    for i in range(user_input):
        l.append([])

        for x in range(i+1):
            x = 1

            l[i].append(x)

    for i in range(len(l)):
        for x in range(1,len(l[i])-1):
            l[i][x] = l[i-1][x-1] + l[i-1][x]

    headers = []

    for i in range(user_input+1):
        headers.append(f"{str(i+1).zfill(2)}")

    print(f"\n\n{tabulate.tabulate(l, headers=headers, tablefmt='grid')}\n\n")
