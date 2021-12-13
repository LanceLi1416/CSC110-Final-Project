""" The entry point of the program """
import os.path
import sys
from zipfile import ZipFile

import requests
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMessageBox

import constants
import ui
from data import process_data


def main():
    # setup files
    unzip_resources()
    get_data()
    # if processed data does not exist, create it
    if not os.path.exists(constants.REAL_DATA_JSON_FILE):
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


def unzip_resources():
    """Unzip the resources files."""
    if not os.path.exists('resources') and os.path.exists('resources.zip'):
        with ZipFile('resources.zip', 'r') as resources_zip:
            resources_zip.extractall()
    else:
        raise FileNotFoundError

    if not os.path.exists('data') and os.path.exists('data.zip'):
        with ZipFile('resources.zip', 'r') as data_zip:
            data_zip.extractall()
    else:
        raise FileNotFoundError


def get_data():
    """Download the dataset."""
    if not os.path.exists('data'):
        os.makedirs('data')
    os.chdir('data')
    if not os.path.exists('COVIDiSTRESS June 17.csv'):
        file = requests.get('https://osf.io/m5s8d/download')
        open('COVIDiSTRESS June 17.csv', 'wb').write(file.content)


if __name__ == '__main__':
    main()
