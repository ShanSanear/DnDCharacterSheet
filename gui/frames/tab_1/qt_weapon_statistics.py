from PyQt5 import QtWidgets, QtCore

from core.character import Character
from gui.frames.qt_generic_classes import DefaultBox
from gui.frames.qt_generic_functions import create_qline_edit, create_qlabel, create_combo_box


class WeaponStatisticsBox(DefaultBox):
    char_core: Character
    # TODO Column labels centered
    # TODO - generalized translation
    # TODO - adding widgets by rows/columns
    def __init__(self, parent, position, size, char_core):
        self.char_core = char_core
        self.root = QtWidgets.QGroupBox(parent)
        self.root.setGeometry(QtCore.QRect(*position, *size))
        self.container = QtWidgets.QWidget(self.root)
        self.layout = QtWidgets.QGridLayout(self.container)
        self.layout.setContentsMargins(8, 8, 8, 12)
        # @self.layout.setSpacing(10)
        self.melee_attr = "str"
        self.ranged_attr = "dex"
        self.bonus_from_melee = 0
        self.bonus_from_ranged = 0

        qline_dict = dict(parent=self.container, enabled=False)
        qlabel_dict = dict(parent=self.container)

        self.weapon_name_label = create_qlabel("weapon_name_label", **qlabel_dict)
        self.attack_bonus_label = create_qlabel("weapon_statistics_attack_bonus_label", **qlabel_dict)
        self.damage_label = create_qlabel("weapon_statistics_damage_label", **qlabel_dict)
        self.crit_label = create_qlabel("weapon_statistics_crit_label", **qlabel_dict)
        self.range_label = create_qlabel("weapon_attribute_choice", **qlabel_dict)


        self.melee_label = create_qlabel("weapon_statistics_melee_label", align=QtCore.Qt.AlignRight, **qlabel_dict)
        self.melee_name = create_qline_edit("weapon_statistics_melee_damage", min_size=[90, None],
                                            parent=self.container, enabled=False)
        self.melee_attack_bonus = create_qline_edit("weapon_statistics_melee_attack_bonus", max_size=[50, None],
                                                    str_format="{:+d}", **qline_dict)
        self.melee_damage = create_qline_edit("weapon_statistics_melee_damage", max_size=[60, None], **qline_dict)
        self.melee_crit = create_qline_edit("weapon_statistics_melee_crit",  parent=self.container, max_size=[60, None],
                                            min_size=[50, None], enabled=False)
        self.melee_range = create_qline_edit("melee_range", parent=self.container,
                                              max_size=[50, None],
                                              enabled=False)

        self.ranged_label = create_qlabel("weapon_statistics_ranged_label", align=QtCore.Qt.AlignRight, **qlabel_dict)
        self.ranged_name = create_qline_edit("weapon_statistics_ranged_crit", min_size=[90, None],
                                             parent=self.container, enabled=False)
        self.ranged_attack_bonus = create_qline_edit("weapon_statistics_ranged_attack_bonus", max_size=[50, None],
                                                     str_format="{:+d}", **qline_dict)
        self.ranged_damage = create_qline_edit("weapon_statistics_ranged_damage", max_size=[60, None], **qline_dict)
        self.ranged_crit = create_qline_edit("weapon_statistics_ranged_crit", parent=self.container, max_size=[60, None],
                                             min_size=[50, None], enabled=False)
        self.ranged_range = create_qline_edit("ranged_range", parent=self.container, max_size=[50, None],
                                             enabled=False)

        self.add_to_layout()
        self.translate()
        self.root.setLayout(self.layout)

    def add_to_layout(self):
        self.layout.addWidget(self.weapon_name_label, 0, 1, 1, 1)
        self.layout.addWidget(self.attack_bonus_label, 0, 2, 1, 1)
        self.layout.addWidget(self.damage_label, 0, 3, 1, 1)
        self.layout.addWidget(self.crit_label, 0, 4, 1, 1)
        self.layout.addWidget(self.range_label, 0, 5, 1, 1)

        self.layout.addWidget(self.melee_label, 1, 0, 1, 1)
        self.layout.addWidget(self.melee_name, 1, 1, 1, 1)
        self.layout.addWidget(self.melee_attack_bonus, 1, 2, 1, 1)
        self.layout.addWidget(self.melee_damage, 1, 3, 1, 1)
        self.layout.addWidget(self.melee_crit, 1, 4, 1, 1)
        self.layout.addWidget(self.melee_range,1,5,1,1)

        self.layout.addWidget(self.ranged_label, 2, 0, 1, 1)
        self.layout.addWidget(self.ranged_name, 2, 1, 1, 1)
        self.layout.addWidget(self.ranged_attack_bonus, 2, 2, 1, 1)
        self.layout.addWidget(self.ranged_damage, 2, 3, 1, 1)
        self.layout.addWidget(self.ranged_crit, 2, 4, 1, 1)
        self.layout.addWidget(self.ranged_range, 2,5,1,1)

    def translate(self):
        _translate = QtCore.QCoreApplication.translate
        self.root.setTitle(_translate("MainWindow", "Current weapon statistics"))
        self.attack_bonus_label.setText(_translate("MainWindow", "Att. bonus"))
        self.damage_label.setText(_translate("MainWindow", "Dmg"))
        self.crit_label.setText(_translate("MainWindow", "Crit"))
        self.melee_label.setText(_translate("MainWindow", "Melee"))
        self.ranged_label.setText(_translate("MainWindow", "Ranged"))
        self.weapon_name_label.setText("Weapon name")
        self.range_label.setText("Range")
        self.melee_range.setText("1 m")

        # self.ranged_damage.setText(_translate("MainWindow", "10"))
        # self.ranged_attack_bonus.setText(_translate("MainWindow", "10"))
        # self.ranged_crit.setText(_translate("MainWindow", "10"))
        # self.melee_attack_bonus.setText(_translate("MainWindow", "10"))
        # self.melee_crit.setText(_translate("MainWindow", "10"))
        # self.melee_damage.setText(_translate("MainWindow", "10"))
