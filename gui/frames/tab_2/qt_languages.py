from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication

from gui.frames.qt_generic_classes import DefaultBox, BoxType
from gui.frames.qt_generic_functions import create_qlabel


class LanguagesBox(BoxType, DefaultBox):
    # TODO - change PlainTextEdit to something else?

    def __init__(self, parent, position, size):
        BoxType.__init__(self, parent=parent, position=position, size=size)
        self.known_languages_label = create_qlabel(parent=self.container, align=QtCore.Qt.AlignCenter)
        self.known_languages = QtWidgets.QPlainTextEdit(self.container)
        self.add_to_layout()

    def add_to_layout(self):
        self.layout.addWidget(self.known_languages_label)
        self.layout.addWidget(self.known_languages)

    def retranslate(self):
        self.root.setTitle(QApplication.translate("Language", "Languages"))
        self.known_languages_label.setText(QApplication.translate("Language", "Known languages"))
