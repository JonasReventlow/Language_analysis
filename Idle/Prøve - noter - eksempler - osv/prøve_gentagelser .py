import sys
#sys er et sidesystem/modul til python (lidt ligesom package eller plugins)
# med kode registrere idle/python at vi bruge dette modul nu
# det kan være at der var et exit fucktion i en anden modul

def name_length():

    name = input('What is you name: ')
    if name == 'stop' :
        sys.exit()

    if len(name)<4:
        print('short name')

    elif 4<=len(name)<8:
        print('name length is ordinary')

    else:
        print('long name')

    name_length()
    #det er denne kode der gør at det hele kører i ring/gentagelser



name_length()
