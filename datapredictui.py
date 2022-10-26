import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from qt_material import apply_stylesheet


########################################################################

app = QApplication()

apply_stylesheet(app, theme='dark_cyan.xml')

frame = QUiLoader().load('window.ui')
frame.show()

app.exec()
