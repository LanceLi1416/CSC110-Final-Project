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
    process_data_if_not_exist()

    app = QApplication(sys.argv)
    # Set application icon
    app_icon = QIcon()
    app_icon.addFile('./resources/img/icons/Bubble.png')
    app.setWindowIcon(app_icon)

    window = ui.MainWindow()
    window.show()

    # Prompt message showing how to use this application
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
        print('Unzipping resources.zip')
        with ZipFile('resources.zip', 'r') as resources_zip:
            resources_zip.extractall()
        print('Finished unzipping resources.zip')

    if not os.path.exists('data') and os.path.exists('data.zip'):
        print('Unzipping data.zip')
        with ZipFile('resources.zip', 'r') as data_zip:
            data_zip.extractall()
        print('Finished unzipping data.zip')


def get_data():
    """Download the dataset."""
    if not os.path.exists('data'):
        os.makedirs('data')
    os.chdir('data')
    if not os.path.exists('COVIDiSTRESS June 17.csv'):
        print('Downloading dataset...')
        file = requests.get('https://osf.io/m5s8d/download')
        open('COVIDiSTRESS June 17.csv', 'wb').write(file.content)
        print('Finished downloading dataset!')
    os.chdir('../')


def process_data_if_not_exist():
    """If real_data.json does not exist, create it."""
    if not os.path.exists(constants.REAL_DATA_JSON_FILE):
        print('Processing data...')
        process_data(constants.REAL_DATA_CSV_FILE, constants.REAL_DATA_JSON_FILE)
        print('Finished processing data!')


if __name__ == '__main__':
    main()
