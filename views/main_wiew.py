# main_view.py

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow

class MainView(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("mainwindow.ui", self)