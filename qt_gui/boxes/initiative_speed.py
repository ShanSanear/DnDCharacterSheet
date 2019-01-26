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
        self.layout.setSpacing(10)
        self.translate_reference = {
            "EN": {"root": {"title": "Initiative and speed"},
                   "initiative_total": "10",
                   "_eq_sign_7": "=",
                   "total_label": "Total",
                   "initiative_misc_bonus": "10",
                   "initiative_dex_bonus": "10",
                   "initiative_misc_bonus_label": "Misc",
                   "initiative_dex_bonus_label": "Dex",
                   "initiative_label": "Init.",
                   "_plus_sign_10": "+",
                   "speed_label": "Sp.",
                   "speed_total": "10",
                   "speed_armor_type_label": "Armor",
                   "speed_armor_type": "Lorem ipsum", }}

        qlabel_eq_sign_dict = dict(parent=self.container, min_size=(8, 20), max_size=(None, 20),
                                   align=QtCore.Qt.AlignCenter)
        qlabel_plus_sign_dict = dict(parent=self.container, min_size=(8, 10), max_size=(10, 10))

        self.total_label = create_qlabel("total_label", parent=self.container)
        self.initiative_misc_bonus_label = create_qlabel("initiative_misc_bonus_label", parent=self.container)
        self.initiative_dex_bonus_label = create_qlabel("initiative_dex_bonus_label", parent=self.container)
        self.initiative_label = create_qlabel("initiative_label", parent=self.container)
        self.speed_label = create_qlabel("speed_label", parent=self.container)
        self.speed_armor_type_label = create_qlabel("speed_armor_type_label", parent=self.container)

        self._eq_sign_7 = create_qlabel("_eq_sign_7", **qlabel_eq_sign_dict)
        self._plus_sign_10 = create_qlabel("_plus_sign_10", **qlabel_plus_sign_dict)

        self.initiative_total = create_qline_edit("initiative_total", parent=self.container)
        self.initiative_misc_bonus = create_qline_edit("initiative_misc_bonus", parent=self.container)
        self.initiative_dex_bonus = create_qline_edit("initiative_dex_bonus", parent=self.container)
        self.speed_total = create_qline_edit("speed_total", parent=self.container)
        self.speed_armor_type = create_qline_edit("speed_armor_type", parent=self.container)

        self.add_to_layout()

        self.translate("EN")
        self.root.setLayout(self.layout)

    def add_to_layout(self):
        add_element_to_layout(self.layout, self.total_label, 0, 1, 1, 1)
        add_element_to_layout(self.layout, self.initiative_dex_bonus_label, 0, 3, 1, 1)
        add_element_to_layout(self.layout, self.initiative_misc_bonus_label, 0, 5, 1, 1)

        second_row = [self.initiative_label, self.initiative_total, self._eq_sign_7,
                      self.initiative_dex_bonus, self._plus_sign_10, self.initiative_misc_bonus, ]
        add_multiple_elements_to_layout_by_row(self.layout, second_row, row=1)

        third_row = [self.speed_label, self.speed_total, self.speed_armor_type_label]
        add_multiple_elements_to_layout_by_row(self.layout, third_row, row=2)

        add_element_to_layout(self.layout, self.speed_armor_type, 2, 3, 1, 3)

    def translate(self, language):
        set_text_of_children(self, self.translate_reference[language])
