# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 450)
        self.actiondark_amber = QAction(MainWindow)
        self.actiondark_amber.setObjectName(u"actiondark_amber")
        self.actiondark_blue = QAction(MainWindow)
        self.actiondark_blue.setObjectName(u"actiondark_blue")
        self.actionDark_red = QAction(MainWindow)
        self.actionDark_red.setObjectName(u"actionDark_red")
        self.actionDark_blue = QAction(MainWindow)
        self.actionDark_blue.setObjectName(u"actionDark_blue")
        self.actionLight_Yellow = QAction(MainWindow)
        self.actionLight_Yellow.setObjectName(u"actionLight_Yellow")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-1, -1, 800, 450))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 400, 50))
        self.label.setStyleSheet(u"font: 86 100px \"Courier\";")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 60, 221, 61))
        self.label_2.setStyleSheet(u"font: 75 10px \"Palatino Linotype\";")
        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 70, 651, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 150, 161, 41))
        self.radioButton = QRadioButton(self.frame)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(50, 386, 101, 31))
        self.label_21 = QLabel(self.frame)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(240, 140, 221, 30))
        self.label_21.setStyleSheet(u"font: 75 10px \"Palatino Linotype\";")
        self.lineEdit = QDateEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(240, 170, 200, 20))
        self.label_22 = QLabel(self.frame)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(240, 200, 221, 30))
        self.label_22.setStyleSheet(u"font: 75 10px \"Palatino Linotype\";")
        self.lineEdit1 = QDateEdit(self.frame)
        self.lineEdit1.setObjectName(u"lineEdit1")
        self.lineEdit1.setGeometry(QRect(240, 230, 200, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 777, 21))
        self.menuSelect_Theme = QMenu(self.menuBar)
        self.menuSelect_Theme.setObjectName(u"menuSelect_Theme")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuSelect_Theme.menuAction())
        self.menuSelect_Theme.addAction(self.actionDark_red)
        self.menuSelect_Theme.addAction(self.actionDark_blue)
        self.menuSelect_Theme.addAction(self.actionLight_Yellow)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actiondark_amber.setText(QCoreApplication.translate("MainWindow", u"dark_amber", None))
        self.actiondark_blue.setText(QCoreApplication.translate("MainWindow", u"dark_blue", None))
        self.actionDark_red.setText(QCoreApplication.translate("MainWindow", u"Dark_red", None))
        self.actionDark_blue.setText(QCoreApplication.translate("MainWindow", u"Dark_blue", None))
        self.actionLight_Yellow.setText(QCoreApplication.translate("MainWindow", u"Light_Yellow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"StockModel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Select a date range and stock symbol", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Generate Models", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Start Date", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"End Date", None))
        self.menuSelect_Theme.setTitle(QCoreApplication.translate("MainWindow", u"Select Theme", None))
    # retranslateUi

