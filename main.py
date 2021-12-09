""" The entry point of the program """
import sys

from PyQt5.QtWidgets import QApplication

import src.ui as ui


def main():
    app = QApplication(sys.argv)
    window = ui.MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
