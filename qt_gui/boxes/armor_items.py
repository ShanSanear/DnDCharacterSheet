from types import SimpleNamespace

from PyQt5 import QtWidgets, QtCore

from qt_gui.boxes.qt_generic_classes import ResizeableBox
from qt_gui.boxes.qt_generic_functions import create_qline_edit, create_qlabel, add_multiple_elements_to_layout_by_row


class ArmorItems(ResizeableBox):
    # TODO - function based widgets and labels
    # TODO - generalized single armor layout (maybe will add option for adding another items here?)
    # TODO - generalized translation
    # TODO - adding widgets by rows/columns
    def __init__(self, parent, position, size):
        self.increase_height = 140
        ResizeableBox.__init__(self, increase_height=self.increase_height, increase_width=0)
        self.root = QtWidgets.QGroupBox(parent)
        self.root.setGeometry(QtCore.QRect(*position, *size))
        self.root.setObjectName("ArmorItems")
        self.initial_armor_height_offset = 30
        self.armors = []
        self.armors = [self.create_armor()]
        self.add_armor_2()

        self.translate()

    def create_armor(self):
        new_armor = SimpleNamespace()
        new_armor.root = QtWidgets.QGroupBox(self.root)
        new_armor.root.setGeometry(QtCore.QRect(10, self.initial_armor_height_offset +
                                                self.increase_height * len(self.armors), 591, 131))
        new_armor.root.setObjectName("Armor1")
        new_armor.container = QtWidgets.QWidget(new_armor.root)
        new_armor.container.setGeometry(QtCore.QRect(10, 20, 571, 101))
        new_armor.container.setObjectName("gridLayoutWidget_15")
        new_armor.layout = QtWidgets.QGridLayout(new_armor.container)
        new_armor.layout.setObjectName("Armor1Layout")
        qline_dict = {"parent": new_armor.container}
        
        new_armor.test_penalty = create_qline_edit("armor_1_test_penalty", **qline_dict)
        new_armor.type = create_qline_edit("armor_1_type", **qline_dict)
        new_armor.max_dex_bonus = create_qline_edit("armor_1_max_dex_bonus", **qline_dict)
        new_armor.name = create_qline_edit("armor_1_name", **qline_dict)
        new_armor.ac_bonus = create_qline_edit("armor_1_ac_bonus", **qline_dict)
        new_armor.weight = create_qline_edit("armor_1_weight", **qline_dict)
        new_armor.spell_fail = create_qline_edit("armor_1_spell_fail", **qline_dict)
        new_armor.speed = create_qline_edit("armor_1_speed", **qline_dict)
        new_armor.special = create_qline_edit("armor_1_special", **qline_dict)
        
        new_armor.max_dex_bonus_label = create_qlabel("armor_1_max_dex_bonus_label", **qline_dict)
        new_armor.test_penalty_label = create_qlabel("armor_1_test_penalty_label", **qline_dict)
        new_armor.type_label = create_qlabel("armor_1_type_label", **qline_dict)
        new_armor.ac_bonus_label = create_qlabel("armor_1_ac_bonus_label", **qline_dict)
        new_armor.weight_label = create_qlabel("armor_1_weight_label", **qline_dict)
        new_armor.spell_fail_label = create_qlabel("armor_1_spell_fail_label", **qline_dict)
        new_armor.speed_label = create_qlabel("armor_1_speed_label", **qline_dict)
        new_armor.name_label = create_qlabel("armor_1_name_label", **qline_dict)
        new_armor.special_label = create_qlabel("armor_1_special_label", **qline_dict)

        first_row_to_add = [new_armor.name_label, new_armor.type_label, new_armor.ac_bonus_label,
                            new_armor.test_penalty_label, new_armor.max_dex_bonus_label]
        add_multiple_elements_to_layout_by_row(new_armor.layout, first_row_to_add)


        second_row = [new_armor.name, new_armor.type, new_armor.ac_bonus,
                      new_armor.test_penalty, new_armor.max_dex_bonus,]

        add_multiple_elements_to_layout_by_row(new_armor.layout, second_row, row=1)

        third_row = [new_armor.weight_label, new_armor.spell_fail_label, new_armor.speed_label,]

        new_armor.layout.addWidget(new_armor.special_label, 2, 0, 1, 2)
        add_multiple_elements_to_layout_by_row(new_armor.layout, third_row, row=2, start_column=2)

        new_armor.layout.addWidget(new_armor.special, 3, 0, 1, 2)

        fourth_row = [new_armor.weight, new_armor.spell_fail, new_armor.speed,]

        add_multiple_elements_to_layout_by_row(new_armor.layout, fourth_row, row=3, start_column=2)
        return new_armor

    def add_armor_2(self):
        self.armor_2 = QtWidgets.QGroupBox(self.root)
        self.armor_2.setGeometry(QtCore.QRect(10, 170, 591, 151))
        self.armor_2.setObjectName("Armor2")
        self.container_2 = QtWidgets.QWidget(self.armor_2)
        self.container_2.setGeometry(QtCore.QRect(10, 20, 571, 101))
        self.container_2.setObjectName("gridLayoutWidget_16")
        self.layout_2 = QtWidgets.QGridLayout(self.container_2)
        self.layout_2.setContentsMargins(9, 9, 9, 9)
        self.layout_2.setSpacing(6)
        self.layout_2.setObjectName("Armor2Layout")
        self.armor_2_test_penalty = QtWidgets.QLineEdit(self.container_2)
        self.armor_2_test_penalty.setMinimumSize(QtCore.QSize(0, 23))
        self.armor_2_test_penalty.setObjectName("armor_2_test_penalty")
        self.armor_2_max_dex_bonus_label = QtWidgets.QLabel(self.container_2)
        self.armor_2_max_dex_bonus_label.setObjectName("armor_2_max_dex_bonus_label")
        self.armor_2_test_penalty_label = QtWidgets.QLabel(self.container_2)
        self.armor_2_test_penalty_label.setObjectName("armor_2_test_penalty_label")
        self.armor_2_type = QtWidgets.QLineEdit(self.container_2)
        self.armor_2_type.setMinimumSize(QtCore.QSize(0, 23))
        self.armor_2_type.setObjectName("armor_2_type")
        self.armor_2_max_dex_bonus = QtWidgets.QLineEdit(self.container_2)
        self.armor_2_max_dex_bonus.setMinimumSize(QtCore.QSize(0, 23))
        self.armor_2_max_dex_bonus.setObjectName("armor_2_max_dex_bonus")
        self.armor_2_name = QtWidgets.QLineEdit(self.container_2)
        self.armor_2_name.setMinimumSize(QtCore.QSize(0, 23))
        self.armor_2_name.setObjectName("armor_2_name")
        self.armor_2_ac_bonus = QtWidgets.QLineEdit(self.container_2)
        self.armor_2_ac_bonus.setMinimumSize(QtCore.QSize(0, 23))
        self.armor_2_ac_bonus.setObjectName("armor_2_ac_bonus")
        self.armor_2_type_label = QtWidgets.QLabel(self.container_2)
        self.armor_2_type_label.setObjectName("armor_2_type_label")
        self.armor_2_ac_bonus_label = QtWidgets.QLabel(self.container_2)
        self.armor_2_ac_bonus_label.setObjectName("armor_2_ac_bonus_label")
        self.armor_2_weight_label = QtWidgets.QLabel(self.container_2)
        self.armor_2_weight_label.setObjectName("armor_2_weight_label")
        self.armor_2_spell_fail_label = QtWidgets.QLabel(self.container_2)
        self.armor_2_spell_fail_label.setObjectName("armor_2_spell_fail_label")
        self.armor_2_speed_label = QtWidgets.QLabel(self.container_2)
        self.armor_2_speed_label.setObjectName("armor_2_speed_label")
        self.armor_2_name_label = QtWidgets.QLabel(self.container_2)
        self.armor_2_name_label.setObjectName("armor_2_name_label")
        self.armor_2_weight = QtWidgets.QLineEdit(self.container_2)
        self.armor_2_weight.setMinimumSize(QtCore.QSize(0, 23))
        self.armor_2_weight.setObjectName("armor_2_weight")
        self.armor_2_spell_fail = QtWidgets.QLineEdit(self.container_2)
        self.armor_2_spell_fail.setMinimumSize(QtCore.QSize(0, 23))
        self.armor_2_spell_fail.setObjectName("armor_2_spell_fail")
        self.armor_2_speed = QtWidgets.QLineEdit(self.container_2)
        self.armor_2_speed.setMinimumSize(QtCore.QSize(0, 23))
        self.armor_2_speed.setObjectName("armor_2_speed")
        self.armor_2_special = QtWidgets.QLineEdit(self.container_2)
        self.armor_2_special.setMinimumSize(QtCore.QSize(0, 23))
        self.armor_2_special.setObjectName("armor_2_special")
        self.armor_2_special_label = QtWidgets.QLabel(self.container_2)
        self.armor_2_special_label.setObjectName("armor_2_special_label")
        self.layout_2.addWidget(self.armor_2_test_penalty, 1, 3, 1, 1)
        self.layout_2.addWidget(self.armor_2_max_dex_bonus_label, 0, 4, 1, 1)
        self.layout_2.addWidget(self.armor_2_test_penalty_label, 0, 3, 1, 1)
        self.layout_2.addWidget(self.armor_2_type, 1, 1, 1, 1)
        self.layout_2.addWidget(self.armor_2_max_dex_bonus, 1, 4, 1, 1)
        self.layout_2.addWidget(self.armor_2_name, 1, 0, 1, 1)
        self.layout_2.addWidget(self.armor_2_ac_bonus, 1, 2, 1, 1)
        self.layout_2.addWidget(self.armor_2_type_label, 0, 1, 1, 1)
        self.layout_2.addWidget(self.armor_2_ac_bonus_label, 0, 2, 1, 1)
        self.layout_2.addWidget(self.armor_2_weight_label, 2, 2, 1, 1)
        self.layout_2.addWidget(self.armor_2_spell_fail_label, 2, 3, 1, 1)
        self.layout_2.addWidget(self.armor_2_speed_label, 2, 4, 1, 1)
        self.layout_2.addWidget(self.armor_2_name_label, 0, 0, 1, 1)
        self.layout_2.addWidget(self.armor_2_weight, 3, 2, 1, 1)
        self.layout_2.addWidget(self.armor_2_spell_fail, 3, 3, 1, 1)
        self.layout_2.addWidget(self.armor_2_speed, 3, 4, 1, 1)
        self.layout_2.addWidget(self.armor_2_special, 3, 0, 1, 2)
        self.layout_2.addWidget(self.armor_2_special_label, 2, 0, 1, 2)


    def create_new_element(self):
        pass


    def translate(self):
        _translate = QtCore.QCoreApplication.translate
        self.root.setTitle(_translate("MainWindow", "Armor items"))

        # new_armor.root.setTitle(_translate("MainWindow", "Armor / Protective item"))
        # new_armor.test_penalty.setText(_translate("MainWindow", "10"))
        # new_armor.max_dex_bonus_label.setText(_translate("MainWindow", "Max dex. bonus"))
        # new_armor.test_penalty_label.setText(_translate("MainWindow", "Tests penalty"))
        # new_armor.type.setText(_translate("MainWindow", "Lorem ipsum"))
        # new_armor.max_dex_bonus.setText(_translate("MainWindow", "10"))
        # new_armor.name.setText(_translate("MainWindow", "Lorem ipsum"))
        # new_armor.ac_bonus.setText(_translate("MainWindow", "10"))
        # new_armor.type_label.setText(_translate("MainWindow", "Type"))
        # new_armor.ac_bonus_label.setText(_translate("MainWindow", "AC bonus"))
        # new_armor.weight_label.setText(_translate("MainWindow", "Weight"))
        # new_armor.spell_fail_label.setText(_translate("MainWindow", "Spell fail"))
        # new_armor.speed_label.setText(_translate("MainWindow", "Speed"))
        # new_armor.name_label.setText(_translate("MainWindow", "Name"))
        # new_armor.weight.setText(_translate("MainWindow", "10"))
        # new_armor.spell_fail.setText(_translate("MainWindow", "10"))
        # new_armor.speed.setText(_translate("MainWindow", "10"))
        # new_armor.special.setText(_translate("MainWindow", "Lorem ipsum"))
        # new_armor.special_label.setText(_translate("MainWindow", "Special"))

        self.armor_2.setTitle(_translate("MainWindow", "Shield / Protective item"))
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
