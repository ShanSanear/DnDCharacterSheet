from PyQt5 import QtWidgets, QtCore

from core.character import Character
from gui.frames.qt_generic_classes import DefaultBox
from gui.frames.qt_generic_functions import create_qline_edit, create_qlabel


class WeaponStatisticsBox(DefaultBox):
    char_core: Character

    # TODO - generalized translation
    # TODO - adding widgets by rows/columns
    def __init__(self, parent, position, size, char_core):
        self.char_core = char_core
        self.root = QtWidgets.QGroupBox(parent)
        self.root.setGeometry(QtCore.QRect(*position, *size))
        self.root.setObjectName("WeaponStatisticsBox")
        self.container = QtWidgets.QWidget(self.root)
        self.layout = QtWidgets.QGridLayout(self.container)
        self.layout.setObjectName("WeaponStatisticsLayout")
        self.layout.setContentsMargins(8, 8, 8, 12)
        self.layout.setSpacing(10)

        qline_dict = dict(parent=self.container, )  # min_size=(60, 23), max_size=(50, 20))
        qlabel_dict = dict(parent=self.container, )  # max_size=(16777215, 20))

        self.weapon_statistics_ranged_damage = create_qline_edit("weapon_statistics_ranged_damage", **qline_dict)
        self.weapon_statistics_melee_damage = create_qline_edit("weapon_statistics_melee_damage", **qline_dict)
        self.weapon_statistics_ranged_attack_bonus = create_qline_edit("weapon_statistics_ranged_attack_bonus", enabled=False,
                                                                       **qline_dict)
        self.weapon_statistics_ranged_crit = create_qline_edit("weapon_statistics_ranged_crit", **qline_dict)
        self.weapon_statistics_melee_attack_bonus = create_qline_edit("weapon_statistics_melee_attack_bonus", enabled=False,
                                                                      **qline_dict)
        self.weapon_statistics_melee_crit = create_qline_edit("weapon_statistics_melee_crit", **qline_dict)

        self.weapon_statistics_attack_bonus_label = create_qlabel("weapon_statistics_attack_bonus_label", **qlabel_dict)
        self.weapon_statistics_damage_label = create_qlabel("weapon_statistics_damage_label", **qlabel_dict)
        self.weapon_statistics_crit_label = create_qlabel("weapon_statistics_crit_label", **qlabel_dict)
        self.weapon_statistics_melee_label = create_qlabel("weapon_statistics_melee_label", **qlabel_dict)
        self.weapon_statistics_ranged_label = create_qlabel("weapon_statistics_ranged_label", **qlabel_dict)

        self.add_to_layout()
        self.translate()
        self.root.setLayout(self.layout)
        self.set_values_from_attributes()

    def add_to_layout(self):
        self.layout.addWidget(self.weapon_statistics_ranged_damage, 2, 2, 1, 1)
        self.layout.addWidget(self.weapon_statistics_melee_damage, 1, 2, 1, 1)
        self.layout.addWidget(self.weapon_statistics_ranged_attack_bonus, 2, 1, 1, 1)
        self.layout.addWidget(self.weapon_statistics_ranged_crit, 2, 3, 1, 1)
        self.layout.addWidget(self.weapon_statistics_melee_attack_bonus, 1, 1, 1, 1)
        self.layout.addWidget(self.weapon_statistics_melee_crit, 1, 3, 1, 1)
        self.layout.addWidget(self.weapon_statistics_attack_bonus_label, 0, 1, 1, 1)
        self.layout.addWidget(self.weapon_statistics_damage_label, 0, 2, 1, 1)
        self.layout.addWidget(self.weapon_statistics_crit_label, 0, 3, 1, 1)
        self.layout.addWidget(self.weapon_statistics_melee_label, 1, 0, 1, 1)
        self.layout.addWidget(self.weapon_statistics_ranged_label, 2, 0, 1, 1)

    def translate(self):
        _translate = QtCore.QCoreApplication.translate
        self.root.setTitle(_translate("MainWindow", "Current weapon statistics"))
        self.weapon_statistics_attack_bonus_label.setText(_translate("MainWindow", "Att. bonus"))
        self.weapon_statistics_ranged_damage.setText(_translate("MainWindow", "10"))
        self.weapon_statistics_ranged_attack_bonus.setText(_translate("MainWindow", "10"))
        self.weapon_statistics_ranged_crit.setText(_translate("MainWindow", "10"))
        self.weapon_statistics_melee_attack_bonus.setText(_translate("MainWindow", "10"))
        self.weapon_statistics_melee_crit.setText(_translate("MainWindow", "10"))
        self.weapon_statistics_damage_label.setText(_translate("MainWindow", "Dmg"))
        self.weapon_statistics_crit_label.setText(_translate("MainWindow", "Crit"))
        self.weapon_statistics_melee_damage.setText(_translate("MainWindow", "10"))
        self.weapon_statistics_melee_label.setText(_translate("MainWindow", "Melee"))
        self.weapon_statistics_ranged_label.setText(_translate("MainWindow", "Ranged"))

    def set_values_from_attributes(self):
        self.weapon_statistics_melee_attack_bonus.setText(str(self.char_core.attributes.str['mod']))
        self.weapon_statistics_ranged_attack_bonus.setText(str(self.char_core.attributes.dex['mod']))

