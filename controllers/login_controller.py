from PyQt6 import QtWidgets, uic




class LoginController :
    def __init__(self,window,model):
        self.window = window
        self.model = model
        self.window.btn_login.clicked.connect(self.handle_login)

        def handle_login(self):
            username = self.window.txt_username()
            password = self.window.txt_passaword()
            if username == " admin" and password == "123":
                self.window.login_succesful.emit()
                print("login corecto")
            else:
                #print("login incorrecto")
                QtWidgets.QMessageBox.warning(
                    self.window,
                    "abarrotes tec -error",
                    "login incorrecto"
                )

            print("login button cliked ")