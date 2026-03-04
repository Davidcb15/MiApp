# main_controller.py
import sqlite3
from login_view import LoginView
from register_view import RegisterView

class MainController:

    def __init__(self, view):
        self.view = view
        self.connect_signals()

    def connect_signals(self):
        self.view.btn_LogIn.clicked.connect(self.open_login)
        self.view.btn_Register.clicked.connect(self.open_register)

    def open_login(self):
        self.login_window = LoginView()
        self.login_window.show()
        self.view.close()

    def open_register(self):
        self.register_window = RegisterView()
        self.register_window.show()
        self.view.close()