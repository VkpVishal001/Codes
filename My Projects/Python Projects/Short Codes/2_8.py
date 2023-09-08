a = 0
b = 1
c = 0
lst = [0,1]
for i in range(7):
	c = a + b
	a = b
	b = c
	lst.append(c)
lst = tuple(lst)
print(lst)