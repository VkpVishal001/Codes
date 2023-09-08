day = input("Day of this year's new year day [Full name] : ")
num = int(input("Day number of the date to be known ( 2 to 365 ) : "))

days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

day=day.capitalize()

if day in days:
	a = num%7
	res = days.index(day)+a-1
	
	if res>6:
		res-=7
		
	print("The day whose day number is given will be",days[res])
	
else:
		print("Check spelling of the day given .")	