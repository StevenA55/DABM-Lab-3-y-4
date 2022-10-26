# -*- coding: utf-8 -*-
import serial
import struct
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tabulate import tabulate
from datetime import datetime
from datetime import timedelta
import pandas as pd
import sys
pause = False
class read:
    file = 'database/read.csv'
    def __init__(self, read, fyh):
        self.read = read
        self.fyh = fyh
    def save(self):
        f = open('database/read.csv','a')
        Linea = ';'.join([self.read,self.fyh])
        f.write(Linea+'\n')
        f.close()
def getAll():
    a = open('database/read.csv','r')
    datos = a.readlines()
    return datos
def lec(cant, puerto):
    reset()
    a = getuser()
    config = []
    for p in a:
        userd = p.split(';')
        config.append(userd)
    for i in range (cant):
        punto = int(puerto.readline().decode().strip())   
        if punto >= int(config[0][0]) and punto <= int(config[0][1]):
            temp = 'H'
        elif punto > int(config[1][0]) and punto <= int(config[1][1]):
            temp = 'N'
        elif punto > int(config[2][0]) and punto <= int(config[2][1]):
            temp = 'F'
        puerto.write(temp.encode())
        f = datetime.now()
        fyh = f.strftime('%d/%m %H:%M:%S')
        punto = str(punto)
        lect = read(punto, fyh)
        lect.save()
        time.sleep(1)
def graficar():
    header = ['Temp', 'Fecha']
    lect = pd.read_csv('database/read.csv',';', names = header) 
    plt.title('Datos temperatura')
    plt.xlabel('Fecha y hora')
    plt.ylabel('Temperatura')
    plt.plot(lect.Fecha,lect.Temp, color ='green')
    plt.show()
def reset():
    file = open('database/read.csv', "w")
    file.close()
def getuser():
    a = open('database/userdata.csv','r')
    datos = a.readlines()
    return datos
def report ():
    header = ['Temp', 'Fecha']
    lect = pd.read_csv('database/read.csv',';', names = header)
    print(lect.describe())
    

