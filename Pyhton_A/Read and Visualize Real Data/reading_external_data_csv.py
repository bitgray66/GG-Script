import bpy
import csv

filepath = r'C:\Works\GG-Script\Pyhton_A\tutorial.csv'

data = dict()

"""
# file handling https://www.geeksforgeeks.org/with-statement-in-python/
 
# 1) without using with statement
file = open('file_path', 'w')
file.write('hello world !')
file.close()
 
# 2) without using with statement
file = open('file_path', 'w')
try:
    file.write('hello world')
finally:
    file.close() 
    
# using with statement
with open('file_path', 'w') as file:
    file.write('hello world !') 
"""

with open(filepath,newline='') as csv_file:
    reader = csv.reader(csv_file)
    print(reader)

    """ for row in reader:
        print(row) 
        le key non sono uniche! uso enumerate!"""

    for ids, row in enumerate(reader):
        data[ids] = {
            'label': row[0],
            'value': row[1],
        }

print(data)