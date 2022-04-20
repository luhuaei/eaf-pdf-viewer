from PyQt6.QtCore import Qt, QRect, QPoint
from PyQt6.QtGui import QPainter

class Progress():
    def __init__(self):
        pass

    def paint(self, painter, option, model_index):
        view_rect = painter.viewport()
        current = model_index.row()
        total = model_index.model().rowCount(model_index)
        progress_percent = int(current * 100 / total)

        progress_rect = QRect(view_rect.bottomRight() - QPoint(100, 100), view_rect.bottomRight())
        painter.eraseRect(progress_rect)
        painter.drawText(progress_rect,
                         Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom,
                         "{0}% ({1}/{2})".format(progress_percent, current, total))

    def role(self):
        return Qt.ItemDataRole.UserRole + 1
