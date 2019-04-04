import json
from pathlib import Path

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QGroupBox, QGridLayout, QWidget, QApplication

from gui.frames.qt_generic_classes import DefaultBox
from gui.frames.qt_generic_functions import create_qlabel, \
    add_multiple_elements_to_layout_by_column, add_multiple_elements_to_layout_by_row


class ExperienceSheet(DefaultBox):
    def __init__(self, parent, position, size):
        self.parent = parent
        self.root = QGroupBox(parent)
        self.root.setGeometry(QtCore.QRect(*position, *size))
        self.container = QWidget(self.root)
        self.layout = QGridLayout(self.container)
        self.root.setLayout(self.layout)

        levels_file = Path("data/cheatsheet_levels.json")
        levels_data = json.load(levels_file.open())

        self.labels = []
        self.exps = []
        for level, data in levels_data.items():
            label = create_qlabel(parent=self.container, text=data["label"], align=Qt.AlignRight | Qt.AlignVCenter)
            label.setFont(QFont('Monospace', 9, QFont.Monospace))
            exp = create_qlabel(parent=self.container, text=str(data["exp"]), align=Qt.AlignCenter | Qt.AlignVCenter)
            exp.setFont(QFont('Monospace', 9, QFont.Monospace))
            self.labels.append(label)
            self.exps.append(exp)

        self.add_to_layout()

    def add_to_layout(self):
        lvl_label_1 = create_qlabel(self.container, text="lvl", align=Qt.AlignRight | Qt.AlignVCenter)
        lvl_label_2 = create_qlabel(self.container, text="lvl", align=Qt.AlignRight | Qt.AlignVCenter)
        xp_label_1 = create_qlabel(self.container, text="XP", align=Qt.AlignCenter | Qt.AlignVCenter)
        xp_label_2 = create_qlabel(self.container, text="XP", align=Qt.AlignCenter | Qt.AlignVCenter)
        add_multiple_elements_to_layout_by_row(layout=self.layout,
                                               elements_to_add=[lvl_label_1, xp_label_1, lvl_label_2, xp_label_2])
        add_multiple_elements_to_layout_by_column(layout=self.layout, elements_to_add=self.labels[:10],
                                                  column=0, start_row=1)
        add_multiple_elements_to_layout_by_column(layout=self.layout, elements_to_add=self.exps[:10],
                                                  column=1, start_row=1)
        add_multiple_elements_to_layout_by_column(layout=self.layout, elements_to_add=self.labels[10:],
                                                  column=2, start_row=1)
        add_multiple_elements_to_layout_by_column(layout=self.layout, elements_to_add=self.exps[10:],
                                                  column=3, start_row=1)

    def retranslate(self):
        self.root.setTitle(QApplication.translate("Experience", "Experience"))
