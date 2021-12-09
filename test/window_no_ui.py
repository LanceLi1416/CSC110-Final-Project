import sys

from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget

import src.constants as constants
from src.user import User


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super(MainWindow, self).__init__(*args, **kwargs)

        # ---------------------------------------- Widgets -----------------------------------------
        # Main Layout ---------------------------------------------------------------------------- |
        grid_central = QtWidgets.QGridLayout()
        wgt_central = QtWidgets.QWidget()
        # Graphics ------------------------------------------------------------------------------- |
        # wgt_avatar = QtWidgets.QWidget()
        wgt_avatar = QtWidgets.QLabel('USER AVATAR')
        lbl_title = QtWidgets.QLabel('ANXIETY')
        plt_data = PlotWidget()
        wgt_gauge = QtWidgets.QWidget()
        plt_user = PlotWidget()
        # Identity input ------------------------------------------------------------------------- |
        grid_id = QtWidgets.QGridLayout()
        frm_id = QtWidgets.QFrame()
        # TODO: review tool tips
        # Age
        lbl_age = QtWidgets.QLabel("Age")
        lbl_age.setToolTip('Your age')
        # Gender
        lbl_gender = QtWidgets.QLabel("Gender")
        # What best describes your level of education?
        lbl_edu = QtWidgets.QLabel("Education")
        # Employment status
        lbl_employment = QtWidgets.QLabel("Employment Status")
        # Country of residence
        lbl_country = QtWidgets.QLabel("Country of Residence")
        # Are you currently living outside of what you consider your home country?
        lbl_expat = QtWidgets.QLabel("Outside Home Country")
        # Marital statue
        lbl_marital = QtWidgets.QLabel("Marital statue")
        # Are you or any of your close relations (family, close friends) in a high-risk group for
        # Coronavirus? (e.g. pregnant, elderly or due to a pre-existing medical condition)
        lbl_risk = QtWidgets.QLabel("Risk Group")
        # What best describes your current situation?
        lbl_situation = QtWidgets.QLabel("Current Situation")
        # If in relative isolation, how many other adults are staying together in the same place as
        # you are?
        lbl_iso_adult = QtWidgets.QLabel("Isolation Adult")
        # If in relative isolation, how many children under the age of 12 are staying together in
        # the same place as you are?
        lbl_iso_children = QtWidgets.QLabel("Isolation Children")

        self._spi_age = QtWidgets.QSpinBox()
        self._cbo_gender = QtWidgets.QComboBox()
        self._cbo_edu = QtWidgets.QComboBox()
        self._cbo_employment = QtWidgets.QComboBox()
        self._cbo_country = QtWidgets.QComboBox()
        self._cbo_expat = QtWidgets.QComboBox()
        self._cbo_martial = QtWidgets.QComboBox()
        self._cbo_risk = QtWidgets.QComboBox()
        self._cbo_situation = QtWidgets.QComboBox()
        self._spi_iso_adult = QtWidgets.QSpinBox()
        self._spi_iso_children = QtWidgets.QSpinBox()

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

        # ------------------------------- Connect Signals and Slots --------------------------------
        # self.connect(self._spi_age, QtWidgets.QSpinBox.valueChanged, print('!!!'))

        # ----------------------------------------- Layout -----------------------------------------
        # Identity input ------------------------------------------------------------------------- |
        self._spi_age.setRange(18, 110)
        self._cbo_gender.addItems(constants.DEM_GENDER)
        self._cbo_edu.addItems(constants.DEM_EDU)
        self._cbo_employment.addItems(constants.DEM_EMPLOYMENT)
        self._cbo_country.addItems(constants.COUNTRY)
        self._cbo_expat.addItems(constants.BINARY)
        self._cbo_martial.addItems(constants.DEM_MARITALSTATUS)
        self._cbo_risk.addItems(constants.TERNARY)
        self._cbo_situation.addItems(constants.DEM_ISLOLATION)
        self._spi_iso_adult.setRange(0, 110)
        self._spi_iso_children.setRange(0, 110)
        # Labels
        grid_id.addWidget(lbl_age, 0, 0)
        grid_id.addWidget(lbl_gender, 1, 0)
        grid_id.addWidget(lbl_edu, 2, 0)
        grid_id.addWidget(lbl_employment, 3, 0)
        grid_id.addWidget(lbl_country, 4, 0)
        grid_id.addWidget(lbl_expat, 5, 0)
        grid_id.addWidget(lbl_marital, 6, 0)
        grid_id.addWidget(lbl_risk, 7, 0)
        grid_id.addWidget(lbl_situation, 8, 0)
        grid_id.addWidget(lbl_iso_adult, 9, 0)
        grid_id.addWidget(lbl_iso_children, 10, 0)
        # Input fields
        grid_id.addWidget(self._spi_age, 0, 1)
        grid_id.addWidget(self._cbo_gender, 1, 1)
        grid_id.addWidget(self._cbo_edu, 2, 1)
        grid_id.addWidget(self._cbo_employment, 3, 1)
        grid_id.addWidget(self._cbo_country, 4, 1)
        grid_id.addWidget(self._cbo_expat, 5, 1)
        grid_id.addWidget(self._cbo_martial, 6, 1)
        grid_id.addWidget(self._cbo_risk, 7, 1)
        grid_id.addWidget(self._cbo_situation, 8, 1)
        grid_id.addWidget(self._spi_iso_adult, 9, 1)
        grid_id.addWidget(self._spi_iso_children, 10, 1)

        frm_id.setLayout(grid_id)

        # Main Layout ---------------------------------------------------------------------------- |
        row = 0
        grid_central.addWidget(frm_id, row, 0)
        grid_central.addWidget(wgt_avatar, row, 1)
        grid_central.addWidget(lbl_title, row, 2)
        row += 1
        grid_central.addWidget(plt_data, row, 0)
        grid_central.addWidget(wgt_gauge, row, 1)
        grid_central.addWidget(plt_user, row, 2)

        wgt_central.setLayout(grid_central)
        self.setCentralWidget(wgt_central)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
