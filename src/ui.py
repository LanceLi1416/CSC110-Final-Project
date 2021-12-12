import os
import platform

import pyqtgraph as pg
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap

from src import constants
from src.data import load_json_data, calculate_extrema
from src.gauge import GaugeWidget
from src.user import User, get_user_percentage


# TODO: pacify python_ta
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
        self._lbl_avatar = QtWidgets.QLabel('USER AVATAR')
        # Title of program
        lbl_title = self._create_title_label()
        # Data plot
        self._cbo_data_graph = QtWidgets.QComboBox()
        self._plt_data = pg.GraphicsLayoutWidget()
        self._plt_data.setToolTip(
            'Left click to pan, middle button scroll to zoom, right click for more options')
        # Gauge
        self._wgt_gauge = GaugeWidget()
        # Specific identity group plot
        self._cbo_user_graph = QtWidgets.QComboBox()
        self._pgb_user = QtWidgets.QProgressBar()
        self._lbl_textual_output = QtWidgets.QLabel()
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
        self._user = User(18, 'Male', 'None', 'Not employed', 'Afghanistan', 'Yes', 'Single', 'Yes',
                          'Life carries on as usual', 0, 0)
        self.anxiety_data = load_json_data(constants.REAL_DATA_JSON_FILE)
        self.extrema = calculate_extrema(self.anxiety_data)

        # --------------------------------------- Behaviour ----------------------------------------
        # Main Window ---------------------------------------------------------------------------- |
        self.setWindowTitle(constants.TITLE)
        # Graphs ----------------------------------------------------------------------------------|
        self._pgb_user.setRange(0, 100)
        self._lbl_avatar.setAlignment(QtCore.Qt.AlignCenter)
        self._lbl_textual_output.setWordWrap(True)
        # Identity input ------------------------------------------------------------------------- |
        self._setup_id_group_labels()
        self._setup_intractable_values()
        self._cbo_data_graph.setToolTip(
            'Select the identity group whose data you want to see.')
        self._cbo_user_graph.setToolTip(
            'Select the identity group of which you would like to compare yourself with.')
        # Status bar
        lbl_status_bar = QtWidgets.QLabel(
            ' * Hover your mouse over the components for more details.')
        lbl_status_bar.setFont(
            QtGui.QFont(constants.BODY_FONT_NAME, constants.BODY_FONT_SIZE))
        status_bar.addWidget(lbl_status_bar)

        # ------------------------------- Connect Signals and Slots --------------------------------
        self._setup_slots()

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
        grid_central.addWidget(frm_id, 0, 0, 3, 1)
        grid_central.addWidget(lbl_title, 0, 1, 1, 2)
        grid_central.addWidget(self._lbl_avatar, 1, 1, 2, 2)

        grid_central.addWidget(self._cbo_data_graph, 3, 0, 1, 1)
        grid_central.addWidget(self._wgt_gauge, 3, 1, 3, 1)
        grid_central.addWidget(self._cbo_user_graph, 3, 2, 1, 1)

        grid_central.addWidget(self._plt_data, 4, 0, 2, 1)
        grid_central.addWidget(self._pgb_user, 4, 2, 1, 1)
        grid_central.addWidget(self._lbl_textual_output, 5, 2, 1, 1)

        wgt_central.setLayout(grid_central)
        self.setCentralWidget(wgt_central)

        # ---------------------------------------- Geometry ----------------------------------------
        self._setup_geometry()

        # ------------------------------------------ Look ------------------------------------------
        # Set style
        self._setup_fonts()
        self._setup_color()

        self._plot_data()
        self._update_output()

    def _create_title_label(self) -> QtWidgets.QLabel:
        """Creates and customized tha title label"""
        lbl_title = QtWidgets.QLabel(constants.TITLE)
        lbl_title.setWordWrap(True)
        lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        QtGui.QFontDatabase.addApplicationFont(
            os.path.join(os.path.dirname(__file__), '../', constants.TITLE_FONT_PATH)
        )
        lbl_title.setFont(QtGui.QFont(constants.TITLE_FONT_NAME, constants.TITLE_FONT_SIZE))
        return lbl_title

    def _setup_fonts(self) -> None:
        """Set customized fonts to all the widgets"""
        QtGui.QFontDatabase.addApplicationFont(
            os.path.join(os.path.dirname(__file__), '../', constants.BODY_FONT_PATH)
        )
        # Labels
        for i in range(constants.NUMBER_OF_IDENTITIES):
            self._id_group_labels[i].setFont(
                QtGui.QFont(constants.BODY_FONT_NAME, constants.BODY_FONT_SIZE))
        # Intractable
        self._spi_age.setFont(
            QtGui.QFont(constants.BODY_FONT_NAME, constants.BODY_FONT_SIZE))
        self._cbo_gender.setFont(
            QtGui.QFont(constants.BODY_FONT_NAME, constants.BODY_FONT_SIZE))
        self._cbo_edu.setFont(
            QtGui.QFont(constants.BODY_FONT_NAME, constants.BODY_FONT_SIZE))
        self._cbo_employment.setFont(
            QtGui.QFont(constants.BODY_FONT_NAME, constants.BODY_FONT_SIZE))
        self._cbo_country.setFont(
            QtGui.QFont(constants.BODY_FONT_NAME, constants.BODY_FONT_SIZE))
        self._cbo_expat.setFont(
            QtGui.QFont(constants.BODY_FONT_NAME, constants.BODY_FONT_SIZE))
        self._cbo_martial.setFont(
            QtGui.QFont(constants.BODY_FONT_NAME, constants.BODY_FONT_SIZE))
        self._cbo_risk.setFont(
            QtGui.QFont(constants.BODY_FONT_NAME, constants.BODY_FONT_SIZE))
        self._cbo_situation.setFont(
            QtGui.QFont(constants.BODY_FONT_NAME, constants.BODY_FONT_SIZE))
        self._spi_iso_adult.setFont(
            QtGui.QFont(constants.BODY_FONT_NAME, constants.BODY_FONT_SIZE))
        self._spi_iso_kids.setFont(
            QtGui.QFont(constants.BODY_FONT_NAME, constants.BODY_FONT_SIZE))
        self._cbo_data_graph.setFont(
            QtGui.QFont(constants.BODY_FONT_NAME, constants.BODY_FONT_SIZE))
        self._cbo_user_graph.setFont(
            QtGui.QFont(constants.BODY_FONT_NAME, constants.BODY_FONT_SIZE))
        # Textual output
        self._lbl_textual_output.setFont(
            QtGui.QFont(constants.BODY_FONT_NAME, constants.BODY_FONT_SIZE))

    def _setup_color(self) -> None:
        """Setup color for all the widgets"""
        style_sheet = f'background-color : {constants.BACKGROUND_COLOR.name()}; ' \
                      f'color : {constants.FOREGROUND_COLOR.name()};'
        spi_style = f'background-color : {constants.WHITE.name()}; ' \
                    f'color : {constants.FOREGROUND_COLOR.name()};'
        combo_style = f'background-color : {constants.WHITE.name()}; ' \
                      f'color : {constants.FOREGROUND_COLOR.name()}; ' \
                      f'QComboBox::drop-down {{ background-color : {constants.WHITE.name()} }}'
        progress_style = f"""
            QProgressBar {{ text-align: center; 
                            background-color : {constants.WHITE.name()}; 
                            border-radius : 10px; 
                          }}
            QProgressBar::chunk {{ background-color: {constants.PLOT_FOREGROUND.name()};
                                   margin: 0.5px;
                                   border-bottom-left-radius: 10px;
                                   border-bottom-right-radius: 10px;
                                }} """
        # Main window
        self.setStyleSheet(style_sheet)
        if platform.platform() != 'Linux':
            self._lbl_textual_output.setStyleSheet('padding : 0px 10px 0px 10px;')
        # Interactive
        self._spi_age.setStyleSheet(spi_style)
        self._cbo_gender.setStyleSheet(combo_style)
        self._cbo_edu.setStyleSheet(combo_style)
        self._cbo_employment.setStyleSheet(combo_style)
        self._cbo_country.setStyleSheet(combo_style)
        self._cbo_expat.setStyleSheet(combo_style)
        self._cbo_martial.setStyleSheet(combo_style)
        self._cbo_risk.setStyleSheet(combo_style)
        self._cbo_situation.setStyleSheet(combo_style)
        self._spi_iso_adult.setStyleSheet(spi_style)
        self._spi_iso_kids.setStyleSheet(spi_style)
        self._cbo_data_graph.setStyleSheet(combo_style)
        self._cbo_user_graph.setStyleSheet(combo_style)

        self._plt_data.setBackground(constants.BACKGROUND_COLOR)
        self._pgb_user.setStyleSheet(progress_style)

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
        self.setFixedSize(1080, 720)
        self._wgt_gauge.setMinimumWidth(250)
        self._wgt_gauge.setMinimumHeight(250)

        self._lbl_avatar.resize(300, 200)

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
        # Update graph for data
        self._cbo_data_graph.currentIndexChanged.connect(self._plot_data)
        # Update user selected outputs
        self._spi_age.valueChanged.connect(self._update_output)
        self._cbo_gender.currentIndexChanged.connect(self._update_output)
        self._cbo_edu.currentIndexChanged.connect(self._update_output)
        self._cbo_employment.currentIndexChanged.connect(self._update_output)
        self._cbo_country.currentIndexChanged.connect(self._update_output)
        self._cbo_expat.currentIndexChanged.connect(self._update_output)
        self._cbo_martial.currentIndexChanged.connect(self._update_output)
        self._cbo_risk.currentIndexChanged.connect(self._update_output)
        self._cbo_situation.currentIndexChanged.connect(self._update_output)
        self._spi_iso_adult.valueChanged.connect(self._update_output)
        self._spi_iso_kids.valueChanged.connect(self._update_output)

        self._cbo_user_graph.currentIndexChanged.connect(self._update_output)

    def _plot_data(self) -> None:
        """Plots the data from the csv file"""
        self._plt_data.clear()  # clear current graph

        id_index, id_group = self._cbo_data_graph.currentIndex(), self._cbo_data_graph.currentText()

        bar_graph = pg.BarGraphItem(
            y=[i for i in range(len(constants.IDENTITY_GROUP_OPTIONS_LIST[id_index]))],
            x0=0,
            width=list(self.anxiety_data[id_index].values()),
            height=0.75, brush=constants.PLOT_FOREGROUND
        )

        string_axis = pg.AxisItem(orientation='left')  # Textual x-axis
        string_axis.setTextPen((0, 0, 0, 255))
        string_axis.setTicks(
            [dict(enumerate(constants.IDENTITY_GROUP_OPTIONS_LIST[id_index])).items()])

        plot_item = self._plt_data.addPlot(axisItems={'left': string_axis})
        plot_item.getAxis("bottom").setTextPen((0, 0, 0, 255))
        # plot_item.setTitle(id_group)
        plot_item.addItem(bar_graph)

    def _update_gauge(self, percentage: float):
        """Calculate the user's anxiety score, then update the gauge"""
        self._wgt_gauge.update_value(percentage)

    def _plot_user(self, id_percentage: float) -> None:
        """Plots the user's ranking"""
        self._pgb_user.setValue(int(id_percentage))

    def _display_textual_output(self, percentage: float,
                                id_percentage: float) -> None:
        """Display the textual output of the user's anxiety data"""
        # id_index = constants.IDENTITY_GROUP_NAMES.index(self._cbo_user_graph.currentText())
        selection = self._cbo_user_graph.currentText()
        if selection == 'Age':
            id_group = self._spi_age.value()
        elif selection == 'Gender':
            id_group = self._cbo_gender.currentText()
        elif selection == 'Education':
            id_group = self._cbo_edu.currentText()
        elif selection == 'Employment Status':
            id_group = self._cbo_employment.currentText()
        elif selection == 'Country of Residence':
            id_group = self._cbo_country.currentText()
        elif selection == 'Expatriate':
            id_group = self._cbo_expat.currentText()
        elif selection == 'Marital status':
            id_group = self._cbo_martial.currentText()
        elif selection == 'Risk Group':
            id_group = self._cbo_risk.currentText()
        elif selection == 'Current Situation':
            id_group = self._cbo_situation.currentText()
        elif selection == 'Isolation Adult':
            id_group = self._spi_iso_adult.value()
        elif selection == 'Isolation Children':
            id_group = self._spi_iso_kids.value()
        else:
            id_group = 'NA'

        textual_output = 'You are '
        if percentage < 50:
            textual_output = textual_output + 'less likely to be anxious than ' \
                                              f'<b>{100 - percentage:.2f}%</b>'
        else:
            textual_output = textual_output + 'more likely to be anxious than ' \
                                              f'<b>{percentage:.2f}%</b>'

        textual_output = textual_output + ' of the population. You are also '
        if id_percentage < 50:
            textual_output = textual_output + 'less likely to be anxious than' \
                                              f' <b>{100 - id_percentage:.2f}%</b> '
        else:
            textual_output = textual_output + 'more likely to be anxious than' \
                                              f' <b>{id_percentage:.2f}%</b> '
        textual_output = textual_output + f'of the population who chose "{id_group}" as their ' \
                                          f'"{self._cbo_user_graph.currentText().lower()}" ' \
                                          'identity.'
        self._lbl_textual_output.setText(textual_output)

    def _update_output(self) -> None:
        """Updates all the output (gauge, progress bar and textual)."""
        self._user.estimate_anxiety_score(self.anxiety_data)

        percentage = (self._user.get_anxiety_score() - self.extrema[0]) / \
                     (self.extrema[1] - self.extrema[0]) * 100
        id_percentage = get_user_percentage(self._user,
                                            self._cbo_user_graph.currentText(),
                                            self.anxiety_data)
        self._update_gauge(percentage)
        self._plot_user(id_percentage)
        self._display_textual_output(percentage, id_percentage)
        self._draw_user_avatar()

    def _draw_user_avatar(self) -> None:
        """Draws the user's cartoon character based on their input identity"""
        flag_name = self._user.country
        hair_name, clothes_name = '', ''
        # set hair image name
        if self._user.dem_gender == constants.DEM_GENDER[0] and \
                self._user.dem_age in constants.DEM_AGE[:4]:
            hair_name = 'hair1'
        # male, age 55+
        elif self._user.dem_gender == constants.DEM_GENDER[0]:
            hair_name = 'hair5'
        # female, age 18-54
        elif self._user.dem_gender == constants.DEM_GENDER[1] and \
                self._user.dem_age in constants.DEM_AGE[:4]:
            hair_name = 'hair2'
        # female, age 55+
        elif self._user.dem_gender == constants.DEM_GENDER[1]:
            hair_name = 'hair4'
        # neutral, age 18-54
        elif self._user.dem_gender == constants.DEM_GENDER[2] and \
                self._user.dem_age in constants.DEM_AGE[:4]:
            hair_name = 'hair1'
        # neutral, age 55+
        elif self._user.dem_gender == constants.DEM_GENDER[2]:
            hair_name = 'hair3'

        # set clothes image name
        # unemployed (not employed, student)
        if self._user.dem_employment in (constants.DEM_EMPLOYMENT[:2]):
            clothes_name = 'unemployed'
        # employed (part time, fill time, self-employed, ~retired~)
        elif self._user.dem_employment in constants.DEM_EMPLOYMENT[2:]:
            clothes_name = 'employed'

        pxm_flag = QtGui.QImage(
            constants.os.path.join(constants.IMAGE_PATH, f'Flags/{flag_name}.png')).convertToFormat(
            QtGui.QImage.Format_ARGB32)
        pxm_hair = QtGui.QImage(
            constants.os.path.join(constants.IMAGE_PATH, f'Character/{hair_name}.png'))
        pxm_face = QtGui.QImage(
            constants.os.path.join(constants.IMAGE_PATH, f'Character/face.png'))
        pxm_cloth = QtGui.QImage(
            constants.os.path.join(constants.IMAGE_PATH, f'Character/{clothes_name}.png'))
        pmx_edu = []

        index = constants.DEM_EDU.index(self._user.dem_edu)
        # PhD
        if index > 5:
            pmx_edu.append(QtGui.QImage(
                constants.os.path.join(constants.IMAGE_PATH, f'Character/school4.png')))
        # college to ~
        if index > 4:
            pmx_edu.append(QtGui.QImage(
                constants.os.path.join(constants.IMAGE_PATH, f'Character/school3.png')))
        # 12 to some college to ~
        if index > 2:
            pmx_edu.append(QtGui.QImage(
                constants.os.path.join(constants.IMAGE_PATH, f'Character/school2.png')))
        # 6 to 9 to ~
        if index > 0:
            pmx_edu.append(QtGui.QImage(
                constants.os.path.join(constants.IMAGE_PATH, f'Character/school1.png')))

        painter = QtGui.QPainter()

        painter.begin(pxm_flag)
        # cloth
        painter.drawImage(0, 0, pxm_cloth)
        # retired vest
        if self._user.dem_employment == constants.DEM_EMPLOYMENT[-1]:
            painter.drawImage(0, 0, QtGui.QImage(
                constants.os.path.join(constants.IMAGE_PATH, f'Character/retired.png')))
            painter.drawImage(0, 0, pxm_face)
        # face
        painter.drawImage(0, 0, pxm_face)
        # hair
        painter.drawImage(0, 0, pxm_hair)
        # education
        for pmx_edu_comp in pmx_edu:
            painter.drawImage(0, 0, pmx_edu_comp)

        # risk group or under isolation
        if self._user.dem_risk_group == constants.RISK_GROUP[0] or \
                self._user.dem_isolation in constants.DEM_ISOLATION[2:]:
            painter.drawImage(0, 0, QtGui.QImage(
                constants.os.path.join(constants.IMAGE_PATH, f'Character/mask.png')))

        painter.end()

        self._lbl_avatar.setPixmap(QPixmap.fromImage(pxm_flag))


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['os', 'platform', 'pyqtgraph', 'PyQt5', 'PyQt5.QtGui', 'src.data',
                          'src.gauge', 'src.user', 'src'],
        'allowed-io': [],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200', 'E0611']
        # E0611 (no-name-in-module): python_ta fails to find PyQt5 modules even if they exist
    })

    import python_ta.contracts

    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod()
