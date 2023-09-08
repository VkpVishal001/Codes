S = input("Enter the sentence : ")
S = S.split(" ")
L = []
max = 0

for i in S:
    if (len(i) > max):
        L.clear()
        L.append(i)
        max = len(i)
    elif (len(i) == max):
        L.append(i)

print(L)