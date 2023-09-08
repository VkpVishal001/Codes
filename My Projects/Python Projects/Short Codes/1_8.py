months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

date = input("Enter date <MMDDYYYY> : ")

print(f"{months[int(date[0:2])-1]} {date[2:4]} , {date[4:8]}")