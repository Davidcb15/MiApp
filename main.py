import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from windows.main_ui import Ui_MainWindow  
from windows.register_ui import Ui_Register
from windows.login_ui import Ui_Login
from windows.recipes_ui import Ui_recipes

# Crear la base de datos al iniciar la aplicación
from database import crear_db
crear_db()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Conecta los botones a sus respectivas funciones para abrir las ventanas de login y registro
        self.ui.btn_LogIn.clicked.connect(self.open_login)
        self.ui.btn_Register.clicked.connect(self.open_register)

        # Inicializa las ventanas de login y registro como None, se crearán al abrirlas por primera vez
        self.login_window = None
        self.register_window = None

    def open_login(self):
        """Show the login window and hide main window."""
        if self.login_window is None:
            self.login_window = QMainWindow()
            self.login_ui = Ui_Login()
            self.login_ui.setupUi(self.login_window)
            # Opcional: conecta señales desde la ventana de login aquí
        self.login_window.show()
        self.hide()

    def open_register(self):
        """Show the register window and hide main window."""
        if self.register_window is None:
            self.register_window = QMainWindow()
            self.register_ui = Ui_Register()
            self.register_ui.setupUi(self.register_window)
            # Conectar el botón de registro a la función que maneja el proceso de registro
            self.register_ui.btn_register.clicked.connect(self.handle_registration)

            # Conectar los checkboxes para que se comporten como opciones mutuamente excluyentes
            # dieta
            self.register_ui.chk_dietRegisterY.toggled.connect(
                lambda checked: self.register_ui.chk_dietRegisterN.setChecked(not checked)
            )
            self.register_ui.chk_dietRegisterN.toggled.connect(
                lambda checked: self.register_ui.chk_dietRegisterY.setChecked(not checked)
            )
            # vegano
            self.register_ui.chk_veganRegisterY.toggled.connect(
                lambda checked: self.register_ui.chk_veganRegisterN.setChecked(not checked)
            )
            self.register_ui.chk_veganRegisterN.toggled.connect(
                lambda checked: self.register_ui.chk_veganRegisterY.setChecked(not checked)
            )
            # vegetariano
            self.register_ui.chk_vegetarianRegisterY.toggled.connect(
                lambda checked: self.register_ui.chk_vegetarianRegisterN.setChecked(not checked)
            )
            self.register_ui.chk_vegetarianRegisterN.toggled.connect(
                lambda checked: self.register_ui.chk_vegetarianRegisterY.setChecked(not checked)
            )
        self.register_window.show()
        self.hide()

    def handle_registration(self):
        """Procesa los datos ingresados en el formulario de registro."""
        user = self.register_ui.txt_userRegister.toPlainText().strip()
        pwd1 = self.register_ui.txt_pwdRegister.toPlainText()
        pwd2 = self.register_ui.txt_pwdRegister2.toPlainText()

        if not user or not pwd1 or not pwd2:
            QMessageBox.warning(self.register_window, "Datos incompletos", "Debe completar todos los campos")
            return
        if pwd1 != pwd2:
            QMessageBox.warning(self.register_window, "Contraseñas", "Las contraseñas no coinciden")
            return

        try:
            conn = sqlite3.connect("usuarios.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuarios (usuario, password) VALUES (?, ?)", (user, pwd1))
            conn.commit()
            conn.close()
        except sqlite3.IntegrityError:
            QMessageBox.warning(self.register_window, "Error", "El nombre de usuario ya existe")
            return

        QMessageBox.information(self.register_window, "Registro", "Usuario creado correctamente")
        # Después de registrar, cerramos la ventana de registro y volvemos a la de login
        self.register_window.close()
        self.open_login()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())