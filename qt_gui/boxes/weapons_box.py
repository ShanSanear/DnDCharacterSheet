from PyQt5 import QtWidgets, QtCore

from qt_gui.boxes.qt_generic_classes import DefaultBox
from qt_gui.boxes.qt_generic_functions import create_qline_edit, create_qlabel


class WeaponsBox(DefaultBox):
    # TODO - function based widgets and labels
    # TODO - generalized translation
    # TODO - adding widgets by rows/columns
    # TODO - change in label of ranged/melee weapon depending on choice option
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

        self.melee_weapon_name = create_qline_edit("melee_weapon_name", **melee_weapon_qedit)
        self.melee_weapon_attack_bonus = create_qline_edit("melee_weapon_attack_bonus", **melee_weapon_qedit)
        self.melee_weapon_damage_roll = create_qline_edit("melee_weapon_damage_roll", **melee_weapon_qedit)
        self.melee_weapon_crit = create_qline_edit("melee_weapon_crit", **melee_weapon_qedit)
        self.melee_weapon_special = create_qline_edit("melee_weapon_special", **melee_weapon_qedit)
        self.melee_weapon_weight = create_qline_edit("melee_weapon_weight", **melee_weapon_qedit)
        self.melee_weapon_size = create_qline_edit("melee_weapon_size", **melee_weapon_qedit)
        self.melee_weapon_type = create_qline_edit("melee_weapon_type", **melee_weapon_qedit)
        self.melee_choice = QtWidgets.QComboBox(self.root)
        self.melee_choice.setGeometry(QtCore.QRect(20, 30, 171, 22))
        self.melee_choice.setObjectName("weapons_melee_weapon_choice")
        self.melee_choice.addItem("")
        self.melee_choice.addItem("")
        self.melee_choice.addItem("")

        self.melee_weapon_name_label = create_qlabel("melee_weapon_name_label", **melee_weapon_qlabel)
        self.melee_weapon_attack_bonus_label = create_qlabel("melee_weapon_attack_bonus_label", **melee_weapon_qlabel)
        self.melee_weapon_damage_roll_label = create_qlabel("melee_weapon_damage_roll_label", **melee_weapon_qlabel)
        self.melee_weapon_crit_label = create_qlabel("melee_weapon_crit_label", **melee_weapon_qlabel)
        self.melee_weapon_special_label = create_qlabel("melee_weapon_special_label", **melee_weapon_qlabel)
        self.melee_weapon_weight_label = create_qlabel("melee_weapon_weight_label", **melee_weapon_qlabel)
        self.melee_weapon_size_label = create_qlabel("melee_weapon_size_label", **melee_weapon_qlabel)
        self.melee_weapon_type_label = create_qlabel("melee_weapon_type_label", **melee_weapon_qlabel)


        self.weapons_ranged_weapon_choice = QtWidgets.QComboBox(self.root)
        self.weapons_ranged_weapon_choice.setGeometry(QtCore.QRect(20, 230, 171, 22))
        self.weapons_ranged_weapon_choice.setObjectName("weapons_ranged_weapon_choice")
        self.weapons_ranged_weapon_choice.addItem("")
        self.weapons_ranged_weapon_choice.addItem("")
        self.weapons_ranged_weapon_choice.addItem("")

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

        self.ranged_weapon_name = create_qline_edit("ranged_weapon_name", **ranged_weapon_qedit)
        self.ranged_weapon_attack_bonus = create_qline_edit("ranged_weapon_attack_bonus", **ranged_weapon_qedit)
        self.ranged_weapon_crit = create_qline_edit("ranged_weapon_crit", **ranged_weapon_qedit)
        self.ranged_weapon_range = create_qline_edit("ranged_weapon_range", **ranged_weapon_qedit)
        self.ranged_weapon_damage_roll = create_qline_edit("ranged_weapon_damage_roll", **ranged_weapon_qedit)
        self.ranged_weapon_special = create_qline_edit("ranged_weapon_special", **ranged_weapon_qedit)
        self.ranged_weapon_ammo = create_qline_edit("ranged_weapon_ammo", **ranged_weapon_qedit)
        self.ranged_weapon_weight = create_qline_edit("ranged_weapon_weight", **ranged_weapon_qedit)
        self.ranged_weapon_size = create_qline_edit("ranged_weapon_size", **ranged_weapon_qedit)
        self.ranged_weapon_type = create_qline_edit("ranged_weapon_type", **ranged_weapon_qedit)
        self.add_to_layout()
        self.translate()
        # self.root.setLayout(self.layout)

    def add_to_ranged_layout(self):
        self.ranged_layout.addWidget(self.ranged_weapon_crit_label, 0, 3, 1, 1)
        self.ranged_layout.addWidget(self.ranged_weapon_damage_roll_label, 0, 2, 1, 1)
        self.ranged_layout.addWidget(self.ranged_weapon_range_label, 0, 4, 1, 1)
        self.ranged_layout.addWidget(self.ranged_weapon_name_label, 0, 0, 1, 1)
        self.ranged_layout.addWidget(self.ranged_weapon_name, 1, 0, 1, 1)
        self.ranged_layout.addWidget(self.ranged_weapon_attack_bonus, 1, 1, 1, 1)
        self.ranged_layout.addWidget(self.ranged_weapon_crit, 1, 3, 1, 1)
        self.ranged_layout.addWidget(self.ranged_weapon_range, 1, 4, 1, 1)
        self.ranged_layout.addWidget(self.ranged_weapon_damage_roll, 1, 2, 1, 1)
        self.ranged_layout.addWidget(self.ranged_weapon_attack_bonus_label, 0, 1, 1, 1)
        self.ranged_layout.addWidget(self.ranged_weapon_special_label, 2, 0, 1, 1)
        self.ranged_layout.addWidget(self.ranged_weapon_special, 3, 0, 1, 1)
        self.ranged_layout.addWidget(self.ranged_weapon_ammo_label, 2, 1, 1, 1)
        self.ranged_layout.addWidget(self.ranged_weapon_weight_label, 2, 2, 1, 1)
        self.ranged_layout.addWidget(self.ranged_weapon_size_label, 2, 3, 1, 1)
        self.ranged_layout.addWidget(self.ranged_weapon_type_label, 2, 4, 1, 1)
        self.ranged_layout.addWidget(self.ranged_weapon_ammo, 3, 1, 1, 1)
        self.ranged_layout.addWidget(self.ranged_weapon_weight, 3, 2, 1, 1)
        self.ranged_layout.addWidget(self.ranged_weapon_size, 3, 3, 1, 1)
        self.ranged_layout.addWidget(self.ranged_weapon_type, 3, 4, 1, 1)

    def add_to_melee_layout(self):
        self.melee_layout.addWidget(self.melee_weapon_name_label, 0, 0, 1, 1)
        self.melee_layout.addWidget(self.melee_weapon_attack_bonus_label, 0, 1, 1, 1)
        self.melee_layout.addWidget(self.melee_weapon_damage_roll_label, 0, 2, 1, 1)
        self.melee_layout.addWidget(self.melee_weapon_crit_label, 0, 3, 1, 1)
        self.melee_layout.addWidget(self.melee_weapon_name, 1, 0, 1, 1)
        self.melee_layout.addWidget(self.melee_weapon_attack_bonus, 1, 1, 1, 1)
        self.melee_layout.addWidget(self.melee_weapon_damage_roll, 1, 2, 1, 1)
        self.melee_layout.addWidget(self.melee_weapon_crit, 1, 3, 1, 1)
        self.melee_layout.addWidget(self.melee_weapon_special_label, 2, 0, 1, 1)
        self.melee_layout.addWidget(self.melee_weapon_weight_label, 2, 1, 1, 1)
        self.melee_layout.addWidget(self.melee_weapon_size_label, 2, 2, 1, 1)
        self.melee_layout.addWidget(self.melee_weapon_type_label, 2, 3, 1, 1)
        self.melee_layout.addWidget(self.melee_weapon_special, 3, 0, 1, 1)
        self.melee_layout.addWidget(self.melee_weapon_weight, 3, 1, 1, 1)
        self.melee_layout.addWidget(self.melee_weapon_size, 3, 2, 1, 1)
        self.melee_layout.addWidget(self.melee_weapon_type, 3, 3, 1, 1)

    def translate(self):
        _translate = QtCore.QCoreApplication.translate
        self.root.setTitle(_translate("MainWindow", "Weapons"))
        self.melee_box.setTitle(_translate("MainWindow", "Currently chosen melee weapon"))
        self.melee_weapon_name_label.setText(_translate("MainWindow", "Name"))
        self.melee_weapon_attack_bonus_label.setText(_translate("MainWindow", "Attack bonus"))
        self.melee_weapon_damage_roll_label.setText(_translate("MainWindow", "Damage roll"))
        self.melee_weapon_crit_label.setText(_translate("MainWindow", "Critical roll / multiplier"))
        self.melee_weapon_name.setText(_translate("MainWindow", "Lorem ipsum"))
        self.melee_weapon_attack_bonus.setText(_translate("MainWindow", "10"))
        self.melee_weapon_damage_roll.setText(_translate("MainWindow", "10"))
        self.melee_weapon_crit.setText(_translate("MainWindow", "10"))
        self.melee_weapon_special_label.setText(_translate("MainWindow", "Special"))
        self.melee_weapon_weight_label.setText(_translate("MainWindow", "Weight"))
        self.melee_weapon_size_label.setText(_translate("MainWindow", "Size"))
        self.melee_weapon_type_label.setText(_translate("MainWindow", "Type"))
        self.melee_weapon_special.setText(_translate("MainWindow", "Lorem ipsum"))
        self.melee_weapon_weight.setText(_translate("MainWindow", "10"))
        self.melee_weapon_size.setText(_translate("MainWindow", "Lorem ipsum"))
        self.melee_weapon_type.setText(_translate("MainWindow", "Lorem ipsum"))
        self.melee_choice.setItemText(0, _translate("MainWindow", "Melee weapon 1"))
        self.melee_choice.setItemText(1, _translate("MainWindow", "Melee weapon 2"))
        self.melee_choice.setItemText(2, _translate("MainWindow", "Melee weapon 3"))
        self.weapons_ranged_weapon_choice.setItemText(0, _translate("MainWindow", "Ranged weapon 1"))
        self.weapons_ranged_weapon_choice.setItemText(1, _translate("MainWindow", "Ranged weapon 2"))
        self.weapons_ranged_weapon_choice.setItemText(2, _translate("MainWindow", "Ranged weapon 3"))
        self.ranged_box.setTitle(_translate("MainWindow", "Currently chosen ranged weapon"))
        self.ranged_weapon_crit_label.setText(_translate("MainWindow", "Critical roll / multiplier"))
        self.ranged_weapon_damage_roll_label.setText(_translate("MainWindow", "Damage roll"))
        self.ranged_weapon_range_label.setText(_translate("MainWindow", "Range"))
        self.ranged_weapon_name_label.setText(_translate("MainWindow", "Name"))
        self.ranged_weapon_name.setText(_translate("MainWindow", "Lorem ipsum"))
        self.ranged_weapon_attack_bonus.setText(_translate("MainWindow", "10"))
        self.ranged_weapon_crit.setText(_translate("MainWindow", "10"))
        self.ranged_weapon_range.setText(_translate("MainWindow", "10"))
        self.ranged_weapon_damage_roll.setText(_translate("MainWindow", "10"))
        self.ranged_weapon_attack_bonus_label.setText(_translate("MainWindow", "Attack bonus"))
        self.ranged_weapon_special_label.setText(_translate("MainWindow", "Special"))
        self.ranged_weapon_special.setText(_translate("MainWindow", "Lorem ipsum"))
        self.ranged_weapon_ammo_label.setText(_translate("MainWindow", "Ammo"))
        self.ranged_weapon_weight_label.setText(_translate("MainWindow", "Weight"))
        self.ranged_weapon_size_label.setText(_translate("MainWindow", "Size"))
        self.ranged_weapon_type_label.setText(_translate("MainWindow", "Type"))
        self.ranged_weapon_ammo.setText(_translate("MainWindow", "10"))
        self.ranged_weapon_weight.setText(_translate("MainWindow", "10"))
        self.ranged_weapon_size.setText(_translate("MainWindow", "Lorem ipsum"))
        self.ranged_weapon_type.setText(_translate("MainWindow", "Lorem ipsum"))

    def add_to_layout(self):
        self.add_to_melee_layout()
        self.add_to_ranged_layout()
