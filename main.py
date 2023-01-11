import sys

from PyQt5 import QtWidgets
from PyQt5.uic import loadUi

# from url import *
from inicial import *




if __name__== "__main__":
      app = QtWidgets.QApplication(sys.argv)
      Form = QtWidgets.QWidget()
      ui = Ui_MainWindow()
      ui.setupUi(Form)
      Form.show()
      sys.exit(app.exec())
