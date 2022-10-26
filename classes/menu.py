# -*- coding: utf-8 -*-
class menu:
    def __init__(self, lab):
        self.lab = lab
    def ver(self):
        print('BIENVENIDO'.center(25,'*'))
        print('Monitor de temperatura ' + '/ ' + self.lab)
        print('1. Captura de datos')
        print('2. Configuración de parámetros')
        print('3. Reportes')
        print('4. salir')
        op = int(input())
        return op
class submenu:
    def __init__(self, lab):
        self.lab = lab
    def ver(self):
        print('Captura de datos'.center(25,'*'))
        print('1. Cantidad de datos')
        print('2. Por gráfica')
        op = int(input())
        return op
