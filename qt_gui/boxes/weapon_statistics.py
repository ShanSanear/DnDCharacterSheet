from PyQt5 import QtWidgets, QtCore

from qt_gui.qt_line_edits import create_qline_edit, create_qlabel


class WeaponStatisticsBox:
    def __init__(self, centralwidget):
        self.Box = QtWidgets.QGroupBox(centralwidget)
        self.Box.setGeometry(QtCore.QRect(1240, 160, 261, 121))
        self.Box.setObjectName("WeaponStatisticsBox")
        self.gridLayoutWidget_13 = QtWidgets.QWidget(self.Box)
        self.gridLayoutWidget_13.setGeometry(QtCore.QRect(10, 20, 243, 91))
        self.gridLayoutWidget_13.setObjectName("gridLayoutWidget_13")
        self.WeaponStatisticsLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_13)
        self.WeaponStatisticsLayout.setContentsMargins(9, 9, 9, 9)
        self.WeaponStatisticsLayout.setSpacing(6)
        self.WeaponStatisticsLayout.setObjectName("WeaponStatisticsLayout")

        qline_dict = dict(parent=self.gridLayoutWidget_13, min_size=(60, 23), max_size=(60, 20))
        qlabel_dict = dict(parent=self.gridLayoutWidget_13, max_size=(16777215, 20))

        self.weapon_statistics_ranged_damage = create_qline_edit("weapon_statistics_ranged_damage", **qline_dict)
        self.weapon_statistics_melee_damage = create_qline_edit("weapon_statistics_melee_damage", **qline_dict)
        self.weapon_statistics_ranged_attack_bonus = create_qline_edit("weapon_statistics_ranged_attack_bonus",
                                                                       **qline_dict)
        self.weapon_statistics_ranged_crit = create_qline_edit("weapon_statistics_ranged_crit", **qline_dict)
        self.weapon_statistics_melee_attack_bonus = create_qline_edit("weapon_statistics_melee_attack_bonus",
                                                                      **qline_dict)
        self.weapon_statistics_melee_crit = create_qline_edit("weapon_statistics_melee_crit", **qline_dict)

        self.weapon_statistics_attack_bonus_label = create_qlabel("weapon_statistics_attack_bonus_label", **qlabel_dict)
        self.weapon_statistics_damage_label = create_qlabel("weapon_statistics_damage_label", **qlabel_dict)
        self.weapon_statistics_crit_label = create_qlabel("weapon_statistics_crit_label", **qlabel_dict)
        self.weapon_statistics_melee_label = create_qlabel("weapon_statistics_melee_label", **qlabel_dict)
        self.weapon_statistics_ranged_label = create_qlabel("weapon_statistics_ranged_label", **qlabel_dict)

        self.WeaponStatisticsLayout.addWidget(self.weapon_statistics_ranged_damage, 2, 2, 1, 1)
        self.WeaponStatisticsLayout.addWidget(self.weapon_statistics_melee_damage, 1, 2, 1, 1)
        self.WeaponStatisticsLayout.addWidget(self.weapon_statistics_ranged_attack_bonus, 2, 1, 1, 1)
        self.WeaponStatisticsLayout.addWidget(self.weapon_statistics_ranged_crit, 2, 3, 1, 1)
        self.WeaponStatisticsLayout.addWidget(self.weapon_statistics_melee_attack_bonus, 1, 1, 1, 1)
        self.WeaponStatisticsLayout.addWidget(self.weapon_statistics_melee_crit, 1, 3, 1, 1)
        self.WeaponStatisticsLayout.addWidget(self.weapon_statistics_attack_bonus_label, 0, 1, 1, 1)
        self.WeaponStatisticsLayout.addWidget(self.weapon_statistics_damage_label, 0, 2, 1, 1)
        self.WeaponStatisticsLayout.addWidget(self.weapon_statistics_crit_label, 0, 3, 1, 1)
        self.WeaponStatisticsLayout.addWidget(self.weapon_statistics_melee_label, 1, 0, 1, 1)
        self.WeaponStatisticsLayout.addWidget(self.weapon_statistics_ranged_label, 2, 0, 1, 1)

        self.translate_weapon_statistics_box()

    def translate_weapon_statistics_box(self):
        _translate = QtCore.QCoreApplication.translate
        self.Box.setTitle(_translate("MainWindow", "Current weapon statistics"))
        self.weapon_statistics_attack_bonus_label.setText(_translate("MainWindow", "Attack bonus"))
        self.weapon_statistics_ranged_damage.setText(_translate("MainWindow", "10"))
        self.weapon_statistics_ranged_attack_bonus.setText(_translate("MainWindow", "10"))
        self.weapon_statistics_ranged_crit.setText(_translate("MainWindow", "10"))
        self.weapon_statistics_melee_attack_bonus.setText(_translate("MainWindow", "10"))
        self.weapon_statistics_melee_crit.setText(_translate("MainWindow", "10"))
        self.weapon_statistics_damage_label.setText(_translate("MainWindow", "Damage"))
        self.weapon_statistics_crit_label.setText(_translate("MainWindow", "Crit range"))
        self.weapon_statistics_melee_damage.setText(_translate("MainWindow", "10"))
        self.weapon_statistics_melee_label.setText(_translate("MainWindow", "Melee"))
        self.weapon_statistics_ranged_label.setText(_translate("MainWindow", "Ranged"))