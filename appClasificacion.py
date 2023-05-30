#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import sys
from PyQt5 import QtWidgets
import VistaClasificacion
import ckCtrlClasificacion

atributos = ckCtrlClasificacion.mC.bcC.listaAtributos()
app = QtWidgets.QApplication(sys.argv)  # Se crea una instancia de aplicación
form = VistaClasificacion.VentanasAtributos("Climas", atributos)  # Se crea una instancia de de una ventana
sys.exit(app.exec_())
