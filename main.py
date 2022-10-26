# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QColor
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice, QPoint
import pyqtgraph as pg
import numpy as np

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('Lab4.ui', self) # Para no convertirlo
        # Elimina la barra de título
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        # Control barra de títulos
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.bt_restaurar.clicked.connect(self.control_bt_normal)
        self.bt_maximizar.clicked.connect(self.control_bt_maximizar)
        self.bt_cerrar.clicked.connect(lambda: self.close())
        self.bt_restaurar.hide()
        # SizeGrip (redimensionar)
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)
        # Mover ventana
        self.frame_superior.mouseMoveEvent= self.mover_ventana
        # Acceder a las páginas
        self.bt_inicio.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        self.bt_graficadatos.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.bt_graficatiempo.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        self.bt_reporte.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_4))
        self.bt_config.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_5))
        # Menu lateral
        self.bt_menu.clicked.connect(self.mover_menu)
        
        # Control connect
        self.serial = QSerialPort()
        self.bt_update.clicked.connect(self.read_ports)
        self.bt_connect.clicked.connect(self.serial_connect)
        self.bt_disconnect.clicked.connect(lambda: self.serial.close())
        self.serial.readyRead.connect(self.read_data)
        self.x = list(np.linspace(0,100,100))
        self.y = list(np.linspace(0,0,100))
        
        # Grafica
        pg.setConfigOption('background', '#ffffff')
        pg.setConfigOption('foreground', '#000000')
        self.plt = pg.PlotWidget(title = 'Grafica Temperatura vs tiempo')
        self.graph_layout.addWidget(self.plt)
        self.read_ports()
        
    def read_ports(self):
        self.baudrates = ['1200', '2400', '4800', '9600', '19200', '38400', '115200']
        portList =[]
        ports = QSerialPortInfo().availablePorts()
        for i in ports:
            portList.append(i.portName())
        
        self.cb_list_ports.clear()
        self.cb_list_baudrates.clear()
        self.cb_list_ports.addItems(portList)
        self.cb_list_baudrates.addItems(self.baudrates)
        self.cb_list_baudrates.setCurrentText('9600')
        
    def serial_connect(self):
        self.serial.waitForReadyRead(100)
        self.port = self.cb_list_ports.currenteText()
        self.baud = self.cb_list_baudrates.currenteText()
        self.serial.setBaudRate(int(self.baud))
        self.serial.setPortName(self.port)
        self.serial.open(QIODevice.ReadWrite)
        
    def read_data(self):
        if not self.serial.canReadLine(): return
        rx = self.serial.readLine()
        x = str(rx, 'utf-8').strip()
        x = float(x)
        print(x)
        self.y = self.y[1:]
        self.y.append(x)
        self.plt.clear()
        self.plt.plot(self.x, self.y, pen=pg.mkPen('#da0037', width=2))
        
    def send_data(self, data):
        data = data + "\n"
        print(data)
        if self.serial.isOpen():
            self.serial.write(data.encode())
        
    def mover_menu(self):
        if True:
            width =self.frame_lateral.width()
            normal = 0
            if width == 0:
                extender = 220
            else:
                extender = normal
        self.animation = QPropertyAnimation(self.frame_lateral, b'minimumWidth')
        self.animation.setDuration(300)
        self.animation.setStartValue(width)
        self.animation.setEndValue(extender)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
    def control_bt_minimizar(self):
        self.showMinimized()
    def control_bt_normal(self):
        self.showNormal()
        self.bt_restaurar.hide()
        self.bt_maximizar.show()
    def control_bt_maximizar(self):
        self.showMaximized()
        self.bt_maximizar.hide()
        self.bt_restaurar.show()   
    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize) 
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
    def mover_ventana(self, event):
        if self.isMaximized() == False:
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()     
        if event.globalPos().y() <= 20:
            self.showMaximized()
            self.bt_maximizar.hide()
            self.bt_restaurar.show()
        else:
            self.showNormal()
            self.bt_restaurar.hide()
            self.bt_maximizar.show()
            
if __name__ == "__main__":
     app = QApplication(sys.argv)
     mi_app = VentanaPrincipal()
     mi_app.show()
     sys.exit(app.exec_())