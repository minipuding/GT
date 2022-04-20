# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GT.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GT(object):
    def setupUi(self, GT):
        GT.setObjectName("GT")
        GT.resize(300, 400)
        self.centralwidget = QtWidgets.QWidget(GT)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.text_browser = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_browser.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.text_browser.setObjectName("text_browser")
        self.gridLayout.addWidget(self.text_browser, 0, 0, 1, 1)
        GT.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GT)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 26))
        self.menubar.setObjectName("menubar")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        GT.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuSetting.menuAction())

        self.retranslateUi(GT)
        QtCore.QMetaObject.connectSlotsByName(GT)

    def retranslateUi(self, GT):
        _translate = QtCore.QCoreApplication.translate
        GT.setWindowTitle(_translate("GT", "GT"))
        self.menuSetting.setTitle(_translate("GT", "Setting"))

