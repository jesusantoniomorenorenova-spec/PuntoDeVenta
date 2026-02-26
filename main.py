from PyQt6 import QtWidgets , uic
import sys
from controllers.login_controller import LoginController
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QPalette

#pip install pyqt6-tools

class Login (QtWidgets.QMainWindow):
    login_sucessfull = pyqtSignal()
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/login.ui",self)
        self.controller = LoginController(self,self)
        self.apply_theme()

    def apply_theme(self):
        is_dark = self.palette().color(QPalette.ColorRole.Window).lightness() <128
        print(f"  dark: {is_dark}")

class Sells (QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/main.ui",self)


class AppManager:
    def __init__(self):
        self.login_window=Login()
        self.sell_window = None
        self.sell_window = Sells()
        self.login_window.login_sucessfull.connect(self.show_main_window)

        self.login_window.show()
    def show_main_window(self):
        self.sell_window.show()#mostrar ventana de muestra
        self.login_window.close()#ceramos ventana

app = QtWidgets.QApplication(sys.argv)
manager = AppManager()
sys.exit(app.exec())