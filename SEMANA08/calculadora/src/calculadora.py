#!usr/bin/python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teclado.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGridLayout, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QFormLayout
from PyQt5.QtCore import Qt
from cmath import *


class Func:
    def __init__(self, f, *args, **kwargs):
        self.a = args
        self.kw = kwargs
        self.f = f

    def __call__(self, *args, **kwargs):
        self.f(*self.a, **self.kw)


class Teclado(QWidget):
    def __init__(self, label: QLabel):
        super().__init__()
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)
        self.grid.setContentsMargins(0, 0, 0, 0)
        self.grid.setHorizontalSpacing(5)
        self.grid.setVerticalSpacing(5)
        self.buttonsId = ['(', ')', '^', 'CE', '7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '.',
                          '=', '+']
        self.buttonsIdEspecial = ['cos', 'sin', 'tan', 'j', 'π']
        self.buttonsIdEspecial2 = ['acos', 'asin', 'atan', 'exp', 'log']
        self.buttonsWidget = None
        self.buttonsEsp = None
        self.putButtons()
        self.label = label
        self.txt = ''
        self.lastTxt = ''
        self.expected = ''
        self.type = 1
        self.__clear()

    def __put(self, txt):
        self.lastTxt = txt
        self.txt = self.txt + txt
        self.label.setText(self.txt + '|' + self.expected)

    def __clear(self):
        self.lastTxt = ''
        self.txt = ''
        self.label.setText('|')
        self.expected = ''

    def __eval(self):
        j = 1j
        log = log10
        self.txt = self.txt.replace('^', '**')
        self.txt = self.txt.replace('π', 'pi')
        ans = eval(self.txt + self.expected)

        if isinstance(ans, complex):
            if ans.imag in [0, 0.0, -0.0]:
                ans = ans.real
        self.txt = str(ans)
        self.expected = ''
        self.lastTxt = self.txt[-1]
        self.label.setText(self.txt)

    def __onClick(self, *args, button: QtWidgets.QPushButton, **kwargs):
        id = button.text()

        # if self.txt in ['0.0', '0', '-0.0']:
            # self.__clear()

        if id in ['7', '8', '9', '4', '5', '6', '1', '2', '3']:
            if self.lastTxt in [')', 'π', 'j']:
                self.__put('*')
            self.__put(id)
            return
        if id == 'CE':
            self.__clear()
            return
        if id in ['*', '^', '/', '-', '+']:
            if self.lastTxt in ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0',')','π', '.']:
                self.__put(id)
            elif id == '-' and self.lastTxt in ['(', ')', '+', '/', '*', '']:
                self.__put(id)
            return
        if id == '=':
            self.__eval()
            return
        if id == ')':
            if len(self.expected) == 0 or self.lastTxt in ['', '(', '*', '^', '/', '-', '+']:
                return
            self.expected = self.expected[1:]
            self.__put(id)
            return
        if id in ['(', 'π', 'cos', 'sin', 'tan', 'acos', 'asin', 'atan', 'exp', 'log']:
            if self.lastTxt in ['7', '8', '9', '4', '5', '6', '1', '2', '3','0', ')', '.', 'j', 'π']:
                self.__put('*')
            if id != 'π':
                self.expected = self.expected + ')'

            self.__put(id)
            if id not in ['(', 'π']:
                self.__put('(')
            return
        self.__put(id)

    def putButtons(self):
        i, j = 0, 1
        sep = 5
        self.buttonsWidget = []
        for bt in self.buttonsId:
            button = QtWidgets.QPushButton(bt, self)
            button.setObjectName(bt)
            button.clicked.connect(Func(self.__onClick, id=bt, button=button))
            self.grid.addWidget(button, i, j, 1, 1)
            self.buttonsWidget.append(button)
            j += 1
            if j >= sep:
                i, j = i + 1, 1
        i = 0
        self.buttonsEsp = []
        for bt in self.buttonsIdEspecial:
            button = QtWidgets.QPushButton(bt, self)
            button.clicked.connect(Func(self.__onClick, id=bt, button=button))
            self.grid.addWidget(button, i, 0, 1, 1)
            i += 1
            self.buttonsEsp.append(button)

    def setButtonEsp(self):
        if self.type == 1:
            comando = self.buttonsIdEspecial2
            self.type = 2
        else:
            comando = self.buttonsIdEspecial
            self.type = 1

        i = 0
        for bt in comando:
            button = self.buttonsEsp[i]
            button.setText(bt)
            # button.clicked.connect(Func(self.__onClick, button=button))
            i += 1


class Calculadora(QWidget):
    def __init__(self):
        super().__init__()
        self.visor = QLabel(self)
        # self.visor.setStyleSheet('background:QColor(200,100,150);')

        self.teclado = Teclado(self.visor)
        self.vlayout = QVBoxLayout(self)
        self.button = QtWidgets.QPushButton('Change', self)
        self.button.clicked.connect(self.teclado.setButtonEsp)
        self.setLayout(self.vlayout)

        self.widgt = QWidget(self)
        self.hlayout = QHBoxLayout(self.widgt)
        self.widgt.setLayout(self.hlayout)
        self.hlayout.addWidget(self.button, 1, Qt.AlignLeft)
        self.hlayout.addWidget(self.visor, 10, Qt.AlignRight)

        self.vlayout.addWidget(self.widgt, 1, Qt.AlignLeft | Qt.AlignTop)
        self.vlayout.addWidget(self.teclado, 10, Qt.AlignHCenter)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    calc = Calculadora()
    calc.setWindowTitle('Calculadora')
    calc.show()

    sys.exit(app.exec_())
