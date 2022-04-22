from PyQt6.QtCore import Qt, QRect
from PyQt6.QtGui import QPainter

class Pixmap():
    def __init__(self):
        pass

    def paint(self, painter, option, model_index):
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceAtop)
        painter.save()

        brush = model_index.data(Qt.ItemDataRole.BackgroundRole)
        painter.setBrush(brush)

        # set pen color with brush color avoid page border
        painter.setPen(brush.color())

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
