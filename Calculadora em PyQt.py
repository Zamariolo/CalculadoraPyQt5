# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 13:41:33 2021

@author: vnsau
"""

######################################
from PyQt5 import QtGui, QtCore  # (the example applies equally well to PySide2)
import pyqtgraph as pg
from PyQt5.QtWidgets import *

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
######################################
# Inserindo os elementos que compoem a aplicacao

#Titulo
label_titulo = QtGui.QLabel("<h1 style='color:#4286f4'>CALCULADORA EM PyQt5</h1>")
#wTitulo.setAlignment(QtGui.AlignCenter)
label_titulo.setAlignment(QtCore.Qt.AlignCenter)

#Autor
label_Autor = QtGui.QLabel("<p>Autor: Vinícius Zamariola - zzamariola@gmail.com</p>")
label_Autor.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom )

# Resultados
lineedit_resultado = QtGui.QLineEdit("0")
lineedit_resultado.setStyleSheet("color: #4286f4; font:30px; background-color:#FCFCFC; text-align: right");
lineedit_resultado.setAlignment(QtCore.Qt.AlignRight)
lineedit_resultado.setReadOnly(True)


# Botoes
btn_soma = QPushButton('+')
btn_subtracao = QPushButton('-')
btn_multiplicacao = QPushButton('x')
btn_divisao = QPushButton('/')
btn_igual = QPushButton("=")
btn_igual.setSizePolicy(QSizePolicy(QSizePolicy.Minimum,QSizePolicy.MinimumExpanding))

btn_0 = QPushButton('0')
btn_1 = QPushButton('1')
btn_2 = QPushButton('2')
btn_3 = QPushButton('3')
btn_4 = QPushButton('4')
btn_5 = QPushButton('5')
btn_6 = QPushButton('6')
btn_7 = QPushButton('7')
btn_8 = QPushButton('8')
btn_9 = QPushButton('9')


######################################
######################################

# Criando o Layout
layout = QtGui.QGridLayout()
# Aplicando o layout a janela (window)
window.setLayout(layout)
window.setGeometry(400,50,400,600)

# Configurando o layout
layout.addWidget(label_titulo, 1,0,1,4)
layout.addWidget(lineedit_resultado, 2,0,2,4)

layout.addWidget(btn_soma, 4,0)
layout.addWidget(btn_subtracao, 4,1)
layout.addWidget(btn_multiplicacao, 4,2)
layout.addWidget(btn_divisao, 4,3)
layout.addWidget(btn_igual, 5,3,4,1)

layout.addWidget(btn_1, 5,0)
layout.addWidget(btn_2, 5,1)
layout.addWidget(btn_3, 5,2)
layout.addWidget(btn_4, 6,0)
layout.addWidget(btn_5, 6,1)
layout.addWidget(btn_6, 6,2)
layout.addWidget(btn_7, 7,0)
layout.addWidget(btn_8, 7,1)
layout.addWidget(btn_9, 7,2)
layout.addWidget(btn_0, 8,1)




layout.addWidget(label_Autor, 9,0,6,4)


######################################
######################################

## Display the widget as a new window
window.show()


## Start the Qt event loop
app.setQuitOnLastWindowClosed(True)
app.exec_()