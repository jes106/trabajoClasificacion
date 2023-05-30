#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import sys
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
import ckCtrlClasificacion


class VentanasAtributos(QtWidgets.QWidget):
    '''
    Cuadro de dialógo para la tarea de clasificacion
    '''
    def __init__(self, name, atributos=None, parent=None):
        '''
        Inicio del cuadro de diálogo
        
        @param name: Nombre del cuadro
        @type name: string
        
        @param atributos: Lista de atributos
        @type atributo: tupla de dos valores 
        
        @param parent: Objeto del que hereda
        @type parent: Objeto padre
        
        '''
        super(VentanasAtributos, self).__init__(parent)

        self.name = name
        labelListA=QtWidgets.QLabel("Selecione los Atributos",self)
        atributos_list = [(f.nombre)  for f in atributos]
        header = ['NOMBRE', 'VALOR']
        self.tableWidgetAtributos = QtWidgets.QTableWidget(len(atributos_list),3) 
        self.tableWidgetAtributos.setColumnWidth(0, 230)
        self.tableWidgetAtributos.setColumnWidth(1, 230)
        self.tableWidgetAtributos.setColumnWidth(2, 0)
        self.tableWidgetAtributos.setHorizontalHeaderLabels(header) 

        for i in range(len(atributos)):
            item1 = QtWidgets.QTableWidgetItem(atributos[i].nombre)
            item1.setCheckState(QtCore.Qt.Unchecked)
            item1.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled) 
            item3 = QtWidgets.QTableWidgetItem(atributos[i].atrib)
            atributo = QtWidgets.QLineEdit()
            atributo.setText(atributos[i].atrib)
            atributo.setEnabled(False)
            self.tableWidgetAtributos.setCellWidget(i, 1, atributo)
            if atributos[i].booleano==None:
                text = QtWidgets.QLineEdit()
                text.setText(atributos[i].defecto)
                self.tableWidgetAtributos.setCellWidget(i, 0, text)
            elif atributos[i].booleano=='True':
                text = QtWidgets.QLineEdit()
                text.setEnabled(False)
                text.setText(atributos[i].defecto)
                self.tableWidgetAtributos.setCellWidget(i, 1, text)
            elif atributos[i].valores.__len__() > 0:
                combobox = QtWidgets.QComboBox()
                for j in atributos[i].valores:
                    combobox.addItem(j) 
                self.tableWidgetAtributos.setCellWidget(i, 1, combobox)
                

            self.tableWidgetAtributos.setItem(i, 0, item1)
            self.tableWidgetAtributos.setItem(i, 2, item3)
                
        labelPosClasificL=QtWidgets.QLabel("Posibles Candidatos",self)
        self.listWidgetPosClasific = QtWidgets.QListWidget()
        
        labelClasificL=QtWidgets.QLabel("Clasificacion",self)
        self.listWidgetClasificacion = QtWidgets.QListWidget()
         
        #Botones
        self.busquedaClasificButton=QtWidgets.QPushButton('Candidatos')
        self.clasificButton=QtWidgets.QPushButton('Clasificar')
        self.exitButton=QtWidgets.QPushButton('Exit') 
        self.buttonsLayout = QtWidgets.QHBoxLayout() 
        self.buttonsLayout.addStretch()
        self.buttonsLayout.addWidget(self.busquedaClasificButton)
        self.buttonsLayout.addWidget(self.clasificButton)
        self.buttonsLayout.addWidget(self.exitButton)
        self.buttonsLayout.addStretch()
        
        #Anadido de celdas
        grid = QtWidgets.QGridLayout()
        grid.setSpacing(5)
        grid.addWidget(labelListA, 0, 0)
        grid.addWidget(self.tableWidgetAtributos, 1, 0)
        
        grid.addWidget(labelPosClasificL, 0, 1)
        grid.addWidget(self.listWidgetPosClasific, 1, 1, 1, 2)
        
        grid.addWidget(labelClasificL, 3, 0)
        grid.addWidget(self.listWidgetClasificacion, 4, 0, 3, 3)
        
        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.addLayout(grid)
        mainLayout.addLayout(self.buttonsLayout)
        self.setLayout(mainLayout)
        
        #Forma de la ventana y mostrado
        self.setGeometry(0, 0, 800, 700)
        self.setWindowTitle(u"TRABAJO DE CLASIFICACIÓN - i02dipea, i02essej, i02himoj".format(self.name))
        #Centrado de la ventana
        self.center()
        self.show()


        #CReacion de eventos
        self.busquedaClasificButton.clicked.connect(self.candidatos)
        self.clasificButton.clicked.connect(self.clasifica)
        self.exitButton.clicked.connect(self.close)
    
    def clasifica(self):
        '''
        Funcion de inicio del envento de clasificacion
        
        @param self: Objeto de la Vista VentanasAtributos
        @type self: VentanasAtributos
        
        '''
        ckCtrlClasificacion.eventClasifica(self)
        
    def candidatos(self):
        '''
        Funcion de inicio del envento de candidatos
        
        @param self: Objeto de la Vista VentanasAtributos
        @type self: VentanasAtributos
        
        '''
        ckCtrlClasificacion.eventCandidatos(self)
    
    def center(self): 
        '''
        Funcion para centrar la ventana
        
        @param self: Objeto de la Vista VentanasAtributos
        @type self: VentanasAtributos
        
        '''
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topRight())

    
if __name__ == "__main__":
    if True:
        #Podemos probar el módulo de vistas de forma autónoma
        
        atributos = ckCtrlClasificacion.mC.bcC.listaAtributos()
        app = QtWidgets.QApplication(sys.argv)
        form = VentanasAtributos("Clasificacion", atributos)
        sys.exit(app.exec_())

         
 
