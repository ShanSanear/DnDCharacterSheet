from PyQt5 import QtWidgets, QtCore


class ArmorItems:
    # TODO - function based widgets and labels
    # TODO - generalized single armor layout (maybe will add option for adding another items here?)
    # TODO - generalized translation
    # TODO - adding widgets by rows/columns
    def __init__(self, parent, position, size):
        self.root = QtWidgets.QGroupBox(parent)
        self.root.setGeometry(QtCore.QRect(*position, *size))
        self.root.setObjectName("ArmorItems")
        self.Armor2 = QtWidgets.QGroupBox(self.root)
        self.Armor2.setGeometry(QtCore.QRect(10, 170, 591, 151))
        self.Armor2.setObjectName("Armor2")
        self.gridLayoutWidget_16 = QtWidgets.QWidget(self.Armor2)
        self.gridLayoutWidget_16.setGeometry(QtCore.QRect(10, 20, 571, 101))
        self.gridLayoutWidget_16.setObjectName("gridLayoutWidget_16")
        self.Armor2Layout = QtWidgets.QGridLayout(self.gridLayoutWidget_16)
        self.Armor2Layout.setContentsMargins(9, 9, 9, 9)
        self.Armor2Layout.setSpacing(6)
        self.Armor2Layout.setObjectName("Armor2Layout")
        self.armor_2_test_penalty = QtWidgets.QLineEdit(self.gridLayoutWidget_16)
        self.armor_2_test_penalty.setMinimumSize(QtCore.QSize(0, 23))
        self.armor_2_test_penalty.setObjectName("armor_2_test_penalty")
        self.Armor2Layout.addWidget(self.armor_2_test_penalty, 1, 3, 1, 1)
        self.armor_2_max_dex_bonus_label = QtWidgets.QLabel(self.gridLayoutWidget_16)
        self.armor_2_max_dex_bonus_label.setObjectName("armor_2_max_dex_bonus_label")
        self.Armor2Layout.addWidget(self.armor_2_max_dex_bonus_label, 0, 4, 1, 1)
        self.armor_2_test_penalty_label = QtWidgets.QLabel(self.gridLayoutWidget_16)
        self.armor_2_test_penalty_label.setObjectName("armor_2_test_penalty_label")
        self.Armor2Layout.addWidget(self.armor_2_test_penalty_label, 0, 3, 1, 1)
        self.armor_2_type = QtWidgets.QLineEdit(self.gridLayoutWidget_16)
        self.armor_2_type.setMinimumSize(QtCore.QSize(0, 23))
        self.armor_2_type.setObjectName("armor_2_type")
        self.Armor2Layout.addWidget(self.armor_2_type, 1, 1, 1, 1)
        self.armor_2_max_dex_bonus = QtWidgets.QLineEdit(self.gridLayoutWidget_16)
        self.armor_2_max_dex_bonus.setMinimumSize(QtCore.QSize(0, 23))
        self.armor_2_max_dex_bonus.setObjectName("armor_2_max_dex_bonus")
        self.Armor2Layout.addWidget(self.armor_2_max_dex_bonus, 1, 4, 1, 1)
        self.armor_2_name = QtWidgets.QLineEdit(self.gridLayoutWidget_16)
        self.armor_2_name.setMinimumSize(QtCore.QSize(0, 23))
        self.armor_2_name.setObjectName("armor_2_name")
        self.Armor2Layout.addWidget(self.armor_2_name, 1, 0, 1, 1)
        self.armor_2_ac_bonus = QtWidgets.QLineEdit(self.gridLayoutWidget_16)
        self.armor_2_ac_bonus.setMinimumSize(QtCore.QSize(0, 23))
        self.armor_2_ac_bonus.setObjectName("armor_2_ac_bonus")
        self.Armor2Layout.addWidget(self.armor_2_ac_bonus, 1, 2, 1, 1)
        self.armor_2_type_label = QtWidgets.QLabel(self.gridLayoutWidget_16)
        self.armor_2_type_label.setObjectName("armor_2_type_label")
        self.Armor2Layout.addWidget(self.armor_2_type_label, 0, 1, 1, 1)
        self.armor_2_ac_bonus_label = QtWidgets.QLabel(self.gridLayoutWidget_16)
        self.armor_2_ac_bonus_label.setObjectName("armor_2_ac_bonus_label")
        self.Armor2Layout.addWidget(self.armor_2_ac_bonus_label, 0, 2, 1, 1)
        self.armor_2_weight_label = QtWidgets.QLabel(self.gridLayoutWidget_16)
        self.armor_2_weight_label.setObjectName("armor_2_weight_label")
        self.Armor2Layout.addWidget(self.armor_2_weight_label, 2, 2, 1, 1)
        self.armor_2_spell_fail_label = QtWidgets.QLabel(self.gridLayoutWidget_16)
        self.armor_2_spell_fail_label.setObjectName("armor_2_spell_fail_label")
        self.Armor2Layout.addWidget(self.armor_2_spell_fail_label, 2, 3, 1, 1)
        self.armor_2_speed_label = QtWidgets.QLabel(self.gridLayoutWidget_16)
        self.armor_2_speed_label.setObjectName("armor_2_speed_label")
        self.Armor2Layout.addWidget(self.armor_2_speed_label, 2, 4, 1, 1)
        self.armor_2_name_label = QtWidgets.QLabel(self.gridLayoutWidget_16)
        self.armor_2_name_label.setObjectName("armor_2_name_label")
        self.Armor2Layout.addWidget(self.armor_2_name_label, 0, 0, 1, 1)
        self.armor_2_weight = QtWidgets.QLineEdit(self.gridLayoutWidget_16)
        self.armor_2_weight.setMinimumSize(QtCore.QSize(0, 23))
        self.armor_2_weight.setObjectName("armor_2_weight")
        self.Armor2Layout.addWidget(self.armor_2_weight, 3, 2, 1, 1)
        self.armor_2_spell_fail = QtWidgets.QLineEdit(self.gridLayoutWidget_16)
        self.armor_2_spell_fail.setMinimumSize(QtCore.QSize(0, 23))
        self.armor_2_spell_fail.setObjectName("armor_2_spell_fail")
        self.Armor2Layout.addWidget(self.armor_2_spell_fail, 3, 3, 1, 1)
        self.armor_2_speed = QtWidgets.QLineEdit(self.gridLayoutWidget_16)
        self.armor_2_speed.setMinimumSize(QtCore.QSize(0, 23))
        self.armor_2_speed.setObjectName("armor_2_speed")
        self.Armor2Layout.addWidget(self.armor_2_speed, 3, 4, 1, 1)
        self.armor_2_special = QtWidgets.QLineEdit(self.gridLayoutWidget_16)
        self.armor_2_special.setMinimumSize(QtCore.QSize(0, 23))
        self.armor_2_special.setObjectName("armor_2_special")
        self.Armor2Layout.addWidget(self.armor_2_special, 3, 0, 1, 2)
        self.armor_2_special_label = QtWidgets.QLabel(self.gridLayoutWidget_16)
        self.armor_2_special_label.setObjectName("armor_2_special_label")
        self.Armor2Layout.addWidget(self.armor_2_special_label, 2, 0, 1, 2)
        self.Armor1 = QtWidgets.QGroupBox(self.root)
        self.Armor1.setGeometry(QtCore.QRect(10, 30, 591, 131))
        self.Armor1.setObjectName("Armor1")
        self.gridLayoutWidget_15 = QtWidgets.QWidget(self.Armor1)
        self.gridLayoutWidget_15.setGeometry(QtCore.QRect(10, 20, 571, 101))
        self.gridLayoutWidget_15.setObjectName("gridLayoutWidget_15")
        self.Armor1Layout = QtWidgets.QGridLayout(self.gridLayoutWidget_15)
        self.Armor1Layout.setContentsMargins(9, 9, 9, 9)
        self.Armor1Layout.setSpacing(6)
        self.Armor1Layout.setObjectName("Armor1Layout")
        self.armor_1_test_penalty = QtWidgets.QLineEdit(self.gridLayoutWidget_15)
        self.armor_1_test_penalty.setMinimumSize(QtCore.QSize(0, 23))
        self.armor_1_test_penalty.setObjectName("armor_1_test_penalty")
        self.Armor1Layout.addWidget(self.armor_1_test_penalty, 1, 3, 1, 1)
        self.armor_1_max_dex_bonus_label = QtWidgets.QLabel(self.gridLayoutWidget_15)
        self.armor_1_max_dex_bonus_label.setObjectName("armor_1_max_dex_bonus_label")
        self.Armor1Layout.addWidget(self.armor_1_max_dex_bonus_label, 0, 4, 1, 1)
        self.armor_1_test_penalty_label = QtWidgets.QLabel(self.gridLayoutWidget_15)
        self.armor_1_test_penalty_label.setObjectName("armor_1_test_penalty_label")
        self.Armor1Layout.addWidget(self.armor_1_test_penalty_label, 0, 3, 1, 1)
        self.armor_1_type = QtWidgets.QLineEdit(self.gridLayoutWidget_15)
        self.armor_1_type.setMinimumSize(QtCore.QSize(0, 23))
        self.armor_1_type.setObjectName("armor_1_type")
        self.Armor1Layout.addWidget(self.armor_1_type, 1, 1, 1, 1)
        self.armor_1_max_dex_bonus = QtWidgets.QLineEdit(self.gridLayoutWidget_15)
        self.armor_1_max_dex_bonus.setMinimumSize(QtCore.QSize(0, 23))
        self.armor_1_max_dex_bonus.setObjectName("armor_1_max_dex_bonus")
        self.Armor1Layout.addWidget(self.armor_1_max_dex_bonus, 1, 4, 1, 1)
        self.armor_1_name = QtWidgets.QLineEdit(self.gridLayoutWidget_15)
        self.armor_1_name.setMinimumSize(QtCore.QSize(0, 23))
        self.armor_1_name.setObjectName("armor_1_name")
        self.Armor1Layout.addWidget(self.armor_1_name, 1, 0, 1, 1)
        self.armor_1_ac_bonus = QtWidgets.QLineEdit(self.gridLayoutWidget_15)
        self.armor_1_ac_bonus.setMinimumSize(QtCore.QSize(0, 23))
        self.armor_1_ac_bonus.setObjectName("armor_1_ac_bonus")
        self.Armor1Layout.addWidget(self.armor_1_ac_bonus, 1, 2, 1, 1)
        self.armor_1_type_label = QtWidgets.QLabel(self.gridLayoutWidget_15)
        self.armor_1_type_label.setObjectName("armor_1_type_label")
        self.Armor1Layout.addWidget(self.armor_1_type_label, 0, 1, 1, 1)
        self.armor_1_ac_bonus_label = QtWidgets.QLabel(self.gridLayoutWidget_15)
        self.armor_1_ac_bonus_label.setObjectName("armor_1_ac_bonus_label")
        self.Armor1Layout.addWidget(self.armor_1_ac_bonus_label, 0, 2, 1, 1)
        self.armor_1_weight_label = QtWidgets.QLabel(self.gridLayoutWidget_15)
        self.armor_1_weight_label.setObjectName("armor_1_weight_label")
        self.Armor1Layout.addWidget(self.armor_1_weight_label, 2, 2, 1, 1)
        self.armor_1_spell_fail_label = QtWidgets.QLabel(self.gridLayoutWidget_15)
        self.armor_1_spell_fail_label.setObjectName("armor_1_spell_fail_label")
        self.Armor1Layout.addWidget(self.armor_1_spell_fail_label, 2, 3, 1, 1)
        self.armor_1_speed_label = QtWidgets.QLabel(self.gridLayoutWidget_15)
        self.armor_1_speed_label.setObjectName("armor_1_speed_label")
        self.Armor1Layout.addWidget(self.armor_1_speed_label, 2, 4, 1, 1)
        self.armor_1_name_label = QtWidgets.QLabel(self.gridLayoutWidget_15)
        self.armor_1_name_label.setObjectName("armor_1_name_label")
        self.Armor1Layout.addWidget(self.armor_1_name_label, 0, 0, 1, 1)
        self.armor_1_weight = QtWidgets.QLineEdit(self.gridLayoutWidget_15)
        self.armor_1_weight.setMinimumSize(QtCore.QSize(0, 23))
        self.armor_1_weight.setObjectName("armor_1_weight")
        self.Armor1Layout.addWidget(self.armor_1_weight, 3, 2, 1, 1)
        self.armor_1_spell_fail = QtWidgets.QLineEdit(self.gridLayoutWidget_15)
        self.armor_1_spell_fail.setMinimumSize(QtCore.QSize(0, 23))
        self.armor_1_spell_fail.setObjectName("armor_1_spell_fail")
        self.Armor1Layout.addWidget(self.armor_1_spell_fail, 3, 3, 1, 1)
        self.armor_1_speed = QtWidgets.QLineEdit(self.gridLayoutWidget_15)
        self.armor_1_speed.setMinimumSize(QtCore.QSize(0, 23))
        self.armor_1_speed.setObjectName("armor_1_speed")
        self.Armor1Layout.addWidget(self.armor_1_speed, 3, 4, 1, 1)
        self.armor_1_special = QtWidgets.QLineEdit(self.gridLayoutWidget_15)
        self.armor_1_special.setMinimumSize(QtCore.QSize(0, 23))
        self.armor_1_special.setObjectName("armor_1_special")
        self.Armor1Layout.addWidget(self.armor_1_special, 3, 0, 1, 2)
        self.armor_1_special_label = QtWidgets.QLabel(self.gridLayoutWidget_15)
        self.armor_1_special_label.setObjectName("armor_1_special_label")
        self.Armor1Layout.addWidget(self.armor_1_special_label, 2, 0, 1, 2)
        self.translate_armor_items_box()

    def translate_armor_items_box(self):
        _translate = QtCore.QCoreApplication.translate
        self.root.setTitle(_translate("MainWindow", "Armor items"))
        self.Armor2.setTitle(_translate("MainWindow", "Shield / Protective item"))
        self.armor_2_test_penalty.setText(_translate("MainWindow", "10"))
        self.armor_2_max_dex_bonus_label.setText(_translate("MainWindow", "Max dex. bonus"))
        self.armor_2_test_penalty_label.setText(_translate("MainWindow", "Tests penalty"))
        self.armor_2_type.setText(_translate("MainWindow", "Lorem ipsum"))
        self.armor_2_max_dex_bonus.setText(_translate("MainWindow", "10"))
        self.armor_2_name.setText(_translate("MainWindow", "Lorem ipsum"))
        self.armor_2_ac_bonus.setText(_translate("MainWindow", "10"))
        self.armor_2_type_label.setText(_translate("MainWindow", "Type"))
        self.armor_2_ac_bonus_label.setText(_translate("MainWindow", "AC bonus"))
        self.armor_2_weight_label.setText(_translate("MainWindow", "Weight"))
        self.armor_2_spell_fail_label.setText(_translate("MainWindow", "Spell fail"))
        self.armor_2_speed_label.setText(_translate("MainWindow", "Speed"))
        self.armor_2_name_label.setText(_translate("MainWindow", "Name"))
        self.armor_2_weight.setText(_translate("MainWindow", "10"))
        self.armor_2_spell_fail.setText(_translate("MainWindow", "10"))
        self.armor_2_speed.setText(_translate("MainWindow", "10"))
        self.armor_2_special.setText(_translate("MainWindow", "Lorem ipsum"))
        self.armor_2_special_label.setText(_translate("MainWindow", "Special"))
        self.Armor1.setTitle(_translate("MainWindow", "Armor / Protective item"))
        self.armor_1_test_penalty.setText(_translate("MainWindow", "10"))
        self.armor_1_max_dex_bonus_label.setText(_translate("MainWindow", "Max dex. bonus"))
        self.armor_1_test_penalty_label.setText(_translate("MainWindow", "Tests penalty"))
        self.armor_1_type.setText(_translate("MainWindow", "Lorem ipsum"))
        self.armor_1_max_dex_bonus.setText(_translate("MainWindow", "10"))
        self.armor_1_name.setText(_translate("MainWindow", "Lorem ipsum"))
        self.armor_1_ac_bonus.setText(_translate("MainWindow", "10"))
        self.armor_1_type_label.setText(_translate("MainWindow", "Type"))
        self.armor_1_ac_bonus_label.setText(_translate("MainWindow", "AC bonus"))
        self.armor_1_weight_label.setText(_translate("MainWindow", "Weight"))
        self.armor_1_spell_fail_label.setText(_translate("MainWindow", "Spell fail"))
        self.armor_1_speed_label.setText(_translate("MainWindow", "Speed"))
        self.armor_1_name_label.setText(_translate("MainWindow", "Name"))
        self.armor_1_weight.setText(_translate("MainWindow", "10"))
        self.armor_1_spell_fail.setText(_translate("MainWindow", "10"))
        self.armor_1_speed.setText(_translate("MainWindow", "10"))
        self.armor_1_special.setText(_translate("MainWindow", "Lorem ipsum"))
        self.armor_1_special_label.setText(_translate("MainWindow", "Special"))