from PyQt6.QtCore import Qt, QRect
from PyQt6.QtGui import QPainter

class Pixmap():
    def __init__(self, color, setting):
        self._color = color
        self._setting = setting

    def brush_pen_color(self):
        # Draw background.
        # change color of background if inverted mode is enable
        if self._setting.follow_emacs_theme:
            color = self._color["theme_background"]
        elif self._setting.inverted_mode:
            color = self._color["default_background"]
        else:
            color = self._color["default_inverted_background"]

        return color

    def paint(self, painter, option, model_index):
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceAtop)
        painter.save()

        color = self.brush_pen_color()
        painter.setBrush(color)
        painter.setPen(color)

        qpixmap = model_index.data(Qt.ItemDataRole.DecorationRole)

        # the page qpixmap rect
        # FIXME:
        # make qpixmap horizontal center when qpixmap overflow visual rect
        rect = QRect(option.rect.x(), option.rect.y(), qpixmap.size().width(), qpixmap.size().height())

        # move the qpixmap rect to visual rect center
        rect.moveCenter(option.rect.center())

        # draw qpixmap rect background color
        painter.drawRect(rect)

        # draw page qpixmap contents
        painter.drawPixmap(rect, qpixmap)
        painter.restore()

    def role(self):
        return Qt.ItemDataRole.UserRole
