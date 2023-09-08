import random
import tabulate

phy=["1-D Kinematics","2-D Kinematics","Laws of Motion","Work , Power and Energy","C.O.M , Momentum & Collisions","Rotational Motion"]

chem = ["Some Basic concepts of Chemistry","Redox Reactions","Atomic Structure","Chemical Equilibrium","Ionic Equilibrium"]

maths = ["Quadratic Equations","Trigonometry","Sequence and Series","Straight Lines","Pair of Straight Lines","Circles","Parabola","Ellipse","Hyperbola","Limits","Differentiation","Complex Numbers"]

list1 = ["Physics","Chemistry","Mathematics"]

list2 = [random.choice(phy),random.choice(chem),random.choice(maths)]

phy.remove(list2[0])
chem.remove(list2[1])
maths.remove(list2[2])

list3 = [random.choice(phy),random.choice(chem),random.choice(maths)]

phy.remove(list3[0])
chem.remove(list3[1])
maths.remove(list3[2])

list4 = [random.choice(phy),random.choice(chem),random.choice(maths)]

phy.remove(list4[0])
chem.remove(list4[1])
maths.remove(list4[2])

list5 = [list2,list3,list4]

table = tabulate.tabulate(list5,headers=list1,tablefmt="grid")

print(table)