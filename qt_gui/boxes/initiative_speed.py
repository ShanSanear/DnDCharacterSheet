from PyQt5 import QtWidgets, QtCore

from qt_gui.boxes.qt_generic_classes import DefaultBox
from qt_gui.boxes.qt_generic_functions import create_qlabel, create_qline_edit, set_text_of_children, \
    add_multiple_elements_to_layout_by_row, add_element_to_layout


class InitiativeSpeedBox(DefaultBox):
    def __init__(self, parent, position, size):
        self.root = QtWidgets.QGroupBox(parent)
        self.root.setGeometry(QtCore.QRect(*position, *size))
        self.root.setObjectName("InitiativeSpeedBox")
        self.container = QtWidgets.QWidget(self.root)
        self.container.setObjectName("gridLayoutWidget_7")
        self.layout = QtWidgets.QGridLayout(self.container)
        self.layout.setObjectName("InitiativeSpeedLayout")
        self.layout.setContentsMargins(8, 8, 8, 12)
        self.layout.setSpacing(4)
        self.translate_reference = {
            "EN": {"root": {"title": "Initiative and speed"},
                   "initiative_total": "10",
                   "total_label": "Total",
                   "initiative_misc_bonus": "10",
                   "initiative_dex_bonus": "10",
                   "initiative_misc_bonus_label": "Misc",
                   "initiative_dex_bonus_label": "Dex",
                   "initiative_label": "Init.",
                   "speed_label": "Speed",
                   "speed_total": "10",}}

        self.total_label = create_qlabel("total_label", parent=self.container)
        self.initiative_misc_bonus_label = create_qlabel("initiative_misc_bonus_label", parent=self.container)
        self.initiative_dex_bonus_label = create_qlabel("initiative_dex_bonus_label", parent=self.container)
        self.initiative_label = create_qlabel("initiative_label", parent=self.container)
        self.speed_label = create_qlabel("speed_label", parent=self.container)
        self.speed_armor_type_label = create_qlabel("speed_armor_type_label", parent=self.container)


        self.initiative_total = create_qline_edit("initiative_total", parent=self.container)
        self.initiative_misc_bonus = create_qline_edit("initiative_misc_bonus", parent=self.container)
        self.initiative_dex_bonus = create_qline_edit("initiative_dex_bonus", parent=self.container, enabled=False)
        self.speed_total = create_qline_edit("speed_total", parent=self.container)

        self.add_to_layout()

        self.translate("EN")
        self.root.setLayout(self.layout)

    def add_to_layout(self):
        add_element_to_layout(self.layout, self.total_label, 0, 1, 1, 1)
        add_element_to_layout(self.layout, self.initiative_dex_bonus_label, 0, 2, 1, 1)
        add_element_to_layout(self.layout, self.initiative_misc_bonus_label, 0, 3, 1, 1)

        add_element_to_layout(self.layout, self.speed_label, 0, 4, 1, 1)
        second_row = [self.initiative_label, self.initiative_total, self.initiative_dex_bonus,self.initiative_misc_bonus]
        add_multiple_elements_to_layout_by_row(self.layout, second_row, row=1)
        add_element_to_layout(self.layout, self.speed_total, 1, 4, 1, 1)


    def translate(self, language):
        set_text_of_children(self, self.translate_reference[language])
