""" The entry point of the program """
import os.path
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMessageBox

import constants
import ui
from data import process_data


def main():
    # if data does not exist, create it
    if not os.path.isfile(constants.REAL_DATA_JSON_FILE):
        process_data(constants.REAL_DATA_CSV_FILE, constants.REAL_DATA_JSON_FILE)

    app = QApplication(sys.argv)

    # Set application icon
    app_icon = QIcon()
    app_icon.addFile('./img/icons/Bubble.png')
    app.setWindowIcon(app_icon)

    window = ui.MainWindow()
    window.show()

    # Prompt message showing how to usd this application
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
