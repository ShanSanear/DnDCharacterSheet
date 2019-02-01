from types import SimpleNamespace

from PyQt5 import QtWidgets, QtCore

from gui.frames.qt_generic_classes import ResizeableBox, DefaultBox
from gui.frames.qt_generic_functions import create_qlabel, set_text_of_children, create_qline_edit, \
    add_multiple_elements_to_layout_by_row, create_push_button


class ItemsBox(DefaultBox, ResizeableBox):
    def __init__(self, parent, position, size):
        # TODO Counting total items weights
        # TODO remove button
        # TODO - scrollbar after achieving certain height
        # TODO - sorting by name
        self.parent = parent
        self.root = QtWidgets.QGroupBox(parent)
        self.root.setGeometry(QtCore.QRect(*position, *size))
        self.root.setObjectName("ItemsBox")
        self.container = QtWidgets.QWidget(self.root)
        self.container.setObjectName("gridLayoutWidget_8")
        self.layout = QtWidgets.QGridLayout(self.container)
        self.layout.setObjectName("ItemsLayout")
        self.add_new = create_push_button("add_new_feat", self.container, max_size=[20, None], text="+")
        qlabel_dict = dict(parent=self.container)
        self.items_name_label = create_qlabel("items_name_label", **qlabel_dict)
        self.items_weight_label = create_qlabel("items_weight_label", **qlabel_dict)
        self.items_count_label = create_qlabel("items_count_label", **qlabel_dict)
        self.items_description_label = create_qlabel("items_description_label", **qlabel_dict)
        self.translate_reference = {"EN": {
            "root": {"title": "Items"},
            "items_weight_label": "Weight",
            "items_name_label": "Item name",
            "items_count_label": "Count",
            "items_description_label": "Description",
        }}
        self.items = []
        self.container.setGeometry(QtCore.QRect(10, 20, 561, 80))
        self.add_to_layout()
        self.translate("EN")
        ResizeableBox.__init__(self, elements_list=self.items, row_offset=1, increase_width=0, increase_height=28)
        self.add_item = self.add_new_element
        self.add_new.clicked.connect(self.add_item)
        self.root.setLayout(self.layout)

    def create_new_item(self):
        new_item = SimpleNamespace()
        new_item.name = create_qline_edit("item_name", self.container, min_size=[0, 23])
        new_item.weight = create_qline_edit("item_weight", self.container, min_size=[None, 23],
                                            max_size=[20, None])

        new_item.count = create_qline_edit("item_count", self.container, min_size=[None, 23],
                                           max_size=[20, None])
        new_item.description = create_qline_edit("item_description", self.container, min_size=[None, 23])
        new_item.delete_item = create_push_button("item_delete", self.container, max_size=[20, None], text="-", function_on_clicked=self._remove_item, args_on_clicked=new_item)

        return new_item

    def create_new_element(self):
        return self.create_new_item()

    def add_to_layout(self):
        labels = [self.items_name_label, self.items_weight_label, self.items_count_label, self.items_description_label]
        add_multiple_elements_to_layout_by_row(self.layout, labels)
        self.layout.addWidget(self.add_new, 1, 0, 1, 1)

    def translate(self, language):
        set_text_of_children(self, self.translate_reference[language])

    def adding_missing_element(self):
        self.add_item()

    def _remove_item(self, item):
        idx = self._get_item_index(item)
        print(idx)
        self._remove_from_layout(item, idx)
        del self.items[idx]
        self.update_size()

    def _get_item_index(self, item):
        for idx, searched_for in enumerate(self.items):
            if item == searched_for:
                return idx

    def _remove_from_layout(self, item, idx):
        elements = self.elements_for_layout(self.items, idx)
        for element in elements:
            element.setParent(None)

