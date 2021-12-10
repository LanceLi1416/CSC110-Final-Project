import sys

import pyqtgraph as pg

from PyQt5 import QtWidgets, QtGui

import src.analoggaugewidget as gauge
import src.constants as constants

from src.data import load_json_data, calculate_extrema
from src.user import User, get_user_percentage


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super(MainWindow, self).__init__(*args, **kwargs)

        # -------------------------------------- Data Fields ---------------------------------------
        # Main Layout ---------------------------------------------------------------------------- |
        grid_central = QtWidgets.QGridLayout()
        wgt_central = QtWidgets.QWidget()
        status_bar = self.statusBar()
        # Graphs --------------------------------------------------------------------------------- |
        # User avatar (cartoon image)
        lbl_avatar = QtWidgets.QLabel('USER AVATAR')
        # Title of program
        lbl_title = QtWidgets.QLabel('ANXIETY')  # TODO: find a font and proper title
        # Data plot
        self._cbo_data_graph = QtWidgets.QComboBox()
        self._plt_data = pg.GraphicsLayoutWidget()
        self._plt_data.setToolTip(
            'Left click to pan, scroll wheel to zoom, right click for more options')
        # Gauge
        self._wgt_gauge = gauge.AnalogGaugeWidget()
        # Specific identity group plot
        self._cbo_user_graph = QtWidgets.QComboBox()
        self._plt_user = QtWidgets.QProgressBar()
        self._plt_user.setRange(0, 100)
        # Identity input ------------------------------------------------------------------------- |
        grid_id = QtWidgets.QGridLayout()
        frm_id = QtWidgets.QFrame()

        self._id_group_labels = [QtWidgets.QLabel() for _ in range(constants.NUMBER_OF_IDENTITIES)]

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
        self._user = User(18, 'Other/would rather not say', 'None', 'Not employed', 'Canada', 'No',
                          'Single', 'No', 'Life carries on as usual', 0, 0)
        self.anxiety_data = load_json_data(constants.REAL_DATA_JSON_FILE)
        self.extrema = calculate_extrema(self.anxiety_data)

        # --------------------------------------- Behaviour ----------------------------------------
        # Main Window ---------------------------------------------------------------------------- |
        self.setWindowTitle("Rate Your Anxiety")  # TODO: find a better name
        # Graphs ----------------------------------------------------------------------------------|
        # Identity input ------------------------------------------------------------------------- |
        self._setup_id_group_labels()
        self._setup_intractable_values()

        # ------------------------------- Connect Signals and Slots --------------------------------
        self._setup_slots()

        # ---------------------------------------- Geometry ----------------------------------------
        # Main Window ---------------------------------------------------------------------------- |
        self.resize(self._cbo_edu.width() + 600, 720)
        self._wgt_gauge.setMinimumWidth(300)
        self._wgt_gauge.setMinimumHeight(300)
        # Identity input ------------------------------------------------------------------------- |
        self._setup_geometry()

        # ----------------------------------------- Layout -----------------------------------------
        # Identity input ------------------------------------------------------------------------- |
        # Labels
        for i in range(constants.NUMBER_OF_IDENTITIES):
            grid_id.addWidget(self._id_group_labels[i], i, 0)
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
        grid_central.addWidget(lbl_avatar, row, 1)
        grid_central.addWidget(lbl_title, row, 2)
        row += 1
        grid_central.addWidget(self._cbo_data_graph, row, 0)
        grid_central.addWidget(self._cbo_user_graph, row, 2)
        row += 1
        grid_central.addWidget(self._plt_data, row, 0)
        grid_central.addWidget(self._wgt_gauge, row, 1)
        grid_central.addWidget(self._plt_user, row, 2)

        wgt_central.setLayout(grid_central)
        self.setCentralWidget(wgt_central)

        # initialize graphs
        self._plot_data()
        self._update_gauge()
        self._plot_user()

    def _setup_id_group_labels(self):
        tool_tips = [
            'What is your age?',
            'What is your gender?',
            'What best describes your level of education?',
            'What is your employment status?',
            'What is your current country of residence?',
            'Are you currently living outside of what you consider your home country?',
            'What is your marital status?',
            'Are you or any of your close relations (family, close friends) in a high-risk group '
            'for Coronavirus? (e.g. pregnant, elderly or due to a pre-existing medical condition)',
            'What best describes your current situation?',
            'If in relative isolation, how many other adults are staying together in the same '
            'place as you are?',
            'If in relative isolation, how many children under the age of 12 are staying together '
            'in the same place as you are?',
        ]
        for i in range(constants.NUMBER_OF_IDENTITIES):
            self._id_group_labels[i].setText(constants.IDENTITY_GROUP_NAMES[i])
            self._id_group_labels[i].setToolTip(tool_tips[i])

    def _setup_intractable_values(self):
        """Initialize the values for the intractable widgets"""
        # Input fields
        self._spi_age.setRange(18, 110)
        self._cbo_gender.addItems(constants.DEM_GENDER)
        self._cbo_edu.addItems(constants.DEM_EDU)
        self._cbo_employment.addItems(constants.DEM_EMPLOYMENT)
        self._cbo_country.addItems(constants.COUNTRIES)
        self._cbo_expat.addItems(constants.EXPAT)
        self._cbo_martial.addItems(constants.DEM_MARITAL_STATUS)
        self._cbo_risk.addItems(constants.RISK_GROUP)
        self._cbo_situation.addItems(constants.DEM_ISOLATION)
        self._spi_iso_adult.setRange(0, 110)
        self._spi_iso_kids.setRange(0, 110)
        # Graphs
        self._cbo_data_graph.addItems(constants.IDENTITY_GROUP_NAMES)
        self._cbo_user_graph.addItems(constants.IDENTITY_GROUP_NAMES)

    def _setup_geometry(self):
        """Set up the sizes of the widgets"""
        for i in range(constants.NUMBER_OF_IDENTITIES):
            self._id_group_labels[i].resize(
                150,
                self._id_group_labels[i].height()
            )

    def _setup_slots(self):
        """Connect components to slots"""
        # Update self._user
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
        # Update Gauge
        self._spi_age.valueChanged.connect(self._update_gauge)
        self._cbo_gender.currentIndexChanged.connect(self._update_gauge)
        self._cbo_edu.currentIndexChanged.connect(self._update_gauge)
        self._cbo_employment.currentIndexChanged.connect(self._update_gauge)
        self._cbo_country.currentIndexChanged.connect(self._update_gauge)
        self._cbo_expat.currentIndexChanged.connect(self._update_gauge)
        self._cbo_martial.currentIndexChanged.connect(self._update_gauge)
        self._cbo_risk.currentIndexChanged.connect(self._update_gauge)
        self._cbo_situation.currentIndexChanged.connect(self._update_gauge)
        self._spi_iso_adult.valueChanged.connect(self._update_gauge)
        self._spi_iso_kids.valueChanged.connect(self._update_gauge)
        # Update graph
        self._cbo_data_graph.currentIndexChanged.connect(self._plot_data)
        # Update progress bar
        self._cbo_user_graph.currentIndexChanged.connect(self._plot_user)
        self._spi_age.valueChanged.connect(self._plot_user)
        self._cbo_gender.currentIndexChanged.connect(self._plot_user)
        self._cbo_edu.currentIndexChanged.connect(self._plot_user)
        self._cbo_employment.currentIndexChanged.connect(self._plot_user)
        self._cbo_country.currentIndexChanged.connect(self._plot_user)
        self._cbo_expat.currentIndexChanged.connect(self._plot_user)
        self._cbo_martial.currentIndexChanged.connect(self._plot_user)
        self._cbo_risk.currentIndexChanged.connect(self._plot_user)
        self._cbo_situation.currentIndexChanged.connect(self._plot_user)
        self._spi_iso_adult.valueChanged.connect(self._plot_user)
        self._spi_iso_kids.valueChanged.connect(self._plot_user)

    def _setup_gauge(self):
        """Set up the gauge widget"""
        self._wgt_gauge.setMinValue(0)
        self._wgt_gauge.setMaxValue(100)

    def _update_gauge(self):
        """Calculate the user's anxiety score, then update the gauge"""
        self._user.estimate_anxiety_score(self.anxiety_data)
        self._wgt_gauge.updateValue((self._user.get_anxiety_score() - self.extrema[0]) /
                                    (self.extrema[1] - self.extrema[0]) * 100)

    def _plot_data(self) -> None:
        """Plots the data from the csv file"""
        self._plt_data.clear()  # clear current graph

        id_index, id_group = self._cbo_data_graph.currentIndex(), self._cbo_data_graph.currentText()

        bar_graph = pg.BarGraphItem(
            y=[i for i in range(len(constants.IDENTITY_GROUP_OPTIONS_LIST[id_index]))],
            x0=0,
            width=list(self.anxiety_data[id_index].values()),
            height=0.75, brush=constants.PLOT_COLOR
        )

        string_axis = pg.AxisItem(orientation='left')  # Textual x-axis
        string_axis.setTicks(
            [dict(enumerate(constants.IDENTITY_GROUP_OPTIONS_LIST[id_index])).items()])

        plot_item = self._plt_data.addPlot(axisItems={'left': string_axis})
        plot_item.setTitle(id_group)
        plot_item.addItem(bar_graph)

    def _plot_user(self) -> None:
        """Plots the user's ranking"""
        self._user.estimate_anxiety_score(self.anxiety_data)
        val = get_user_percentage(
            self._user,
            self._cbo_user_graph.currentText(),
            self.anxiety_data
        )
        self._plt_user.setValue(int(val))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
