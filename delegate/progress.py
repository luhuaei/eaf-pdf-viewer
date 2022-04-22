from PyQt6.QtCore import Qt, QRect, QPoint
from PyQt6.QtGui import QPainter, QFont

class Progress():
    def __init__(self):
        pass

    def paint(self, painter, option, model_index):
        view_rect = painter.viewport()

        current = model_index.row()
        total = model_index.model().rowCount(model_index)
        progress_percent = int(current * 100 / total)

        progress_rect = QRect(view_rect.bottomRight() - QPoint(180, 40), view_rect.bottomRight())

        # compute pdf page rect
        size = model_index.data(Qt.ItemDataRole.SizeHintRole)
        rect = QRect(option.rect.topLeft(), size)

        # if page intersects with progress, set background color
        if rect.intersects(progress_rect):
            brush = model_index.data(Qt.ItemDataRole.BackgroundRole)
            painter.fillRect(progress_rect, brush)
        else:
            painter.eraseRect(progress_rect)

        font = QFont()
        font.setPointSize(24)
        painter.setFont(font)

        painter.drawText(progress_rect,
                         Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom,
                         "{0}% ({1}/{2})".format(progress_percent, current, total))

    def role(self):
        return Qt.ItemDataRole.UserRole + 1
