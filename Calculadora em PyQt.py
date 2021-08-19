# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 13:41:33 2021

@author: vnsau
"""

######################################
from PyQt5 import QtGui, QtCore  # (the example applies equally well to PySide2)
import pyqtgraph as pg
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence
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
label_operacao = QtGui.QLabel("<p>- | -</p>")

# Resultados
lineedit_resultado = QtGui.QLineEdit("")
lineedit_resultado.setStyleSheet("color: #4286f4; font:30px; background-color:#FCFCFC; text-align: right");
lineedit_resultado.setAlignment(QtCore.Qt.AlignRight)
lineedit_resultado.setReadOnly(True)

# Botoes
btn_soma = QPushButton('+')
btn_subtracao = QPushButton('-')
btn_multiplicacao = QPushButton('*')
btn_divisao = QPushButton('/')
btn_igual = QPushButton("=")
btn_igual.setSizePolicy(QSizePolicy(QSizePolicy.Minimum,QSizePolicy.MinimumExpanding))

btn_decimal = QPushButton('.')
btn_limpa = QPushButton('C')
btn_backspace = QPushButton("Backspace")

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
btn_igual.setShortcut("Enter")

btn_decimal.setShortcut('.')
btn_limpa.setShortcut('c')
btn_backspace.setShortcut("Backspace")

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

#enter_click = QShortcut(QKeySequence("Enter"))
#enter_click.activated.connect(calculate("="))



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
layout.addWidget(label_operacao, 4,0,1,4)

layout.addWidget(btn_soma, 5,0)
layout.addWidget(btn_subtracao, 5,1)
layout.addWidget(btn_multiplicacao, 5,2)
layout.addWidget(btn_divisao, 5,3)
layout.addWidget(btn_igual, 6,3,3,1)

layout.addWidget(btn_decimal, 9,2)
layout.addWidget(btn_limpa, 5,3)
layout.addWidget(btn_backspace, 9,0)

layout.addWidget(btn_1, 6,0)
layout.addWidget(btn_2, 6,1)
layout.addWidget(btn_3, 6,2)
layout.addWidget(btn_4, 7,0)
layout.addWidget(btn_5, 7,1)
layout.addWidget(btn_6, 7,2)
layout.addWidget(btn_7, 8,0)
layout.addWidget(btn_8, 8,1)
layout.addWidget(btn_9, 8,2)
layout.addWidget(btn_0, 9,1)

layout.addWidget(label_Autor, 9,0,6,4)
######################################
######################################
# VARIAVEIS GLOBAIS

var1 = None
var2 = None
last_operacao = None

######################################
######################################
# FUNCOES E ROTINAS (SLOTS)

def clear():
    global var1
    global var2
    global last_operacao

    var1 = None
    var2 = None
    last_operacao = None

    lineedit_resultado.setText("")
    label_operacao.setText("%s  %s  %s" %(var1, last_operacao, var2))

def apaga_valor():
    lineedit_resultado.setText(lineedit_resultado.text()[:-1])

def escreve_valor(numero):
    # Configura a escrita do numero no app
    
    # Obtem o numero atual e adiciona o numero clicado
    conteudo_lineedit = lineedit_resultado.text() + numero
    lineedit_resultado.setText(conteudo_lineedit)
    
def calculate(operacao):

    global var1
    global var2
    global last_operacao
        

    # Se for a variavel 1
    if (var1 == None):
        var1 = lineedit_resultado.text();
        # Limpa valore escritos
        lineedit_resultado.setText("")

        if (operacao!="="):
            last_operacao = operacao
            label_operacao.setText("%s  %s  %s" %(var1, last_operacao, "?"))

    # Se for a variavel 2 fazer a operacao
    elif (var2==None):

        if (operacao!="="):
            last_operacao = operacao
            label_operacao.setText("%s  %s  %s" %(var1, last_operacao, "?"))

        elif operacao=="=":
            var2 = lineedit_resultado.text()
            label_operacao.setText("%s  %s  %s" %(var1, last_operacao, var2))

            if (last_operacao=="+"):
                var1 = soma(float(var1), float(var2))

            elif (last_operacao=="-"):
                var1 = soma(float(var1), -float(var2))

            elif (last_operacao=="*"):
                var1 = multiplicacao(float(var1), float(var2))

            elif (last_operacao=="/"):
                var1 = multiplicacao(float(var1), 1/float(var2))

        
            lineedit_resultado.setText(str(var1))

    else:
        # Uma conta ja foi feita, devemos resetar para continuar as operacoes
        last_operacao = operacao
        var2 = None

        label_operacao.setText("%s  %s  %s" %(var1, last_operacao, var2))
        lineedit_resultado.setText("")

        

    
    # Adicionar verificacao de tamanho de numero  

    

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

btn_limpa.clicked.connect(lambda: clear())
btn_backspace.clicked.connect(lambda: apaga_valor())


######################################
######################################

## Display the widget as a new window
window.show()


## Start the Qt event loop
app.setQuitOnLastWindowClosed(True)
app.exec()