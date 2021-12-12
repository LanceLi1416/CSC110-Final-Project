""" The entry point of the program """
import sys

from PyQt5.QtWidgets import QApplication, QMessageBox

import src.ui as ui


def main():
    app = QApplication(sys.argv)
    window = ui.MainWindow()
    window.show()

    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle('Instructions')
    msg.setText('Enter your information in the fields provided to receive an estimate of your '
                'likelihood of experiencing anxiety due to COVID-19. To see the trend of the '
                'general population, refer to the graph on the bottom left.')
    msg.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
