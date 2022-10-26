# -*- coding: utf-8 -*-
from classes.read import *
from classes.menu import *
from classes.userdata import *
pause = False
if __name__=='__main__':
    try:
        puerto = serial.Serial('COM3', 9600)
        puerto.close()
        puerto.open()
        ban = 1
        print('Puerto abierto')
    except:
        ban = 0
        print('Problemas abriendo el puerto')
    if ban == 1:
        menu = menu('Escuela de Ingeniería')
        op = menu.ver() # Menu principal
        while 1 < op and op > 4:
            print('No es una opción válida'.center(25,'*'))
            op = menu.ver() 
        if op == 1: # INICIO SUBMENU
            menu2 = submenu('Escuela de Ingeniería')
            op2 = menu2.ver()
            while 1 < op2 and op2 > 2:
                print('No es una opción válida'.center(25,'*'))
                op2 = menu2.ver()   
            if op2 ==1:
                if ban == 1:
                    cant = int(input('¿Cuántos datos quiere registrar? '))
                    lec(cant, puerto)
                    graficar()
            elif op2==2:
                a = getuser()
                config = []
                for p in a:
                    userd = p.split(';')
                    config.append(userd)
                fig, ax = plt.subplots()
                ydata =[]
                ani = animation.FuncAnimation(fig,update_data)
                fig.canvas.mpl_connect('button_press_event',onclik)
                plt.show()  # FIN SUBMENU  
        elif op == 2: # INICIO CONFIGURACIÓN
            userdata()
        elif op == 3:
            report()
    def onclik(event):
        global pause
        pause = True
    def update_data(i):
        if not pause: 
            punto = int(puerto.readline().decode().strip()) 
            ydata.append(punto)
            ax.clear()
            ax.plot(ydata)
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
    