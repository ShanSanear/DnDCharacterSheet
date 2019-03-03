from PyQt5 import QtWidgets, QtCore

from gui.frames.qt_generic_classes import DefaultBox, BoxType
from gui.frames.qt_generic_functions import set_text_of_children, create_qlabel


class NotesBox(BoxType, DefaultBox):
    def __init__(self, parent, position, size):
        BoxType.__init__(self, parent=parent, position=position, size=size, margins=[10, 10, 10, 10])
        self.translate_reference = {
            "EN":
                {
                    "root": {
                        "title": "Notes",
                    },
                    "notes_label": "Notes",
                }
        }
        self.notes_label = create_qlabel(self.container, align=QtCore.Qt.AlignCenter)
        self.notes = QtWidgets.QPlainTextEdit(self.container)
        self.translate("EN")
        self.add_to_layout()
        self.root.setLayout(self.layout)

    def add_to_layout(self):
        self.layout.addWidget(self.notes_label)
        self.layout.addWidget(self.notes)

    def translate(self, language):
        set_text_of_children(self, self.translate_reference[language])
