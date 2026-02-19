import sys
from PyQt6 import QtWidgets
from ..QTDesign.login import Ui_Login

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

Ui_Login().setupUi(MainWindow)
MainWindow.show()

sys.exit(app.exec())  