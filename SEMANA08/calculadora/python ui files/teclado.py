# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teclado.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(400, 300)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(1)
		sizePolicy.setVerticalStretch(1)
		sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
		Form.setSizePolicy(sizePolicy)
		self.gridLayoutWidget = QtWidgets.QWidget(Form)
		self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 311))
		self.gridLayoutWidget.setObjectName("gridLayoutWidget")
		self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
		self.gridLayout.setContentsMargins(0, 0, 0, 0)
		self.gridLayout.setHorizontalSpacing(4)
		self.gridLayout.setVerticalSpacing(5)
		self.gridLayout.setObjectName("gridLayout")
		self.buttonsId = ['(',')','^','CE','7','8','9','/','4','5','6','*','1','2','3','-','0','.','=','+']
		i,j =  0,0
		sep = 4
		self.buttonsWidget = []
		for bt in self.buttonsId:
			button = QtWidgets.QPushButton(self.gridLayoutWidget)
			button.setObjectName(bt)
			self.gridLayout.addWidget(button, i, j, 1, 1)
			self.buttonsWidget.append(button)
			j += 1
			if j>=sep:
				i , j = i+1,0
		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "teclado"))
		for btid,bt in zip(self.buttonsId,self.buttonsWidget):
			bt.setText(_translate("Form", btid))



if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	Form = QtWidgets.QWidget()
	ui = Ui_Form()
	ui.setupUi(Form)
	Form.show()
	sys.exit(app.exec_())
