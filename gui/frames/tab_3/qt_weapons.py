from types import SimpleNamespace

from PyQt5 import QtWidgets, QtCore

from gui.frames.qt_generic_classes import DefaultBox
from gui.frames.qt_generic_functions import create_qline_edit, create_qlabel, create_combo_box, \
    add_multiple_elements_to_layout_by_row, set_text_of_children


class WeaponsBox(DefaultBox):
    # TODO - change in label of ranged/melee weapon depending on choice option
    # TODO - changing selected weapon using combo box
    # TODO - more than 3 choices for weapons
    def __init__(self, parent, position, size):
        self.root = QtWidgets.QGroupBox(parent)
        self.root.setGeometry(QtCore.QRect(*position, *size))
        self.root.setObjectName("WeaponsBox")
        self.melee_box = QtWidgets.QGroupBox(self.root)
        self.melee_box.setGeometry(QtCore.QRect(10, 60, 591, 161))
        self.melee_box.setMaximumSize(QtCore.QSize(591, 44444))
        self.melee_box.setObjectName("CurrentMeleeWeaponBox")
        self.melee_container = QtWidgets.QWidget(self.melee_box)
        self.melee_container.setGeometry(QtCore.QRect(11, 21, 571, 121))
        self.melee_container.setObjectName("layoutWidget3")
        self.melee_layout = QtWidgets.QGridLayout(self.melee_container)
        self.melee_layout.setContentsMargins(9, 9, 9, 9)
        self.melee_layout.setSpacing(6)
        self.melee_layout.setObjectName("MeleeWeapon")
        melee_weapon_qedit = dict(parent=self.melee_container, min_size=(0, 23), max_size=(138, 20))
        melee_weapon_qlabel = dict(parent=self.melee_container, max_size=(138, 16))
        self.melee_weapons = []
        self.ranged_weapons = []
        self.translate_reference = {
            "EN":
                {
                    "root": {
                        "title": "Weapons"
                    },
                    "melee_box": {
                        "title": "Currently chosen melee weapon"
                    },
                    "ranged_box": {
                        "title": "Currently chosen ranged weapon"
                    },
                    "melee_weapon_name_label": "Name",
                    "melee_weapon_attack_bonus_label": "Attack bonus",
                    "melee_weapon_damage_roll_label": "Damage roll",
                    "melee_weapon_crit_label": "Critical roll / multiplier",
                    "melee_weapon_special_label": "Special",
                    "melee_weapon_weight_label": "Weight",
                    "melee_weapon_size_label": "Size",
                    "melee_weapon_type_label": "Type",
                    "melee_choice": {
                        "choices": ["Melee weapon 1", "Melee weapon 2", "Melee weapon 3"]
                    },
                    "ranged_choice": {
                        "choices": ["Ranged weapon 1", "Ranged weapon 2", "Ranged weapon 3"]
                    },

                    "ranged_weapon_crit_label": "Critical roll / multiplier",
                    "ranged_weapon_damage_roll_label": "Damage roll",
                    "ranged_weapon_range_label": "Range",
                    "ranged_weapon_name_label": "Name",
                    "ranged_weapon_attack_bonus_label": "Attack bonus",
                    "ranged_weapon_special_label": "Special",
                    "ranged_weapon_ammo_label": "Ammo",
                    "ranged_weapon_weight_label": "Weight",
                    "ranged_weapon_size_label": "Size",
                    "ranged_weapon_type_label": "Type"}}

        self.current_melee = SimpleNamespace()

        self.current_melee.name = create_qline_edit("melee_weapon_name", **melee_weapon_qedit)
        self.current_melee.attack_bonus = create_qline_edit("melee_weapon_attack_bonus", **melee_weapon_qedit)
        self.current_melee.damage_roll = create_qline_edit("melee_weapon_damage_roll", **melee_weapon_qedit)
        self.current_melee.crit = create_qline_edit("melee_weapon_crit", **melee_weapon_qedit)
        self.current_melee.special = create_qline_edit("melee_weapon_special", **melee_weapon_qedit)
        self.current_melee.weight = create_qline_edit("melee_weapon_weight", **melee_weapon_qedit)
        self.current_melee.size = create_qline_edit("melee_weapon_size", **melee_weapon_qedit)
        self.current_melee.type = create_qline_edit("melee_weapon_type", **melee_weapon_qedit)

        self.melee_choice = create_combo_box("weapons_melee_choice", self.root, 3, min_size=[171, 22])
        self.melee_choice.move(20, 30)
        self.melee_weapon_name_label = create_qlabel("melee_weapon_name_label", **melee_weapon_qlabel)
        self.melee_weapon_attack_bonus_label = create_qlabel("melee_weapon_attack_bonus_label", **melee_weapon_qlabel)
        self.melee_weapon_damage_roll_label = create_qlabel("melee_weapon_damage_roll_label", **melee_weapon_qlabel)
        self.melee_weapon_crit_label = create_qlabel("melee_weapon_crit_label", **melee_weapon_qlabel)
        self.melee_weapon_special_label = create_qlabel("melee_weapon_special_label", **melee_weapon_qlabel)
        self.melee_weapon_weight_label = create_qlabel("melee_weapon_weight_label", **melee_weapon_qlabel)
        self.melee_weapon_size_label = create_qlabel("melee_weapon_size_label", **melee_weapon_qlabel)
        self.melee_weapon_type_label = create_qlabel("melee_weapon_type_label", **melee_weapon_qlabel)

        self.ranged_choice = create_combo_box("weapons_ranged_choice", self.root, 3, min_size=[171, 22])
        self.ranged_choice.move(20, 230)

        self.ranged_box = QtWidgets.QGroupBox(self.root)
        self.ranged_box.setGeometry(QtCore.QRect(10, 260, 591, 151))
        self.ranged_box.setObjectName("CurrentRangedWeaponBox")
        self.ranged_container = QtWidgets.QWidget(self.ranged_box)
        self.ranged_container.setGeometry(QtCore.QRect(10, 20, 571, 111))
        self.ranged_container.setObjectName("gridLayoutWidget_17")
        self.ranged_layout = QtWidgets.QGridLayout(self.ranged_container)
        self.ranged_layout.setContentsMargins(9, 9, 9, 9)
        self.ranged_layout.setSpacing(6)
        self.ranged_layout.setObjectName("RangedWeapon")

        ranged_weapon_qlabel = dict(parent=self.ranged_container)
        ranged_weapon_qedit = dict(parent=self.ranged_container, min_size=(0, 23))

        self.ranged_weapon_crit_label = create_qlabel("ranged_weapon_crit_label", **ranged_weapon_qlabel)
        self.ranged_weapon_damage_roll_label = create_qlabel("ranged_weapon_damage_roll_label", **ranged_weapon_qlabel)
        self.ranged_weapon_range_label = create_qlabel("ranged_weapon_range_label", **ranged_weapon_qlabel)
        self.ranged_weapon_name_label = create_qlabel("ranged_weapon_name_label", **ranged_weapon_qlabel)
        self.ranged_weapon_attack_bonus_label = create_qlabel("ranged_weapon_attack_bonus_label",
                                                              **ranged_weapon_qlabel)
        self.ranged_weapon_special_label = create_qlabel("ranged_weapon_special_label", **ranged_weapon_qlabel)
        self.ranged_weapon_ammo_label = create_qlabel("ranged_weapon_ammo_label", **ranged_weapon_qlabel)
        self.ranged_weapon_weight_label = create_qlabel("ranged_weapon_weight_label", **ranged_weapon_qlabel)
        self.ranged_weapon_size_label = create_qlabel("ranged_weapon_size_label", **ranged_weapon_qlabel)
        self.ranged_weapon_type_label = create_qlabel("ranged_weapon_type_label", **ranged_weapon_qlabel)

        self.current_ranged = SimpleNamespace()
        self.current_ranged.name = create_qline_edit("ranged_weapon_name", **ranged_weapon_qedit)
        self.current_ranged.attack_bonus = create_qline_edit("ranged_weapon_attack_bonus", **ranged_weapon_qedit)
        self.current_ranged.damage_roll = create_qline_edit("ranged_weapon_damage_roll", **ranged_weapon_qedit)
        self.current_ranged.crit = create_qline_edit("ranged_weapon_crit", **ranged_weapon_qedit)
        self.current_ranged.range = create_qline_edit("ranged_weapon_range", **ranged_weapon_qedit)
        self.current_ranged.special = create_qline_edit("ranged_weapon_special", **ranged_weapon_qedit)
        self.current_ranged.ammo = create_qline_edit("ranged_weapon_ammo", **ranged_weapon_qedit)
        self.current_ranged.weight = create_qline_edit("ranged_weapon_weight", **ranged_weapon_qedit)
        self.current_ranged.size = create_qline_edit("ranged_weapon_size", **ranged_weapon_qedit)
        self.current_ranged.type = create_qline_edit("ranged_weapon_type", **ranged_weapon_qedit)
        self.add_to_layout()
        self.translate("EN")
        # self.root.setLayout(self.layout)

    def add_to_ranged_layout(self):
        first_row = [self.ranged_weapon_name_label, self.ranged_weapon_attack_bonus_label,
                     self.ranged_weapon_damage_roll_label, self.ranged_weapon_crit_label,
                     self.ranged_weapon_range_label, ]
        add_multiple_elements_to_layout_by_row(self.ranged_layout, first_row)

        second_row = [self.current_ranged.name, self.current_ranged.attack_bonus, self.current_ranged.damage_roll,
                      self.current_ranged.crit, self.current_ranged.range, ]
        add_multiple_elements_to_layout_by_row(self.ranged_layout, second_row, row=1)

        third_row = [self.ranged_weapon_special_label, self.ranged_weapon_ammo_label, self.ranged_weapon_weight_label,
                     self.ranged_weapon_size_label, self.ranged_weapon_type_label, ]
        add_multiple_elements_to_layout_by_row(self.ranged_layout, third_row, row=2)

        fourth_row = [self.current_ranged.special, self.current_ranged.ammo, self.current_ranged.weight,
                      self.current_ranged.size, self.current_ranged.type, ]
        add_multiple_elements_to_layout_by_row(self.ranged_layout, fourth_row, row=3)

    def add_to_melee_layout(self):
        first_row = [self.melee_weapon_name_label, self.melee_weapon_attack_bonus_label,
                     self.melee_weapon_damage_roll_label, self.melee_weapon_crit_label, ]
        add_multiple_elements_to_layout_by_row(self.melee_layout, first_row)

        second_row = [self.current_melee.name, self.current_melee.attack_bonus, self.current_melee.damage_roll,
                      self.current_melee.crit, ]
        add_multiple_elements_to_layout_by_row(self.melee_layout, second_row, row=1)

        third_row = [self.melee_weapon_special_label, self.melee_weapon_weight_label, self.melee_weapon_size_label,
                     self.melee_weapon_type_label]
        add_multiple_elements_to_layout_by_row(self.melee_layout, third_row, row=2)

        fourth_row = [self.current_melee.special, self.current_melee.weight, self.current_melee.size,
                      self.current_melee.type, ]
        add_multiple_elements_to_layout_by_row(self.melee_layout, fourth_row, row=3)

    def translate(self, language):
        set_text_of_children(self, self.translate_reference[language])

    def add_to_layout(self):
        self.add_to_melee_layout()
        self.add_to_ranged_layout()

    def create_melee_weapon(self):
        melee_weapon = SimpleNamespace()
        attributes = ["name", "attack_bonus", "damage_roll", "crit", "special", "weight", "size", "type"]
        for attribute in attributes:
            setattr(melee_weapon, attribute, "")
        return melee_weapon

    def create_ranged_weapon(self):
        ranged_weapon = SimpleNamespace()
        attributes = ["name", "attack_bonus", "damage_roll", "crit", "range",
                      "special", "ammo" "weight", "size", "type"]
        for attribute in attributes:
            setattr(ranged_weapon, attribute, "")
        return ranged_weapon
