# main.py

import sys
from PyQt6.QtWidgets import QApplication
from views import MainView
from controllers import main_controller

def main():
    app = QApplication(sys.argv)

    view = MainView()
    controller = MainController(view)

    view.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()