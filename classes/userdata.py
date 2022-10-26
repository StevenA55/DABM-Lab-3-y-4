# -*- coding: utf-8 -*-
class user:
    file = 'database/read.csv'
    def __init__(self, minV,maxV,c):
        self.minV = minV
        self.maxV = maxV
        self.c = c
    def save(self):
        f = open('database/userdata.csv','a')
        Linea = ';'.join([self.minV,self.maxV,self.c])
        f.write(Linea+'\n')
        f.close()
def userdata():
        reset()
        print('Configuración'.center(25,'*'))
        print('Podrá elegir valores mínimos y máximos'.center(25,'*'))
        cri = ['H','N','F']
        for i in range (3):
            print('Configuración para', cri[i])
            c = cri[i]
            minV = input('Diga el valor mínimo: ')
            maxV = input('Diga el valor máximo: ')
            direc = user(minV,maxV,c)
            direc.save()
def reset():
    file = open('database/userdata.csv', "w")
    file.close()
def getAll():
    a = open('database/userdata.csv','r')
    datos = a.readlines()
    return datos