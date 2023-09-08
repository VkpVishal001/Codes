def matrix(lst):
	order = input("Enter the order of matrix (like 2,3) : ")
	print()
	
	order = order.split(",")
	
	for i in range(2): 
		order[i] = int(order[i])
		
	lst = []
	
	for i in range(order[0]):
		row = input("Enter the elements of row ( separared by comma ) : ")
		row = row.split(",")
		
		for i in range(len(row)) : row[i] = int(row[i])
		lst.append(row[0:order[1]])
		
	print("\n")
	print("-"*50)
	print("\n")
	
	return lst


def add_matrix(lst1,lst2,lst3):
	row1=len(lst1)
	col1=len(lst1[0])
	row2=len(lst2)
	col2=len(lst2[0])
	
	if (row1==row2) and (col1==col2):
		for i in range(row1*col1):
			lst3.append(lst1[i//row1][i%row1]+lst2[i//row1][i%row1])
		n = col1
		
	lst3 = [lst3[i:i + col1] for i in range(0, len(lst3), col1)] 
	
	print("Addition of the two matrices : \n")
	for i in lst3:
		print(i)
			
			
lst1 = []
lst2 = []
lst3 = []

a = matrix(lst1)
b = matrix(lst2)
add_matrix(a,b,lst3)