from PyQt5.QtWidgets import QApplication
from controller.login import LoginController
from controller.home import HomeController
from controller.curso import CursoController

if __name__ == "__main__":
    app = QApplication([])
    # login = LoginController()
    
    # if login.exec_():
    main = CursoController()
    app.exec_()
      