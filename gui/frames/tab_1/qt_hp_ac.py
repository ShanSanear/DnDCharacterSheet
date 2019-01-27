from PyQt5 import QtWidgets, QtCore

from gui.frames.qt_generic_classes import DefaultBox
from gui.frames.qt_generic_functions import create_qlabel, create_qline_edit, add_element_to_layout, \
    add_multiple_elements_to_layout_by_row, set_text_of_children


class HpAcBox(DefaultBox):
    def __init__(self, parent, position, size):
        self.root = QtWidgets.QGroupBox(parent)
        self.root.setGeometry(QtCore.QRect(*position, *size))
        self.root.setObjectName("HpAcBox")
        self.container = QtWidgets.QWidget(self.root)
        self.container.setObjectName("layoutWidget")
        self.layout = QtWidgets.QGridLayout(self.container)
        self.layout.setObjectName("HpAcLayout")
        self.layout.setContentsMargins(20, 10, 10, 20)
        self.layout.setSpacing(8)
        self.translate_reference = {
            "EN":
                {
                    "root": {
                        "title": "HP / AC"
                    },
                    "hp_total_label": "Total",
                    "hp_hp_wounds_current_hp_label": "Wounds / Current HP",
                    "hp_label": "HP",
                    "hp_total": "10",
                    "ac_label": "AC",
                    "ac_total": "10",
                    "ac_base": "10",
                    "ac_armor_bonus": "10",
                    "ac_shield_bonus": "10",
                    "ac_dex_bonus": "10",
                    "ac_size_bonus": "10",
                    "ac_misc_bonus": "10",
                    "ac_total_label": "Total",
                    "ac_base_bonus_label": "Base",
                    "ac_armor_bonus_label": "Armor",
                    "ac_shield_bonus_label": "Shield",
                    "ac_dex_bonus_label": "Dex",
                    "ac_size_bonus_label": "Size",
                    "ac_misc_bonus_label": "Misc",
                    "hp_hp_wounds_current_hp": "10/10",
                    "hp_dice_label" : "HP Dice",
                    "hp_dice" : "d10",
                    "hp_contusion": "10",
                    "contusion_label": "Contusion",
                }
        }
        self.hp_total_label = create_qlabel("hp_ac_hp_total_label", self.container)
        self.hp_hp_wounds_current_hp_label = create_qlabel("hp_ac_hp_hp_wounds_current_hp_label", self.container)
        self.hp_label = create_qlabel("hp_ac_hp_label", self.container)
        self.hp_total = create_qline_edit("hp_ac_hp_total", self.container)
        self.ac_label = create_qlabel("hp_ac_ac_label", self.container)
        self.hp_dice_label = create_qlabel("hp_ac_hp_dice_label", self.container)
        self.hp_dice = create_qline_edit("hp_ac_hp_dice", self.container)
        self.ac_total = create_qline_edit("hp_ac_ac_total", self.container)
        self.ac_base = create_qline_edit("hp_ac_ac_base", self.container)
        self.ac_armor_bonus = create_qline_edit("hp_ac_ac_armor_bonus", self.container)
        self.ac_shield_bonus = create_qline_edit("hp_ac_ac_shield_bonus", self.container)
        self.ac_dex_bonus = create_qline_edit("hp_ac_ac_dex_bonus", self.container)
        self.ac_size_bonus = create_qline_edit("hp_ac_ac_size_bonus", self.container)
        self.ac_misc_bonus = create_qline_edit("hp_ac_ac_misc_bonus", self.container)
        self.ac_total_label = create_qlabel("hp_ac_ac_total_label", self.container)
        self.ac_base_bonus_label = create_qlabel("hp_ac_ac_base_bonus_label", self.container)
        self.ac_armor_bonus_label = create_qlabel("hp_ac_ac_armor_bonus_label", self.container)
        self.ac_shield_bonus_label = create_qlabel("hp_ac_ac_shield_bonus_label", self.container)
        self.ac_dex_bonus_label = create_qlabel("hp_ac_ac_dex_bonus_label", self.container)
        self.ac_size_bonus_label = create_qlabel("hp_ac_ac_size_bonus_label", self.container)
        self.ac_misc_bonus_label = create_qlabel("hp_ac_ac_misc_bonus_label", self.container)
        self.hp_hp_wounds_current_hp = create_qline_edit("hp_ac_hp_hp_wounds_current_hp", self.container)
        self.hp_contusion = create_qline_edit("hp_ac_hp_contusion", self.container)
        self.contusion_label = create_qlabel("hp_ac_contusion_label", self.container)

        self.add_to_layout()
        self.translate("EN")
        self.root.setLayout(self.layout)

    def add_to_layout(self):
        add_element_to_layout(self.layout, self.hp_total_label, 0, 1, 1, 1)
        add_element_to_layout(self.layout, self.hp_hp_wounds_current_hp_label, 0, 2, 1, 2)
        self.layout.addWidget(self.hp_hp_wounds_current_hp, 1, 2, 1, 2)
        add_element_to_layout(self.layout, self.contusion_label, 0, 4, 1, 2)
        add_element_to_layout(self.layout, self.hp_dice_label, 0, 6, 1, 2)

        add_element_to_layout(self.layout, self.hp_label, 1, 0, 1, 1)
        add_element_to_layout(self.layout, self.hp_total, 1, 1, 1, 1)
        add_element_to_layout(self.layout, self.hp_contusion, 1, 4, 1, 2)
        add_element_to_layout(self.layout, self.hp_dice, 1, 6, 1, 2)

        third_row = [self.ac_label, self.ac_total, self.ac_base,
                     self.ac_armor_bonus, self.ac_shield_bonus,
                     self.ac_dex_bonus, self.ac_size_bonus,self.ac_misc_bonus]
        add_multiple_elements_to_layout_by_row(self.layout, third_row, row=2)

        # TODO need to add them in another fasion (with additional offsets?)
        self.layout.addWidget(self.ac_total_label, 3, 1, 1, 1)
        self.layout.addWidget(self.ac_base_bonus_label, 3, 2, 1, 1)
        self.layout.addWidget(self.ac_armor_bonus_label, 3, 3, 1, 1)
        self.layout.addWidget(self.ac_shield_bonus_label, 3, 4, 1, 1)
        self.layout.addWidget(self.ac_dex_bonus_label, 3, 5, 1, 1)
        self.layout.addWidget(self.ac_size_bonus_label, 3, 6, 1, 1)
        self.layout.addWidget(self.ac_misc_bonus_label, 3, 7, 1, 1)

    def translate(self, language):
        set_text_of_children(self, self.translate_reference[language])