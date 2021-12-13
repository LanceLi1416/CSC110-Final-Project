# -*- coding: <UTF-8> -*-
"""Your Anxiety During COVID-19: ui

Module Description
==================
This file defines the look of the UI and handles the interaction with the user. It works with the
data module and user module to create an interactive application.

Copyright and Usage Information
===============================
This project is licensed under the GNU General Public License v3.0.
    Permissions of this strong copyleft license are conditioned on making available complete source
    code of licensed works and modifications, which include larger works using a licensed work,
    under the same license. Copyright and license notices must be preserved. Contributors provide an
    express grant of patent rights.

Authors (by alphabetical order):
  - Faruk, Fardin   https://github.com/Fard-Faru
  - Hsieh, Sharon   https://github.com/SharonHsieh22
  - Li, Sinan       https://github.com/LanceLi1416/
  - Zhan, Jeffery   https://github.com/jeffzhan
"""
import os
import platform
from typing import Dict, List, Tuple, Union

import pyqtgraph as pg
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QPixmap

import constants
from data import load_json_data, calculate_extrema
from gauge import GaugeWidget
from user import User, get_user_percentage


def _create_title_label() -> QtWidgets.QLabel:
    """Creates and customized tha title label"""
    lbl_title = QtWidgets.QLabel(constants.TITLE)
    lbl_title.setWordWrap(True)
    lbl_title.setAlignment(QtCore.Qt.AlignCenter)
    QtGui.QFontDatabase.addApplicationFont(
        os.path.join(os.path.dirname(__file__), constants.TITLE_FONT_PATH)
    )
    lbl_title.setFont(QtGui.QFont(constants.TITLE_FONT_NAME, constants.TITLE_FONT_SIZE))
    return lbl_title


class MainWindow(QtWidgets.QMainWindow):
    """The main window of the GUI interface.

    This class defines the loop and interactive logic of the main window of the GUI application. It
    acts as a 'manager' class that summarizes all the logic in the project.

    Instance Attributes:
      - _id_group_labels: a list of QLabel which displays of the identity group names
      - _input_fields: all the input fields, which includes the ones allowing the user to enter
      - _plt_data: the widget on which the visualization of the processed data is displayed
      - _graphical_output: a list of graphical outputs based on the user's input, which are, in
                           order: User avatar (cartoon image), Gauge, Progress bar of user in
                           identity, Textual output
                       their identities, and the selection menus specifying the fields to output.
      - _user: an instance of the User class from the user module that stores the user's identities
               and the corresponding logic
      - anxiety_data: the data processed from the data module
      - extrema: the maximum and minimum anxiety score in the processed data

    Representation Invariants:
      - len(self._graphical_output) == 4
      - len(self._id_group_labels) == constants.NUMBER_OF_IDENTITIES
      - len(self._input_fields) == constants.NUMBER_OF_IDENTITIES + 2
      - len(self.anxiety_data) == constants.NUMBER_OF_IDENTITIES
      - self.extrema[0] < self.extrema[1]
    """
    _id_group_labels: List[QtWidgets.QLabel]
    _input_fields: List[Union[QtWidgets.QSpinBox, QtWidgets.QComboBox]]
    _plt_data: pg.GraphicsLayoutWidget
    _graphical_output: List[Union[QtWidgets.QLabel, GaugeWidget, QtWidgets.QProgressBar]]
    _user: User
    anxiety_data: List[Dict[str, float]]
    extrema: Tuple[float, float]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # -------------------------------------- Data Fields ---------------------------------------
        # Main Layout ---------------------------------------------------------------------------- |
        grid_central = QtWidgets.QGridLayout()
        wgt_central = QtWidgets.QWidget()
        status_bar = self.statusBar()
        # Identity input ------------------------------------------------------------------------- |
        grid_id = QtWidgets.QGridLayout()
        frm_id = QtWidgets.QFrame()
        self._id_group_labels = [QtWidgets.QLabel() for _ in range(constants.NUMBER_OF_IDENTITIES)]
        self._input_fields = [
            QtWidgets.QSpinBox(),  # 0 age
            QtWidgets.QComboBox(),  # 1  gender
            QtWidgets.QComboBox(),  # 2  education
            QtWidgets.QComboBox(),  # 3  employment
            QtWidgets.QComboBox(),  # 4  country
            QtWidgets.QComboBox(),  # 5  expat
            QtWidgets.QComboBox(),  # 6  martial
            QtWidgets.QComboBox(),  # 7  risk
            QtWidgets.QComboBox(),  # 8  situation
            QtWidgets.QSpinBox(),  # 9  ido_adults
            QtWidgets.QSpinBox(),  # 10 ido_kids
            QtWidgets.QComboBox(),  # 11 data visualization selection
            QtWidgets.QComboBox()  # 12 user visualization selection
        ]
        # Visualization -------------------------------------------------------------------------- |
        # Title of program
        lbl_title = _create_title_label()
        # Data plot
        self._plt_data = pg.GraphicsLayoutWidget()
        # Graphical outputs
        self._graphical_output = [
            QtWidgets.QLabel(),  # User avatar (cartoon image)
            GaugeWidget(),  # Gauge
            QtWidgets.QProgressBar(),  # User percentage in population
            QtWidgets.QLabel()  # Textual output
        ]
        # Data storage --------------------------------------------------------------------------- |
        self._user = User([18, 'Male', 'None', 'Not employed', 'Afghanistan', 'Yes', 'Single',
                           'Yes', 'Life carries on as usual', 0, 0])
        self.anxiety_data = load_json_data(constants.REAL_DATA_JSON_FILE)
        self.extrema = calculate_extrema(self.anxiety_data)

        # --------------------------------------- Behaviour ----------------------------------------
        # Main Window ---------------------------------------------------------------------------- |
        self.setWindowTitle(constants.TITLE)
        # Graphs ----------------------------------------------------------------------------------|
        self._plt_data.setToolTip(
            'Left click to pan, middle button scroll to zoom, right click for more options')
        self._graphical_output[0].setAlignment(QtCore.Qt.AlignCenter)
        self._graphical_output[2].setRange(0, 100)
        self._graphical_output[3].setWordWrap(True)
        # Identity input ------------------------------------------------------------------------- |
        self._setup_id_group_labels()
        self._setup_intractable_values()
        self._input_fields[11].setToolTip(
            'Select the identity group whose data you want to see.')
        self._input_fields[12].setToolTip(
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
        for i in range(constants.NUMBER_OF_IDENTITIES):
            grid_id.addWidget(self._id_group_labels[i], i, 0)
        for i in range(len(self._input_fields) - 2):
            grid_id.addWidget(self._input_fields[i], i, 1)
        frm_id.setLayout(grid_id)
        # Main Layout ---------------------------------------------------------------------------- |
        grid_central.addWidget(frm_id, 0, 0, 3, 1)
        grid_central.addWidget(lbl_title, 0, 1, 1, 2)
        grid_central.addWidget(self._graphical_output[0], 1, 1, 2, 2)
        grid_central.addWidget(self._input_fields[11], 3, 0, 1, 1)
        grid_central.addWidget(self._graphical_output[1], 3, 1, 3, 1)
        grid_central.addWidget(self._input_fields[12], 3, 2, 1, 1)
        grid_central.addWidget(self._plt_data, 4, 0, 2, 1)
        grid_central.addWidget(self._graphical_output[2], 4, 2, 1, 1)
        grid_central.addWidget(self._graphical_output[3], 5, 2, 1, 1)

        wgt_central.setLayout(grid_central)
        self.setCentralWidget(wgt_central)

        # ---------------------------------------- Geometry ----------------------------------------
        self._setup_geometry()

        # ------------------------------------------ Look ------------------------------------------
        self._setup_fonts()
        self._setup_color()

        self._plot_data()
        self._update_output()

    def _setup_id_group_labels(self) -> None:
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
            self._id_group_labels[i].setText(constants.IDENTITY_NAMES[i])
            self._id_group_labels[i].setToolTip(tool_tips[i])

    def _setup_intractable_values(self) -> None:
        """Initialize the values for the intractable widgets"""
        # Input fields
        self._input_fields[0].setRange(18, 110)
        for i in range(1, 9):
            self._input_fields[i].addItems(constants.IDENTITY_GROUP_OPTIONS_LIST[i])
        self._input_fields[9].setRange(0, 110)
        self._input_fields[10].setRange(0, 110)
        # Graphs
        self._input_fields[11].addItems(constants.IDENTITY_NAMES)
        self._input_fields[12].addItems(constants.IDENTITY_NAMES)

    def _setup_fonts(self) -> None:
        """Set customized fonts to all the widgets"""
        QtGui.QFontDatabase.addApplicationFont(
            os.path.join(os.path.dirname(__file__), constants.BODY_FONT_PATH)
        )
        # Labels
        for i in range(constants.NUMBER_OF_IDENTITIES):
            self._id_group_labels[i].setFont(
                QtGui.QFont(constants.BODY_FONT_NAME, constants.BODY_FONT_SIZE))
        # Intractable
        for input_field in self._input_fields:
            input_field.setFont(QtGui.QFont(constants.BODY_FONT_NAME, constants.BODY_FONT_SIZE))
        # Textual output
        self._graphical_output[3].setFont(
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
            self._graphical_output[3].setStyleSheet('padding : 0px 10px 0px 10px;')
        # Interactive
        for input_field in self._input_fields[1:9] + self._input_fields[11:]:
            input_field.setStyleSheet(combo_style)
        for i in [0, 9, 10]:
            self._input_fields[i].setStyleSheet(spi_style)

        self._plt_data.setBackground(constants.BACKGROUND_COLOR)
        self._graphical_output[2].setStyleSheet(progress_style)

    def _setup_geometry(self) -> None:
        """Set up the sizes of the widgets"""
        self.setFixedSize(1080, 720)
        self._graphical_output[1].setMinimumWidth(250)
        self._graphical_output[1].setMinimumHeight(250)

        self._graphical_output[0].resize(300, 200)

        for i in range(constants.NUMBER_OF_IDENTITIES):
            self._id_group_labels[i].resize(
                150,
                self._id_group_labels[i].height()
            )

    def _setup_slots(self) -> None:
        """Connect components to slots"""
        # Update self._user
        self._input_fields[0].valueChanged.connect(
            lambda: self._user.set_age(self._input_fields[0].value()))
        self._input_fields[9].valueChanged.connect(
            lambda: self._user.set_isolation_adults(self._input_fields[9].value()))
        self._input_fields[10].valueChanged.connect(
            lambda: self._user.set_isolation_kids(self._input_fields[10].value()))
        for i in [0, 9, 10]:
            self._input_fields[i].valueChanged.connect(self._update_output)

        # WARNING: Due to how Qt works with its signals and lots, the following block WILL NOT WORK
        # IN A LOOP, as every 'i' in the expression would be stuck with 8 after the initial setup,
        # meaning that we would be stuck with the 'Current Situation' input. As such, every setting
        # value connection MUST NOT be set in a loop. PLEASE DO NOT SIMPLIFY INTO THE LOOP.
        self._input_fields[1].currentIndexChanged.connect(lambda: self._user.identity.__setitem__(
            constants.IDENTITY_NAMES[1], self._input_fields[1].currentText()))
        self._input_fields[2].currentIndexChanged.connect(lambda: self._user.identity.__setitem__(
            constants.IDENTITY_NAMES[2], self._input_fields[2].currentText()))
        self._input_fields[3].currentIndexChanged.connect(lambda: self._user.identity.__setitem__(
            constants.IDENTITY_NAMES[3], self._input_fields[3].currentText()))
        self._input_fields[4].currentIndexChanged.connect(lambda: self._user.identity.__setitem__(
            constants.IDENTITY_NAMES[4], self._input_fields[4].currentText()))
        self._input_fields[5].currentIndexChanged.connect(lambda: self._user.identity.__setitem__(
            constants.IDENTITY_NAMES[5], self._input_fields[5].currentText()))
        self._input_fields[6].currentIndexChanged.connect(lambda: self._user.identity.__setitem__(
            constants.IDENTITY_NAMES[6], self._input_fields[6].currentText()))
        self._input_fields[7].currentIndexChanged.connect(lambda: self._user.identity.__setitem__(
            constants.IDENTITY_NAMES[7], self._input_fields[7].currentText()))
        self._input_fields[8].currentIndexChanged.connect(lambda: self._user.identity.__setitem__(
            constants.IDENTITY_NAMES[8], self._input_fields[8].currentText()))
        for i in range(1, 9):
            self._input_fields[i].currentIndexChanged.connect(self._update_output)

        # Update visual
        self._input_fields[11].currentIndexChanged.connect(self._plot_data)
        self._input_fields[12].currentIndexChanged.connect(self._update_output)
        # self._cbo_data_graph.currentIndexChanged.connect(self._plot_data)
        # self._cbo_user_graph.currentIndexChanged.connect(self._update_output)

    def _plot_data(self) -> None:
        """Plots the data from the csv file"""
        self._plt_data.clear()  # clear current graph

        id_index = self._input_fields[11].currentIndex()

        bar_graph = pg.BarGraphItem(
            y=list(range(len(constants.IDENTITY_GROUP_OPTIONS_LIST[id_index]))),
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

    def _draw_user_avatar(self) -> None:
        """Draws the user's cartoon character based on their input identity"""
        if self._user.identity[constants.IDENTITY_NAMES[4]] == 'Côte d’Ivoire':
            flag_name = 'Cote dIvoire'
        else:
            flag_name = self._user.identity[constants.IDENTITY_NAMES[4]]
        # set hair image name
        hair_name = \
            self._user.identity[constants.IDENTITY_NAMES[0]][:2] + \
            '_' + \
            self._user.identity[constants.IDENTITY_NAMES[1]][0]

        # set clothes image name
        # unemployed (not employed, student)
        if self._user.identity[constants.IDENTITY_NAMES[3]] in (constants.DEM_EMPLOYMENT[:2]):
            clothes_name = 'unemployed'
        # employed (part time, fill time, self-employed, ~retired~)
        else:
            clothes_name = 'employed'

        pxm_flag = QtGui.QImage(
            constants.os.path.join(constants.IMAGE_PATH, f'Flags/{flag_name}.png')).convertToFormat(
            QtGui.QImage.Format_ARGB32)
        pxm_hair = QtGui.QImage(
            constants.os.path.join(constants.IMAGE_PATH, f'Character/hair/{hair_name}.png'))
        pxm_face = QtGui.QImage(
            constants.os.path.join(constants.IMAGE_PATH, 'Character/face.png'))
        pxm_cloth = QtGui.QImage(
            constants.os.path.join(constants.IMAGE_PATH, f'Character/{clothes_name}.png'))
        pmx_edu = []

        index = constants.DEM_EDU.index(self._user.identity[constants.IDENTITY_NAMES[2]])
        # PhD
        if index > 5:
            pmx_edu.append(QtGui.QImage(
                constants.os.path.join(constants.IMAGE_PATH, 'Character/school4.png')))
        # college to ~
        if index > 4:
            pmx_edu.append(QtGui.QImage(
                constants.os.path.join(constants.IMAGE_PATH, 'Character/school3.png')))
        # 12 to some college to ~
        if index > 2:
            pmx_edu.append(QtGui.QImage(
                constants.os.path.join(constants.IMAGE_PATH, 'Character/school2.png')))
        # 6 to 9 to ~
        if index > 0:
            pmx_edu.append(QtGui.QImage(
                constants.os.path.join(constants.IMAGE_PATH, 'Character/school1.png')))

        painter = QtGui.QPainter()

        painter.begin(pxm_flag)
        # cloth
        painter.drawImage(0, 0, pxm_cloth)
        # retired vest
        if self._user.identity[constants.IDENTITY_NAMES[3]] == constants.DEM_EMPLOYMENT[-1]:
            painter.drawImage(0, 0, QtGui.QImage(
                constants.os.path.join(constants.IMAGE_PATH, 'Character/retired.png')))
            painter.drawImage(0, 0, pxm_face)
        # face
        painter.drawImage(0, 0, pxm_face)
        # hair
        painter.drawImage(0, 0, pxm_hair)
        # education
        for pmx_edu_comp in pmx_edu:
            painter.drawImage(0, 0, pmx_edu_comp)

        # risk group or under isolation
        if self._user.identity[constants.IDENTITY_NAMES[7]] != constants.RISK_GROUP[1] or \
                self._user.identity[constants.IDENTITY_NAMES[8]] in constants.DEM_ISOLATION[2:]:
            painter.drawImage(0, 0, QtGui.QImage(
                constants.os.path.join(constants.IMAGE_PATH, 'Character/mask.png')))

        painter.end()

        self._graphical_output[0].setPixmap(QPixmap.fromImage(pxm_flag))

    def _update_gauge(self, percentage: float) -> None:
        """Calculate the user's anxiety score, then update the gauge

        Preconditions:
          - 0 <= percentage <= 100
          """
        self._graphical_output[1].update_value(percentage)

    def _plot_user(self, id_percentage: float) -> None:
        """Plots the user's ranking

        Preconditions:
          - 0 <= id_percentage <= 100
          """
        self._graphical_output[2].setValue(int(id_percentage))

    def _display_textual_output(self, percentage: float,
                                id_percentage: float) -> None:
        """Display the textual output of the user's anxiety data

        Preconditions:
          - 0 <= percentage <= 100
          - 0 <= id_percentage <= 100
          """
        id_group = self._user.identity[self._input_fields[12].currentText()]

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
                                          f'"{self._input_fields[12].currentText().lower()}" ' \
                                          'identity.'
        self._graphical_output[3].setText(textual_output)

    def _update_output(self) -> None:
        """Updates all the output (gauge, progress bar and textual)."""
        self._user.estimate_anxiety_score(self.anxiety_data)

        percentage = (self._user.get_anxiety_score() - self.extrema[0]) / \
                     (self.extrema[1] - self.extrema[0]) * 100
        id_percentage = get_user_percentage(self._user,
                                            self._input_fields[12].currentText(),
                                            self.anxiety_data)
        self._update_gauge(percentage)
        self._plot_user(id_percentage)
        self._display_textual_output(percentage, id_percentage)
        self._draw_user_avatar()


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'os', 'platform', 'pyqtgraph', 'PyQt5',
                          'PyQt5.QtGui', 'constants', 'data', 'gauge', 'user'],
        'allowed-io': [],
        'max-line-length': 100,
        # 'disable': ['R1705', 'C0200']
        # E0611 (no-name-in-module): python_ta fails to find PyQt5 modules even if they exist
        'disable': ['R1705', 'C0200', 'E0611']
    })

    import python_ta.contracts

    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod()
