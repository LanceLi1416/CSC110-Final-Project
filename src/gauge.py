import math
import os

from PyQt5.QtCore import Qt, QPoint, QPointF, QEvent
from PyQt5.QtGui import QPolygon, QPolygonF, QColor, QPen, QFont, QPainter, QFontMetrics, \
    QConicalGradient, QRadialGradient, QFontDatabase
from PyQt5.QtWidgets import QWidget

import src.constants as constants


class GaugeWidget(QWidget):
    """An analog gauge widget.

    modified from
    https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/custom-analog-gauge.html
    under the GNU General Public License v3.0
    """

    def __init__(self, *args, **kwargs) -> None:
        super(GaugeWidget, self).__init__(*args, **kwargs)

        # Value needle
        self.value_needle = QPolygon()
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
        # self.scale_polygon_colors = [[.10, Qt.red], [.25, Qt.yellow], [.5, Qt.green]]
        self.scale_polygon_colors = [
            [.10, constants.RED],
            [.25, constants.YELLOW],
            [.50, constants.BLUE]]

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
        # self.outer_circle_bg = [
        #     [0.0645161, QColor(30, 35, 45, 255)],
        #     [0.37788, QColor(57, 67, 86, 255)],
        #     [1, QColor(30, 36, 45, 255)]
        # ]
        self.outer_circle_bg = [
            [0, QColor(255, 255, 255, 255)]
        ]

        # Resize gauge
        self.widget_diameter = 0
        self.rescale_method()

    def rescale_method(self) -> None:
        """Rescale the gauge """
        self.widget_diameter = min(self.width(), self.height())

        # Set needle size
        self.value_needle = QPolygon(
            [QPoint(4, 30),
             QPoint(-4, 30),
             QPoint(-2, - self.widget_diameter / 2 * self.needle_scale_factor),
             QPoint(0, - self.widget_diameter / 2 * self.needle_scale_factor - 6),
             QPoint(2, - self.widget_diameter / 2 * self.needle_scale_factor)
             ])

        # Set font size
        self.scale_fontsize = self.initial_scale_fontsize * self.widget_diameter / 400
        self.value_fontsize = self.initial_value_fontsize * self.widget_diameter / 400

    def update_value(self, value) -> None:
        """Update the value of the gauge, and repaint."""
        if value <= self.min_val:
            self.value = self.min_val
        elif value >= self.max_val:
            self.value = self.max_val
        else:
            self.value = value
        self.update()

    def _create_polygon_pie(self, outer_radius: float, inner_radius: float,
                            start: float, length: int) -> QPolygonF:
        """Create the outer polygon pie."""
        polygon_pie = QPolygonF()
        w = 1  # angle per step
        x = 0
        y = 0

        # add the points of polygon
        for i in range(length + 1):
            t = w * i + start
            x = outer_radius * math.cos(math.radians(t))
            y = outer_radius * math.sin(math.radians(t))
            polygon_pie.append(QPointF(x, y))
        # create inner circle line
        for i in range(length + 1):
            t = w * (length - i) + start
            x = inner_radius * math.cos(math.radians(t))
            y = inner_radius * math.sin(math.radians(t))
            polygon_pie.append(QPointF(x, y))

        # close outer line
        polygon_pie.append(QPointF(x, y))
        return polygon_pie

    def _draw_filled_polygon(self, outline_pen_with=0) -> None:
        """Draws the outer filled pie area"""
        painter_filled_polygon = QPainter(self)
        painter_filled_polygon.setRenderHint(QPainter.Antialiasing)
        painter_filled_polygon.translate(
            self.width() / 2, self.height() / 2)

        painter_filled_polygon.setPen(Qt.NoPen)

        self.pen.setWidth(outline_pen_with)
        if outline_pen_with > 0:
            painter_filled_polygon.setPen(self.pen)

        colored_scale_polygon = self._create_polygon_pie(
            ((self.widget_diameter / 2) - (self.pen.width() / 2)) * 1,
            (((self.widget_diameter / 2) - (self.pen.width() / 2)) * 0.9
             ),
            self.scale_angle_start, self.scale_angle_size)

        grad = QConicalGradient(QPointF(0, 0), - self.scale_angle_size - self.scale_angle_start - 1)

        for color in self.scale_polygon_colors:
            grad.setColorAt(color[0], color[1])
        painter_filled_polygon.setBrush(grad)

        painter_filled_polygon.drawPolygon(colored_scale_polygon)

    def _draw_big_scaled_marker(self) -> None:
        """Draw the markers for the big scales."""
        my_painter = QPainter(self)
        my_painter.setRenderHint(QPainter.Antialiasing)
        my_painter.translate(self.width() / 2, self.height() / 2)

        self.pen = QPen(constants.GAUGE_BIG_SCALE_COLOR)
        self.pen.setWidth(2)
        my_painter.setPen(self.pen)

        my_painter.rotate(self.scale_angle_start)
        steps_size = (float(self.scale_angle_size) / float(self.scala_count))
        scale_line_outer_start = self.widget_diameter / 2
        scale_line_length = (self.widget_diameter / 2) - (self.widget_diameter / 20)
        for i in range(self.scala_count + 1):
            my_painter.drawLine(scale_line_length, 0, scale_line_outer_start, 0)
            my_painter.rotate(steps_size)

    def _create_scale_marker_values_text(self) -> None:
        """Create the text for the scale."""
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

            text = [x - int(w / 2), y - int(h / 2), int(w), int(h), Qt.AlignCenter, text]
            painter.drawText(text[0], text[1], text[2], text[3], text[4], text[5])

    def _create_fine_scaled_marker(self):
        """Create the markers for the fine scale"""
        my_painter = QPainter(self)

        my_painter.setRenderHint(QPainter.Antialiasing)
        my_painter.translate(self.width() / 2, self.height() / 2)

        my_painter.setPen(constants.GAUGE_FINE_SCALE_COLOR)
        my_painter.rotate(self.scale_angle_start)
        steps_size = (
                float(self.scale_angle_size) / float(self.scala_count * self.scala_subdiv_count))
        scale_line_outer_start = self.widget_diameter / 2
        scale_line_length = (self.widget_diameter / 2) - (self.widget_diameter / 40)
        for i in range((self.scala_count * self.scala_subdiv_count) + 1):
            my_painter.drawLine(scale_line_length, 0, scale_line_outer_start, 0)
            my_painter.rotate(steps_size)

    def _create_values_text(self) -> None:
        """Create the main value text"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.HighQualityAntialiasing)

        painter.translate(self.width() / 2, self.height() / 2)
        font = QFont(self.value_fontname, self.value_fontsize, QFont.Bold)
        font_matrices = QFontMetrics(font)

        pen_shadow = QPen()

        pen_shadow.setBrush(constants.GAUGE_TEXT_COLOR)
        painter.setPen(pen_shadow)

        text_radius = self.widget_diameter / 2 * 0.5

        text = f'{self.value:.0f} %'
        w = font_matrices.width(text) + 1
        h = font_matrices.height()
        painter.setFont(QFont(self.value_fontname, self.value_fontsize, QFont.Bold))

        angle_end = float(self.scale_angle_start + self.scale_angle_size - 360)
        angle = (angle_end - self.scale_angle_start) / 2 + self.scale_angle_start

        x = text_radius * math.cos(math.radians(angle))
        y = text_radius * math.sin(math.radians(angle))
        text = [x - int(w / 2), y - int(h / 2), int(w), int(h), Qt.AlignCenter, text]
        painter.drawText(text[0], text[1], text[2], text[3], text[4], text[5])

    def _draw_center_point_cover(self) -> None:
        """Draw the center pointer cover"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.translate(self.width() / 2, self.height() / 2)
        painter.setPen(Qt.NoPen)

        colored_scale_polygon = self._create_polygon_pie(
            ((self.widget_diameter / 8) - (self.pen.width() / 2)),
            0, self.scale_angle_start, 360)

        grad = QConicalGradient(QPointF(0, 0), 0)

        for color in self.needle_center_bg:
            grad.setColorAt(color[0], color[1])
        painter.setBrush(grad)

        painter.drawPolygon(colored_scale_polygon)

    def _draw_outer_circle(self) -> None:
        """Create the outer circle of the gauge"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.translate(self.width() / 2, self.height() / 2)
        painter.setPen(Qt.NoPen)
        colored_scale_polygon = self._create_polygon_pie(
            ((self.widget_diameter / 2) - (self.pen.width())),
            (self.widget_diameter / 6), self.scale_angle_start / 10, 360)

        radial_gradient = QRadialGradient(QPointF(0, 0), self.width())

        for color in self.outer_circle_bg:
            radial_gradient.setColorAt(color[0], color[1])

        painter.setBrush(radial_gradient)

        painter.drawPolygon(colored_scale_polygon)

    def _draw_needle(self) -> None:
        """Draw the needle pointer"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(self.width() / 2, self.height() / 2)
        painter.setPen(Qt.NoPen)
        painter.setBrush(constants.GAUGE_NEEDLE_COLOR)
        painter.rotate(((self.value - self.min_val) * self.scale_angle_size /
                        (self.max_val - self.min_val)) + 90 + self.scale_angle_start)

        painter.drawConvexPolygon(self.value_needle)

    def resizeEvent(self, event: QEvent) -> None:
        """The resize event. Called automatically on window resize."""
        self.rescale_method()

    def paintEvent(self, event: QEvent) -> None:
        """The main drawing event for the gauge. Called automatically on paint event."""
        self._draw_outer_circle()
        # colored pie area
        self._draw_filled_polygon()
        # draw scale marker lines
        self._create_fine_scaled_marker()
        self._draw_big_scaled_marker()
        # draw scale marker value text
        self._create_scale_marker_values_text()
        # Display value
        self._create_values_text()
        # draw needle
        self._draw_needle()
        # Draw center point
        self._draw_center_point_cover()
