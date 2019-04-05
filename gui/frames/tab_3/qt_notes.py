from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication

from gui.frames.qt_generic_classes import DefaultBox, BoxType
from gui.frames.qt_generic_functions import create_qlabel


class NotesBox(BoxType, DefaultBox):
    def __init__(self, parent, position, size):
        BoxType.__init__(self, parent=parent, position=position, size=size, margins=[10, 10, 10, 10])
        self.notes_label = create_qlabel(self.container, align=QtCore.Qt.AlignCenter)
        self.notes = QtWidgets.QPlainTextEdit(self.container)
        self.add_to_layout()
        self.root.setLayout(self.layout)

    def add_to_layout(self):
        self.layout.addWidget(self.notes_label)
        self.layout.addWidget(self.notes)

    def retranslate(self):
        self.root.setTitle(QApplication.translate("Notes", "Notes"))
        self.notes_label.setText(QApplication.translate("Notes", "Notes"))
