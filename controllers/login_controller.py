from PyQt6 import QtWidgets, uic
import sys




class LoginController :
    def __init__(self,window,model):
        self.window = window
        self.model = model
        self.window.btn_login.clicked.connect(self.handle_login)

        def handle_login(self):
            print("login button cliked ")