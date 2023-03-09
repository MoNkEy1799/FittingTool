import sys

from PyQt5.QtWidgets import QApplication
from CustomWidgets import MainWindow

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())