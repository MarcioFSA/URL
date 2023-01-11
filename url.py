from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtGui import QPixmap
import os
from PIL import ImageQt


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(890, 470)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 350, 311, 71))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 20, 500, 250))
        # self.label.setGeometry(QtCore.QRect(190, 20, 461, 241))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 270, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(190, 270, 351, 31))
        self.lineEdit.setObjectName("lineEdit")
        # MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_2.clicked.connect(self.selecionaImagem)
        estado = QtCore.pyqtSignal(bool)
        self.pushButton.clicked.connect(self.salvarEvidencia)


        


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))

    def selecionaImagem(self):
        fname, _ = QtWidgets.QFileDialog.getOpenFileName(parent=self, caption='Select File', directory = QtCore.QDir.currentPath(),
         filter = 'All Files(*.*);; Images (*.jpg; *.png)', initialFilter = 'Images (*.jpg; *.png)')
        self.label.setPixmap(QPixmap(fname))
        self.label.setScaledContents(True)

    def salvarEvidencia(self, fname):
        banco_db = '3'
        pixmap = QPixmap(self.label.pixmap())
        pixmap.save(f"evidencia/{banco_db}.png", "png")

        # banco_db = '2'
        # imagem = ImageQt.fromqpixmap(self.label.pixmap())
        # imagem.save(f'Evidencia/{banco_db }.png')


        # img, _ = QFileDialog.getSaveFileName(self, "Salvar Arquivo",














