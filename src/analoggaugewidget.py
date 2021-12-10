import os
import sys
import math

from PyQt5.QtWidgets import QWidget

from PyQt5.QtGui import QPolygon, QPolygonF, QColor, QPen, QFont, QPainter, QFontMetrics, \
    QConicalGradient, QRadialGradient, QFontDatabase

from PyQt5.QtCore import Qt, QPoint, QPointF, QObject, pyqtSignal

import src.constants as constants


class AnalogGaugeWidget(QWidget):
    valueChanged = pyqtSignal(int)

    def __init__(self, parent=None):
        super(AnalogGaugeWidget, self).__init__(parent)

        # DEFAULT NEEDLE COLOR
        self.NeedleColor = Qt.black

        # DEFAULT SCALE TEXT COLOR
        self.ScaleValueColor = constants.GAUGE_SCALE_TEXT_COLOR

        # DEFAULT VALUE COLOR
        self.DisplayValueColor = constants.GAUGE_TEXT_COLOR

        self.value_needle = QObject

        # DEFAULT MINIMUM AND MAXIMUM VALUE
        self.minValue = 0
        self.maxValue = 100
        # DEFAULT START VALUE
        self.value = self.minValue

        self.valueNeedleSnapzone = 0.05
        self.last_value = 0

        # DEFAULT RADIUS
        self.gauge_color_outer_radius_factor = 1
        self.gauge_color_inner_radius_factor = 0.9

        self.center_horizontal_value = 0
        self.center_vertical_value = 0

        # Default scale value
        self.scale_angle_start_value = 135
        self.scale_angle_size = 270
        # Number of scales
        self.scalaCount = 10
        self.scala_subdiv_count = 5

        self.pen = QPen(QColor(0, 0, 0))

        # Load custom font
        QFontDatabase.addApplicationFont(
            os.path.join(os.path.dirname(__file__), '../', constants.GAUGE_FONT_PATH)
        )

        # DEFAULT POLYGON COLOR
        self.scale_polygon_colors = []

        # SCALE COLOR
        self.bigScaleMarker = constants.GAUGE_BIG_SCALE_COLOR
        self.fineScaleColor = constants.GAUGE_FINE_SCALE_COLOR

        # DEFAULT SCALE TEXT STATUS
        self.scale_fontname = constants.GAUGE_FONT_NAME
        self.initial_scale_fontsize = 14
        self.scale_fontsize = self.initial_scale_fontsize

        # DEFAULT VALUE TEXT STATUS
        self.enable_value_text = True
        self.value_fontname = constants.GAUGE_FONT_NAME
        self.initial_value_fontsize = 40
        self.value_fontsize = self.initial_value_fontsize
        self.text_radius_factor = 0.5

        # ENABLE BAR GRAPH BY DEFAULT
        self.setEnableBarGraph(True)
        # FILL POLYGON COLOR BY DEFAULT
        self.setEnableScalePolygon(True)
        # ENABLE CENTER POINTER BY DEFAULT
        self.enable_CenterPoint = True
        # ENABLE FINE SCALE BY DEFAULT
        self.enable_fine_scaled_marker = True
        # ENABLE BIG SCALE BY DEFAULT
        self.enable_big_scaled_marker = True

        # NEEDLE SCALE FACTOR/LENGTH
        self.needle_scale_factor = 0.8
        # ENABLE NEEDLE POLYGON BY DEFAULT
        self.enable_Needle_Polygon = True

        # SET DEFAULT THEME
        self.set_scale_polygon_colors([[.10, Qt.red], [.25, Qt.yellow], [.5, Qt.green]])
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
        if value <= self.minValue:
            self.value = self.minValue
        elif value >= self.maxValue:
            self.value = self.maxValue
        else:
            self.value = value
        # self.paintEvent("")
        self.valueChanged.emit(int(value))
        # print(self.value)

        # ohne timer: aktiviere self.update()
        self.update()

    def center_horizontal(self, value):
        self.center_horizontal_value = value
        # print("horizontal: " + str(self.center_horizontal_value))

    def center_vertical(self, value):
        self.center_vertical_value = value

    ################################################################################################
    # SHOW HIDE BAR GRAPH
    ################################################################################################
    def setEnableBarGraph(self, enable=True):
        self.enableBarGraph = enable
        self.update()

    ################################################################################################
    # SHOW HIDE VALUE TEXT
    ################################################################################################
    def setEnableValueText(self, enable=True):
        self.enable_value_text = enable
        self.update()

    ################################################################################################
    # SHOW HIDE CENTER POINTER
    ################################################################################################
    def setEnableCenterPoint(self, enable=True):
        self.enable_CenterPoint = enable
        self.update()

    ################################################################################################
    # SHOW HIDE FILLED POLYGON
    ################################################################################################
    def setEnableScalePolygon(self, enable=True):
        self.enable_filled_Polygon = enable
        self.update()

    ################################################################################################
    # SHOW HIDE BIG SCALE
    ################################################################################################
    def setEnableBigScaleGrid(self, enable=True):
        self.enable_big_scaled_marker = enable
        self.update()

    ################################################################################################
    # SHOW HIDE FINE SCALE
    ################################################################################################

    def setEnableFineScaleGrid(self, enable=True):
        self.enable_fine_scaled_marker = enable
        self.update()

    ################################################################################################
    # SHOW HIDE SCALA MAIN CONT
    ################################################################################################
    def setScalaCount(self, count):
        if count < 1:
            count = 1
        self.scalaCount = count
        self.update()

    ################################################################################################
    # SET MINIMUM VALUE
    ################################################################################################
    def setMinValue(self, min):
        if self.value < min:
            self.value = min
        if min >= self.maxValue:
            self.minValue = self.maxValue - 1
        else:
            self.minValue = min
        self.update()

    ################################################################################################
    # SET MAXIMUM VALUE
    ################################################################################################
    def setMaxValue(self, max):
        if self.value > max:
            self.value = max
        if max <= self.minValue:
            self.maxValue = self.minValue + 1
        else:
            self.maxValue = max
        self.update()

    ################################################################################################
    # SET SCALE ANGLE
    ################################################################################################
    def setScaleStartAngle(self, value):
        # Value range in DEG: 0 - 360
        self.scale_angle_start_value = value
        # print("startFill: " + str(self.scale_angle_start_value))
        self.update()

    ################################################################################################
    # SET SCALE SIZE
    ################################################################################################
    def setTotalScaleAngleSize(self, value):
        self.scale_angle_size = value
        # print("stopFill: " + str(self.scale_angle_size))
        self.update()

    ################################################################################################
    # SET GAUGE COLOR OUTER RADIUS
    ################################################################################################
    def setGaugeColorOuterRadiusFactor(self, value):
        self.gauge_color_outer_radius_factor = float(value) / 1000
        self.update()

    ################################################################################################
    # SET GAUGE COLOR INNER RADIUS
    ################################################################################################
    def setGaugeColorInnerRadiusFactor(self, value):
        self.gauge_color_inner_radius_factor = float(value) / 1000
        self.update()

    ################################################################################################
    # SET SCALE POLYGON COLOR
    ################################################################################################
    def set_scale_polygon_colors(self, color_array):
        # print(type(color_array))
        if 'list' in str(type(color_array)):
            self.scale_polygon_colors = color_array
        elif color_array == None:
            self.scale_polygon_colors = [[.0, Qt.transparent]]
        else:
            self.scale_polygon_colors = [[.0, Qt.transparent]]
        self.update()

    ################################################################################################
    # GET MAXIMUM VALUE
    ################################################################################################
    def get_value_max(self):
        return self.maxValue

    # CREATE PIE
    def create_polygon_pie(self, outer_radius, inner_raduis, start, lenght, bar_graph=True):
        polygon_pie = QPolygonF()
        n = 360  # angle steps size for full circle
        w = 360 / n  # angle per step
        x = 0
        y = 0

        if not self.enableBarGraph and bar_graph:
            lenght = int(
                round((lenght / (self.maxValue - self.minValue)) * (self.value - self.minValue)))

        # add the points of polygon
        for i in range(lenght + 1):
            t = w * i + start
            x = outer_radius * math.cos(math.radians(t))
            y = outer_radius * math.sin(math.radians(t))
            polygon_pie.append(QPointF(x, y))
        # create inner circle line from "start + lenght"-angle to "start"-angle add the points of
        # polygon
        for i in range(lenght + 1):
            t = w * (lenght - i) + start
            x = inner_raduis * math.cos(math.radians(t))
            y = inner_raduis * math.sin(math.radians(t))
            polygon_pie.append(QPointF(x, y))

        # close outer line
        polygon_pie.append(QPointF(x, y))
        return polygon_pie

    def draw_filled_polygon(self, outline_pen_with=0):
        if not self.scale_polygon_colors == None:
            painter_filled_polygon = QPainter(self)
            painter_filled_polygon.setRenderHint(QPainter.Antialiasing)
            painter_filled_polygon.translate(
                self.width() / 2, self.height() / 2)

            painter_filled_polygon.setPen(Qt.NoPen)

            self.pen.setWidth(outline_pen_with)
            if outline_pen_with > 0:
                painter_filled_polygon.setPen(self.pen)

            colored_scale_polygon = self.create_polygon_pie(
                ((self.widget_diameter / 2) - (self.pen.width() / 2)) *
                self.gauge_color_outer_radius_factor,
                (((self.widget_diameter / 2) - (self.pen.width() / 2))
                 * self.gauge_color_inner_radius_factor),
                self.scale_angle_start_value, self.scale_angle_size)

            grad = QConicalGradient(QPointF(0, 0),
                                    - self.scale_angle_size - self.scale_angle_start_value - 1)

            for eachcolor in self.scale_polygon_colors:
                grad.setColorAt(eachcolor[0], eachcolor[1])
            painter_filled_polygon.setBrush(grad)

            painter_filled_polygon.drawPolygon(colored_scale_polygon)

    # BIG SCALE MARKERS
    def draw_big_scaled_marker(self):
        my_painter = QPainter(self)
        my_painter.setRenderHint(QPainter.Antialiasing)
        my_painter.translate(self.width() / 2, self.height() / 2)

        self.pen = QPen(self.bigScaleMarker)
        self.pen.setWidth(2)
        my_painter.setPen(self.pen)

        my_painter.rotate(self.scale_angle_start_value)
        steps_size = (float(self.scale_angle_size) / float(self.scalaCount))
        scale_line_outer_start = self.widget_diameter / 2
        scale_line_lenght = (self.widget_diameter / 2) - \
                            (self.widget_diameter / 20)
        for i in range(self.scalaCount + 1):
            my_painter.drawLine(scale_line_lenght, 0,
                                scale_line_outer_start, 0)
            my_painter.rotate(steps_size)

    def create_scale_marker_values_text(self):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.translate(self.width() / 2, self.height() / 2)
        font = QFont(self.scale_fontname, self.scale_fontsize, QFont.Bold)
        fm = QFontMetrics(font)

        pen_shadow = QPen()

        pen_shadow.setBrush(self.ScaleValueColor)
        painter.setPen(pen_shadow)

        text_radius_factor = 0.8
        text_radius = self.widget_diameter / 2 * text_radius_factor

        scale_per_div = int((self.maxValue - self.minValue) / self.scalaCount)

        angle_distance = (float(self.scale_angle_size) /
                          float(self.scalaCount))
        for i in range(self.scalaCount + 1):
            text = str(int(self.minValue + scale_per_div * i))
            w = fm.width(text) + 1
            h = fm.height()
            painter.setFont(QFont(self.scale_fontname,
                                  self.scale_fontsize, QFont.Bold))
            angle = angle_distance * i + float(self.scale_angle_start_value)
            x = text_radius * math.cos(math.radians(angle))
            y = text_radius * math.sin(math.radians(angle))
            # print(w, h, x, y, text)

            text = [x - int(w / 2), y - int(h / 2), int(w),
                    int(h), Qt.AlignCenter, text]
            painter.drawText(text[0], text[1], text[2],
                             text[3], text[4], text[5])
        # painter.restore()

    # FINE SCALE MARKERS
    def create_fine_scaled_marker(self):
        #  Description_dict = 0
        my_painter = QPainter(self)

        my_painter.setRenderHint(QPainter.Antialiasing)
        # Koordinatenursprung in die Mitte der Flaeche legen
        my_painter.translate(self.width() / 2, self.height() / 2)

        my_painter.setPen(self.fineScaleColor)
        my_painter.rotate(self.scale_angle_start_value)
        steps_size = (
                float(self.scale_angle_size) / float(self.scalaCount * self.scala_subdiv_count))
        scale_line_outer_start = self.widget_diameter / 2
        scale_line_lenght = (self.widget_diameter / 2) - (self.widget_diameter / 40)
        for i in range((self.scalaCount * self.scala_subdiv_count) + 1):
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

        pen_shadow.setBrush(self.DisplayValueColor)
        painter.setPen(pen_shadow)

        text_radius = self.widget_diameter / 2 * self.text_radius_factor

        text = str(int(self.value))
        w = fm.width(text) + 1
        h = fm.height()
        painter.setFont(QFont(self.value_fontname,
                              self.value_fontsize, QFont.Bold))

        angle_end = float(self.scale_angle_start_value + self.scale_angle_size - 360)
        angle = (angle_end - self.scale_angle_start_value) / 2 + self.scale_angle_start_value

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
            0, self.scale_angle_start_value, 360, False)

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
            self.scale_angle_start_value / 10, 360, False)

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
        painter.setBrush(self.NeedleColor)
        painter.rotate(((self.value - self.minValue) * self.scale_angle_size /
                        (self.maxValue - self.minValue)) + 90 + self.scale_angle_start_value)

        painter.drawConvexPolygon(self.value_needle[0])

    # ON WINDOW RESIZE
    def resizeEvent(self, event):
        self.rescale_method()

    # ON PAINT EVENT
    def paintEvent(self, event):
        # Main Drawing Event:
        # Will be executed on every change
        # vgl http://doc.qt.io/qt-4.8/qt-demos-affine-xform-cpp.html
        # print("event", event)

        self.draw_outer_circle()
        # colored pie area
        if self.enable_filled_Polygon:
            self.draw_filled_polygon()

        # draw scale marker lines
        if self.enable_fine_scaled_marker:
            self.create_fine_scaled_marker()
        if self.enable_big_scaled_marker:
            self.draw_big_scaled_marker()

        # draw scale marker value text
        self.create_scale_marker_values_text()

        # Display Value
        if self.enable_value_text:
            self.create_values_text()

        # draw needle 1
        if self.enable_Needle_Polygon:
            self.draw_needle()

        # Draw Center Point
        if self.enable_CenterPoint:
            self.draw_big_needle_center_point()
