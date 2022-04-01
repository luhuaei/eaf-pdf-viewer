# -*- coding: utf-8 -*-

# Copyright (C) 2018 Andy Stewart
#
# Author:     Andy Stewart <lazycat.manatee@gmail.com>
# Maintainer: Andy Stewart <lazycat.manatee@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from PyQt6.QtGui import QColor
from PyQt6.QtCore import Qt

from core.utils import get_emacs_theme_background, get_emacs_theme_foreground, get_emacs_var

class Color():
    def __init__(self):
        self.color_map = {
            "buffer_background": "eaf-buffer-background-color",
            "text_highlight_annot": "eaf-pdf-text-highlight-annot-color",
            "text_underline_annot": "eaf-pdf-text-underline-annot-color",
            "inline_text_annot": "eaf-pdf-inline-text-annot-color",
            "theme_foreground": get_emacs_theme_foreground,
            "theme_background": get_emacs_theme_background,
            "default_background": QColor(20, 20, 20, 255),
            "default_inverted_background": Qt.GlobalColor.white,
            "synctex_indicator_fill": QColor(236, 96, 31, 255),
            "synctex_indicator_border": QColor(255, 91, 15, 255),
            "jump_link_text": QColor(0, 0, 0),
            "jump_link_fill": QColor(255, 197, 36)
        }
    def __getitem__(self, attr):
        var = self.color_map[attr]
        if callable(var):
            return QColor(var())
        elif type(var) == Qt.GlobalColor:
            return var
        elif type(var) == QColor:
            return var
        else:
            return QColor(get_emacs_var(var))

    def rgbfList(self, attr):
        color = self.__getitem__(attr)
        return color.getRgbF()[0:3]
