from types import SimpleNamespace

from PyQt5 import QtWidgets, QtCore

from gui.frames.qt_generic_classes import DefaultBox
from gui.frames.qt_generic_functions import create_qline_edit, create_qlabel, add_multiple_elements_to_layout_by_row, \
    set_text_of_children, get_float_from_widget, get_int_from_widget, create_checkbox
from gui.frames.tab_1.qt_hp_ac import HpAcBox
from gui.frames.tab_2.qt_items import ItemsBox


class ArmorItems(DefaultBox):
    def __init__(self, parent, position, size, items_box: ItemsBox, hp_ac_box: HpAcBox):
        # TODO checkboxes for setting in the first tab
        self.increase_height = 170
        self.items_box = items_box
        self.hp_ac_box = hp_ac_box
        self.root = QtWidgets.QGroupBox(parent)
        self.root.setGeometry(QtCore.QRect(*position, *size))
        self.initial_armor_height_offset = 20
        self.armors = []
        self.item_count = len(self.armors)
        self.translate_reference_new_element = {
            "EN": {"root": {
                "title": f"Armor_0"
            },
                "test_penalty": "10",
                "max_dex_bonus_label": "Max dex. bonus",
                "test_penalty_label": "Test penalty",
                "type": "Lorem ipsum",
                "max_dex_bonus": "10",
                "name": "Lorem ipsum",
                "ac_bonus": "10",
                "type_label": "Type",
                "ac_bonus_label": "AC bonus",
                "weight_label": "Weight",
                "spell_fail_label": "Spell fail",
                "speed_label": "Speed",
                "name_label": "Name",
                "weight": "10",
                "spell_fail": "10",
                "speed": "10",
                "special": "Lorem ipsum",
                "special_label": "Special",
                "equipped_label" : "Equipped"}
        }
        for _ in range(4):
            self.armors.append(self.create_armor())
            self.update_size()

        self.translate()
        self._update_weight()
        self._update_armor_ac()

    def create_armor(self):
        new_armor = SimpleNamespace()
        self.item_count = len(self.armors)
        new_armor.root = QtWidgets.QGroupBox(self.root)
        new_armor.root.setGeometry(QtCore.QRect(10, self.initial_armor_height_offset +
                                                self.increase_height * self.item_count, 590, 160))

        new_armor.container = QtWidgets.QWidget(new_armor.root)
        new_armor.container.setGeometry(QtCore.QRect(10, 20, 570, 130))
        new_armor.layout = QtWidgets.QGridLayout(new_armor.container)
        qline_dict = dict(parent=new_armor.container)

        new_armor.test_penalty = create_qline_edit(**qline_dict)
        new_armor.type = create_qline_edit(**qline_dict)
        new_armor.max_dex_bonus = create_qline_edit(**qline_dict)
        new_armor.name = create_qline_edit(**qline_dict)
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

        self._change_root_title("EN")
        set_text_of_children(new_armor, self.translate_reference_new_element["EN"])
        return new_armor

    def update_size(self):
        root_width = self.root.width()
        root_height = self.root.height()
        self.root.setMinimumSize(QtCore.QSize(root_width, root_height + self.increase_height))

    def translate(self):
        self.root.setTitle("Armor items")

    def add_to_layout(self, **kwargs):
        pass

    def _update_weight(self):
        total_weight = 0
        for armor in self.armors:
            total_weight += get_float_from_widget(armor.weight, 0)
        self.items_box.armor_weight = total_weight
        self.items_box.calculate_weight()

    def _add_new_element_to_layout(self, new_armor):
        first_row = [new_armor.equipped_label, new_armor.equipped]

        second_row = [new_armor.name_label, new_armor.type_label, new_armor.ac_bonus_label,
                            new_armor.test_penalty_label, new_armor.max_dex_bonus_label]
        third_row = [new_armor.name, new_armor.type, new_armor.ac_bonus,
                      new_armor.test_penalty, new_armor.max_dex_bonus, ]
        fourth_row = [new_armor.weight_label, new_armor.spell_fail_label, new_armor.speed_label, ]

        # TODO - better handling of single elements with non-1 width
        add_multiple_elements_to_layout_by_row(new_armor.layout, first_row)
        add_multiple_elements_to_layout_by_row(new_armor.layout, second_row, row=1)
        add_multiple_elements_to_layout_by_row(new_armor.layout, third_row, row=2)
        new_armor.layout.addWidget(new_armor.special_label, 3, 0, 1, 2)
        add_multiple_elements_to_layout_by_row(new_armor.layout, fourth_row, row=3, start_column=2)
        new_armor.layout.addWidget(new_armor.special, 4, 0, 1, 2)
        fith_row = [new_armor.weight, new_armor.spell_fail, new_armor.speed]
        add_multiple_elements_to_layout_by_row(new_armor.layout, fith_row, row=4, start_column=2)

    def _change_root_title(self, language):
        self.translate_reference_new_element[language]["root"]["title"] = f"Armor_{self.item_count}"

    def _update_armor_ac(self):
        total_ac = 0
        for armor in self.armors:
            if armor.equipped.isChecked():
                total_ac += get_int_from_widget(armor.ac_bonus, 0)
        self.hp_ac_box.ac_armor_bonus.setText(str(total_ac))
