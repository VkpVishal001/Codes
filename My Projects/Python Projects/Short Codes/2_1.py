var = input("Enter a valid phone no. : ")
var=var.split("-")
validity = 0

if (len(var[0]) == len(var[1]) == 3) and (len(var[2]) == 4):
	for i in range(3):
		if var[i].isdigit() == True:
			validity += 1
		else:
			pass
			
	if validity == 3:
		print("Valid phone number")
	else:
		print("Invalid phone number")
		
else:
	print("Wrong format")

