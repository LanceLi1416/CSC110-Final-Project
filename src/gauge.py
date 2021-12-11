import os
import math

from PyQt5.QtWidgets import QWidget

from PyQt5.QtGui import QPolygon, QPolygonF, QColor, QPen, QFont, QPainter, QFontMetrics, \
    QConicalGradient, QRadialGradient, QFontDatabase, QPaintEvent

from PyQt5.QtCore import Qt, QPoint, QPointF, QObject, pyqtSignal

import src.constants as constants


class GaugeWidget(QWidget):
    valueChanged = pyqtSignal(int)

    def __init__(self, *args, **kwargs):
        super(GaugeWidget, self).__init__(*args, **kwargs)

        # Value needle
        self.value_needle = QObject
        self.pen = QPen()

        # Min and max
        self.min_val = 0
        self.max_val = 100
        # starting value
        self.value = self.min_val

        # Scale value
        self.scale_angle_start = 135
        self.scale_angle_size = 270
        # Number of scales
        self.scala_count = 10
        self.scala_subdiv_count = 5

        # Load custom font
        QFontDatabase.addApplicationFont(
            os.path.join(os.path.dirname(__file__), '../', constants.GAUGE_FONT_PATH)
        )

        # Polygon color
        self.scale_polygon_colors = [[.10, Qt.red], [.25, Qt.yellow], [.5, Qt.green]]

        # Scale text
        self.initial_scale_fontsize = 14
        self.scale_fontsize = self.initial_scale_fontsize

        # Value text status
        self.enable_value_text = True
        self.value_fontname = constants.GAUGE_FONT_NAME
        self.initial_value_fontsize = 40
        self.value_fontsize = self.initial_value_fontsize

        # NEEDLE SCALE FACTOR/LENGTH
        self.needle_scale_factor = 0.8

        # SET DEFAULT THEME
        self.needle_center_bg = [
            [0, QColor(35, 40, 3, 255)],
            [0.16, QColor(30, 36, 45, 255)],
            [0.225, QColor(36, 42, 54, 255)],
            [0.423963, QColor(19, 23, 29, 255)],
            [0.580645, QColor(45, 53, 68, 255)],
            [0.792627, QColor(59, 70, 88, 255)],
            [0.935, QColor(30, 35, 45, 255)],
            [1, QColor(35, 40, 3, 255)]
        ]
        self.outer_circle_bg = [
            [0.0645161, QColor(30, 35, 45, 255)],
            [0.37788, QColor(57, 67, 86, 255)],
            [1, QColor(30, 36, 45, 255)]
        ]

        self.update()
        # RESIZE GAUGE
        self.rescale_method()

    # RESCALE
    def rescale_method(self):
        # SET WIDTH AND HEIGHT
        if self.width() <= self.height():
            self.widget_diameter = self.width()
        else:
            self.widget_diameter = self.height()

        # SET NEEDLE SIZE
        self.change_value_needle_style(
            [QPolygon(
                [QPoint(4, 30),
                 QPoint(-4, 30),
                 QPoint(-2, - self.widget_diameter /
                        2 * self.needle_scale_factor),
                 QPoint(0, - self.widget_diameter / 2 *
                        self.needle_scale_factor - 6),
                 QPoint(2, - self.widget_diameter /
                        2 * self.needle_scale_factor)
                 ])
            ])

        # SET FONT SIZE
        self.scale_fontsize = self.initial_scale_fontsize * self.widget_diameter / 400
        self.value_fontsize = self.initial_value_fontsize * self.widget_diameter / 400

    def change_value_needle_style(self, design):
        # prepared for multiple needle instrument
        self.value_needle = []
        for i in design:
            self.value_needle.append(i)
        self.update()

    ################################################################################################
    # UPDATE VALUE
    ################################################################################################
    def updateValue(self, value):
        if value <= self.min_val:
            self.value = self.min_val
        elif value >= self.max_val:
            self.value = self.max_val
        else:
            self.value = value
        # self.paintEvent("")
        self.valueChanged.emit(int(value))
        # print(self.value)

        # ohne timer: aktiviere self.update()
        self.update()

    ################################################################################################
    # SHOW HIDE SCALA MAIN CONT
    ################################################################################################
    def setScalaCount(self, count):
        if count < 1:
            count = 1
        self.scala_count = count
        self.update()

    ################################################################################################
    # SET MINIMUM VALUE
    ################################################################################################
    def setMinValue(self, min):
        if self.value < min:
            self.value = min
        if min >= self.max_val:
            self.min_val = self.max_val - 1
        else:
            self.min_val = min
        self.update()

    ################################################################################################
    # SET MAXIMUM VALUE
    ################################################################################################
    def setMaxValue(self, max):
        if self.value > max:
            self.value = max
        if max <= self.min_val:
            self.max_val = self.min_val + 1
        else:
            self.max_val = max
        self.update()

    ################################################################################################
    # SET SCALE SIZE
    ################################################################################################
    def setTotalScaleAngleSize(self, value):
        self.scale_angle_size = value
        # print("stopFill: " + str(self.scale_angle_size))
        self.update()

    ################################################################################################
    # GET MAXIMUM VALUE
    ################################################################################################
    def get_value_max(self):
        return self.max_val

    # CREATE PIE
    def create_polygon_pie(self, outer_radius: int, inner_radius: int, start: int, length: int):
        polygon_pie = QPolygonF()
        n = 360  # angle steps size for full circle
        w = 360 / n  # angle per step
        x = 0
        y = 0

        # add the points of polygon
        for i in range(length + 1):
            t = w * i + start
            x = outer_radius * math.cos(math.radians(t))
            y = outer_radius * math.sin(math.radians(t))
            polygon_pie.append(QPointF(x, y))
        # create inner circle line from "start + lenght"-angle to "start"-angle add the points of
        # polygon
        for i in range(length + 1):
            t = w * (length - i) + start
            x = inner_radius * math.cos(math.radians(t))
            y = inner_radius * math.sin(math.radians(t))
            polygon_pie.append(QPointF(x, y))

        # close outer line
        polygon_pie.append(QPointF(x, y))
        return polygon_pie

    def draw_filled_polygon(self, outline_pen_with=0):
        painter_filled_polygon = QPainter(self)
        painter_filled_polygon.setRenderHint(QPainter.Antialiasing)
        painter_filled_polygon.translate(
            self.width() / 2, self.height() / 2)

        painter_filled_polygon.setPen(Qt.NoPen)

        self.pen.setWidth(outline_pen_with)
        if outline_pen_with > 0:
            painter_filled_polygon.setPen(self.pen)

        colored_scale_polygon = self.create_polygon_pie(
            ((self.widget_diameter / 2) - (self.pen.width() / 2)) * 1,
            (((self.widget_diameter / 2) - (self.pen.width() / 2)) * 0.9
             ),
            self.scale_angle_start, self.scale_angle_size)

        grad = QConicalGradient(QPointF(0, 0), - self.scale_angle_size - self.scale_angle_start - 1)

        for color in self.scale_polygon_colors:
            grad.setColorAt(color[0], color[1])
        painter_filled_polygon.setBrush(grad)

        painter_filled_polygon.drawPolygon(colored_scale_polygon)

    # BIG SCALE MARKERS
    def draw_big_scaled_marker(self):
        my_painter = QPainter(self)
        my_painter.setRenderHint(QPainter.Antialiasing)
        my_painter.translate(self.width() / 2, self.height() / 2)

        self.pen = QPen(constants.GAUGE_BIG_SCALE_COLOR)
        self.pen.setWidth(2)
        my_painter.setPen(self.pen)

        my_painter.rotate(self.scale_angle_start)
        steps_size = (float(self.scale_angle_size) / float(self.scala_count))
        scale_line_outer_start = self.widget_diameter / 2
        scale_line_lenght = (self.widget_diameter / 2) - \
                            (self.widget_diameter / 20)
        for i in range(self.scala_count + 1):
            my_painter.drawLine(scale_line_lenght, 0,
                                scale_line_outer_start, 0)
            my_painter.rotate(steps_size)

    def create_scale_marker_values_text(self):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.translate(self.width() / 2, self.height() / 2)
        font = QFont(constants.GAUGE_FONT_NAME, self.scale_fontsize, QFont.Bold)
        font_matrices = QFontMetrics(font)

        pen_shadow = QPen()

        pen_shadow.setBrush(constants.GAUGE_SCALE_TEXT_COLOR)
        painter.setPen(pen_shadow)

        text_radius_factor = 0.8
        text_radius = self.widget_diameter / 2 * text_radius_factor

        scale_per_div = int((self.max_val - self.min_val) / self.scala_count)

        angle_distance = (float(self.scale_angle_size) / float(self.scala_count))

        for i in range(self.scala_count + 1):
            text = str(int(self.min_val + scale_per_div * i))
            w = font_matrices.width(text) + 1
            h = font_matrices.height()
            painter.setFont(font)
            angle = angle_distance * i + float(self.scale_angle_start)
            x = text_radius * math.cos(math.radians(angle))
            y = text_radius * math.sin(math.radians(angle))
            # print(w, h, x, y, text)

            text = [x - int(w / 2), y - int(h / 2), int(w),
                    int(h), Qt.AlignCenter, text]
            painter.drawText(text[0], text[1], text[2],
                             text[3], text[4], text[5])

    # FINE SCALE MARKERS
    def create_fine_scaled_marker(self):
        #  Description_dict = 0
        my_painter = QPainter(self)

        my_painter.setRenderHint(QPainter.Antialiasing)
        my_painter.translate(self.width() / 2, self.height() / 2)

        my_painter.setPen(constants.GAUGE_FINE_SCALE_COLOR)
        my_painter.rotate(self.scale_angle_start)
        steps_size = (
                float(self.scale_angle_size) / float(self.scala_count * self.scala_subdiv_count))
        scale_line_outer_start = self.widget_diameter / 2
        scale_line_lenght = (self.widget_diameter / 2) - (self.widget_diameter / 40)
        for i in range((self.scala_count * self.scala_subdiv_count) + 1):
            my_painter.drawLine(scale_line_lenght, 0, scale_line_outer_start, 0)
            my_painter.rotate(steps_size)

    # VALUE TEXT
    def create_values_text(self):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.HighQualityAntialiasing)

        painter.translate(self.width() / 2, self.height() / 2)
        font = QFont(self.value_fontname, self.value_fontsize, QFont.Bold)
        fm = QFontMetrics(font)

        pen_shadow = QPen()

        pen_shadow.setBrush(constants.GAUGE_TEXT_COLOR)
        painter.setPen(pen_shadow)

        text_radius = self.widget_diameter / 2 * 0.5

        text = f'{self.value:.0f} %'
        w = fm.width(text) + 1
        h = fm.height()
        painter.setFont(QFont(self.value_fontname,
                              self.value_fontsize,
                              QFont.Bold))

        angle_end = float(self.scale_angle_start + self.scale_angle_size - 360)
        angle = (angle_end - self.scale_angle_start) / 2 + self.scale_angle_start

        x = text_radius * math.cos(math.radians(angle))
        y = text_radius * math.sin(math.radians(angle))
        text = [x - int(w / 2), y - int(h / 2), int(w), int(h), Qt.AlignCenter, text]
        painter.drawText(text[0], text[1], text[2], text[3], text[4], text[5])

    # CENTER POINTER
    def draw_big_needle_center_point(self):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.translate(self.width() / 2, self.height() / 2)
        painter.setPen(Qt.NoPen)

        colored_scale_polygon = self.create_polygon_pie(
            ((self.widget_diameter / 8) - (self.pen.width() / 2)),
            0, self.scale_angle_start, 360)

        grad = QConicalGradient(QPointF(0, 0), 0)

        for eachcolor in self.needle_center_bg:
            grad.setColorAt(eachcolor[0], eachcolor[1])
        painter.setBrush(grad)

        painter.drawPolygon(colored_scale_polygon)

    # CREATE OUTER COVER
    def draw_outer_circle(self):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.translate(self.width() / 2, self.height() / 2)
        painter.setPen(Qt.NoPen)
        colored_scale_polygon = self.create_polygon_pie(
            ((self.widget_diameter / 2) - (self.pen.width())),
            (self.widget_diameter / 6),
            self.scale_angle_start / 10, 360)

        radialGradient = QRadialGradient(QPointF(0, 0), self.width())

        for eachcolor in self.outer_circle_bg:
            radialGradient.setColorAt(eachcolor[0], eachcolor[1])

        painter.setBrush(radialGradient)

        painter.drawPolygon(colored_scale_polygon)

    # NEEDLE POINTER
    def draw_needle(self):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(self.width() / 2, self.height() / 2)
        painter.setPen(Qt.NoPen)
        painter.setBrush(constants.GAUGE_NEEDLE_COLOR)
        painter.rotate(((self.value - self.min_val) * self.scale_angle_size /
                        (self.max_val - self.min_val)) + 90 + self.scale_angle_start)

        painter.drawConvexPolygon(self.value_needle[0])

    # ON WINDOW RESIZE
    def resizeEvent(self, event):
        self.rescale_method()

    # ON PAINT EVENT
    def paintEvent(self, event: QPaintEvent):
        # Main Drawing Event:

        self.draw_outer_circle()
        # colored pie area
        self.draw_filled_polygon()

        # draw scale marker lines
        self.create_fine_scaled_marker()
        self.draw_big_scaled_marker()

        # draw scale marker value text
        self.create_scale_marker_values_text()

        # Display Value
        self.create_values_text()

        # draw needle
        self.draw_needle()

        # Draw Center Point
        self.draw_big_needle_center_point()
