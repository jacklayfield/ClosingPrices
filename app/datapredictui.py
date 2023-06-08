from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.uic import loadUi
import sys
import datapredict

# import the themes
from qt_material import *


class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()

        loadUi("window.ui", self)

        self.setFixedSize(self.size())

        self.pushButton.clicked.connect(self.generateModels)
        self.dateStart.editingFinished.connect(self.dateStartBehavior)
        self.dateEnd.editingFinished.connect(self.dateEndBehavior)
        self.stockSymbol.editingFinished.connect(self.stockSymbolBehavior)
        self.darkMode.triggered.connect(self.darkModeBehavior)
        self.lightMode.triggered.connect(self.lightModeBehavior)
        

        self.startDate = ""
        self.endDate = ""
        self.stock = ""

        apply_stylesheet(app, theme='dark_purple.xml')

    def generateModels(self):
        res = datapredict.generate(self.startDate, self.endDate, self.stock)
        if res == "er_sq":
            msg = QMessageBox()
            msg.setWindowTitle("Stock Quote Error")
            msg.setText("Could not gather stock quote. Please ensure the stock symbol and date range are valid and try again.")
            msg.exec_()

    
    def dateStartBehavior(self):
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

        if int(month) < 10 : month = "0" + str(month)
        if int(day) < 10 : day = "0" + str(day)

        print(month, day)

        print("year = " + year + " month = " + month + " day = " + day)

        self.startDate = str(year) + "-" + str(month) + "-" + str(day)

        print(self.startDate)


    def dateEndBehavior(self):
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

        if int(month) < 10 : month = "0" + str(month)
        if int(day) < 10 : day = "0" + str(day)

        print("year = " + year + " month = " + month + " day = " + day)

        self.endDate = str(year) + "-" + str(month) + "-" + str(day)

        print(self.endDate)
    
    def stockSymbolBehavior(self):
        value = self.stockSymbol.text()
        stockFormatted = value.upper().strip()
        print(stockFormatted)
        self.stock = stockFormatted

    def darkModeBehavior(self):
        apply_stylesheet(app, theme='dark_purple.xml')

    def lightModeBehavior(self):
        apply_stylesheet(app, theme='light_purple.xml')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec_()
