import sys

from PyQt5 import QtWidgets, QtCore, uic


class Section(QtWidgets.QWidget):
    def __init__(self, title="", animationDuration=100, parent=None):
        super().__init__(parent)
        self.animation_duration = animationDuration
        self.toggle_button = QtWidgets.QToolButton(self)
        self.header_line = QtWidgets.QFrame(self)
        self.toggle_animation = QtCore.QParallelAnimationGroup(self)
        self.content_area = QtWidgets.QScrollArea(self)
        self.main_layout = QtWidgets.QGridLayout(self)

        self.toggle_button.setStyleSheet("QToolButton {border: none;}")
        self.toggle_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toggle_button.setArrowType(QtCore.Qt.RightArrow)
        self.toggle_button.setText(title)
        self.toggle_button.setCheckable(True)
        self.toggle_button.setChecked(False)

        self.header_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.header_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.header_line.setSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                       QtWidgets.QSizePolicy.Maximum)

        # self.contentArea.setLayout(wd.QHBoxLayout())
        self.content_area.setSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                        QtWidgets.QSizePolicy.Fixed)

        # start out collapsed
        self.content_area.setMaximumHeight(0)
        self.content_area.setMinimumHeight(0)

        # let the entire widget grow and shrink with its content
        self.toggle_animation.addAnimation(QtCore.QPropertyAnimation(self, b"minimumHeight"))
        self.toggle_animation.addAnimation(QtCore.QPropertyAnimation(self, b"maximumHeight"))
        self.toggle_animation.addAnimation(
            QtCore.QPropertyAnimation(self.content_area, b"maximumHeight"))

        self.main_layout.setVerticalSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        row = 0
        self.main_layout.addWidget(self.toggle_button, row, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.main_layout.addWidget(self.header_line, row, 2, 1, 1)
        self.main_layout.addWidget(self.content_area, row + 1, 0, 1, 3)
        self.setLayout(self.main_layout)

        self.toggle_button.toggled.connect(self.toggle)

    def set_content_layout(self, content_layout):
        layout = self.content_area.layout()
        del layout
        self.content_area.setLayout(content_layout)
        collapsed_height = self.sizeHint().height() - self.content_area.maximumHeight()
        content_height = content_layout.sizeHint().height()
        for i in range(0, self.toggle_animation.animationCount() - 1):
            section_animation = self.toggle_animation.animationAt(i)
            section_animation.setDuration(self.animation_duration)
            section_animation.setStartValue(collapsed_height)
            section_animation.setEndValue(collapsed_height + content_height)
        content_animation = self.toggle_animation.animationAt(
            self.toggle_animation.animationCount() - 1)
        content_animation.setDuration(self.animation_duration)
        content_animation.setStartValue(0)
        content_animation.setEndValue(content_height)

    def toggle(self, collapsed):
        if collapsed:
            self.toggle_button.setArrowType(QtCore.Qt.DownArrow)
            self.toggle_animation.setDirection(QtCore.QAbstractAnimation.Forward)
        else:
            self.toggle_button.setArrowType(QtCore.Qt.RightArrow)
            self.toggle_animation.setDirection(QtCore.QAbstractAnimation.Backward)
        self.toggle_animation.start()


class MainWindowHorizontal(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super(MainWindowHorizontal, self).__init__(*args, **kwargs)
        uic.loadUi('Horizontal.ui', self)

        section_risk_group = Section("Risk Group", 100, self)
        section_risk_group.set_content_layout(
            self.findChild(QtWidgets.QVBoxLayout, 'verticalLayout'))
        self._gridlayout = self.findChild(QtWidgets.QGridLayout, 'gridLayout')
        self._gridlayout.addWidget(section_risk_group, 7, 0)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindowHorizontal()
    window.show()
    sys.exit(app.exec_())
