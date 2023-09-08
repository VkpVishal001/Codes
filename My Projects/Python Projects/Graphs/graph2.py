import matplotlib.pyplot as plt
import math

the_element_list = [['Hydrogen',1,'Non Metal',1,1,'s',1.01,'Gaseous',0.08,2.2],#H
                    ['Helium',2,'Noble Gas',18,1,'s',4.00,'Gaseous',0.18,'Unavailable'],#He

                    ['Lithium',3,'Alkaline Metal',1,2,'s',6.94,'Solid',0.53,0.98],#Li
                    ['Beryllium',4,'Alkaline Earth Metal',2,2,'s',9.01,'Solid',1.84,1.57],#Be
                    ['Boron',5,'Metalloid',13,2,'p',10.81,'Solid',2.46,2.04],#B
                    ['Carbon',6,'Non Metal',14,2,'p',12.01,'Solid',2.26,2.55],#C
                    ['Nitrogen',7,'Non Metal',15,2,'p',14.00,'Gaseous',1.17,3.04],#N
                    ['Oxygen',8,'Non Metal',16,2,'p',15.99,'Gaseous',1.43,3.44],#O
                    ['Fluorine',9,'Halogen',17,2,'p',18.99,'Gaseous',1.70,3.98],#F
                    ['Neon',10,'Noble Gas',18,2,'p',20.17,'Gaseous',0.90,'Unavailable'],#Ne
                
                    ['Sodium',11,'Alkaline Metal',1,3,'s',22.99,'Solid',0.97,0.93],#Na
                    ['Magnesium',12,'Alkaline Earth Metal',2,3,'s',24.31,'Solid',1.74,1.31],#Mg
                    ['Aluminium',13,'Metal',13,3,'p',26.98,'Solid',2.69,1.61],#Al
                    ['Silicon',14,'Metalloid',14,3,'p',28.08,'Solid',2.34,1.90],#Si
                    ['Phosphorus',15,'Non Metal',15,3,'p',30.97,'Solid',2.4,2.19],#P
                    ['Sulphur',16,'Non Metal',16,3,'p',32.06,'Solid',2.07,2.58],#S
                    ['Chlorine',17,'Halogen',17,3,'p',35.45,'Gaseous',3.22,3.16],#Cl
                    ['Argon',18,'Noble Gas',18,3,'p',39.95,'Gaseous',1.78,'Unavailable'],#Ar

                    ['Potassium',19,'Alkaline Metal',1,4,'s',39.09,'Solid',0.86,0.82],#K
                    ['Calicium',20,'Alkaline Earth Metal',2,4,'s',40.08,'Solid',1.55,1.00],#Ca                   
                    ['Scandium',21,'Transition Metal',3,4,'d',44.96,'Solid',2.99,1.36],#Sc
                    ['Titanium',22,'Transition Metal',4,4,'d',47.87,'Solid',4.5,1.54],#Ti
                    ['Vanadium',23,'Transition Metal',5,4,'d',50.94,'Solid',6.11,1.63],#V
                    ['Chromium',24,'Transition Metal',6,4,'d',51.99,'Solid',7.14,1.66],#Cr
                    ['Manganese',25,'Transition Metal',7,4,'d',54.94,'Solid',7.43,1.55],#Mn
                    ['Iron',26,'Transition Metal',8,4,'d',55.85,'Solid',7.87,1.83],#Fe
                    ['Cobalt',27,'Transition Metal',9,4,'d',58.93,'Solid',8.90,1.88],#Co
                    ['Nickel',28,'Transition Metal',10,4,'d',58.69,'Solid',8.90,1.91],#Ni                
                    ['Copper',29,'Transition Metal',11,4,'d',63.54,'Solid',8.92,1.90],#Cu
                    ['Zinc',30,'Transition Metal',12,4,'d',65.38,'Solid',7.14,1.65],#Zn
                    ['Gallium',31,'Metal',13,4,'p',69.72,'Solid',5.90,1.81],#Ga
                    ['Germanium',32,'Metalloid',14,4,'p',72.63,'Solid',5.32,2.01],#Ge
                    ['Arsenic',33,'Metalloid',15,4,'p',74.92,'Solid',5.73,2.18],#As
                    ['Selenium',34,'Metalloid',16,4,'p',78.97,'Solid',4.82,2.55],#Se
                    ['Bromine',35,'Halogen',17,4,'p',79.90,'Liquid',3.12,2.96],#Br
                    ['Krypton',36,'Noble Gas',18,4,'p',83.80,'Gaseous',3.75,3.00],#Kr
                    
                    ['Rubidium',37,'Alkaline Metal',1,5,'s',85.47,'Solid',1.53,0.82],#Rb
                    ['Strontium',38,'Alkaline Earth Metal',2,5,'s',87.62,'Solid',2.63,0.95],#Sr
                    ['Yttrium',39,'Transition Metal',3,5,'d',88.91,'Solid',4.47,1.22],#Y
                    ['Zirconium',40,'Transition Metal',4,5,'d',91.22,'Solid',6.50,1.33],#Zr
                    ['Niobium',41,'Transition Metal',5,5,'d',92.90,'Solid',8.57,1.6],#Nb
                    ['Molybednium',42,'Transition Metal',6,5,'d',95.95,'Solid',10.28,2.16],#Mo
                    ['Technetium',43,'Transition Metal',7,5,'d',98.90,'Solid',11.5,1.9],#Tc
                    ['Ruthenium',44,'Transition Metal',8,5,'d',101.07,'Solid',12.37,2.2],#Ru                    
                    ['Rhodium',45,'Transition Metal',9,5,'d',102.90,'Solid',12.38,2.28],#Rh
                    ['Palladium',46,'Transition Metal',10,5,'d',106.42,'Solid',11.99,2.20],#Pd
                    ['ilver',47,'Transition Metal',11,5,'d',107.87,'Solid',10.49,1.93],#Ag
                    ['Cadmium',48,'Transition Metal',12,5,'d',112.41,'Solid',8.65,1.69],#Cd
                    ['Indium',49,'Metal',13,5,'p',114.82,'Solid',7.31,1.78],#In
                    ['Tin',50,'Metal',14,5,'p',118.71,'Solid',5.77,1.96],#Sn
                    ['Antimony',51,'Metalloid',15,5,'p',121.76,'Solid',6.70,2.05],#Sb
                    ['Tellurium',52,'Metalloid',16,5,'p',127.60,'Solid',6.24,2.10],#Te                
                    ['Iodine',53,'Halogen',17,5,'p',126.90,'Solid',4.94,2.66],#I
                    ['Xenon',54,'Noble Gas',18,5,'p',131.29,'Gaseous',5.90,2.6],#Xe

                    ['Caesium',55,'Alkaline Metal',1,6,'s',132.91,'Solid',1.90,0.79],#Cs
                    ['Barium',56,'Alkaline Earth Metal',2,6,'s',137.33,'Solid',3.62,0.89],#Ba

                    ['Lanthanum',57,'Transition Metal',3,6,'d',138.90,'Solid',6.17,1.1],#La
                    ['Cerium',58,'Lanthanide','La',6,'f',140.12,'Solid',6.77,1.12],#Ce
                    ['Praseodymium',59,'Lanthanide','La',6,'f',140.91,'Solid',6.48,1.13],#Pr
                    ['Neodymium',60,'Lanthanide','La',6,'f',144.24,'Solid',7.00,1.14],#Nd
                    ['Promethium',61,'Lanthanide','La',6,'f',146.91,'Solid',7.2,'Unavailable'],#Pm               
                    ['Samarium',62,'Lanthanide','La',6,'f',150.36,'Solid',7.54,1.17],#Sm
                    ['Europium',63,'Lanthanide','La',6,'f',151.96,'Solid',5.25,'Unavailable'],#Eu
                    ['Gadolinium',64,'Lanthanide','La',6,'f',157.25,'Solid',7.89,1.20],#Gd
                    ['Terbium',65,'Lanthanide','La',6,'f',158.93,'Solid',8.25,'Unavailable'],#Tb
                    ['Dysprosium',66,'Lanthanide','La',6,'f',162.50,'Solid',8.56,1.22],#Dy
                    ['Holmium',67,'Lanthanide','La',6,'f',164.93,'Solid',8.78,1.23],#Ho
                    ['Erbium',68,'Lanthanide','La',6,'f',167.26,'Solid',9.05,1.24],#Er
                    ['Thulium',69,'Lanthanide','La',6,'f',168.93,'Solid',9.32,1.25],#Tm                    
                    ['Ytterbium',70,'Lanthanide','La',6,'f',173.05,'Solid',6.97,'Unavailable'],#Yb
                    ['Lutetium',71,'Lanthanide','La',6,'f',174.97,'Solid',9.84,1.27],#Lu

                    ['Hafnium',72,'Transition Metal',4,6,'d',178.49,'Solid',13.28,1.3],#Hf
                    ['Tantalum',73,'Transition Metal',5,6,'d',180.95,'Solid',16.65,1.5],#Ta
                    ['Tungsten',74,'Transition Metal',6,6,'d',183.84,'Solid',19.25,2.36],#W
                    ['Rhenium',75,'Transition Metal',7,6,'d',186.21,'Solid',21.00,1.9],#Re
                    ['Osmium',76,'Transition Metal',8,6,'d',190.23,'Solid',22.59,2.2],#Os
                    ['Irdium',77,'Transition Metal',9,6,'d',192.22,'Solid',22.56,2.2],#Ir
                    ['Platinum',78,'Transition Metal',10,6,'d',195.08,'Solid',21.45,2.2],#Pt
                    ['Gold',79,'Transition Metal',11,6,'d',196.97,'Solid',19.32,2.54],#Au
                    ['Mercury',80,'Transition Metal',12,6,'d',200.59,'Liquid',13.55,2.00],#Hg
                    ['Thalium',81,'Metal',13,6,'p',204.38,'Solid',11.85,1.62],#Tl
                    ['Lead',82,'Metal',14,6,'p',207.20,'Solid',11.34,2.33],#Pb
                    ['Bismuth',83,'Metal',15,6,'p',208.98,'Solid',9.78,2.02],#Bi
                    ['Polonium',84,'Metal',16,6,'p',209.98,'Solid',9.20,2.0],#Po
                    ['Astatine',85,'Halogen',17,6,'p',209.99,'Solid','Unavailable',2.2],#At
                    ['Radon',86,'Noble Gas',18,6,'p',222.00,'Gaseous',9.73,'Unavailable'],#Rn

                    ['Francium',87,'Alkaline Metal',1,7,'s',223.02,'Solid','Unavailable',0.7],#Fr
                    ['Radium',88,'Alkaline Earth Metal',2,7,'s',226.03,'Solid',5.5,0.9],#Ra

                    ['Actinium',89,'Transition Metal',3,7,'d',227.03,'Solid',10.07,1.1],#Ac
                    ['Thorium',90,'Actinide','Ac',7,'f',232.04,'Solid',11.72,1.3],#Th
                    ['Protactinium',91,'Actinide','Ac',7,'f',231.04,'Solid',15.37,1.5],#Pa
                    ['Uranium',92,'Actinide','Ac',7,'f',238.03,'Solid',19.16,1.38],#U
                    ['Neptunium',93,'Actinide','Ac',7,'f',237.05,'Solid',20.45,1.36],#Np
                    ['Plutonium',94,'Actinide','Ac',7,'f',244.06,'Solid',19.82,1.28],#Pu
                    ['Americium',95,'Actinide','Ac',7,'f',243.06,'Solid',13.67,1.3],#Am                    
                    ['Curium',96,'Actinide','Ac',7,'f',247.07,'Solid',13.51,1.3],#Cm
                    ['Berkelium',97,'Actinide','Ac',7,'f',247,'Solid',14.78,1.3],#Bk
                    ['Californium',98,'Actinide','Ac',7,'f',251,'Solid',15.1,1.3],#Cf
                    ['Einsteinium',99,'Actinide','Ac',7,'f',252,'Solid',8.84,'Unavailable'],#Es
                    ['Fermium',100,'Actinide','Ac',7,'f',257.10,'Solid','Unavailable','Unavailable'],#Fm
                    ['Medelevium',101,'Actinide','Ac',7,'f',258,'Solid','Unavailable','Unavailable'],#Md
                    ['Nobelium',102,'Actinide','Ac',7,'f',259,'Solid','Unavailable','Unavailable'],#No
                    ['Lawrencium',103,'Actinide','Ac',7,'f',266,'Solid','Unavailable','Unavailable'],#Lr
                    
                    ['Rutherfordium',104,'Transition Metal',4,7,'d',261.11,'Solid',17.00,'Unavailable'],#Rf
                    ['Dubnium',105,'Transition Metal',5,7,'d',262.11,'Unavailable','Unavailable','Unavailable'],#Db
                    ['Seaborgium',106,'Transition Metal',6,7,'d',263.12,'Unavailable','Unavailable','Unavailable'],#Sg
                    ['Bohrium',107,'Transition Metal',7,7,'d',262.12,'Unavailable','Unavailable','Unavailable'],#Bh
                    ['Hassium',108,'Transition Metal',8,7,'d',265,'Unavailable','Unavailable','Unavailable'],#Hs
                    ['Meitnerium',109,'Unknown',9,7,'d',268,'Unavailable','Unavailable','Unavailable'],#Mt
                    ['Darmstadtium',110,'Unknown',10,7,'d',281,'Unavailable','Unavailable','Unavailable'],#Ds
                    ['Roentgenium',111,'Unknown',11,7,'d',280,'Unavailable','Unavailable','Unavailable'],#Rg
                    ['Copernicium',112,'Unknown',12,7,'d',277,'Unavailable','Unavailable','Unavailable'],#Cn
                    ['Nihonium',113,'Unknown',13,7,'p',287,'Unavailable','Unavailable','Unavailable'],#Nh
                    ['Flerovium',114,'Unknown',14,7,'p',289,'Unavailable','Unavailable','Unavailable'],#Fl
                    ['Moscovium',115,'Unknown',15,7,'p',288,'Unavailable','Unavailable','Unavailable'],#Mc
                    ['Livermorium',116,'Unknown',16,7,'p',293,'Unavailable','Unavailable','Unavailable'],#Lv
                    ['Tennessine',117,'Unknown',17,7,'p',292,'Unavailable','Unavailable','Unavailable'],#Ts
                    ['Oganesson',118,'Unknown',18,7,'p',294,'Solid',6.6,'Unavailable']]#Og

elements = list(zip(*the_element_list))

atomic_numbers = list(elements[1])
atomic_masses = list(elements[6])
densities = list(elements[8])
electronegativities = list(elements[9])
    
for i in range(len(atomic_numbers)):
    if electronegativities[i] == 'Unavailable':
        electronegativities[i] = 0

for i in range(len(densities)):
    if densities[i] == 'Unavailable':
        densities[i] = 0
    else:
        densities[i] = int(densities[i])

def intro():
    '''
1. -> Atomic No. - Atomic Mass Graph
2. -> Atomic No. - Density Graph
3. -> Atomic No. - Electronegativity Graph
    '''


print(intro.__doc__)

while True:
    user_input = int(input("Enter the type of graph needed (in number) : "))

    y_axis = [atomic_masses,densities,electronegativities]

    plt.plot(atomic_numbers,y_axis[user_input-1])
    plt.show()

    print()