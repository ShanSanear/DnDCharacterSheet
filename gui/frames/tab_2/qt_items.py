from types import SimpleNamespace

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication

from core.character import Character
from gui.frames.qt_generic_classes import ScrollableBox
from gui.frames.qt_generic_functions import create_qlabel, create_qline_edit, \
    add_multiple_elements_to_layout_by_row, create_push_button, get_int_from_widget, get_float_from_widget, \
    add_element_to_layout


class ItemsBox(ScrollableBox):
    def __init__(self, parent, position, size, char_core: Character):
        self.char_core = char_core
        base_size = [size[0], 100]
        height_increment = 29
        max_height = size[1]
        ScrollableBox.__init__(self, parent=parent, position=position, original_size=size, base_size=base_size,
                               max_height=max_height, height_increment=height_increment, row_offset=1,
                               last_row_column=4)

        self.max_encumbrance_map = {1: 1.5, 2: 3, 3: 5, 4: 6.5, 5: 8, 6: 10, 7: 11.5, 8: 13, 9: 15, 10: 16.5, 11: 19,
                                    12: 21.5, 13: 25, 14: 29, 15: 33, 16: 38, 17: 43, 18: 50, 19: 58, 20: 66.5,
                                    21: 76.5, 22: 86.5, 23: 100, 24: 116.5, 25: 133, 26: 153, 27: 173, 28: 200,
                                    29: 233.3, }

        qlabel_dict = dict(parent=self.container)
        self.items_name_label = create_qlabel(**qlabel_dict)
        self.items_weight_label = create_qlabel(**qlabel_dict)
        self.items_count_label = create_qlabel(**qlabel_dict)
        self.items_description_label = create_qlabel(**qlabel_dict)
        self.total_encumbrance = create_qline_edit(self.container, max_size=[30, None], enabled=False,
                                                   align=QtCore.Qt.AlignCenter)
        self.total_encumbrance_label = create_qlabel(self.container,
                                                     align=QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.weight_separator_label = create_qlabel(self.container,
                                                    align=QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter, text="/")
        self.max_encumbrance = create_qline_edit(self.container, max_size=[30, None], enabled=False,
                                                 align=QtCore.Qt.AlignCenter)
        self.labels = [self.items_name_label, self.items_weight_label, self.items_count_label,
                       self.items_description_label]
        self.add_to_layout()
        self.add_item = self.add_new_element
        self.add_new.clicked.connect(self.add_item)
        self.melee_weapons_weight = 0
        self.ranged_weapons_weight = 0
        self.armor_weight = 0
        self.add_item()

    def create_new_item(self):
        new_item = SimpleNamespace()
        new_item.name = create_qline_edit(self.container, min_size=[200, 23])
        new_item.weight = create_qline_edit(self.container, min_size=[None, 23],
                                            max_size=[30, None], function_on_text_changed=self.calculate_weight)

        new_item.count = create_qline_edit(self.container, min_size=[None, 23],
                                           max_size=[30, None], function_on_text_changed=self.calculate_weight)
        new_item.description = create_qline_edit(self.container, min_size=[None, 23])
        new_item.delete_item = create_push_button("item_delete", self.container, min_size=[20, 20], max_size=[20, 20],
                                                  text="-",
                                                  function_on_clicked=self._remove_element, args_on_clicked=new_item)

        return new_item

    def add_last_row(self):
        last_row_idx = len(self.elements_list) + 1
        add_element_to_layout(self.layout, self.total_encumbrance_label, row=last_row_idx, column=0, width=1, height=1)
        add_element_to_layout(self.layout, self.total_encumbrance, row=last_row_idx, column=1, width=1, height=1)
        add_element_to_layout(self.layout, self.weight_separator_label, row=last_row_idx, column=2, width=1, height=1)
        add_element_to_layout(self.layout, self.max_encumbrance, row=last_row_idx, column=3, width=1, height=1)
        add_element_to_layout(self.layout, self.sort_button, row=last_row_idx, column=8, width=1, height=1)
        add_element_to_layout(self.layout, self.add_new, row=last_row_idx, column=9, width=1, height=1)

    def create_new_element(self):
        self.increase_height()
        return self.create_new_item()

    def add_to_layout(self):
        item_name_label = self.labels[0]
        rest = self.labels[1:]
        add_element_to_layout(self.layout, item_name_label, row=0, column=0, height=1, width=5)
        add_multiple_elements_to_layout_by_row(self.layout, rest, start_column=5)
        self.add_last_row()

    def set_values_from_attributes(self):
        str_ref_core = getattr(self.char_core.attributes, "str")
        str_value = str_ref_core['value']
        try:
            max_encumbrance = self.max_encumbrance_map[str_value]
        except KeyError:
            max_encumbrance = str_value * 6.4
        self.max_encumbrance.setText(str(max_encumbrance))

    def calculate_weight(self):
        total_weight = 0
        for item in self.elements_list:
            count = get_int_from_widget(item.count, 1)
            total_weight += get_float_from_widget(item.weight, 0) * count
        total_weight += self.melee_weapons_weight
        total_weight += self.ranged_weapons_weight
        total_weight += self.armor_weight
        self.total_encumbrance.setText(str(total_weight))

    def adding_new_element_to_layout(self, element_idx, values):
        self.layout.removeWidget(self.add_new)
        item_name = values[0]
        rest = values[1:-2]
        description_field = values[-2]
        remove_item_button = values[-1]
        add_element_to_layout(self.layout, item_name, row=self.row_offset + element_idx, column=0, height=1,
                              width=5)
        add_multiple_elements_to_layout_by_row(self.layout, rest, start_column=5, row=self.row_offset + element_idx)
        add_element_to_layout(self.layout, description_field, row=self.row_offset + element_idx, column=7, height=1,
                              width=2)
        add_element_to_layout(self.layout, remove_item_button, row=self.row_offset + element_idx, column=9, height=1,
                              width=1)
        self.add_last_row()

    def retranslate(self):
        self.root.setTitle(QApplication.translate("Items", "Items"))
        self.items_weight_label.setText(QApplication.translate("Items", "Weight"))
        self.items_name_label.setText(QApplication.translate("Items", "Item name"))
        self.items_count_label.setText(QApplication.translate("Items", "Count"))
        self.items_description_label.setText(QApplication.translate("Items", "Description"))
        self.total_encumbrance_label.setText(QApplication.translate("Items", "Total encumbrance:"))
