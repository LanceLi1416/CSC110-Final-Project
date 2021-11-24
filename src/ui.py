""" The file associated with the main UI of the project

Naming Conventions:
QLabel      lbl
QComboBox   cbo
QLineEdit   lne

Quotation Rules:
''  for char
""  for string
"""
from PyQt5 import QtCore, QtWidgets, uic

import src.constants as constants
from src.user import User


class Ui(QtWidgets.QMainWindow):
    """ The master UI class for the GUI Application """
    # ------------------------------------------ Widgets -------------------------------------------
    _statusBar: QtWidgets.QStatusBar
    _cboAge: QtWidgets.QComboBox
    _cboGender: QtWidgets.QComboBox
    _cboEducation: QtWidgets.QComboBox
    _cboEmployment: QtWidgets.QComboBox
    _cboCountry: QtWidgets.QComboBox
    _cboExpat: QtWidgets.QComboBox
    _lneState: QtWidgets.QLineEdit

    # -------------------------------------------- Data --------------------------------------------
    _user: User

    def __init__(self, *args, **kwargs) -> None:
        super(Ui, self).__init__(*args, **kwargs)
        # Load the UI file
        uic.loadUi('src/ui/MainWindow.ui', self)

        # ---------------------------------------- Widgets -----------------------------------------
        # PyCharm will display error message saying "Expected type '...', got 'Ui' instead".
        # This is normal. Please ignore them.

        self._statusBar = self.statusBar()

        self._cboAge = self.findChild(QtWidgets.QComboBox, "cboAge")
        self._cboAge.addItems(str(_) for _ in range(18, 111))

        self._cboGender = self.findChild(QtWidgets.QComboBox, "cboGender")
        self._cboGender.addItems(constants.DEM_GENDER)

        self._cboEducation = self.findChild(QtWidgets.QComboBox, "cboEducation")
        self._cboEducation.addItems(constants.DEM_EDU)

        self._cboEmployment = self.findChild(QtWidgets.QComboBox, "cboEmployment")
        self._cboEmployment.addItems(constants.DEM_EMPLOYMENT)

        self._cboCountry = self.findChild(QtWidgets.QComboBox, "cboCountry")
        self._cboCountry.addItems(constants.COUNTRY)

        self._cboExpat = self.findChild(QtWidgets.QComboBox, "cboExpat")
        self._cboExpat.addItems(constants.BINARY)

        self._lneState = self.findChild(QtWidgets.QLineEdit, "lneState")
        self._lneState.setPlaceholderText('the state / province you live in')

        # https://www.pythonguis.com/tutorials/embed-pyqtgraph-custom-widgets-qt-app/
        self._graphWidget = self.findChild(QtWidgets.QWidget, "graphWidget")

        # ------------------------------------------ Data ------------------------------------------
        self._user = User(18,
                          "Other / would rather not say",
                          "None",
                          "None",
                          "Not employed",
                          "Canada",
                          False,
                          "",
                          "Single",
                          0,
                          "no",
                          "Life carries on as usual",
                          0,
                          0)

        # ------------------------------------ Display Settings ------------------------------------
        # Title
        self.setWindowTitle("Rate Your Anxiety")  # TODO: fina a proper name
        # Copyright message in status bar
        lbl_copyright = QtWidgets.QLabel(
            "Fardin Faruk, Sharon Hsieh, Sinan Li, and Jeffery Zhan \u00A9 2021")
        lbl_copyright.setAlignment(QtCore.Qt.AlignCenter)
        self._statusBar.addWidget(lbl_copyright, 1)

    def plot(self):
        pass
