num = int(input("Enter no. of co-ordinates of polygon : "))

xlist = []
ylist = []
results = []

for i in range(1,num+1):
	element = tuple(eval(input(f"Enter P{i} co-ordinate : ")))
	xlist.append(element[0])
	ylist.append(element[1])
	
def matrix(x1,x2,y1,y2):
	value = (x1*y2)-(y1*x2)
	results.append(value)
	
for i in range(num):
	matrix(xlist[i-1],xlist[i],ylist[i-1],ylist[i])
	
area = 0.5*abs(sum(results))
print(area)