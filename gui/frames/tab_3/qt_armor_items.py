from types import SimpleNamespace

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication

from gui.frames.qt_generic_classes import DefaultBox
from gui.frames.qt_generic_functions import create_qline_edit, create_qlabel, add_multiple_elements_to_layout_by_row, \
    get_float_from_widget, get_int_from_widget, create_checkbox, add_element_to_layout
from gui.frames.tab_1.qt_hp_ac import HpAcBox
from gui.frames.tab_2.qt_items import ItemsBox


class ArmorItems(DefaultBox):
    def __init__(self, parent, position, size, items_box: ItemsBox, hp_ac_box: HpAcBox):
        self.increase_height = 170
        self.items_box = items_box
        self.hp_ac_box = hp_ac_box
        self.root = QtWidgets.QGroupBox(parent)
        self.root.setGeometry(QtCore.QRect(*position, *size))
        self.initial_armor_height_offset = 20
        self.armors = []
        self.item_count = len(self.armors)
        for _ in range(4):
            self.armors.append(self.create_armor())
            self.update_size()

        self._update_weight()
        self._update_armor_ac()

    def create_armor(self):
        new_armor = SimpleNamespace()
        self.item_count = len(self.armors)
        new_armor.root = QtWidgets.QGroupBox(self.root)
        new_armor.root.setGeometry(QtCore.QRect(10, self.initial_armor_height_offset +
                                                self.increase_height * self.item_count, 590, 160))
        new_armor.root.setTitle("Armor")

        new_armor.container = QtWidgets.QWidget(new_armor.root)
        new_armor.container.setGeometry(QtCore.QRect(10, 20, 570, 130))
        new_armor.layout = QtWidgets.QGridLayout(new_armor.container)
        qline_dict = dict(parent=new_armor.container)

        new_armor.test_penalty = create_qline_edit(**qline_dict)
        new_armor.type = create_qline_edit(**qline_dict)
        new_armor.max_dex_bonus = create_qline_edit(**qline_dict)
        new_armor.name = create_qline_edit(**qline_dict, min_size=[150, None],
                                           function_on_text_changed=self._update_root_text,
                                           args_on_text_changed=[new_armor])
        new_armor.ac_bonus = create_qline_edit(function_on_text_changed=self._update_armor_ac,
                                               **qline_dict)
        new_armor.weight = create_qline_edit(function_on_text_changed=self._update_weight, **qline_dict)
        new_armor.spell_fail = create_qline_edit(**qline_dict)
        new_armor.speed = create_qline_edit(**qline_dict)
        new_armor.equipped = create_checkbox(function_on_toggle=self._update_armor_ac, **qline_dict)
        new_armor.special = create_qline_edit(**qline_dict)

        new_armor.max_dex_bonus_label = create_qlabel(**qline_dict)
        new_armor.test_penalty_label = create_qlabel(**qline_dict)
        new_armor.type_label = create_qlabel(**qline_dict)
        new_armor.ac_bonus_label = create_qlabel(**qline_dict)
        new_armor.weight_label = create_qlabel(**qline_dict)
        new_armor.spell_fail_label = create_qlabel(**qline_dict)
        new_armor.speed_label = create_qlabel(**qline_dict)
        new_armor.equipped_label = create_qlabel(**qline_dict)
        new_armor.name_label = create_qlabel(**qline_dict)
        new_armor.special_label = create_qlabel(**qline_dict)

        self._add_new_element_to_layout(new_armor)

        return new_armor

    def update_size(self):
        root_width = self.root.width()
        root_height = self.root.height()
        self.root.setMinimumSize(QtCore.QSize(root_width, root_height + self.increase_height))


    def add_to_layout(self, **kwargs):
        pass

    def _update_weight(self):
        total_weight = 0
        for armor in self.armors:
            total_weight += get_float_from_widget(armor.weight, 0)
        self.items_box.armor_weight = total_weight
        self.items_box.calculate_weight()

    def _add_new_element_to_layout(self, new_armor):
        # TODO - better handling of single elements with non-1 width
        first_row = [new_armor.equipped_label, new_armor.equipped]
        add_multiple_elements_to_layout_by_row(new_armor.layout, first_row)

        second_row = [new_armor.name_label, new_armor.type_label, new_armor.ac_bonus_label,
                      new_armor.test_penalty_label, new_armor.max_dex_bonus_label]
        add_element_to_layout(new_armor.layout, second_row[0], row=1, column=0, height=1, width=3)
        add_multiple_elements_to_layout_by_row(new_armor.layout, second_row[1:], row=1, start_column=3)

        third_row = [new_armor.name, new_armor.type, new_armor.ac_bonus,
                     new_armor.test_penalty, new_armor.max_dex_bonus, ]
        add_element_to_layout(new_armor.layout, third_row[0], row=2, column=0, height=1, width=3)
        add_multiple_elements_to_layout_by_row(new_armor.layout, third_row[1:], row=2, start_column=3)

        fourth_row = [new_armor.weight_label, new_armor.spell_fail_label, new_armor.speed_label, ]
        add_element_to_layout(new_armor.layout, new_armor.special_label, 3, 0, 1, 4)
        add_multiple_elements_to_layout_by_row(new_armor.layout, fourth_row, row=3, start_column=4)

        fith_row = [new_armor.weight, new_armor.spell_fail, new_armor.speed]
        add_element_to_layout(new_armor.layout, new_armor.special, 4, 0, 1, 4)
        add_multiple_elements_to_layout_by_row(new_armor.layout, fith_row, row=4, start_column=4)

    def _update_armor_ac(self):
        total_ac = 0
        for armor in self.armors:
            if armor.equipped.isChecked():
                total_ac += get_int_from_widget(armor.ac_bonus, 0)
        self.hp_ac_box.ac_armor_bonus.setText(str(total_ac))

    def _update_root_text(self, new_armor):
        name = new_armor.name.text()
        new_armor.root.setTitle(name)

    def retranslate(self):
        self.root.setTitle(QApplication.translate("Armors", "Armor items"))
        for armor in self.armors:
            armor.max_dex_bonus_label.setText(QApplication.translate("Armors", "Max dex. bonus"))
            armor.test_penalty_label.setText(QApplication.translate("Armors", "Test penalty"))
            armor.type_label.setText(QApplication.translate("Armors", "Type"))
            armor.ac_bonus_label.setText(QApplication.translate("Armors", "AC bonus"))
            armor.weight_label.setText(QApplication.translate("Armors", "Weight"))
            armor.spell_fail_label.setText(QApplication.translate("Armors", "Spell fail"))
            armor.speed_label.setText(QApplication.translate("Armors", "Speed"))
            armor.name_label.setText(QApplication.translate("Armors", "Name"))
            armor.special_label.setText(QApplication.translate("Armors", "Special"))
            armor.equipped_label.setText(QApplication.translate("Armors", "Equipped"))
