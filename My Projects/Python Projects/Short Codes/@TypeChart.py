import tabulate

print(tabulate.tabulate(["Pokemon Type Charts"],tablefmt="grid"),"\n\n")

def info():
	"""
	
	
	
	
	"""

print(tabulate.tabulate(["|1. Attack Types Chart|"]),"\n\n")

list1=["Grass","Fire","Water","Normal","Bug","Poison","Flying","Electrc","Ground","Rock","Ice","Steel","Fight","Dark","Ghost","Psychic","Dragon","Fairy"]

list2=[list1[0]]+["-","-","+","","-","-","-","","+","+","","-","","","","","-",""]
list3=[list1[1]]+["+","-","-","","+","","","","","-","+","+","","","","","-",""]
list4=[list1[2]]+["-","+","-","","","","","","+","+","","","","","","","-",""]
list5=[list1[3]]+["","","","","","","","","","-","","-","","","*","","",""]
list6=[list1[4]]+["+","-","","","","-","-","","","","","-","-","+","-","+","","-"]
list7=[list1[5]]+["" for i in range(18)]
list8=[list1[6]]+["" for i in range(18)]
list9=[list1[7]]+["" for i in range(18)]
list10=[list1[8]]+["" for i in range(18)]
list11=[list1[9]]+["" for i in range(18)]
list12=[list1[10]]+["" for i in range(18)]
list13=[list1[11]]+["" for i in range(18)]
list14=[list1[12]]+["" for i in range(18)]
list15=[list1[13]]+["" for i in range(18)]
list16=[list1[14]]+["" for i in range(18)]
list17=[list1[15]]+["" for i in range(18)]
list18=[list1[16]]+["" for i in range(18)]
list19=[list1[17]]+["" for i in range(18)]

for i in range(len(list1)):
	a="\n".join(list1[i])
	list1[i]=a
	
list20=[list2,list3,list4,list5,list6,list7,list8,list9,list10,list11,list12,list13,list14,list15,list16,list17,list18,list19]

table=tabulate.tabulate(list20,headers=list1,tablefmt="grid")

print(table,"\n\n")

lst1=["Grass","Fire","Water","Normal","Bug","Poison","Flying","Electrc","Ground","Rock","Ice","Steel","Fight","Dark","Ghost","Psychic","Dragon","Fairy"]

print(tabulate.tabulate(["|2. Defense Types Chart|"]),"\n\n")

lst2=[lst1[0]]+["" for i in range(18)]
lst3=[lst1[1]]+["" for i in range(18)]
lst4=[lst1[2]]+["" for i in range(18)]
lst5=[lst1[3]]+["" for i in range(18)]
lst6=[lst1[4]]+["" for i in range(18)]
lst7=[lst1[5]]+["" for i in range(18)]
lst8=[lst1[6]]+["" for i in range(18)]
lst9=[lst1[7]]+["" for i in range(18)]
lst10=[lst1[8]]+["" for i in range(18)]
lst11=[lst1[9]]+["" for i in range(18)]
lst12=[lst1[10]]+["" for i in range(18)]
lst13=[lst1[11]]+["" for i in range(18)]
lst14=[lst1[12]]+["" for i in range(18)]
lst15=[lst1[13]]+["" for i in range(18)]
lst16=[lst1[14]]+["" for i in range(18)]
lst17=[lst1[15]]+["" for i in range(18)]
lst18=[lst1[16]]+["" for i in range(18)]
lst19=[lst1[17]]+["" for i in range(18)]

for i in range(len(lst1)):
	a="\n".join(lst1[i])
	lst1[i]=a

lst20=[lst2,lst3,lst4,lst5,lst6,lst7,lst8,lst9,lst10,lst11,lst12,lst13,lst14,lst15,lst16,lst17,lst18,lst19]

table=tabulate.tabulate(lst20,headers=lst1,tablefmt="grid")

print(table)