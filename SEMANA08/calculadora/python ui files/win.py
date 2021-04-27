# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fist.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calulator(object):
    def setupUi(self, Calulator):
        Calulator.setObjectName("Calulator")
        Calulator.resize(382, 396)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Calulator.sizePolicy().hasHeightForWidth())
        Calulator.setSizePolicy(sizePolicy)
        Calulator.setMinimumSize(QtCore.QSize(240, 240))
        Calulator.setWindowOpacity(1.0)
        Calulator.setLayoutDirection(QtCore.Qt.LeftToRight)
        Calulator.setAutoFillBackground(True)
        Calulator.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(Calulator)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 381, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        Calulator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Calulator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 382, 22))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        Calulator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Calulator)
        self.statusbar.setObjectName("statusbar")
        Calulator.setStatusBar(self.statusbar)
        self.actionopen = QtWidgets.QAction(Calulator)
        self.actionopen.setObjectName("actionopen")
        self.actionsave = QtWidgets.QAction(Calulator)
        self.actionsave.setObjectName("actionsave")
        self.actionexit = QtWidgets.QAction(Calulator)
        self.actionexit.setObjectName("actionexit")
        self.actiondocumentation = QtWidgets.QAction(Calulator)
        self.actiondocumentation.setObjectName("actiondocumentation")
        self.actioninfo = QtWidgets.QAction(Calulator)
        self.actioninfo.setObjectName("actioninfo")
        self.menufile.addSeparator()
        self.menufile.addSeparator()
        self.menufile.addAction(self.actionopen)
        self.menufile.addAction(self.actionsave)
        self.menufile.addAction(self.actionexit)
        self.menuhelp.addAction(self.actiondocumentation)
        self.menuhelp.addAction(self.actioninfo)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())

        self.retranslateUi(Calulator)
        QtCore.QMetaObject.connectSlotsByName(Calulator)

    def retranslateUi(self, Calulator):
        _translate = QtCore.QCoreApplication.translate
        Calulator.setWindowTitle(_translate("Calulator", "Calculadora"))
        self.label.setText(_translate("Calulator", "TextLabel"))
        self.pushButton.setText(_translate("Calulator", "PushButton"))
        self.pushButton_2.setText(_translate("Calulator", "PushButton"))
        self.menufile.setTitle(_translate("Calulator", "file"))
        self.menuhelp.setTitle(_translate("Calulator", "help"))
        self.actionopen.setText(_translate("Calulator", "open"))
        self.actionsave.setText(_translate("Calulator", "save"))
        self.actionexit.setText(_translate("Calulator", "exit"))
        self.actiondocumentation.setText(_translate("Calulator", "documentation"))
        self.actioninfo.setText(_translate("Calulator", "about"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calulator = QtWidgets.QMainWindow()
    ui = Ui_Calulator()
    ui.setupUi(Calulator)
    Calulator.show()
    sys.exit(app.exec_())
