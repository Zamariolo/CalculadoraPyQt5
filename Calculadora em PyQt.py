# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 13:41:33 2021

@author: vnsau
"""

######################################
from PyQt5 import QtGui, QtCore  # (the example applies equally well to PySide2)
import pyqtgraph as pg
from PyQt5.QtWidgets import *
from operacoes_matematicas import *

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
# Inserindo os elementos (widgets) da aplicacao

#Titulo
label_titulo = QtGui.QLabel("<h1 style='color:#4286f4'>CALCULADORA EM PyQt5</h1>")
#wTitulo.setAlignment(QtGui.AlignCenter)
label_titulo.setAlignment(QtCore.Qt.AlignCenter)

#Autor
label_Autor = QtGui.QLabel("<p>Autor: Vinícius Zamariola - zzamariola@gmail.com</p>")
label_Autor.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom )

# Resultados
lineedit_resultado = QtGui.QLineEdit("")
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

btn_decimal = QPushButton('.')
btn_limpa = QPushButton('C')

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
# TECLAS DE ATALHO
btn_soma.setShortcut("+")
btn_subtracao.setShortcut("-")
btn_multiplicacao.setShortcut("*")
btn_divisao.setShortcut("/")
btn_igual.setShortcut("=")

btn_decimal.setShortcut('.')
btn_limpa.setShortcut('c')

btn_0.setShortcut("0")
btn_1.setShortcut("1")
btn_2.setShortcut("2")
btn_3.setShortcut("3")
btn_4.setShortcut("4")
btn_5.setShortcut("5")
btn_6.setShortcut("6")
btn_7.setShortcut("7")
btn_8.setShortcut("8")
btn_9.setShortcut("9")

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
layout.addWidget(btn_igual, 6,3,3,1)

layout.addWidget(btn_decimal, 8,2)
layout.addWidget(btn_limpa, 5,3)

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
# VARIAVEIS GLOBAIS

var1 = None
var2 = None

######################################
######################################
# FUNCOES E ROTINAS (SLOTS)

def escreve_valor(numero):
    # Configura a escrita do numero no app
    
    # Obtem o numero atual e adiciona o numero clicado
    conteudo_lineedit = lineedit_resultado.text() + numero
    lineedit_resultado.setText(conteudo_lineedit)
    
def calculate(operacao):

    global var1
    global var2
        
    # Identificar se é a variavel 1 ou 2 sendo escrita


    # Se for a variavel 1
    if (var1 == None):
        var1 = lineedit_resultado.text();

    # Se for a variavel 2 fazer a operacao
    else:
        var2 = lineedit_resultado.text()
        QMessageBox.about(window, "Operação clicada", operacao)


    
    # Adicionar verificacao de tamanho de numero  
    # Limpa valore escritos
    lineedit_resultado.setText("")
    

def mensagemTeste():
    QMessageBox.about(window, "Title", "Message")

######################################
######################################
# SIGNALS AND SLOTS

#Exemplo de conextao do signal a um slot
#widget.signal.connect(slot_function)
btn_0.clicked.connect(lambda: escreve_valor(btn_0.text()))
btn_1.clicked.connect(lambda: escreve_valor(btn_1.text()))
btn_2.clicked.connect(lambda: escreve_valor(btn_2.text()))
btn_3.clicked.connect(lambda: escreve_valor(btn_3.text()))
btn_4.clicked.connect(lambda: escreve_valor(btn_4.text()))
btn_5.clicked.connect(lambda: escreve_valor(btn_5.text()))
btn_6.clicked.connect(lambda: escreve_valor(btn_6.text()))
btn_7.clicked.connect(lambda: escreve_valor(btn_7.text()))
btn_8.clicked.connect(lambda: escreve_valor(btn_8.text()))
btn_9.clicked.connect(lambda: escreve_valor(btn_9.text()))

btn_decimal.clicked.connect(lambda: escreve_valor(btn_decimal.text()))

btn_igual.clicked.connect(lambda: calculate(btn_igual.text()))
btn_soma.clicked.connect(lambda: calculate(btn_soma.text()))
btn_subtracao.clicked.connect(lambda: calculate(btn_subtracao.text()))
btn_divisao.clicked.connect(lambda: calculate(btn_divisao.text()))
btn_multiplicacao.clicked.connect(lambda: calculate(btn_multiplicacao.text()))


######################################
######################################

## Display the widget as a new window
window.show()


## Start the Qt event loop
app.setQuitOnLastWindowClosed(True)
app.exec()