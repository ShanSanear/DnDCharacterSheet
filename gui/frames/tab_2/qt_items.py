from types import SimpleNamespace

from PyQt5 import QtWidgets, QtCore

from gui.frames.qt_generic_classes import ResizeableBox, DefaultBox
from gui.frames.qt_generic_functions import create_qlabel, set_text_of_children, create_qline_edit, \
    add_multiple_elements_to_layout_by_row, create_push_button


class ItemsBox(DefaultBox, ResizeableBox):
    def __init__(self, parent, position, size):
        # TODO - scrollbar after achieving certain height
        self.parent = parent
        self.root = QtWidgets.QGroupBox(parent)
        self.root.setGeometry(QtCore.QRect(*position, *size))
        self.root.setObjectName("ItemsBox")
        self.container = QtWidgets.QWidget(self.root)
        self.container.setObjectName("gridLayoutWidget_8")
        self.layout = QtWidgets.QGridLayout(self.container)
        self.layout.setObjectName("ItemsLayout")
        self.items = []
        self.add_new = create_push_button("add_new_feat", self.container, min_size=[20, 20], max_size=[20, 20], text="+")
        ResizeableBox.__init__(self, elements_list=self.items, row_offset=1, increase_width=0, increase_height=28,
                               last_row_column=4)

        qlabel_dict = dict(parent=self.container)
        self.items_name_label = create_qlabel("items_name_label", **qlabel_dict)
        self.items_weight_label = create_qlabel("items_weight_label", **qlabel_dict)
        self.items_count_label = create_qlabel("items_count_label", **qlabel_dict)
        self.items_description_label = create_qlabel("items_description_label", **qlabel_dict)
        self.total_weight = create_qline_edit("items_total_weight", self.container, max_size=[30, None],
                                              align=QtCore.Qt.AlignCenter)
        self.total_weight_label = create_qlabel("items_total_weight_label", self.container,
                                                align=QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.translate_reference = {"EN": {
            "root": {"title": "Items"},
            "items_weight_label": "Weight",
            "items_name_label": "Item name",
            "items_count_label": "Count",
            "items_description_label": "Description",
            "total_weight_label" : "Total weight:"
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


    def create_new_item(self):
        new_item = SimpleNamespace()
        new_item.name = create_qline_edit("item_name", self.container, min_size=[0, 23],
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
        self.layout.addWidget(self.add_new, last_row, 4, 1, 1)
        self.layout.addWidget(self.total_weight_label, last_row, 0, 1, 1)
        self.layout.addWidget(self.total_weight, last_row, 1, 1, 1)


    def create_new_element(self):
        return self.create_new_item()

    def add_to_layout(self):
        add_multiple_elements_to_layout_by_row(self.layout, self.labels)
        self.add_last_row()


    def translate(self, language):
        set_text_of_children(self, self.translate_reference[language])

    def calculate_weight(self):
        weight = 0
        for item in self.items:
            try:
                count = int(item.count.text())

            except ValueError:
                count = 1

            try:
                weight += float(item.weight.text().replace(',', '.')) * count

            except ValueError:
                weight += 0
        self.total_weight.setText(str(weight))
