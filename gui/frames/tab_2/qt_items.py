from types import SimpleNamespace

from PyQt5 import QtWidgets, QtCore

from core.character import Character
from gui.frames.qt_generic_classes import ResizeableBox, DefaultBox
from gui.frames.qt_generic_functions import create_qlabel, set_text_of_children, create_qline_edit, \
    add_multiple_elements_to_layout_by_row, create_push_button, get_int_from_widget, get_float_from_widget, \
    add_element_to_layout


class ItemsBox(DefaultBox, ResizeableBox):
    def __init__(self, parent, position, size, char_core: Character):
        # TODO - scrollbar after achieving certain height
        self.parent = parent
        self.root = QtWidgets.QGroupBox(parent)
        self.root.setGeometry(QtCore.QRect(*position, *size))
        self.char_core = char_core
        self.root.setObjectName("ItemsBox")
        self.container = QtWidgets.QWidget(self.root)
        self.container.setObjectName("gridLayoutWidget_8")
        self.layout = QtWidgets.QGridLayout(self.container)
        self.layout.setObjectName("ItemsLayout")
        self.items = []
        self.add_new = create_push_button("add_new_feat", self.container, min_size=[20, 20], max_size=[20, 20], text="+")
        ResizeableBox.__init__(self, elements_list=self.items, row_offset=1, increase_width=0, increase_height=28,
                               last_row_column=4)

        self.max_encumbrance_map = {1: 1.5, 2: 3, 3: 5, 4: 6.5, 5: 8, 6: 10, 7: 11.5, 8: 13, 9: 15, 10: 16.5, 11: 19,
                                    12: 21.5, 13: 25, 14: 29, 15: 33, 16: 38, 17: 43, 18: 50, 19: 58, 20: 66.5,
                                    21: 76.5, 22: 86.5, 23: 100, 24: 116.5, 25: 133, 26: 153, 27: 173, 28: 200,
                                    29: 233.3, }

        qlabel_dict = dict(parent=self.container)
        self.items_name_label = create_qlabel("items_name_label", **qlabel_dict)
        self.items_weight_label = create_qlabel("items_weight_label", **qlabel_dict)
        self.items_count_label = create_qlabel("items_count_label", **qlabel_dict)
        self.items_description_label = create_qlabel("items_description_label", **qlabel_dict)
        self.total_encumbrance = create_qline_edit("items_total_weight", self.container, max_size=[30, None], enabled=False,
                                                   align=QtCore.Qt.AlignCenter)
        self.total_encumbrance_label = create_qlabel("items_total_weight_label", self.container,
                                                     align=QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.weight_separator_label = create_qlabel("max_weight_label", self.container,
                                                    align=QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.max_encumbrance = create_qline_edit("max_weight", self.container, max_size=[30, None], enabled=False,
                                                 align=QtCore.Qt.AlignCenter)
        self.translate_reference = {"EN": {
            "root": {"title": "Items"},
            "items_weight_label": "Weight",
            "items_name_label": "Item name",
            "items_count_label": "Count",
            "items_description_label": "Description",
            "total_encumbrance_label" : "Total encumbrance:",
            "weight_separator_label" : "/"
        }}
        self.last_row = [self.add_new]
        self.container.setGeometry(QtCore.QRect(10, 20, 561, 80))
        self.labels = [self.items_name_label, self.items_weight_label, self.items_count_label,
                       self.items_description_label]
        self.add_to_layout()
        self.translate("EN")
        self.add_item = self.add_new_element
        self.add_new.clicked.connect(self.add_item)
        self.root.setLayout(self.layout)
        self.weapons_weight = 0
        self.armor_weight = 0
        for _ in range(5):
            self.add_item()


    def create_new_item(self):
        new_item = SimpleNamespace()
        new_item.name = create_qline_edit("item_name", self.container, min_size=[200, 23],
                                          function_on_unfocused=self.sort_elements)
        new_item.weight = create_qline_edit("item_weight", self.container, min_size=[None, 23],
                                            max_size=[30, None], function_on_text_changed=self.calculate_weight)

        new_item.count = create_qline_edit("item_count", self.container, min_size=[None, 23],
                                           max_size=[30, None], function_on_text_changed=self.calculate_weight)
        new_item.description = create_qline_edit("item_description", self.container, min_size=[None, 23])
        new_item.delete_item = create_push_button("item_delete", self.container, min_size=[20, 20], max_size=[20, 20], text="-",
                                                  function_on_clicked=self._remove_element, args_on_clicked=new_item)

        return new_item

    def add_last_row(self):
        last_row = len(self.items) + 1
        self.layout.addWidget(self.total_encumbrance_label, last_row, 0, 1, 1)
        self.layout.addWidget(self.total_encumbrance, last_row, 1, 1, 1)
        self.layout.addWidget(self.weight_separator_label, last_row, 2, 1, 1)
        self.layout.addWidget(self.max_encumbrance, last_row, 3, 1, 1)
        self.layout.addWidget(self.add_new, last_row, 8, 1, 1)


    def create_new_element(self):
        return self.create_new_item()

    def add_to_layout(self):
        item_name_label = self.labels[0]
        rest = self.labels[1:]
        add_element_to_layout(self.layout, item_name_label, row=0, column=0, height=1, width=5)
        add_multiple_elements_to_layout_by_row(self.layout, rest, start_column=5)
        self.add_last_row()


    def translate(self, language):
        set_text_of_children(self, self.translate_reference[language])

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
        for item in self.items:
            count = get_int_from_widget(item.count, 1)
            total_weight += get_float_from_widget(item.weight, 0) * count
        total_weight += self.weapons_weight
        total_weight += self.armor_weight
        self.total_encumbrance.setText(str(total_weight))


    def adding_new_element_to_layout(self, element_idx, values):
        if hasattr(self, "add_new"):
            self.layout.removeWidget(self.add_new)
        item_name = values[0]
        rest = values[1:]
        add_element_to_layout(self.layout, item_name, row=self.row_offset + element_idx, column=0, height=1,
                              width=5)
        add_multiple_elements_to_layout_by_row(self.layout, rest, start_column=5, row=self.row_offset + element_idx)
        if hasattr(self, "add_new"):
            self.add_last_row()
