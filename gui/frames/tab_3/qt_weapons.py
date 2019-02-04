from types import SimpleNamespace

from PyQt5 import QtWidgets, QtCore

from gui.frames.qt_generic_classes import DefaultBox
from gui.frames.qt_generic_functions import create_qline_edit, create_qlabel, create_combo_box, \
    add_multiple_elements_to_layout_by_row


class WeaponsBox(DefaultBox):
    # TODO - function based widgets and labels
    # TODO - generalized translation
    # TODO - adding widgets by rows/columns
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
        self.translate()
        # self.root.setLayout(self.layout)

    def add_to_ranged_layout(self):
        first_row = [self.ranged_weapon_name_label, self.ranged_weapon_attack_bonus_label,
                     self.ranged_weapon_damage_roll_label, self.ranged_weapon_crit_label,
                     self.ranged_weapon_range_label,]
        add_multiple_elements_to_layout_by_row(self.ranged_layout, first_row)

        second_row = [self.current_ranged.name, self.current_ranged.attack_bonus, self.current_ranged.damage_roll,
                      self.current_ranged.crit, self.current_ranged.range,]
        add_multiple_elements_to_layout_by_row(self.ranged_layout, second_row, row=1)

        third_row = [self.ranged_weapon_special_label, self.ranged_weapon_ammo_label,self.ranged_weapon_weight_label,
                     self.ranged_weapon_size_label, self.ranged_weapon_type_label,]
        add_multiple_elements_to_layout_by_row(self.ranged_layout, third_row, row=2)

        fourth_row = [self.current_ranged.special, self.current_ranged.ammo, self.current_ranged.weight,
                      self.current_ranged.size, self.current_ranged.type,]
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

    def translate(self):
        _translate = QtCore.QCoreApplication.translate
        self.root.setTitle(_translate("MainWindow", "Weapons"))
        self.melee_box.setTitle(_translate("MainWindow", "Currently chosen melee weapon"))
        self.melee_weapon_name_label.setText(_translate("MainWindow", "Name"))
        self.melee_weapon_attack_bonus_label.setText(_translate("MainWindow", "Attack bonus"))
        self.melee_weapon_damage_roll_label.setText(_translate("MainWindow", "Damage roll"))
        self.melee_weapon_crit_label.setText(_translate("MainWindow", "Critical roll / multiplier"))
        self.current_melee.name.setText(_translate("MainWindow", "Lorem ipsum"))
        self.current_melee.attack_bonus.setText(_translate("MainWindow", "10"))
        self.current_melee.damage_roll.setText(_translate("MainWindow", "10"))
        self.current_melee.crit.setText(_translate("MainWindow", "10"))
        self.melee_weapon_special_label.setText(_translate("MainWindow", "Special"))
        self.melee_weapon_weight_label.setText(_translate("MainWindow", "Weight"))
        self.melee_weapon_size_label.setText(_translate("MainWindow", "Size"))
        self.melee_weapon_type_label.setText(_translate("MainWindow", "Type"))
        self.current_melee.special.setText(_translate("MainWindow", "Lorem ipsum"))
        self.current_melee.weight.setText(_translate("MainWindow", "10"))
        self.current_melee.size.setText(_translate("MainWindow", "Lorem ipsum"))
        self.current_melee.type.setText(_translate("MainWindow", "Lorem ipsum"))
        self.melee_choice.setItemText(0, _translate("MainWindow", "Melee weapon 1"))
        self.melee_choice.setItemText(1, _translate("MainWindow", "Melee weapon 2"))
        self.melee_choice.setItemText(2, _translate("MainWindow", "Melee weapon 3"))
        self.ranged_choice.setItemText(0, _translate("MainWindow", "Ranged weapon 1"))
        self.ranged_choice.setItemText(1, _translate("MainWindow", "Ranged weapon 2"))
        self.ranged_choice.setItemText(2, _translate("MainWindow", "Ranged weapon 3"))
        self.ranged_box.setTitle(_translate("MainWindow", "Currently chosen ranged weapon"))
        self.ranged_weapon_crit_label.setText(_translate("MainWindow", "Critical roll / multiplier"))
        self.ranged_weapon_damage_roll_label.setText(_translate("MainWindow", "Damage roll"))
        self.ranged_weapon_range_label.setText(_translate("MainWindow", "Range"))
        self.ranged_weapon_name_label.setText(_translate("MainWindow", "Name"))
        self.current_ranged.name.setText(_translate("MainWindow", "Lorem ipsum"))
        self.current_ranged.attack_bonus.setText(_translate("MainWindow", "10"))
        self.current_ranged.crit.setText(_translate("MainWindow", "10"))
        self.current_ranged.range.setText(_translate("MainWindow", "10"))
        self.current_ranged.damage_roll.setText(_translate("MainWindow", "10"))
        self.ranged_weapon_attack_bonus_label.setText(_translate("MainWindow", "Attack bonus"))
        self.ranged_weapon_special_label.setText(_translate("MainWindow", "Special"))
        self.current_ranged.special.setText(_translate("MainWindow", "Lorem ipsum"))
        self.ranged_weapon_ammo_label.setText(_translate("MainWindow", "Ammo"))
        self.ranged_weapon_weight_label.setText(_translate("MainWindow", "Weight"))
        self.ranged_weapon_size_label.setText(_translate("MainWindow", "Size"))
        self.ranged_weapon_type_label.setText(_translate("MainWindow", "Type"))
        self.current_ranged.ammo.setText(_translate("MainWindow", "10"))
        self.current_ranged.weight.setText(_translate("MainWindow", "10"))
        self.current_ranged.size.setText(_translate("MainWindow", "Lorem ipsum"))
        self.current_ranged.type.setText(_translate("MainWindow", "Lorem ipsum"))

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
