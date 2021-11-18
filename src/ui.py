""" The file associated with the main UI of the project

Naming Conventions:
QLabel      lbl
QComboBox   cbo
QLineEdit   lne
"""
from PyQt5 import QtCore, QtWidgets, uic

import src.constants as constants


class Ui(QtWidgets.QMainWindow):
    """ The master UI class for the GUI Application """

    def __init__(self, *args, **kwargs) -> None:
        super(Ui, self).__init__(*args, **kwargs)
        # Load the UI file
        uic.loadUi('src/ui/MainWindow.ui', self)

        # ---------------------------------------- Widgets -----------------------------------------
        self.statusBar = self.statusBar()
        # https://www.pythonguis.com/tutorials/embed-pyqtgraph-custom-widgets-qt-app/
        self.cboAge = self.findChild(QtWidgets.QComboBox, 'cboAge')
        self.cboAge.addItems(str(_) for _ in range(1, 111))

        self.cboGender = self.findChild(QtWidgets.QComboBox, 'cboGender')
        self.cboGender.addItems(constants.DEM_GENDER)

        self.cboEducation = self.findChild(QtWidgets.QComboBox, 'cboEducation')
        self.cboEducation.addItems(constants.DEM_EDU)

        self.cboEmployment = self.findChild(QtWidgets.QComboBox, 'cboEmployment')
        self.cboEmployment.addItems(constants.DEM_EMPLOYMENT)

        self.cboCountry = self.findChild(QtWidgets.QComboBox, 'cboCountry')
        self.cboCountry.addItems(constants.COUNTRY)

        self.cboExpat = self.findChild(QtWidgets.QComboBox, 'cboExpat')
        self.cboExpat.addItems(constants.BINARY)

        self.lneState = self.findChild(QtWidgets.QLineEdit, 'lneState')
        self.lneState.setPlaceholderText('the state / province you live in')

        # ------------------------------------ Display Settings ------------------------------------
        # Title
        self.setWindowTitle("Rate Your Anxiety")  # TODO: fina a proper name
        # Copyright message in status bar
        lblTemp_message = QtWidgets.QLabel(
            "Fardin Faruk, Sharon Hsieh, Sinan Li, and Jeffery Zhan \u00A9 2021")
        lblTemp_message.setAlignment(QtCore.Qt.AlignCenter)
        self.statusBar.addWidget(lblTemp_message, 1)
        self.show()

    def plot(self):
        pass
