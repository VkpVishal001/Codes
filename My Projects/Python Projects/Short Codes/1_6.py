def func1():
	global value
	value = float(input("Enter length ( in foots ) : "))
	return value
	
def func2():
	global inches
	inches=value*12
	return inches
	
def func3():
	print("Length ( in inches ) : ",inches)
	
func1()
func2()
func3()