from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
import sys
import datapredict

# import the themes
from qt_material import *


class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()

        loadUi("window.ui", self)

        self.pushButton.clicked.connect(self.generate_models)

        apply_stylesheet(app, theme='dark_purple.xml')

    def generate_models(self):
        print("Epic model")
        datapredict.generate()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec_()
