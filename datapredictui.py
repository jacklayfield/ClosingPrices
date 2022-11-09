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
        self.dateStart.editingFinished.connect(self.test)
        self.dateEnd.editingFinished.connect(self.test1)

        self.startDate = ""
        self.endDate = ""

        apply_stylesheet(app, theme='dark_purple.xml')

    def generate_models(self):
        print("Epic model")
        datapredict.generate(self.startDate, self.endDate)
    
    def test(self):
        value = self.dateStart.date()
        print(str(value))
        partitioned = str(value).split("(")
        print(partitioned)
        trimmedEnd = partitioned[1].split(")")
        print(trimmedEnd)
        parsedDate = trimmedEnd[0]
        ymd = parsedDate.split(",")
        year = ymd[0].strip()
        month = ymd[1].strip()
        day = ymd[2].strip()

        print("year = " + year + " month = " + month + " day = " + day)

        self.startDate = str(year) + "-" + str(month) + "-" + str(day)

        print(self.startDate)


    def test1(self):
        value = self.dateEnd.date()
        print(str(value))
        partitioned = str(value).split("(")
        print(partitioned)
        trimmedEnd = partitioned[1].split(")")
        print(trimmedEnd)
        parsedDate = trimmedEnd[0]
        ymd = parsedDate.split(",")
        year = ymd[0].strip()
        month = ymd[1].strip()
        day = ymd[2].strip()

        print("year = " + year + " month = " + month + " day = " + day)

        self.endDate = str(year) + "-" + str(month) + "-" + str(day)

        print(self.endDate)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec_()
