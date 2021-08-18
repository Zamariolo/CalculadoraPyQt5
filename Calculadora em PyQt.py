# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 13:41:33 2021

@author: vnsau
"""

######################################
from PyQt5 import QtGui  # (the example applies equally well to PySide2)
import pyqtgraph as pg

######################################
## Iniciando a aplicacao (uma por aplicacao)
app = QtGui.QApplication([])

######################################
## Criando a janela (window) 
window = QtGui.QWidget()

# Configurando a janela
window.setWindowTitle("Calculadora em PyQt5")
window.setStyleSheet("background-color: #f4f4f4;")

######################################
# Inserindo os elementos que compoem a aplicacao

#Titulo
wTitulo = QtGui.QLabel("<h1 style='color:#4286f4'>CALCULADORA EM PyQt5</h1>")
#Titulo.setAlignment(QtGui.AlignCenter)

# Resultados
wResultado = QtGui.QLineEdit("0")
wResultado.setStyleSheet("color: #4286f4; font-size:30");


# Criando o Layout
layout = QtGui.QGridLayout()
# Aplicando o layout a janela (window)
window.setLayout(layout)

# Configurando o layout
layout.addWidget(wTitulo, 0,0, 0, 3)
layout.addWidget(wResultado, 1,0)

## Display the widget as a new window
window.show()

## Start the Qt event loop
app.exec_()