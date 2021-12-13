# -*- coding: <UTF-8> -*-
"""Your Anxiety During COVID-19: data

Module Description
==================
This module defines the look of the analogue gauge used in the MainWindow. This widget is inspired
and modified from
https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/custom-analog-gauge.html,
permitted by the GNU General Public License v3.0 (GPLv3).

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
import math
import os
import platform
from typing import Dict, Union

from PyQt5.QtCore import Qt, QPoint, QPointF
from PyQt5.QtGui import QPolygon, QPolygonF, QPen, QFont, QPainter, QFontMetrics, \
    QConicalGradient, QRadialGradient, QFontDatabase, QResizeEvent, QPaintEvent
from PyQt5.QtWidgets import QWidget

import constants


def _create_polygon_pie(outer_radius: float, inner_radius: float,
                        start: float, length: int) -> QPolygonF:
    """Create the outer polygon pie.

    Preconditions:
      - inner_radius < outer_radius
    """
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


class GaugeWidget(QWidget):
    """An analog gauge widget.

    Instance Attributes:
      - value_needle: the value needle shape
      - pen: the QPen object in charge of drawing the shapes
      - values: a dictionary storing all the numerical values used by the gauge, with the key being
                the name / purpose of the value
      - diameter: the diameter of the gauge, used when rescaling the widget
    """
    _value_needle: QPolygon
    _pen: QPen
    _values: Dict[str, Union[int, float]]
    _diameter: int

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # Value needle
        self._value_needle = QPolygon()
        self._pen = QPen()

        self._values = {
            # min, max and current value
            'min_val': 0,
            'value': 0.0,
            'max_val': 100,
            # scale
            'scale_angle_start': 135,
            'scale_angle_size': 270,
            # number of scales
            'scala_count': 10,
            'scala_subdiv_count': 5,
            # scalable font sizes
            'scale_fontsize': 14.0,
            'value_fontsize': 40.0,
            # needle length (0 to 1)
            'needle_length': 0.75
        }

        # Load custom font
        QFontDatabase.addApplicationFont(
            os.path.join(os.path.dirname(__file__), constants.GAUGE_FONT_PATH)
        )

        # Resize gauge
        self._diameter = 0
        self.rescale_method()

    def rescale_method(self) -> None:
        """Rescale the gauge """
        self._diameter = min(self.width(), self.height())

        # Set needle size
        self._value_needle = QPolygon(
            [QPoint(4, 30),
             QPoint(-4, 30),
             QPoint(-2, - self._diameter / 2 * self._values['needle_length']),
             QPoint(0, - self._diameter / 2 * self._values['needle_length'] - 6),
             QPoint(2, - self._diameter / 2 * self._values['needle_length'])
             ])

        # Set font size
        scale_factor = 400
        if platform.system() == 'Darwin':
            scale_factor = 250
        self._values['scale_fontsize'] = 14 * self._diameter / scale_factor
        self._values['value_fontsize'] = 40 * self._diameter / scale_factor

    def update_value(self, value: float) -> None:
        """Update the value of the gauge, and repaint.

        Preconditions:
          - self.values['min_val'] <= value <= self.values[max_val]"""
        self._values['value'] = value
        self.update()

    def _draw_filled_polygon(self, outline_pen_with: int = 0) -> None:
        """Draws the outer filled pie area"""
        painter_filled_polygon = QPainter(self)
        painter_filled_polygon.setRenderHint(QPainter.Antialiasing)
        painter_filled_polygon.translate(
            self.width() / 2, self.height() / 2)

        painter_filled_polygon.setPen(Qt.NoPen)

        self._pen.setWidth(outline_pen_with)
        if outline_pen_with > 0:
            painter_filled_polygon.setPen(self._pen)

        colored_scale_polygon = _create_polygon_pie(
            ((self._diameter / 2) - (self._pen.width() / 2)) * 1,
            (((self._diameter / 2) - (self._pen.width() / 2)) * 0.9),
            self._values['scale_angle_start'], self._values['scale_angle_size'])

        grad = QConicalGradient(QPointF(0, 0), - self._values['scale_angle_size'] - self._values[
            'scale_angle_start'] - 1)

        for color in constants.GAUGE_SCALE_POLYGON_GRAD_COLOR:
            grad.setColorAt(color[0], color[1])
        painter_filled_polygon.setBrush(grad)

        painter_filled_polygon.drawPolygon(colored_scale_polygon)

    def _draw_big_scaled_marker(self) -> None:
        """Draw the markers for the big scales."""
        my_painter = QPainter(self)
        my_painter.setRenderHint(QPainter.Antialiasing)
        my_painter.translate(self.width() / 2, self.height() / 2)

        self._pen = QPen(constants.GAUGE_BIG_SCALE_COLOR)
        self._pen.setWidth(2)
        my_painter.setPen(self._pen)

        my_painter.rotate(self._values['scale_angle_start'])
        steps_size = (float(self._values['scale_angle_size']) / float(self._values['scala_count']))
        scale_line_outer_start = self._diameter / 2
        scale_line_length = (self._diameter / 2) - (self._diameter / 20)
        for _ in range(self._values['scala_count'] + 1):
            my_painter.drawLine(scale_line_length, 0, scale_line_outer_start, 0)
            my_painter.rotate(steps_size)

    def _create_scale_marker_values_text(self) -> None:
        """Create the text for the scale."""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.translate(self.width() / 2, self.height() / 2)
        font_matrices = QFontMetrics(
            QFont(constants.GAUGE_FONT_NAME, self._values['scale_fontsize'], QFont.Bold))

        pen_shadow = QPen()

        pen_shadow.setBrush(constants.GAUGE_SCALE_TEXT_COLOR)
        painter.setPen(pen_shadow)

        text_radius_factor = 0.8
        text_radius = self._diameter / 2 * text_radius_factor

        scale_per_div = int(
            (self._values['max_val'] - self._values['min_val']) / self._values['scala_count'])

        angle_distance = (self._values['scale_angle_size'] / self._values['scala_count'])

        for i in range(self._values['scala_count'] + 1):
            text = str(self._values['min_val'] + scale_per_div * i)
            w = font_matrices.width(text) + 1
            h = font_matrices.height()
            painter.setFont(
                QFont(constants.GAUGE_FONT_NAME, self._values['scale_fontsize'], QFont.Bold))
            angle = angle_distance * i + float(self._values['scale_angle_start'])
            x = text_radius * math.cos(math.radians(angle))
            y = text_radius * math.sin(math.radians(angle))

            text = [x - int(w / 2), y - int(h / 2), int(w), int(h), Qt.AlignCenter, text]
            painter.drawText(text[0], text[1], text[2], text[3], text[4], text[5])

    def _create_fine_scaled_marker(self) -> None:
        """Create the markers for the fine scale"""
        my_painter = QPainter(self)

        my_painter.setRenderHint(QPainter.Antialiasing)
        my_painter.translate(self.width() / 2, self.height() / 2)

        my_painter.setPen(constants.GAUGE_FINE_SCALE_COLOR)
        my_painter.rotate(self._values['scale_angle_start'])
        steps_size = (float(self._values['scale_angle_size']) / float(
            self._values['scala_count'] * self._values['scala_subdiv_count']))
        scale_line_outer_start = self._diameter / 2
        scale_line_length = (self._diameter / 2) - (self._diameter / 40)
        for _ in range((self._values['scala_count'] * self._values['scala_subdiv_count']) + 1):
            my_painter.drawLine(scale_line_length, 0, scale_line_outer_start, 0)
            my_painter.rotate(steps_size)

    def _create_values_text(self) -> None:
        """Create the main value text"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.HighQualityAntialiasing)

        painter.translate(self.width() / 2, self.height() / 2)
        font = QFont(constants.GAUGE_FONT_NAME, self._values['value_fontsize'], QFont.Bold)
        font_matrices = QFontMetrics(font)

        pen_shadow = QPen()

        pen_shadow.setBrush(constants.GAUGE_TEXT_COLOR)
        painter.setPen(pen_shadow)

        text_radius = self._diameter / 2 * 0.5

        text = f'{self._values["value"]:.0f} %'
        w = font_matrices.width(text) + 1
        h = font_matrices.height()
        painter.setFont(
            QFont(constants.GAUGE_FONT_NAME, self._values['value_fontsize'], QFont.Bold))

        angle_end = float(
            self._values['scale_angle_start'] + self._values['scale_angle_size'] - 360)
        angle = (angle_end - self._values['scale_angle_start']) / 2 + self._values[
            'scale_angle_start']

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

        colored_scale_polygon = _create_polygon_pie(
            ((self._diameter / 8) - (self._pen.width() / 2)), 0, self._values['scale_angle_start'],
            360)

        grad = QConicalGradient(QPointF(0, 0), 0)

        for color in constants.GAUGE_CENTER_COVER_GRAD_COLOR:
            grad.setColorAt(color[0], color[1])
        painter.setBrush(grad)

        painter.drawPolygon(colored_scale_polygon)

    def _draw_outer_circle(self) -> None:
        """Create the outer circle of the gauge"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.translate(self.width() / 2, self.height() / 2)
        painter.setPen(Qt.NoPen)
        colored_scale_polygon = _create_polygon_pie(((self._diameter / 2) - (self._pen.width())),
                                                    (self._diameter / 6),
                                                    self._values['scale_angle_start'] / 10, 360)

        radial_gradient = QRadialGradient(QPointF(0, 0), self.width())

        for color in constants.GAUGE_BACKGROUND_GRAD_COLOR:
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
        r = ((self._values['value'] - self._values['min_val']) * self._values[
            'scale_angle_size'] / (self._values['max_val'] - self._values['min_val'])) + 90 + \
            self._values['scale_angle_start']
        painter.rotate(r)

        painter.drawConvexPolygon(self._value_needle)

    def resizeEvent(self, event: QResizeEvent) -> None:
        """The resize event. Called automatically on window resize."""
        self.rescale_method()

    def paintEvent(self, event: QPaintEvent) -> None:
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


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'math', 'os', 'platform', 'PyQt5.QtCore',
                          'PyQt5.QtGui', 'PyQt5.QtWidgets', 'constants'],
        'allowed-io': [],
        'max-line-length': 100,
        # 'disable': ['R1705', 'C0200']
        # E0611 (no-name-in-module): python_ta fails to find PyQt5 modules even if they exist
        # C0103 (invalid-name), W0613 (unused-argument): resizeEvent(self, event: QEvent) and
        #       paintEvent(self, event: QEvent) are the methods provided in PyQt5.QtWidgets, which
        #       uses a different naming conversion than the one we use in CSC110. These two methods
        #       also requires to pass the trigger event(QResizeEvent / QPaintEvent) as the
        #       parameter, defined by the signature model in QWidget.
        'disable': ['R1705', 'C0200', 'E0611', 'C0103', 'W0613']
    })

    import python_ta.contracts

    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod()
