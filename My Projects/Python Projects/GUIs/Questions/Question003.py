# Question : How to delete temporary files automatically ?

# Program : Deleting all ( if possible ) temporary files from Appdata temporary files .

import os

os.chdir(r"C:\Users\RINKU\AppData\Local\Temp")

path_name = os.getcwd()


for i in os.listdir(path_name):
    try:
        os.remove(i)

    except Exception :
        continue