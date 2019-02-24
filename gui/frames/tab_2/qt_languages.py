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
                "known_languages": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sapien urna, "
                                   "egestas eu tempor at, pretium nec orci. In nec pharetra tellus. In malesuada erat "
                                   "tellus, eget efficitur elit convallis eu. Integer consectetur porttitor eros "
                                   "vitae sagittis. Vestibulum commodo suscipit varius. Nulla vitae fringilla velit. "
                                   "Mauris sagittis tellus urna. Class aptent taciti sociosqu ad litora torquent per "
                                   "conubia nostra, per inceptos himenaeos. Fusce in arcu justo.\n\nMauris auctor, "
                                   "elit sed tristique maximus, libero quam feugiat dolor, in laoreet massa libero a "
                                   "tortor. Donec molestie pretium tempus. Integer lacinia magna lacus, nec volutpat "
                                   "felis condimentum id. Vivamus orci ante, gravida sed velit vel, venenatis "
                                   "pellentesque est. Maecenas laoreet laoreet ullamcorper. Phasellus rutrum felis "
                                   "non sapien aliquam semper. Morbi tempus, quam in luctus tempor, mauris neque "
                                   "faucibus libero, ut porta justo sem eu orci. Suspendisse consectetur sem ac neque "
                                   "mollis, sed iaculis tellus elementum. Nulla facilisis turpis vel sagittis "
                                   "pharetra. Donec nec odio pharetra, vestibulum lorem accumsan, tempus nulla. Donec "
                                   "blandit nisi in elit pulvinar, nec feugiat metus egestas. "
            }
        }
        self.translate("EN")

    def add_to_layout(self):
        self.layout.addWidget(self.known_languages_label)
        self.layout.addWidget(self.known_languages)

    def translate(self, language):
        set_text_of_children(self, self.translate_reference[language])
