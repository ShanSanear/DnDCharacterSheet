from PyQt5 import QtWidgets, QtCore

from gui.frames.qt_generic_classes import DefaultBox, BoxType
from gui.frames.qt_generic_functions import create_qlabel, set_text_of_children


class LanguagesBox(BoxType, DefaultBox):
    # TODO - change PlainTextEdit to something else?

    def __init__(self, parent, position, size):
        BoxType.__init__(self, parent=parent, position=position, size=size)
        self.known_languages_label = create_qlabel(parent=self.container, align=QtCore.Qt.AlignCenter)
        self.known_languages = QtWidgets.QPlainTextEdit(self.container)
        self.add_to_layout()
        self.translate_reference = {
            "EN": {
                "root": {
                    "title": "Languages",
                },
                "known_languages_label": "Known Languages",
            }
        }
        self.translate("EN")

    def add_to_layout(self):
        self.layout.addWidget(self.known_languages_label)
        self.layout.addWidget(self.known_languages)

    def translate(self, language):
        set_text_of_children(self, self.translate_reference[language])

    def set_default_state(self):
        self.known_languages.setPlainText("")
