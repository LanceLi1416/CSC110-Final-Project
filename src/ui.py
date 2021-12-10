import sys

from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget

import src.analoggaugewidget as gauge
import src.constants as constants

from src.data import load_json_data
from src.user import User


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super(MainWindow, self).__init__(*args, **kwargs)

        # -------------------------------------- Data Fields ---------------------------------------
        # Main Layout ---------------------------------------------------------------------------- |
        grid_central = QtWidgets.QGridLayout()
        wgt_central = QtWidgets.QWidget()
        status_bar = self.statusBar()
        # Graphs --------------------------------------------------------------------------------- |
        # wgt_avatar = QtWidgets.QWidget()
        wgt_avatar = QtWidgets.QLabel('USER AVATAR')
        lbl_title = QtWidgets.QLabel('ANXIETY')
        plt_data = PlotWidget()
        # wgt_gauge = QtWidgets.QWidget()
        wgt_gauge = gauge.AnalogGaugeWidget()
        wgt_gauge.setMinimumWidth(300)
        plt_user = PlotWidget()
        # Identity input ------------------------------------------------------------------------- |
        grid_id = QtWidgets.QGridLayout()
        frm_id = QtWidgets.QFrame()

        # Age
        lbl_age = QtWidgets.QLabel("Age")
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
        lbl_marital = QtWidgets.QLabel("Marital status")
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
        self._spi_iso_kids = QtWidgets.QSpinBox()

        # Data storage --------------------------------------------------------------------------- |
        self._user = User(18, 'Other/would rather not say', 'None', 'Not employed', 'Canada', 'no',
                          'Single', 'no', 'Life carries on as usual', 0, 0)
        self.anxiety_data = load_json_data(constants.TEST_DATA_JSON_FILE)

        # ------------------------------- Connect Signals and Slots --------------------------------
        self._spi_age.valueChanged.connect(
            lambda: self._user.set_age(self._spi_age.value()))
        self._cbo_gender.currentIndexChanged.connect(
            lambda: setattr(self._user, 'dem_gender', self._cbo_gender.currentText()))
        self._cbo_edu.currentIndexChanged.connect(
            lambda: setattr(self._user, 'dem_edu', self._cbo_edu.currentText()))
        self._cbo_employment.currentIndexChanged.connect(
            lambda: setattr(self._user, 'dem_employment', self._cbo_employment.currentText()))
        self._cbo_country.currentIndexChanged.connect(
            lambda: setattr(self._user, 'country', self._cbo_country.currentText()))
        self._cbo_expat.currentIndexChanged.connect(
            lambda: setattr(self._user, 'dem_expat', self._cbo_expat.currentText()))
        self._cbo_martial.currentIndexChanged.connect(
            lambda: setattr(self._user, 'dem_marital_status', self._cbo_martial.currentText()))
        self._cbo_risk.currentIndexChanged.connect(
            lambda: setattr(self._user, 'dem_risk_group', self._cbo_risk.currentText()))
        self._cbo_situation.currentIndexChanged.connect(
            lambda: setattr(self._user, 'dem_isolation', self._cbo_situation.currentText()))
        self._spi_iso_adult.valueChanged.connect(
            lambda: self._user.set_isolation_adults(self._spi_iso_adult.value()))
        self._spi_iso_kids.valueChanged.connect(
            lambda: self._user.set_isolation_kids(self._spi_iso_kids.value()))

        # --------------------------------------- Behaviour ----------------------------------------
        # Main Window ---------------------------------------------------------------------------- |
        self.setWindowTitle("Rate Your Anxiety")  # TODO: find a better name
        # Graphs ----------------------------------------------------------------------------------|
        # Identity input ------------------------------------------------------------------------- |
        # Labels - Tips
        lbl_age.setToolTip('What is your age?')
        lbl_gender.setToolTip('What is your gender?')
        lbl_edu.setToolTip('What best describes your level of education?')
        lbl_employment.setToolTip('What is your employment status?')
        lbl_country.setToolTip('What is your current country of residence?')
        lbl_expat.setToolTip('Are you currently living outside of what you consider your home '
                             'country?')
        lbl_marital.setToolTip('What is yoru marital status?')
        lbl_risk.setToolTip('Are you or any of your close relations (family, close friends) in a '
                            'high-risk group for Coronavirus? (e.g. pregnant, elderly or due to a '
                            'pre-existing medical condition)')
        lbl_situation.setToolTip('What best describes your current situation?')
        lbl_iso_adult.setToolTip('If in relative isolation, how many other adults are staying '
                                 'together in the same place as you are?')
        lbl_iso_children.setToolTip('If in relative isolation, how many children under the age of '
                                    '12 are staying together in the same place as you are?')
        # Input fields - Values
        self._spi_age.setRange(18, 110)
        self._cbo_gender.addItems(constants.DEM_GENDER)
        self._cbo_edu.addItems(constants.DEM_EDU)
        self._cbo_employment.addItems(constants.DEM_EMPLOYMENT)
        self._cbo_country.addItems(constants.COUNTRIES)
        self._cbo_expat.addItems(constants.BINARY)
        self._cbo_martial.addItems(constants.DEM_MARITALSTATUS)
        self._cbo_risk.addItems(constants.TERNARY)
        self._cbo_situation.addItems(constants.DEM_ISLOLATION)
        self._spi_iso_adult.setRange(0, 110)
        self._spi_iso_kids.setRange(0, 110)

        # --------------------------------------- Dimensions ---------------------------------------
        # Main Window ---------------------------------------------------------------------------- |
        # self.resize(self._cbo_edu.width() + 600, 720)
        # Identity input ------------------------------------------------------------------------- |
        # Labels
        lbl_age.resize(150, lbl_age.height())
        lbl_gender.resize(150, lbl_gender.height())
        lbl_edu.resize(150, lbl_edu.height())
        lbl_employment.resize(150, lbl_employment.height())
        lbl_country.resize(150, lbl_country.height())
        lbl_expat.resize(150, lbl_expat.height())
        lbl_marital.resize(150, lbl_marital.height())
        lbl_risk.resize(150, lbl_risk.height())
        lbl_situation.resize(150, lbl_situation.height())
        lbl_iso_adult.resize(150, lbl_iso_adult.height())
        lbl_iso_children.resize(150, lbl_iso_children.height())
        # Input fields
        # self._spi_age.resize(150, self._spi_age.height())
        # self._cbo_gender.resize(150, self._cbo_gender.height())
        # self._cbo_edu.resize(150, self._cbo_edu.height())
        # self._cbo_employment.resize(150, self._cbo_employment.height())
        # self._cbo_country.resize(150, self._cbo_country.height())
        # self._cbo_expat.resize(150, self._cbo_expat.height())
        # self._cbo_martial.resize(150, self._cbo_martial.height())
        # self._cbo_risk.resize(150, self._cbo_risk.height())
        # self._cbo_situation.resize(150, self._cbo_situation.height())
        # self._spi_iso_adult.resize(150, self._spi_iso_adult.height())
        # self._spi_iso_kids.resize(150, self._spi_iso_kids.height())
        # ----------------------------------------- Layout -----------------------------------------
        # Identity input ------------------------------------------------------------------------- |
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
        grid_id.addWidget(self._spi_iso_kids, 10, 1)

        frm_id.setLayout(grid_id)

        # Main Layout ---------------------------------------------------------------------------- |
        row = 0
        grid_central.addWidget(frm_id, row, 0)
        grid_central.addWidget(wgt_avatar, row, 1)
        grid_central.addWidget(lbl_title, row, 2)
        row += 1

        # row += 1
        grid_central.addWidget(plt_data, row, 0)
        grid_central.addWidget(wgt_gauge, row, 1)
        grid_central.addWidget(plt_user, row, 2)

        wgt_central.setLayout(grid_central)
        self.setCentralWidget(wgt_central)

        self._spi_age.valueChanged.connect(
            lambda val=self._spi_age.value(): wgt_gauge.updateValue(val))
        wgt_gauge.updateValue(50)
        wgt_gauge.setMinValue(0)
        wgt_gauge.setMaxValue(100)
        wgt_gauge.setMouseTracking(False)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
