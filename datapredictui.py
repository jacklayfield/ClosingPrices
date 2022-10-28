import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from qt_material import apply_stylesheet


########################################################################


def main():
    app = QApplication()

    apply_stylesheet(app, theme='dark_purple.xml')

    frame = QUiLoader().load('window.ui')
    frame.show()

    app.exec()


if __name__ == "__main__":
    main()
