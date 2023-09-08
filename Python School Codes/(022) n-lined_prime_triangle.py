n = int(input("Enter no. of rows : "))
x = 3

for i in range(n):
    print(2, end=" ")
    for j in range(i):
        ok = False
        while (not ok):
            ok = True
            for k in range(2,x):
                if (x%k == 0):
                    ok = False
                    break
            if (not ok):
                x += 1
        print(x, end=" ")
        x += 1
    x = 3
    print()