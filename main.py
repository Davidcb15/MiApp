import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from windows.main_ui import Ui_MainWindow  
from windows.register_ui import Ui_Register
from windows.login_ui import Ui_Login
from windows.recipes_ui import Ui_recipes

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())