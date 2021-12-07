""" The file associated with the main UI of the project

Naming Conventions:
QLabel      lbl
QComboBox   cbo
QLineEdit   lne

Quotation Rules:
''  for char
""  for string
"""
from PyQt5 import QtCore, QtWidgets, QtGui, uic

import src.constants as constants
from src.user import User


class Ui(QtWidgets.QMainWindow):
    """ The master UI class for the GUI Application """
    # ------------------------------------------ Widgets -------------------------------------------
    _statusBar: QtWidgets.QStatusBar
    _spiAge = QtWidgets.QSpinBox
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

        self._spiAge = self.findChild(QtWidgets.QSpinBox, "spiAge")
        self._spiAge.setRange(18, 110)

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
                          "Not employed",
                          "Canada",
                          False,
                          "Single",
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
        # Disable resize
        # self.setFixedSize(self.size())

        shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(0.5)
        shadow.setOffset(5)
        shadow.setColor(QtGui.QColor.fromRgb(255, 255, 255))
        self._lneState.setGraphicsEffect(shadow)

        self._btnRun = self.findChild(QtWidgets.QPushButton, "btnRun")
        self._btnRun.setStyleSheet(
            """ QPushButton { 
                    background-color: red; 
                    border-style: outset;
                    border-width: 2px;
                    border-radius: 10px;
                    border-color: beige;
                    font: bold 14px;
                    min-width: 10em;
                    padding: 6px; 
                } 
                QPushButton:pressed { 
                    background-color: rgb(224, 0, 0); 
                    border-style: inset; 
                } """)
        self._cboGender.setStyleSheet(
            """ QComboBox:item { 
                    color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(199, 199, 199, 255), stop:1 rgba(99, 99, 99, 255));
                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(99, 99, 99, 255), stop:1 rgba(199, 199, 199, 255));
                }
                QComboBox:item:selected {
                    padding-left: 20px;
                    color: blue;
                    background-color: red;
                }
                QComboBox:item:checked {
                    padding-left: 20px;
                    color: yellow;
                    background-color: blue;
                } """)

    def plot(self):
        pass
