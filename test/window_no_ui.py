from load_ui import Section

import sys

from PyQt5 import QtWidgets, QtCore


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super(MainWindow, self).__init__(*args, **kwargs)

        lbl_age = QtWidgets.QLabel("Age")
        lbl_gender = QtWidgets.QLabel("Gender")
        lbl_edu = QtWidgets.QLabel("Education")
        lbl_employment = QtWidgets.QLabel("Employment")
        lbl_country = QtWidgets.QLabel("Country of Residence")

        self._spi_age = QtWidgets.QSpinBox()
        self._cbo_gander = QtWidgets.QComboBox()
        self._cbo_edu = QtWidgets.QComboBox()
        self._cbo_employment = QtWidgets.QComboBox()
        self._lne_country = QtWidgets.QLineEdit()

        grid_id = QtWidgets.QGridLayout()
        self.setLayout(grid_id)
        grid_id.addWidget(lbl_age, 0, 0)
        grid_id.addWidget(lbl_gender, 1, 0)
        grid_id.addWidget(lbl_edu, 2, 0)
        grid_id.addWidget(lbl_employment, 3, 0)
        grid_id.addWidget(lbl_country, 4, 0)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
