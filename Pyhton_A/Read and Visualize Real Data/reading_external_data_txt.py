import bpy


filepath = r'C:\Works\GG-Script\Pyhton_A\tutorial.txt'

data = dict() # è come scrivere data{}

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

""" with open(filepath, 'r') as txt_file:
    #print(txt_file.readlines())
    for line in txt_file.readlines():
        # print(line)
        line = line.rstrip('\n')
        #print(line)
        # test = line.split(',')
        # print(test)
        day = line.split(',')[0]
        hours_worked = line.split(',')[1]
        print(day, hours_worked) """

with open(filepath, 'r') as txt_file:
    #print(txt_file.readlines())
    """ for idx in range(txt_file.readlines()):
        line = txt_file.readlines()[idx] """
    for idx, line in enumerate(txt_file.readlines()): # uso un ulteriore key(idx) perchè essendoci nel txt chiavi doppie verrebbero sovrascritte vedi # esempio01
        # print(line)
        if idx > 0:
            line = line.rstrip('\n')
            #print(line)
            # test = line.split(',')
            # print(test)
            day = line.split(',')[0]
            hours_worked = line.split(',')[1]
            # print(day, hours_worked)
            # data[day] = hours_worked # esempio01 - questo data conterrà solo l'ultima settimana perche le key uguali ferranno sempre sovrascritte
            data[idx] = {
                'day' : day,
                'hours_worked' : hours_worked,
            }

print(data)
# the file will be closed here
