from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtGui import QPixmap
import os
from PIL import ImageQt

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1122, 909)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget_2.setMaximumSize(QtCore.QSize(840, 70))
        self.stackedWidget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(6, 0, 3, -1)
        self.horizontalLayout_12.setSpacing(9)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.btn_dashboard = QtWidgets.QPushButton(self.page_3)
        self.btn_dashboard.setMinimumSize(QtCore.QSize(100, 40))
        self.btn_dashboard.setMaximumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setBold(False)
        self.btn_dashboard.setFont(font)
        self.btn_dashboard.setStatusTip("")
        self.btn_dashboard.setStyleSheet("QPushButton#btn_dashboard{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_dashboard:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_dashboard:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Imagens/dashboard (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_dashboard.setIcon(icon)
        self.btn_dashboard.setIconSize(QtCore.QSize(24, 24))
        self.btn_dashboard.setObjectName("btn_dashboard")
        self.horizontalLayout_12.addWidget(self.btn_dashboard)
        self.btn_rnc = QtWidgets.QPushButton(self.page_3)
        self.btn_rnc.setEnabled(False)
        self.btn_rnc.setMinimumSize(QtCore.QSize(100, 40))
        self.btn_rnc.setMaximumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(False)
        self.btn_rnc.setFont(font)
        self.btn_rnc.setStyleSheet("QPushButton#btn_rnc{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_rnc:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_rnc:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Imagens/registro-online.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_rnc.setIcon(icon1)
        self.btn_rnc.setIconSize(QtCore.QSize(24, 24))
        self.btn_rnc.setObjectName("btn_rnc")
        self.horizontalLayout_12.addWidget(self.btn_rnc)
        self.btn_tratativa = QtWidgets.QPushButton(self.page_3)
        self.btn_tratativa.setEnabled(False)
        self.btn_tratativa.setMinimumSize(QtCore.QSize(100, 40))
        self.btn_tratativa.setMaximumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(False)
        self.btn_tratativa.setFont(font)
        self.btn_tratativa.setStyleSheet("QPushButton#btn_tratativa{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_tratativa:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_tratativa:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Imagens/investigacao.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_tratativa.setIcon(icon2)
        self.btn_tratativa.setIconSize(QtCore.QSize(24, 24))
        self.btn_tratativa.setDefault(False)
        self.btn_tratativa.setObjectName("btn_tratativa")
        self.horizontalLayout_12.addWidget(self.btn_tratativa)
        self.btn_consultar = QtWidgets.QPushButton(self.page_3)
        self.btn_consultar.setEnabled(False)
        self.btn_consultar.setMinimumSize(QtCore.QSize(100, 40))
        self.btn_consultar.setMaximumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(False)
        self.btn_consultar.setFont(font)
        self.btn_consultar.setStyleSheet("QPushButton#btn_consultar{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_consultar:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_consultar:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Imagens/pesquisa-de-dados (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_consultar.setIcon(icon3)
        self.btn_consultar.setIconSize(QtCore.QSize(24, 24))
        self.btn_consultar.setObjectName("btn_consultar")
        self.horizontalLayout_12.addWidget(self.btn_consultar)
        spacerItem = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem)
        self.btn_usuarios = QtWidgets.QPushButton(self.page_3)
        self.btn_usuarios.setEnabled(False)
        self.btn_usuarios.setMinimumSize(QtCore.QSize(100, 40))
        self.btn_usuarios.setMaximumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(False)
        self.btn_usuarios.setFont(font)
        self.btn_usuarios.setStyleSheet("QPushButton#btn_usuarios{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_usuarios:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_usuarios:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Imagem/password.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_usuarios.setIcon(icon4)
        self.btn_usuarios.setIconSize(QtCore.QSize(24, 24))
        self.btn_usuarios.setObjectName("btn_usuarios")
        self.horizontalLayout_12.addWidget(self.btn_usuarios)
        self.gridLayout_8.addLayout(self.horizontalLayout_12, 0, 0, 1, 1)
        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget_2.addWidget(self.page_4)
        self.gridLayout_3.addWidget(self.stackedWidget_2, 0, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setStyleSheet("image: url(:/Imagens/HEC.jpg);")
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.gridLayout_3.addWidget(self.label_22, 0, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.frame_3 = QtWidgets.QFrame(self.page)
        self.frame_3.setGeometry(QtCore.QRect(259, 40, 281, 511))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.frame_3.setFont(font)
        self.frame_3.setStyleSheet("border-top-left-radius:50px;\n"
"image: url(:/Imagens/Fundo_login.jpg);\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(13, 110, 261, 351))
        self.label_2.setStyleSheet("image: url(:/Imagens/Dia-da-Qualidadecorte (1).png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.layoutWidget = QtWidgets.QWidget(self.frame_3)
        self.layoutWidget.setGeometry(QtCore.QRect(51, 28, 179, 70))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(12)
        font.setBold(False)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(108, 52, 19);")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_15.addWidget(self.label_12)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(12)
        font.setBold(False)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(108, 52, 19);")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_15.addWidget(self.label_20)
        self.frame_4 = QtWidgets.QFrame(self.page)
        self.frame_4.setGeometry(QtCore.QRect(540, 40, 281, 511))
        self.frame_4.setStyleSheet("border-bottom-right-radius:50px;\n"
"background-color: rgb(244, 244, 244);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.layoutWidget_4 = QtWidgets.QWidget(self.frame_4)
        self.layoutWidget_4.setGeometry(QtCore.QRect(40, 211, 204, 105))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.txt_usuario = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.txt_usuario.setMinimumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.txt_usuario.setFont(font)
        self.txt_usuario.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 20px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;")
        self.txt_usuario.setText("")
        self.txt_usuario.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_usuario.setObjectName("txt_usuario")
        self.verticalLayout_13.addWidget(self.txt_usuario)
        self.txt_senha = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.txt_senha.setMinimumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.txt_senha.setFont(font)
        self.txt_senha.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 20px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;")
        self.txt_senha.setText("")
        self.txt_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_senha.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_senha.setObjectName("txt_senha")
        self.verticalLayout_13.addWidget(self.txt_senha)
        self.verticalLayout_12.addLayout(self.verticalLayout_13)
        self.cb_empresa = QtWidgets.QComboBox(self.layoutWidget_4)
        self.cb_empresa.setMinimumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.cb_empresa.setFont(font)
        self.cb_empresa.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cb_empresa.setStyleSheet("border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 20px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;")
        self.cb_empresa.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.cb_empresa.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.cb_empresa.setPlaceholderText("")
        self.cb_empresa.setObjectName("cb_empresa")
        self.cb_empresa.addItem("")
        self.verticalLayout_12.addWidget(self.cb_empresa)
        self.btn_anonimo = QtWidgets.QPushButton(self.frame_4)
        self.btn_anonimo.setGeometry(QtCore.QRect(90, 470, 100, 30))
        self.btn_anonimo.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.btn_anonimo.setFont(font)
        self.btn_anonimo.setStyleSheet("QPushButton#btn_anonimo{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_anonimo:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_anonimo:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}\n"
"")
        self.btn_anonimo.setObjectName("btn_anonimo")
        self.layoutWidget_6 = QtWidgets.QWidget(self.frame_4)
        self.layoutWidget_6.setGeometry(QtCore.QRect(90, 330, 102, 68))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.btn_login = QtWidgets.QPushButton(self.layoutWidget_6)
        self.btn_login.setEnabled(False)
        self.btn_login.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.btn_login.setFont(font)
        self.btn_login.setStyleSheet("QPushButton#btn_login{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_login:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_login:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}\n"
"")
        self.btn_login.setObjectName("btn_login")
        self.verticalLayout_14.addWidget(self.btn_login)
        self.btn_SairApp = QtWidgets.QPushButton(self.layoutWidget_6)
        self.btn_SairApp.setEnabled(False)
        self.btn_SairApp.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.btn_SairApp.setFont(font)
        self.btn_SairApp.setStyleSheet("QPushButton#btn_SairApp{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_SairApp:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_SairApp:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}\n"
"")
        self.btn_SairApp.setObjectName("btn_SairApp")
        self.verticalLayout_14.addWidget(self.btn_SairApp)
        self.label_11 = QtWidgets.QLabel(self.frame_4)
        self.label_11.setGeometry(QtCore.QRect(70, 40, 141, 151))
        self.label_11.setStyleSheet("image: url(:/Imagens/password.png);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.stackedWidget.addWidget(self.page)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.scrollArea = QtWidgets.QScrollArea(self.page_6)
        self.scrollArea.setGeometry(QtCore.QRect(40, 8, 1032, 600))
        self.scrollArea.setMinimumSize(QtCore.QSize(1032, 600))
        self.scrollArea.setMaximumSize(QtCore.QSize(1024, 600))
        self.scrollArea.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 1018, 1418))
        self.scrollAreaWidgetContents_3.setStyleSheet("")
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_16 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.frame_16.setEnabled(True)
        self.frame_16.setMinimumSize(QtCore.QSize(1000, 1400))
        self.frame_16.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.frame_16.setMouseTracking(False)
        self.frame_16.setTabletTracking(False)
        self.frame_16.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.frame_16.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.frame_16.setAcceptDrops(False)
        self.frame_16.setWhatsThis("")
        self.frame_16.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.frame_16.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.label = QtWidgets.QLabel(self.frame_16)
        self.label.setGeometry(QtCore.QRect(241, 285, 481, 111))
        self.label.setStyleSheet("image: url(:/Imagens/Peixe.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.layoutWidget_5 = QtWidgets.QWidget(self.frame_16)
        self.layoutWidget_5.setGeometry(QtCore.QRect(820, 258, 112, 149))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.btn_buscarInv = QtWidgets.QPushButton(self.layoutWidget_5)
        self.btn_buscarInv.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(True)
        self.btn_buscarInv.setFont(font)
        self.btn_buscarInv.setStyleSheet("QPushButton#btn_buscarInv{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_buscarInv:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_buscarInv:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Imagens/historia.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_buscarInv.setIcon(icon5)
        self.btn_buscarInv.setIconSize(QtCore.QSize(24, 24))
        self.btn_buscarInv.setObjectName("btn_buscarInv")
        self.verticalLayout_17.addWidget(self.btn_buscarInv)
        self.label_114 = QtWidgets.QLabel(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(9)
        font.setBold(True)
        self.label_114.setFont(font)
        self.label_114.setStyleSheet("color: rgb(0,0,0);")
        self.label_114.setAlignment(QtCore.Qt.AlignCenter)
        self.label_114.setObjectName("label_114")
        self.verticalLayout_17.addWidget(self.label_114)
        self.txt_paciente_4 = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.txt_paciente_4.setEnabled(False)
        self.txt_paciente_4.setMinimumSize(QtCore.QSize(100, 21))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.txt_paciente_4.setFont(font)
        self.txt_paciente_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;")
        self.txt_paciente_4.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_paciente_4.setObjectName("txt_paciente_4")
        self.verticalLayout_17.addWidget(self.txt_paciente_4)
        self.btn_editarInv = QtWidgets.QPushButton(self.layoutWidget_5)
        self.btn_editarInv.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(True)
        self.btn_editarInv.setFont(font)
        self.btn_editarInv.setStyleSheet("QPushButton#btn_editarInv{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_btn_editarInv:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_editarInv:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Imagens/registro (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_editarInv.setIcon(icon6)
        self.btn_editarInv.setIconSize(QtCore.QSize(24, 24))
        self.btn_editarInv.setObjectName("btn_editarInv")
        self.verticalLayout_17.addWidget(self.btn_editarInv)
        self.frame_5 = QtWidgets.QFrame(self.frame_16)
        self.frame_5.setGeometry(QtCore.QRect(68, 228, 861, 8))
        self.frame_5.setStyleSheet("background-color: rgb(244, 244, 244);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_8 = QtWidgets.QFrame(self.frame_16)
        self.frame_8.setGeometry(QtCore.QRect(77, 876, 861, 8))
        self.frame_8.setStyleSheet("background-color: rgb(198, 198, 198);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.btn_alterarInv = QtWidgets.QPushButton(self.frame_16)
        self.btn_alterarInv.setEnabled(False)
        self.btn_alterarInv.setGeometry(QtCore.QRect(100, 1180, 100, 40))
        self.btn_alterarInv.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(True)
        self.btn_alterarInv.setFont(font)
        self.btn_alterarInv.setStyleSheet("QPushButton#btn_alterarInv{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_alterarInv:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_alterarInv:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_alterarInv.setIcon(icon6)
        self.btn_alterarInv.setIconSize(QtCore.QSize(24, 24))
        self.btn_alterarInv.setObjectName("btn_alterarInv")
        self.layoutWidget_2 = QtWidgets.QWidget(self.frame_16)
        self.layoutWidget_2.setGeometry(QtCore.QRect(740, 1170, 208, 42))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.btn_conclusao = QtWidgets.QPushButton(self.layoutWidget_2)
        self.btn_conclusao.setEnabled(False)
        self.btn_conclusao.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(True)
        self.btn_conclusao.setFont(font)
        self.btn_conclusao.setStyleSheet("QPushButton#btn_conclusao{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_conclusao:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_conclusao:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/Imagens/salve-.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_conclusao.setIcon(icon7)
        self.btn_conclusao.setIconSize(QtCore.QSize(24, 24))
        self.btn_conclusao.setObjectName("btn_conclusao")
        self.horizontalLayout_34.addWidget(self.btn_conclusao)
        self.btn_cancela_investiga = QtWidgets.QPushButton(self.layoutWidget_2)
        self.btn_cancela_investiga.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(True)
        self.btn_cancela_investiga.setFont(font)
        self.btn_cancela_investiga.setStyleSheet("QPushButton#btn_cancela_investiga{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_cancela_investiga:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_cancela_investiga:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/Imagens/cancelar (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cancela_investiga.setIcon(icon8)
        self.btn_cancela_investiga.setIconSize(QtCore.QSize(24, 24))
        self.btn_cancela_investiga.setObjectName("btn_cancela_investiga")
        self.horizontalLayout_34.addWidget(self.btn_cancela_investiga)
        self.layoutWidget_3 = QtWidgets.QWidget(self.frame_16)
        self.layoutWidget_3.setGeometry(QtCore.QRect(341, 240, 226, 29))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.label_31 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_31.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_37.addWidget(self.label_31)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget_3)
        self.comboBox.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("color: rgb(0, 0, 0);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_37.addWidget(self.comboBox)
        self.layoutWidget_7 = QtWidgets.QWidget(self.frame_16)
        self.layoutWidget_7.setGeometry(QtCore.QRect(67, 278, 114, 126))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget_7)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_30 = QtWidgets.QLabel(self.layoutWidget_7)
        self.label_30.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_5.addWidget(self.label_30)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_iniciar_investigacao = QtWidgets.QPushButton(self.layoutWidget_7)
        self.btn_iniciar_investigacao.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(True)
        self.btn_iniciar_investigacao.setFont(font)
        self.btn_iniciar_investigacao.setStyleSheet("QPushButton#btn_iniciar_investigacao{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_iniciar_investigacao:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_iniciar_investigacao:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_iniciar_investigacao.setIcon(icon2)
        self.btn_iniciar_investigacao.setIconSize(QtCore.QSize(24, 24))
        self.btn_iniciar_investigacao.setObjectName("btn_iniciar_investigacao")
        self.verticalLayout_4.addWidget(self.btn_iniciar_investigacao)
        self.label_110 = QtWidgets.QLabel(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(9)
        font.setBold(True)
        self.label_110.setFont(font)
        self.label_110.setStyleSheet("color: rgb(0,0,0);")
        self.label_110.setAlignment(QtCore.Qt.AlignCenter)
        self.label_110.setObjectName("label_110")
        self.verticalLayout_4.addWidget(self.label_110)
        self.txt_paciente_3 = QtWidgets.QLineEdit(self.layoutWidget_7)
        self.txt_paciente_3.setEnabled(False)
        self.txt_paciente_3.setMinimumSize(QtCore.QSize(100, 21))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.txt_paciente_3.setFont(font)
        self.txt_paciente_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;")
        self.txt_paciente_3.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_paciente_3.setObjectName("txt_paciente_3")
        self.verticalLayout_4.addWidget(self.txt_paciente_3)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.layoutWidget1 = QtWidgets.QWidget(self.frame_16)
        self.layoutWidget1.setGeometry(QtCore.QRect(52, 410, 905, 755))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_94 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(10)
        font.setBold(False)
        self.label_94.setFont(font)
        self.label_94.setStyleSheet("color: rgb(0,0,0);")
        self.label_94.setObjectName("label_94")
        self.horizontalLayout_19.addWidget(self.label_94)
        self.txt_pessoas = QtWidgets.QLineEdit(self.layoutWidget1)
        self.txt_pessoas.setEnabled(True)
        self.txt_pessoas.setMinimumSize(QtCore.QSize(811, 0))
        self.txt_pessoas.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;")
        self.txt_pessoas.setObjectName("txt_pessoas")
        self.horizontalLayout_19.addWidget(self.txt_pessoas)
        self.verticalLayout.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_98 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(10)
        font.setBold(False)
        self.label_98.setFont(font)
        self.label_98.setStyleSheet("color: rgb(0,0,0);")
        self.label_98.setObjectName("label_98")
        self.horizontalLayout_25.addWidget(self.label_98)
        self.txt_pessoas_6 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.txt_pessoas_6.setEnabled(False)
        self.txt_pessoas_6.setMinimumSize(QtCore.QSize(811, 0))
        self.txt_pessoas_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;")
        self.txt_pessoas_6.setObjectName("txt_pessoas_6")
        self.horizontalLayout_25.addWidget(self.txt_pessoas_6)
        self.verticalLayout.addLayout(self.horizontalLayout_25)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_95 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(10)
        font.setBold(False)
        self.label_95.setFont(font)
        self.label_95.setStyleSheet("color: rgb(0,0,0);")
        self.label_95.setObjectName("label_95")
        self.horizontalLayout_21.addWidget(self.label_95)
        self.txt_processos = QtWidgets.QLineEdit(self.layoutWidget1)
        self.txt_processos.setEnabled(False)
        self.txt_processos.setMinimumSize(QtCore.QSize(811, 0))
        self.txt_processos.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.txt_processos.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;")
        self.txt_processos.setObjectName("txt_processos")
        self.horizontalLayout_21.addWidget(self.txt_processos)
        self.verticalLayout.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_99 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(10)
        font.setBold(False)
        self.label_99.setFont(font)
        self.label_99.setStyleSheet("color: rgb(0,0,0);")
        self.label_99.setObjectName("label_99")
        self.horizontalLayout_22.addWidget(self.label_99)
        self.txt_pessoas_7 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.txt_pessoas_7.setEnabled(False)
        self.txt_pessoas_7.setMinimumSize(QtCore.QSize(811, 0))
        self.txt_pessoas_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;")
        self.txt_pessoas_7.setObjectName("txt_pessoas_7")
        self.horizontalLayout_22.addWidget(self.txt_pessoas_7)
        self.verticalLayout.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.label_97 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(10)
        font.setBold(False)
        self.label_97.setFont(font)
        self.label_97.setStyleSheet("color: rgb(0,0,0);")
        self.label_97.setObjectName("label_97")
        self.horizontalLayout_30.addWidget(self.label_97)
        self.txt_equipamentos = QtWidgets.QLineEdit(self.layoutWidget1)
        self.txt_equipamentos.setEnabled(False)
        self.txt_equipamentos.setMinimumSize(QtCore.QSize(800, 0))
        self.txt_equipamentos.setMaximumSize(QtCore.QSize(380, 16777215))
        self.txt_equipamentos.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;")
        self.txt_equipamentos.setObjectName("txt_equipamentos")
        self.horizontalLayout_30.addWidget(self.txt_equipamentos)
        self.verticalLayout.addLayout(self.horizontalLayout_30)
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.label_96 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(10)
        font.setBold(False)
        self.label_96.setFont(font)
        self.label_96.setStyleSheet("color: rgb(0,0,0);")
        self.label_96.setObjectName("label_96")
        self.horizontalLayout_33.addWidget(self.label_96)
        self.txt_ambiente = QtWidgets.QLineEdit(self.layoutWidget1)
        self.txt_ambiente.setEnabled(False)
        self.txt_ambiente.setMinimumSize(QtCore.QSize(755, 0))
        self.txt_ambiente.setMaximumSize(QtCore.QSize(350, 16777215))
        self.txt_ambiente.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;")
        self.txt_ambiente.setObjectName("txt_ambiente")
        self.horizontalLayout_33.addWidget(self.txt_ambiente)
        self.verticalLayout.addLayout(self.horizontalLayout_33)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.label_32 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_32.setFont(font)
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.verticalLayout_3.addWidget(self.label_32)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.label_88 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(10)
        font.setBold(False)
        self.label_88.setFont(font)
        self.label_88.setStyleSheet("color: rgb(0,0,0);")
        self.label_88.setObjectName("label_88")
        self.horizontalLayout_29.addWidget(self.label_88)
        self.txt_pessoas_2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.txt_pessoas_2.setEnabled(False)
        self.txt_pessoas_2.setMinimumSize(QtCore.QSize(811, 0))
        self.txt_pessoas_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;")
        self.txt_pessoas_2.setObjectName("txt_pessoas_2")
        self.horizontalLayout_29.addWidget(self.txt_pessoas_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_29)
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.label_89 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(10)
        font.setBold(False)
        self.label_89.setFont(font)
        self.label_89.setStyleSheet("color: rgb(0,0,0);")
        self.label_89.setObjectName("label_89")
        self.horizontalLayout_32.addWidget(self.label_89)
        self.txt_pessoas_3 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.txt_pessoas_3.setEnabled(False)
        self.txt_pessoas_3.setMinimumSize(QtCore.QSize(811, 0))
        self.txt_pessoas_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;")
        self.txt_pessoas_3.setObjectName("txt_pessoas_3")
        self.horizontalLayout_32.addWidget(self.txt_pessoas_3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_32)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_90 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(10)
        font.setBold(False)
        self.label_90.setFont(font)
        self.label_90.setStyleSheet("color: rgb(0,0,0);")
        self.label_90.setObjectName("label_90")
        self.horizontalLayout_24.addWidget(self.label_90)
        self.txt_pessoas_4 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.txt_pessoas_4.setEnabled(False)
        self.txt_pessoas_4.setMinimumSize(QtCore.QSize(811, 0))
        self.txt_pessoas_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;")
        self.txt_pessoas_4.setObjectName("txt_pessoas_4")
        self.horizontalLayout_24.addWidget(self.txt_pessoas_4)
        self.verticalLayout_7.addLayout(self.horizontalLayout_24)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_91 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(10)
        font.setBold(False)
        self.label_91.setFont(font)
        self.label_91.setStyleSheet("color: rgb(0,0,0);")
        self.label_91.setObjectName("label_91")
        self.horizontalLayout_20.addWidget(self.label_91)
        self.txt_pessoas_5 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.txt_pessoas_5.setEnabled(False)
        self.txt_pessoas_5.setMinimumSize(QtCore.QSize(811, 0))
        self.txt_pessoas_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;")
        self.txt_pessoas_5.setObjectName("txt_pessoas_5")
        self.horizontalLayout_20.addWidget(self.txt_pessoas_5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_92 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(10)
        font.setBold(False)
        self.label_92.setFont(font)
        self.label_92.setStyleSheet("color: rgb(0,0,0);")
        self.label_92.setObjectName("label_92")
        self.horizontalLayout_16.addWidget(self.label_92)
        self.txt_pessoas_8 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.txt_pessoas_8.setEnabled(False)
        self.txt_pessoas_8.setMinimumSize(QtCore.QSize(811, 0))
        self.txt_pessoas_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;")
        self.txt_pessoas_8.setObjectName("txt_pessoas_8")
        self.horizontalLayout_16.addWidget(self.txt_pessoas_8)
        self.verticalLayout_7.addLayout(self.horizontalLayout_16)
        self.verticalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_86 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(11)
        font.setBold(True)
        self.label_86.setFont(font)
        self.label_86.setStyleSheet("color: rgb(0,0,0);")
        self.label_86.setAlignment(QtCore.Qt.AlignCenter)
        self.label_86.setObjectName("label_86")
        self.verticalLayout_8.addWidget(self.label_86)
        self.txt_recomendacao_2 = QtWidgets.QTextEdit(self.layoutWidget1)
        self.txt_recomendacao_2.setEnabled(True)
        self.txt_recomendacao_2.setMinimumSize(QtCore.QSize(811, 51))
        self.txt_recomendacao_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"\n"
"border-top-right-radius: 20px;\n"
"border-bottom-left-radius: 50px;\n"
"border-bottom-right-radius: 10px;")
        self.txt_recomendacao_2.setObjectName("txt_recomendacao_2")
        self.verticalLayout_8.addWidget(self.txt_recomendacao_2)
        self.verticalLayout_6.addLayout(self.verticalLayout_8)
        self.layoutWidget2 = QtWidgets.QWidget(self.frame_16)
        self.layoutWidget2.setGeometry(QtCore.QRect(65, 20, 866, 182))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_29 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_2.addWidget(self.label_29)
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.label_19 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_19.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_31.addWidget(self.label_19)
        self.cb_setor = QtWidgets.QComboBox(self.layoutWidget2)
        self.cb_setor.setEnabled(False)
        self.cb_setor.setMinimumSize(QtCore.QSize(250, 23))
        self.cb_setor.setMaximumSize(QtCore.QSize(250, 16777215))
        self.cb_setor.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;")
        self.cb_setor.setObjectName("cb_setor")
        self.cb_setor.addItem("")
        self.cb_setor.setItemText(0, "")
        self.horizontalLayout_31.addWidget(self.cb_setor)
        self.verticalLayout_2.addLayout(self.horizontalLayout_31)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_26 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_5.addWidget(self.label_26)
        self.cd_tipo_rnc_2 = QtWidgets.QComboBox(self.layoutWidget2)
        self.cd_tipo_rnc_2.setEnabled(False)
        self.cd_tipo_rnc_2.setMinimumSize(QtCore.QSize(751, 23))
        self.cd_tipo_rnc_2.setMaximumSize(QtCore.QSize(751, 16777215))
        self.cd_tipo_rnc_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;")
        self.cd_tipo_rnc_2.setObjectName("cd_tipo_rnc_2")
        self.cd_tipo_rnc_2.addItem("")
        self.cd_tipo_rnc_2.setItemText(0, "")
        self.horizontalLayout_5.addWidget(self.cd_tipo_rnc_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_9.addLayout(self.verticalLayout_2)
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.label_27 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_38.addWidget(self.label_27)
        self.label_28 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_38.addWidget(self.label_28)
        self.horizontalLayout_36.addLayout(self.horizontalLayout_38)
        self.cb_funcao_3 = QtWidgets.QComboBox(self.layoutWidget2)
        self.cb_funcao_3.setEnabled(False)
        self.cb_funcao_3.setMinimumSize(QtCore.QSize(240, 23))
        self.cb_funcao_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;")
        self.cb_funcao_3.setObjectName("cb_funcao_3")
        self.cb_funcao_3.addItem("")
        self.cb_funcao_3.setItemText(0, "")
        self.cb_funcao_3.addItem("")
        self.cb_funcao_3.addItem("")
        self.cb_funcao_3.addItem("")
        self.horizontalLayout_36.addWidget(self.cb_funcao_3)
        self.horizontalLayout_28.addLayout(self.horizontalLayout_36)
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.label_33 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_40.addWidget(self.label_33)
        self.label_34 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_40.addWidget(self.label_34)
        self.horizontalLayout_39.addLayout(self.horizontalLayout_40)
        self.dt_rnc_2 = QtWidgets.QDateEdit(self.layoutWidget2)
        self.dt_rnc_2.setEnabled(False)
        self.dt_rnc_2.setMinimumSize(QtCore.QSize(150, 23))
        self.dt_rnc_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;")
        self.dt_rnc_2.setAlignment(QtCore.Qt.AlignCenter)
        self.dt_rnc_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 1, 1), QtCore.QTime(18, 0, 0)))
        self.dt_rnc_2.setCalendarPopup(True)
        self.dt_rnc_2.setObjectName("dt_rnc_2")
        self.horizontalLayout_39.addWidget(self.dt_rnc_2)
        self.horizontalLayout_28.addLayout(self.horizontalLayout_39)
        self.verticalLayout_9.addLayout(self.horizontalLayout_28)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.label_23 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_27.addWidget(self.label_23)
        self.horizontalLayout_26.addLayout(self.horizontalLayout_27)
        self.cb_funcao_outros_2 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.cb_funcao_outros_2.setEnabled(False)
        self.cb_funcao_outros_2.setMinimumSize(QtCore.QSize(220, 23))
        self.cb_funcao_outros_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;")
        self.cb_funcao_outros_2.setObjectName("cb_funcao_outros_2")
        self.horizontalLayout_26.addWidget(self.cb_funcao_outros_2)
        self.verticalLayout_9.addLayout(self.horizontalLayout_26)
        self.verticalLayout_11.addWidget(self.frame_16)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.stackedWidget.addWidget(self.page_6)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.label_35 = QtWidgets.QLabel(self.page_5)
        self.label_35.setGeometry(QtCore.QRect(120, 20, 862, 28))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_35.setFont(font)
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.layoutWidget3 = QtWidgets.QWidget(self.page_5)
        self.layoutWidget3.setGeometry(QtCore.QRect(310, 72, 516, 470))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_42 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_42.setObjectName("horizontalLayout_42")
        self.btn_novoUser = QtWidgets.QPushButton(self.layoutWidget3)
        self.btn_novoUser.setMinimumSize(QtCore.QSize(100, 40))
        self.btn_novoUser.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.btn_novoUser.setFont(font)
        self.btn_novoUser.setStyleSheet("QPushButton#btn_novoUser{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_novoUser:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_novoUser:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/Imagem/adicionar-usuario.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_novoUser.setIcon(icon9)
        self.btn_novoUser.setIconSize(QtCore.QSize(24, 24))
        self.btn_novoUser.setObjectName("btn_novoUser")
        self.horizontalLayout_42.addWidget(self.btn_novoUser)
        self.btn_editaUser = QtWidgets.QPushButton(self.layoutWidget3)
        self.btn_editaUser.setEnabled(False)
        self.btn_editaUser.setMinimumSize(QtCore.QSize(100, 40))
        self.btn_editaUser.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.btn_editaUser.setFont(font)
        self.btn_editaUser.setStyleSheet("QPushButton#btn_editaUser{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_editaUser:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_editaUser:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/Imagem/do-utilizador.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_editaUser.setIcon(icon10)
        self.btn_editaUser.setIconSize(QtCore.QSize(24, 24))
        self.btn_editaUser.setObjectName("btn_editaUser")
        self.horizontalLayout_42.addWidget(self.btn_editaUser)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_42.addItem(spacerItem1)
        self.btn_alterarUser = QtWidgets.QPushButton(self.layoutWidget3)
        self.btn_alterarUser.setEnabled(False)
        self.btn_alterarUser.setMinimumSize(QtCore.QSize(100, 40))
        self.btn_alterarUser.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.btn_alterarUser.setFont(font)
        self.btn_alterarUser.setStyleSheet("QPushButton#btn_alterarUser{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_alterarUser:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_alterarUser:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/Imagem/registro (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_alterarUser.setIcon(icon11)
        self.btn_alterarUser.setIconSize(QtCore.QSize(24, 24))
        self.btn_alterarUser.setObjectName("btn_alterarUser")
        self.horizontalLayout_42.addWidget(self.btn_alterarUser)
        self.verticalLayout_10.addLayout(self.horizontalLayout_42)
        self.frame_6 = QtWidgets.QFrame(self.layoutWidget3)
        self.frame_6.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_46 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_46.setObjectName("horizontalLayout_46")
        self.label_100 = QtWidgets.QLabel(self.frame_6)
        self.label_100.setStyleSheet("color:rgb(0,0,0);")
        self.label_100.setAlignment(QtCore.Qt.AlignCenter)
        self.label_100.setObjectName("label_100")
        self.horizontalLayout_46.addWidget(self.label_100)
        self.txt_cadnome = QtWidgets.QLineEdit(self.frame_6)
        self.txt_cadnome.setEnabled(True)
        self.txt_cadnome.setMinimumSize(QtCore.QSize(421, 0))
        self.txt_cadnome.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;\n"
"")
        self.txt_cadnome.setText("")
        self.txt_cadnome.setObjectName("txt_cadnome")
        self.horizontalLayout_46.addWidget(self.txt_cadnome)
        self.gridLayout_4.addLayout(self.horizontalLayout_46, 0, 0, 1, 1)
        self.horizontalLayout_47 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_47.setObjectName("horizontalLayout_47")
        self.label_101 = QtWidgets.QLabel(self.frame_6)
        self.label_101.setStyleSheet("color:rgb(0,0,0);")
        self.label_101.setAlignment(QtCore.Qt.AlignCenter)
        self.label_101.setObjectName("label_101")
        self.horizontalLayout_47.addWidget(self.label_101)
        self.txt_cadnome_2 = QtWidgets.QLineEdit(self.frame_6)
        self.txt_cadnome_2.setEnabled(False)
        self.txt_cadnome_2.setMinimumSize(QtCore.QSize(421, 0))
        self.txt_cadnome_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;\n"
"")
        self.txt_cadnome_2.setText("")
        self.txt_cadnome_2.setObjectName("txt_cadnome_2")
        self.horizontalLayout_47.addWidget(self.txt_cadnome_2)
        self.gridLayout_4.addLayout(self.horizontalLayout_47, 1, 0, 1, 1)
        self.horizontalLayout_48 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_48.setObjectName("horizontalLayout_48")
        self.label_102 = QtWidgets.QLabel(self.frame_6)
        self.label_102.setStyleSheet("color:rgb(0,0,0);")
        self.label_102.setAlignment(QtCore.Qt.AlignCenter)
        self.label_102.setObjectName("label_102")
        self.horizontalLayout_48.addWidget(self.label_102)
        self.txt_cadnome_3 = QtWidgets.QLineEdit(self.frame_6)
        self.txt_cadnome_3.setEnabled(False)
        self.txt_cadnome_3.setMinimumSize(QtCore.QSize(421, 0))
        self.txt_cadnome_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;\n"
"")
        self.txt_cadnome_3.setText("")
        self.txt_cadnome_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_cadnome_3.setObjectName("txt_cadnome_3")
        self.horizontalLayout_48.addWidget(self.txt_cadnome_3)
        self.gridLayout_4.addLayout(self.horizontalLayout_48, 2, 0, 1, 1)
        self.horizontalLayout_50 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_50.setObjectName("horizontalLayout_50")
        self.label_103 = QtWidgets.QLabel(self.frame_6)
        self.label_103.setStyleSheet("color:rgb(0,0,0);")
        self.label_103.setAlignment(QtCore.Qt.AlignCenter)
        self.label_103.setObjectName("label_103")
        self.horizontalLayout_50.addWidget(self.label_103)
        self.cb_outros_3 = QtWidgets.QComboBox(self.frame_6)
        self.cb_outros_3.setEnabled(True)
        self.cb_outros_3.setMinimumSize(QtCore.QSize(300, 0))
        self.cb_outros_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;\n"
"")
        self.cb_outros_3.setObjectName("cb_outros_3")
        self.cb_outros_3.addItem("")
        self.cb_outros_3.setItemText(0, "")
        self.cb_outros_3.addItem("")
        self.cb_outros_3.addItem("")
        self.cb_outros_3.addItem("")
        self.cb_outros_3.addItem("")
        self.horizontalLayout_50.addWidget(self.cb_outros_3)
        self.gridLayout_4.addLayout(self.horizontalLayout_50, 3, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.verticalLayout_10.addWidget(self.frame_6)
        self.gridLayout_6.addLayout(self.verticalLayout_10, 0, 0, 1, 1)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.horizontalLayout_43 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_43.setObjectName("horizontalLayout_43")
        self.label_104 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_104.setStyleSheet("color:rgb(0,0,0);")
        self.label_104.setObjectName("label_104")
        self.horizontalLayout_43.addWidget(self.label_104)
        self.txt_consultaUser = QtWidgets.QLineEdit(self.layoutWidget3)
        self.txt_consultaUser.setMinimumSize(QtCore.QSize(351, 22))
        self.txt_consultaUser.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;\n"
"")
        self.txt_consultaUser.setObjectName("txt_consultaUser")
        self.horizontalLayout_43.addWidget(self.txt_consultaUser)
        self.btn_consultaUser = QtWidgets.QPushButton(self.layoutWidget3)
        self.btn_consultaUser.setMinimumSize(QtCore.QSize(111, 40))
        self.btn_consultaUser.setMaximumSize(QtCore.QSize(100, 40))
        self.btn_consultaUser.setStyleSheet("QPushButton#btn_consultaUser{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_consultaUser:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_consultaUser:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/Imagem/historia.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_consultaUser.setIcon(icon12)
        self.btn_consultaUser.setIconSize(QtCore.QSize(24, 24))
        self.btn_consultaUser.setObjectName("btn_consultaUser")
        self.horizontalLayout_43.addWidget(self.btn_consultaUser)
        self.verticalLayout_18.addLayout(self.horizontalLayout_43)
        self.tableWidget = QtWidgets.QTableWidget(self.layoutWidget3)
        self.tableWidget.setStyleSheet("background-color: rgba(10,0,0,50);\n"
"\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"\n"
"padding-bottom: 7px")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.verticalLayout_18.addWidget(self.tableWidget)
        self.gridLayout_6.addLayout(self.verticalLayout_18, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_5)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.page_2)
        self.frame.setMaximumSize(QtCore.QSize(1085, 800))
        self.frame.setStyleSheet("\n"
"background-color: rgb(207, 207, 207);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_51 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_51.setObjectName("horizontalLayout_51")
        spacerItem2 = QtWidgets.QSpacerItem(37, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_51.addItem(spacerItem2)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.btn_nova_rnc = QtWidgets.QPushButton(self.frame)
        self.btn_nova_rnc.setMinimumSize(QtCore.QSize(100, 40))
        self.btn_nova_rnc.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(False)
        self.btn_nova_rnc.setFont(font)
        self.btn_nova_rnc.setStyleSheet("QPushButton#btn_nova_rnc{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_nova_rnc:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_nova_rnc:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/Imagens/registro.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_nova_rnc.setIcon(icon13)
        self.btn_nova_rnc.setIconSize(QtCore.QSize(24, 24))
        self.btn_nova_rnc.setObjectName("btn_nova_rnc")
        self.horizontalLayout_17.addWidget(self.btn_nova_rnc)
        self.label_81 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.label_81.setFont(font)
        self.label_81.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_81.setAlignment(QtCore.Qt.AlignCenter)
        self.label_81.setObjectName("label_81")
        self.horizontalLayout_17.addWidget(self.label_81)
        self.txt_consultaNoti = QtWidgets.QLineEdit(self.frame)
        self.txt_consultaNoti.setMinimumSize(QtCore.QSize(60, 30))
        self.txt_consultaNoti.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.txt_consultaNoti.setFont(font)
        self.txt_consultaNoti.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 2px;\n"
"border-top-right-radius : 20px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;")
        self.txt_consultaNoti.setText("")
        self.txt_consultaNoti.setObjectName("txt_consultaNoti")
        self.horizontalLayout_17.addWidget(self.txt_consultaNoti)
        self.btn_pesquisar_rnc = QtWidgets.QPushButton(self.frame)
        self.btn_pesquisar_rnc.setMinimumSize(QtCore.QSize(100, 40))
        self.btn_pesquisar_rnc.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(False)
        self.btn_pesquisar_rnc.setFont(font)
        self.btn_pesquisar_rnc.setStyleSheet("QPushButton#btn_pesquisar_rnc{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_pesquisar_rnc:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_pesquisar_rnc:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_pesquisar_rnc.setIcon(icon5)
        self.btn_pesquisar_rnc.setIconSize(QtCore.QSize(24, 24))
        self.btn_pesquisar_rnc.setObjectName("btn_pesquisar_rnc")
        self.horizontalLayout_17.addWidget(self.btn_pesquisar_rnc)
        self.btn_gerar_pdf = QtWidgets.QPushButton(self.frame)
        self.btn_gerar_pdf.setEnabled(False)
        self.btn_gerar_pdf.setMinimumSize(QtCore.QSize(100, 40))
        self.btn_gerar_pdf.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(8)
        font.setBold(False)
        self.btn_gerar_pdf.setFont(font)
        self.btn_gerar_pdf.setStyleSheet("QPushButton#btn_gerar_pdf{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_gerar_pdf:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_gerar_pdf:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/Imagens/pdf (3).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_gerar_pdf.setIcon(icon14)
        self.btn_gerar_pdf.setIconSize(QtCore.QSize(24, 24))
        self.btn_gerar_pdf.setObjectName("btn_gerar_pdf")
        self.horizontalLayout_17.addWidget(self.btn_gerar_pdf)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem3)
        self.horizontalLayout_51.addLayout(self.horizontalLayout_17)
        spacerItem4 = QtWidgets.QSpacerItem(37, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_51.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout_51, 0, 0, 1, 1)
        self.horizontalLayout_49 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_49.setObjectName("horizontalLayout_49")
        self.horizontalLayout_45 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_45.setObjectName("horizontalLayout_45")
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setMinimumSize(QtCore.QSize(290, 30))
        self.frame_7.setMaximumSize(QtCore.QSize(292, 30))
        self.frame_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-top-left-radius: 35px;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-left-radius: 50px;\n"
"border-bottom-right-radius: 10px;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_10.setContentsMargins(0, 6, 0, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_3 = QtWidgets.QLabel(self.frame_7)
        self.label_3.setMinimumSize(QtCore.QSize(92, 16))
        self.label_3.setMaximumSize(QtCore.QSize(92, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_10.addWidget(self.label_3)
        self.horizontalLayout_45.addWidget(self.frame_7)
        self.cb_setor_1 = QtWidgets.QComboBox(self.frame)
        self.cb_setor_1.setEnabled(False)
        self.cb_setor_1.setMinimumSize(QtCore.QSize(200, 23))
        self.cb_setor_1.setMaximumSize(QtCore.QSize(200, 16777215))
        self.cb_setor_1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;\n"
"")
        self.cb_setor_1.setObjectName("cb_setor_1")
        self.cb_setor_1.addItem("")
        self.cb_setor_1.setItemText(0, "")
        self.horizontalLayout_45.addWidget(self.cb_setor_1)
        self.horizontalLayout_49.addLayout(self.horizontalLayout_45)
        spacerItem5 = QtWidgets.QSpacerItem(37, 17, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_49.addItem(spacerItem5)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame_11 = QtWidgets.QFrame(self.frame)
        self.frame_11.setMinimumSize(QtCore.QSize(290, 30))
        self.frame_11.setMaximumSize(QtCore.QSize(290, 30))
        self.frame_11.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-top-left-radius: 35px;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-left-radius: 50px;\n"
"border-bottom-right-radius: 10px;")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setContentsMargins(0, 6, 0, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_4 = QtWidgets.QLabel(self.frame_11)
        self.label_4.setMinimumSize(QtCore.QSize(250, 16))
        self.label_4.setMaximumSize(QtCore.QSize(250, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_9.addWidget(self.label_4)
        self.horizontalLayout_11.addWidget(self.frame_11)
        self.cb_setor_2 = QtWidgets.QComboBox(self.frame)
        self.cb_setor_2.setEnabled(False)
        self.cb_setor_2.setMinimumSize(QtCore.QSize(200, 23))
        self.cb_setor_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.cb_setor_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;\n"
"")
        self.cb_setor_2.setObjectName("cb_setor_2")
        self.cb_setor_2.addItem("")
        self.cb_setor_2.setItemText(0, "")
        self.horizontalLayout_11.addWidget(self.cb_setor_2)
        self.horizontalLayout_49.addLayout(self.horizontalLayout_11)
        self.gridLayout.addLayout(self.horizontalLayout_49, 1, 0, 1, 1)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.frame_10 = QtWidgets.QFrame(self.frame)
        self.frame_10.setMinimumSize(QtCore.QSize(290, 30))
        self.frame_10.setMaximumSize(QtCore.QSize(290, 30))
        self.frame_10.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-top-left-radius: 35px;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-left-radius: 50px;\n"
"border-bottom-right-radius: 10px;")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_3.setContentsMargins(0, 6, 0, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_21 = QtWidgets.QLabel(self.frame_10)
        self.label_21.setMinimumSize(QtCore.QSize(150, 16))
        self.label_21.setMaximumSize(QtCore.QSize(150, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_3.addWidget(self.label_21)
        self.horizontalLayout_13.addWidget(self.frame_10)
        self.cd_tipo_rnc = QtWidgets.QComboBox(self.frame)
        self.cd_tipo_rnc.setEnabled(False)
        self.cd_tipo_rnc.setMinimumSize(QtCore.QSize(751, 23))
        self.cd_tipo_rnc.setMaximumSize(QtCore.QSize(751, 16777215))
        self.cd_tipo_rnc.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;\n"
"")
        self.cd_tipo_rnc.setObjectName("cd_tipo_rnc")
        self.cd_tipo_rnc.addItem("")
        self.cd_tipo_rnc.setItemText(0, "")
        self.horizontalLayout_13.addWidget(self.cd_tipo_rnc)
        self.gridLayout.addLayout(self.horizontalLayout_13, 2, 0, 1, 1)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.frame_12 = QtWidgets.QFrame(self.frame)
        self.frame_12.setMinimumSize(QtCore.QSize(290, 30))
        self.frame_12.setMaximumSize(QtCore.QSize(290, 30))
        self.frame_12.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-top-left-radius: 35px;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-left-radius: 50px;\n"
"border-bottom-right-radius: 10px;")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_4.setContentsMargins(0, 6, 0, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.frame_12)
        self.label_6.setMinimumSize(QtCore.QSize(190, 16))
        self.label_6.setMaximumSize(QtCore.QSize(190, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.horizontalLayout_15.addWidget(self.frame_12)
        self.txt_descreva = QtWidgets.QPlainTextEdit(self.frame)
        self.txt_descreva.setEnabled(False)
        self.txt_descreva.setMinimumSize(QtCore.QSize(751, 100))
        self.txt_descreva.setMaximumSize(QtCore.QSize(751, 200))
        self.txt_descreva.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"\n"
"border-top-right-radius: 20px;\n"
"border-bottom-left-radius: 50px;\n"
"border-bottom-right-radius: 10px;")
        self.txt_descreva.setObjectName("txt_descreva")
        self.horizontalLayout_15.addWidget(self.txt_descreva)
        self.gridLayout.addLayout(self.horizontalLayout_15, 3, 0, 1, 1)
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.horizontalLayout_44 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_44.setObjectName("horizontalLayout_44")
        self.frame_13 = QtWidgets.QFrame(self.frame)
        self.frame_13.setMinimumSize(QtCore.QSize(290, 30))
        self.frame_13.setMaximumSize(QtCore.QSize(290, 30))
        self.frame_13.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-top-left-radius: 35px;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-left-radius: 50px;\n"
"border-bottom-right-radius: 10px;")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_6.setContentsMargins(0, 6, 0, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.frame_13)
        self.label_7.setMinimumSize(QtCore.QSize(250, 16))
        self.label_7.setMaximumSize(QtCore.QSize(250, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.horizontalLayout_44.addWidget(self.frame_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setEnabled(False)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_14.addWidget(self.radioButton)
        self.cb_sn = QtWidgets.QComboBox(self.frame)
        self.cb_sn.setEnabled(False)
        self.cb_sn.setMinimumSize(QtCore.QSize(50, 23))
        self.cb_sn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;\n"
"")
        self.cb_sn.setObjectName("cb_sn")
        self.cb_sn.addItem("")
        self.cb_sn.setItemText(0, "")
        self.cb_sn.addItem("")
        self.horizontalLayout_14.addWidget(self.cb_sn)
        self.horizontalLayout_44.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setEnabled(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_2.addWidget(self.radioButton_2)
        self.cb_mt = QtWidgets.QComboBox(self.frame)
        self.cb_mt.setEnabled(False)
        self.cb_mt.setMinimumSize(QtCore.QSize(50, 23))
        self.cb_mt.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;\n"
"")
        self.cb_mt.setObjectName("cb_mt")
        self.cb_mt.addItem("")
        self.cb_mt.setItemText(0, "")
        self.cb_mt.addItem("")
        self.horizontalLayout_2.addWidget(self.cb_mt)
        self.horizontalLayout_44.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_35.addLayout(self.horizontalLayout_44)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(290, 30))
        self.frame_2.setMaximumSize(QtCore.QSize(290, 30))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-top-left-radius: 35px;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-left-radius: 50px;\n"
"border-bottom-right-radius: 10px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setMaximumSize(QtCore.QSize(230, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("border-top-left-radius: 35px;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-left-radius: 50px;\n"
"border-bottom-right-radius: 10px;")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.horizontalLayout_23.addWidget(self.frame_2)
        self.dt_rnc = QtWidgets.QDateEdit(self.frame)
        self.dt_rnc.setEnabled(False)
        self.dt_rnc.setMinimumSize(QtCore.QSize(150, 23))
        self.dt_rnc.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;\n"
"")
        self.dt_rnc.setAlignment(QtCore.Qt.AlignCenter)
        self.dt_rnc.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 1, 1), QtCore.QTime(12, 0, 0)))
        self.dt_rnc.setCalendarPopup(True)
        self.dt_rnc.setObjectName("dt_rnc")
        self.horizontalLayout_23.addWidget(self.dt_rnc)
        self.horizontalLayout_35.addLayout(self.horizontalLayout_23)
        self.gridLayout.addLayout(self.horizontalLayout_35, 4, 0, 1, 1)
        self.horizontalLayout_55 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_55.setObjectName("horizontalLayout_55")
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.frame_17 = QtWidgets.QFrame(self.frame)
        self.frame_17.setMinimumSize(QtCore.QSize(290, 30))
        self.frame_17.setMaximumSize(QtCore.QSize(290, 30))
        self.frame_17.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-top-left-radius: 35px;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-left-radius: 50px;\n"
"border-bottom-right-radius: 10px;")
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_53 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_53.setContentsMargins(0, 6, 0, -1)
        self.horizontalLayout_53.setObjectName("horizontalLayout_53")
        self.label_9 = QtWidgets.QLabel(self.frame_17)
        self.label_9.setMinimumSize(QtCore.QSize(130, 16))
        self.label_9.setMaximumSize(QtCore.QSize(130, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_53.addWidget(self.label_9)
        self.horizontalLayout_41.addWidget(self.frame_17)
        self.cb_funcao = QtWidgets.QComboBox(self.frame)
        self.cb_funcao.setEnabled(False)
        self.cb_funcao.setMinimumSize(QtCore.QSize(240, 23))
        self.cb_funcao.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;\n"
"")
        self.cb_funcao.setObjectName("cb_funcao")
        self.cb_funcao.addItem("")
        self.cb_funcao.setItemText(0, "")
        self.horizontalLayout_41.addWidget(self.cb_funcao)
        self.horizontalLayout_55.addLayout(self.horizontalLayout_41)
        self.horizontalLayout_52 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_52.setObjectName("horizontalLayout_52")
        self.frame_15 = QtWidgets.QFrame(self.frame)
        self.frame_15.setMinimumSize(QtCore.QSize(290, 30))
        self.frame_15.setMaximumSize(QtCore.QSize(290, 30))
        self.frame_15.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-top-left-radius: 35px;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-left-radius: 50px;\n"
"border-bottom-right-radius: 10px;")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.frame_15)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        self.horizontalLayout_52.addWidget(self.frame_15)
        self.cb_funcao_outros = QtWidgets.QLineEdit(self.frame)
        self.cb_funcao_outros.setEnabled(False)
        self.cb_funcao_outros.setMinimumSize(QtCore.QSize(220, 23))
        self.cb_funcao_outros.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;\n"
"")
        self.cb_funcao_outros.setObjectName("cb_funcao_outros")
        self.horizontalLayout_52.addWidget(self.cb_funcao_outros)
        self.horizontalLayout_55.addLayout(self.horizontalLayout_52)
        self.gridLayout.addLayout(self.horizontalLayout_55, 5, 0, 1, 1)
        self.horizontalLayout_54 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_54.setObjectName("horizontalLayout_54")
        self.frame_18 = QtWidgets.QFrame(self.frame)
        self.frame_18.setMinimumSize(QtCore.QSize(290, 30))
        self.frame_18.setMaximumSize(QtCore.QSize(290, 30))
        self.frame_18.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-top-left-radius: 35px;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-left-radius: 50px;\n"
"border-bottom-right-radius: 10px;")
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_18)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_24 = QtWidgets.QLabel(self.frame_18)
        self.label_24.setMinimumSize(QtCore.QSize(120, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_7.addWidget(self.label_24)
        self.horizontalLayout_54.addWidget(self.frame_18)
        self.cb_funcao_outros_3 = QtWidgets.QLineEdit(self.frame)
        self.cb_funcao_outros_3.setEnabled(False)
        self.cb_funcao_outros_3.setMinimumSize(QtCore.QSize(220, 23))
        self.cb_funcao_outros_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 2px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius : 3px;\n"
"")
        self.cb_funcao_outros_3.setObjectName("cb_funcao_outros_3")
        self.horizontalLayout_54.addWidget(self.cb_funcao_outros_3)
        self.gridLayout.addLayout(self.horizontalLayout_54, 6, 0, 1, 1)
        self.horizontalLayout_56 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_56.setObjectName("horizontalLayout_56")
        self.label_82 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(12)
        self.label_82.setFont(font)
        self.label_82.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_82.setAlignment(QtCore.Qt.AlignCenter)
        self.label_82.setObjectName("label_82")
        self.horizontalLayout_56.addWidget(self.label_82)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setMinimumSize(QtCore.QSize(500, 250))
        self.label_5.setMaximumSize(QtCore.QSize(500, 250))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_56.addWidget(self.label_5)
        self.btn_anexar = QtWidgets.QPushButton(self.frame)
        self.btn_anexar.setEnabled(True)
        self.btn_anexar.setMinimumSize(QtCore.QSize(100, 40))
        self.btn_anexar.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.btn_anexar.setFont(font)
        self.btn_anexar.setStyleSheet("QPushButton#btn_anexar{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_anexar:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_anexar:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_anexar.setIcon(icon7)
        self.btn_anexar.setIconSize(QtCore.QSize(24, 24))
        self.btn_anexar.setObjectName("btn_anexar")
        self.horizontalLayout_56.addWidget(self.btn_anexar)
        self.gridLayout.addLayout(self.horizontalLayout_56, 7, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setMinimumSize(QtCore.QSize(1060, 5))
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 5))
        self.label_13.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 8, 0, 1, 1)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setContentsMargins(0, 9, -1, -1)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem6)
        self.btn_salva_rnc = QtWidgets.QPushButton(self.frame)
        self.btn_salva_rnc.setEnabled(True)
        self.btn_salva_rnc.setMinimumSize(QtCore.QSize(100, 40))
        self.btn_salva_rnc.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.btn_salva_rnc.setFont(font)
        self.btn_salva_rnc.setStyleSheet("QPushButton#btn_salva_rnc{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_salva_rnc:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_salva_rnc:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_salva_rnc.setIcon(icon7)
        self.btn_salva_rnc.setIconSize(QtCore.QSize(24, 24))
        self.btn_salva_rnc.setObjectName("btn_salva_rnc")
        self.horizontalLayout_18.addWidget(self.btn_salva_rnc)
        self.btn_cancela_rnc = QtWidgets.QPushButton(self.frame)
        self.btn_cancela_rnc.setEnabled(True)
        self.btn_cancela_rnc.setMinimumSize(QtCore.QSize(100, 40))
        self.btn_cancela_rnc.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        self.btn_cancela_rnc.setFont(font)
        self.btn_cancela_rnc.setStyleSheet("QPushButton#btn_cancela_rnc{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(100, 19,11, 219), stop:1 rgba(0, 0, 0, 80));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_cancela_rnc:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_cancela_rnc:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_cancela_rnc.setIcon(icon8)
        self.btn_cancela_rnc.setIconSize(QtCore.QSize(24, 24))
        self.btn_cancela_rnc.setObjectName("btn_cancela_rnc")
        self.horizontalLayout_18.addWidget(self.btn_cancela_rnc)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem7)
        self.gridLayout.addLayout(self.horizontalLayout_18, 9, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout_3.addWidget(self.stackedWidget, 1, 0, 1, 2)
        # MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "REGISTRO DE NÃO CONFORMIDADE"))
        self.btn_dashboard.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">GERENCIAMENTO DE INFORMAÇÕES</span></p></body></html>"))
        self.btn_dashboard.setText(_translate("MainWindow", "DASHBOARD"))
        self.btn_rnc.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">FORMULÁRIO DE NOTIFICAÇÃO</span></p></body></html>"))
        self.btn_rnc.setText(_translate("MainWindow", "RNC"))
        self.btn_tratativa.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">FORMULÁRIO DE INVESTIGAÇÃO</span></p></body></html>"))
        self.btn_tratativa.setText(_translate("MainWindow", "TRATATIVA"))
        self.btn_consultar.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">CONSULTA DE NOTIFICAÇÃO</span></p></body></html>"))
        self.btn_consultar.setText(_translate("MainWindow", "CONSULTA"))
        self.btn_usuarios.setText(_translate("MainWindow", "U S U Á R I O S"))
        self.label_12.setText(_translate("MainWindow", "REGISTRO DE"))
        self.label_20.setText(_translate("MainWindow", " NÃO CONFORMIDADE"))
        self.txt_usuario.setPlaceholderText(_translate("MainWindow", "Digite seu Usuário"))
        self.txt_senha.setPlaceholderText(_translate("MainWindow", "Digite sua Senha"))
        self.cb_empresa.setItemText(0, _translate("MainWindow", "bd_rnc"))
        self.btn_anonimo.setText(_translate("MainWindow", "ANÔNIMO"))
        self.btn_login.setText(_translate("MainWindow", "L O G I N"))
        self.btn_SairApp.setText(_translate("MainWindow", "S A I R"))
        self.btn_buscarInv.setText(_translate("MainWindow", "BUSCAR"))
        self.label_114.setText(_translate("MainWindow", "NC:"))
        self.btn_editarInv.setText(_translate("MainWindow", "EDITAR"))
        self.btn_alterarInv.setText(_translate("MainWindow", "ALTERAR"))
        self.btn_conclusao.setText(_translate("MainWindow", "CONCLUIR"))
        self.btn_cancela_investiga.setText(_translate("MainWindow", "CANCELAR"))
        self.label_31.setText(_translate("MainWindow", "Status NC"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Não iniciada"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Em andamento"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Com Pendências"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Concluído"))
        self.label_30.setText(_translate("MainWindow", "Iniciar Tratativa"))
        self.btn_iniciar_investigacao.setText(_translate("MainWindow", "TRATATIVA"))
        self.label_110.setText(_translate("MainWindow", "NC:"))
        self.label_94.setText(_translate("MainWindow", "Método"))
        self.txt_pessoas.setToolTip(_translate("MainWindow", "como a forma de desenvolver o trabalho influencia o problema?"))
        self.label_98.setText(_translate("MainWindow", "Mão de Obra:"))
        self.txt_pessoas_6.setToolTip(_translate("MainWindow", "como as pessoas envolvidas na atividade influenciam o problema?"))
        self.label_95.setText(_translate("MainWindow", "Máquina:"))
        self.txt_processos.setToolTip(_translate("MainWindow", "como os equipamentos utilizados no processo influenciam o problema?"))
        self.label_99.setText(_translate("MainWindow", "Medida:"))
        self.txt_pessoas_7.setToolTip(_translate("MainWindow", "como as métricas utilizadas para medir o desenvolvimento da atividade influenciam o problema?"))
        self.label_97.setText(_translate("MainWindow", "Material:"))
        self.txt_equipamentos.setToolTip(_translate("MainWindow", "como a qualidade e o tipo dos materiais utilizados influenciam o problema?"))
        self.label_96.setText(_translate("MainWindow", "Meio Ambiente:"))
        self.txt_ambiente.setToolTip(_translate("MainWindow", "como o meio em que a atividade está sendo desenvolvida influencia o problema?"))
        self.label_32.setText(_translate("MainWindow", "PLANO DE AÇÃO"))
        self.label_88.setText(_translate("MainWindow", "O Que?"))
        self.label_89.setText(_translate("MainWindow", "Por que?"))
        self.label_90.setText(_translate("MainWindow", "Quem?"))
        self.label_91.setText(_translate("MainWindow", "Quando?"))
        self.label_92.setText(_translate("MainWindow", "Como?"))
        self.label_86.setText(_translate("MainWindow", "Análise de eficácia"))
        self.label_29.setText(_translate("MainWindow", "INFORMAÇÕES DA NÃO CONFORMIDADE"))
        self.label_19.setText(_translate("MainWindow", "Setor de ocorrência da Não Conformidade:"))
        self.label_26.setText(_translate("MainWindow", "Não Conformidade:"))
        self.label_27.setText(_translate("MainWindow", "Classificação"))
        self.label_28.setText(_translate("MainWindow", "*"))
        self.cb_funcao_3.setToolTip(_translate("MainWindow", "Não Conformidade Maior: Quando um requisito inteiro da norma não é atendido, caracterizando uma falha sistêmica. Também poderão ser emitidas quando falhas existirem nos produtos e for constatado que os mesmos cheguem ao cliente. Caracteriza também o acúmulo de não conformidades menores a um mesmo item normativo ou então a reincidência de uma não conformidade menor identificada em uma auditoria externa anterior;\n"
"\n"
"Não Conformidade Menor: Lapso do controle de um requisito pré-estabelecido. Apesar de não ser grave, indica não cumprimento de um processo específico;\n"
"\n"
"Oportunidade de Melhoria: Melhoria significativa diagnosticada que possa evoluir algum processo e diminuir ou eliminar as não conformidades."))
        self.cb_funcao_3.setItemText(1, _translate("MainWindow", "Oportunidade de Melhoria"))
        self.cb_funcao_3.setItemText(2, _translate("MainWindow", "Maior"))
        self.cb_funcao_3.setItemText(3, _translate("MainWindow", "Menor"))
        self.label_33.setText(_translate("MainWindow", "Prazo para Análise de Eficácia"))
        self.label_34.setText(_translate("MainWindow", "*"))
        self.label_23.setText(_translate("MainWindow", "Abrangência"))
        self.label_35.setText(_translate("MainWindow", "CADASTRO DE USUÁRIOS"))
        self.btn_novoUser.setText(_translate("MainWindow", "N O V O"))
        self.btn_editaUser.setText(_translate("MainWindow", "E D I T A R"))
        self.btn_alterarUser.setText(_translate("MainWindow", "A L T E R A R"))
        self.label_100.setText(_translate("MainWindow", "Nome:"))
        self.label_101.setText(_translate("MainWindow", "Usuário"))
        self.label_102.setText(_translate("MainWindow", "Senha:"))
        self.label_103.setText(_translate("MainWindow", "Perfil:"))
        self.cb_outros_3.setItemText(1, _translate("MainWindow", "NOTIFICADOR"))
        self.cb_outros_3.setItemText(2, _translate("MainWindow", "QUALIDADE"))
        self.cb_outros_3.setItemText(3, _translate("MainWindow", "SESMT"))
        self.cb_outros_3.setItemText(4, _translate("MainWindow", "ADMINISTRADOR"))
        self.label_104.setText(_translate("MainWindow", "Nome:"))
        self.btn_consultaUser.setText(_translate("MainWindow", "C O N S U L T A "))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Usuário"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Perfil"))
        self.btn_nova_rnc.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">CRIAR NOVA NOTIFICAÇÃO</span></p></body></html>"))
        self.btn_nova_rnc.setText(_translate("MainWindow", "N O V O"))
        self.label_81.setText(_translate("MainWindow", "Número da não conformidade"))
        self.btn_pesquisar_rnc.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">PESQUISAR NOTIFICAÇÃO</span></p></body></html>"))
        self.btn_pesquisar_rnc.setText(_translate("MainWindow", "P E S Q U I S A R"))
        self.btn_gerar_pdf.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">CRIAR NOVA NOTIFICAÇÃO</span></p></body></html>"))
        self.btn_gerar_pdf.setText(_translate("MainWindow", "GERAR PDF"))
        self.label_3.setText(_translate("MainWindow", "Setor de Registro:"))
        self.label_4.setText(_translate("MainWindow", "Setor de ocorrência da Não Conformidade:"))
        self.label_21.setText(_translate("MainWindow", "Não Conformidade:"))
        self.label_6.setText(_translate("MainWindow", "Descreva a Não Conformidade"))
        self.txt_descreva.setToolTip(_translate("MainWindow", "Ocorrência: Iniciar o relato com uma breve frase que possa resumir a ocorrência da Não Conformidade constatado, de forma clara, concisa e compreensível;\n"
"\n"
"Evidência Objetiva: Apresentar as evidências objetivas (dados, informações) que dão veracidade a informação;\n"
"\n"
"Contrariedade: Justifica a existência da não conformidade (Contrário normativa Institucional/Informação documentada);\n"
"\n"
"Cláusula e Requisitos: Identificar o requisito pertinente e desenvolver um breve relato sobre o item não atendido. (Se conhecimento da norma ou informação documentada)."))
        self.label_7.setText(_translate("MainWindow", "Turno de ocorrência da Não Conformidade"))
        self.radioButton.setText(_translate("MainWindow", "SN"))
        self.cb_sn.setItemText(1, _translate("MainWindow", "SIM"))
        self.radioButton_2.setText(_translate("MainWindow", "MT"))
        self.cb_mt.setItemText(1, _translate("MainWindow", "SIM"))
        self.label_8.setText(_translate("MainWindow", "Data da Ocorrência da Não Conformidade:"))
        self.label_9.setText(_translate("MainWindow", "Informe a Função:"))
        self.cb_funcao.setToolTip(_translate("MainWindow", "Informe neste campo a função relacionada a não conformidade. Neste Campo não deve ser informada a sua função."))
        self.label_10.setText(_translate("MainWindow", "Se outra função, especifique:"))
        self.label_24.setText(_translate("MainWindow", "Nome do Colaborador:"))
        self.cb_funcao_outros_3.setToolTip(_translate("MainWindow", "Em caso de Não Conformidade NR32, informe o nome do colaborador"))
        self.label_82.setText(_translate("MainWindow", "Evidência:"))
        self.btn_anexar.setText(_translate("MainWindow", "ANEXAR"))
        self.btn_salva_rnc.setText(_translate("MainWindow", "S A L V A R"))
        self.btn_cancela_rnc.setText(_translate("MainWindow", "C A N C E L A "))
        self.btn_anexar.clicked.connect(self.selecionaImagem)

    def selecionaImagem(self):
            fname, _ = QtWidgets.QFileDialog.getOpenFileName(parent=self, caption='Select File',
                                                             directory=QtCore.QDir.currentPath(),
                                                             filter='All Files(*.*);; Images (*.jpg; *.png)',
                                                             initialFilter='Images (*.jpg; *.png)')
            self.label_5.setPixmap(QPixmap(fname))
            self.label_5.setScaledContents(True)

