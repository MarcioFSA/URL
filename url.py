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
        self.label.setGeometry(QtCore.QRect(190, 20, 461, 241))
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

        # if self.pushButton.click() == True:
        #     print('clicando')
        #     options = QFileDialog.DontUseNativeDialog
        #     arquivo, _ = QFileDialog.getSaveFileName(self, 'Salvar', 'D:\\Git\\Nova pasta\\URL\\evidencia',
        #                                              'Imagem (*.jpg);; PNG File (*.png)', options=options)
        #     self.label.save()







    def salvarEvidencia(self, fname):
        # options = QFileDialog.DontUseNativeDialog
        # salvar, _ = QFileDialog.getSaveFileName(self, 'Salvar', 'D:\\Git\\Nova pasta\\URL\\evidencia', 'Imagem (*.jpg);; PNG File (*.png)', options=options)

        imagem = ImageQt.fromqpixmap(self.label.pixmap())
        imagem.save('Evidencia/salvando.png')
        # img, _ = QFileDialog.getSaveFileName(self, "Salvar Arquivo",
        #                                      filter="PNG(*.png);; JPEG(*.jpg)")
        # file_filter = 'Images (*.jpg; *.png)'
        # response = QFileDialog.getSaveFileName(
        #     parent=self,
        #     caption='Selecione o local',
        #     directory='evidencia',
        #     filter=file_filter,
        #     initialFilter='Images (*.jpg; *.png)'
        # # )
        # # return response[0]
        # options = QFileDialog.DontUseNativeDialog
        # imagem, _ = QFileDialog.getSaveFileName(self, 'Salvar', 'D:\\Git\\Nova pasta\\URL\\evidencia', 'Imagem (*.jpg);; PNG File (*.png)', options=options)
        # imagem = self.label.pixmap()
        # print(imagem)
        # imagem.save('test.png')

        # with open(arquivo, 'wt') as f:
        #     self.label = QPixmap.save(f)
        # # with open(arquivo, 'w') as fp:
        # #     fp.writelines(lines)

        # path = os.path.join(self.active_folder, self.ui.lineEditFileName.text())
        # options = QFileDialog.DontUseNativeDialog
        # fileName, _ = QFileDialog.getSaveFileName(self, "Save Measurement", path, "(*.jpg)", options=options)
        # self.active_folder = os.path.dirname(fileName)
        pass


















            # label = QLabel(self)
        # # imagePath = fname[0]
        #
        # pixmap = QPixmap(fname[0])
        # print(pixmap)
        # label.setPixmap(pixmap)
        # # self.label.setPixmap(QPixmap(pixmap))
        #
        # self.resize(pixmap.width(), pixmap.height())

        # label = QLabel(self)
        # pixmap = QPixmap("HEC.jpg")
        # label.setPixmap(pixmap)
