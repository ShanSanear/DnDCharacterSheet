from types import SimpleNamespace

from PyQt5 import QtWidgets, QtCore

from qt_gui.boxes.qt_generic_classes import ResizeableBox, DefaultBox
from qt_gui.boxes.qt_generic_functions import create_qlabel, set_text_of_children, create_qline_edit, \
    add_multiple_elements_to_layout_by_row


class ItemsBox(DefaultBox, ResizeableBox):
    def __init__(self, parent, position, size):
        ResizeableBox.__init__(self, increase_width=0, increase_height=40)
        self.root = QtWidgets.QGroupBox(parent)
        self.root.setGeometry(QtCore.QRect(*position, *size))
        self.root.setObjectName("ItemsBox")
        self.container = QtWidgets.QWidget(self.root)
        self.container.setObjectName("gridLayoutWidget_8")
        self.layout = QtWidgets.QGridLayout(self.container)
        self.layout.setObjectName("ItemsLayout")
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
        for _ in range(12):
            self.add_item()
        self.translate("EN")
        self.root.setLayout(self.layout)

    def create_new_item(self):
        new_item = SimpleNamespace()
        new_item.name = create_qline_edit("item_name", self.container, min_size=[0, 23])
        new_item.weight = create_qline_edit("item_weight", self.container, min_size=[None, 23],
                                            max_size=[50, None])
        new_item.count = create_qline_edit("item_count", self.container, min_size=[None, 23],
                                           max_size=[40, None])
        new_item.description = QtWidgets.QPlainTextEdit(self.container)
        new_item.description.setMaximumSize(QtCore.QSize(16777215, 40))
        new_item.description.setObjectName("item_description")
        return new_item

    def create_new_element(self):
        return self.create_new_item()

    def add_to_layout(self):
        labels = [self.items_name_label, self.items_weight_label, self.items_count_label, self.items_description_label]
        add_multiple_elements_to_layout_by_row(self.layout, labels)

    def add_item(self):
        self.add_new_element(self.items, self.layout, 1)

    def translate(self, language):
        set_text_of_children(self, self.translate_reference[language])
