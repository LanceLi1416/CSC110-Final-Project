""" The entry point of the program """
import sys

import src.ui as ui


def main():
    app = ui.QtWidgets.QApplication(sys.argv)
    window = ui.Ui()
    app.exec_()


if __name__ == '__main__':
    main()
