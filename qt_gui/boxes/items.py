from types import SimpleNamespace

from PyQt5 import QtWidgets, QtCore

from qt_gui.boxes.qt_generic_functions import create_qlabel


class ItemsBox:
    # TODO - generalized adding item (looks messy)
    # TODO - generalized translation
    # TODO - adding widgets by rows/columns
    def __init__(self, parent, position, size):
        self.root = QtWidgets.QGroupBox(parent)
        self.root.setGeometry(QtCore.QRect(*position, *size))
        self.root.setObjectName("ItemsBox")
        self.container = QtWidgets.QWidget(self.root)
        self.container.setObjectName("gridLayoutWidget_8")
        self.layout = QtWidgets.QGridLayout(self.container)
        self.layout.setObjectName("ItemsLayout")
        qlabel_dict = dict(parent=self.container)
        self.items_weight_label = create_qlabel("items_weight_label", **qlabel_dict)
        self.items_name_label = create_qlabel("items_name_label", **qlabel_dict)
        self.items_count_label = create_qlabel("items_count_label", **qlabel_dict)
        self.items_description_label = create_qlabel("items_description_label", **qlabel_dict)
        self.items = []
        # self.items.append(self.create_item(1))
        # self.items.append(self.create_item(2))
        # self.items.append(self.create_item(3))
        self.container.setGeometry(QtCore.QRect(10, 20, 561, 80 + len(self.items) * 40))
        self.add_to_layout()
        self.add_item()
        self.add_item()
        self.add_item()
        self.add_item()
        self.add_item()
        # self.add_item(self.items[0], 1)
        # self.add_item(self.items[1], 2)
        # self.add_item(self.items[2], 3)
        self.translate()
        self.root.setLayout(self.layout)

    def create_new_item(self):
        new_item = SimpleNamespace()
        item_idx = len(self.items)
        new_item.name = QtWidgets.QLineEdit(self.container)
        new_item.name.setMinimumSize(QtCore.QSize(0, 23))
        new_item.name.setObjectName(f"item_{item_idx}_name")
        new_item.weight = QtWidgets.QLineEdit(self.container)
        new_item.weight.setMinimumSize(QtCore.QSize(0, 23))
        new_item.weight.setMaximumSize(QtCore.QSize(50, 16777215))
        new_item.weight.setObjectName(f"item_{item_idx}_weight")
        new_item.count = QtWidgets.QLineEdit(self.container)
        new_item.count.setMinimumSize(QtCore.QSize(0, 23))
        new_item.count.setMaximumSize(QtCore.QSize(40, 16777215))
        new_item.count.setObjectName(f"item_{item_idx}_count")
        new_item.description = QtWidgets.QPlainTextEdit(self.container)
        new_item.description.setMaximumSize(QtCore.QSize(16777215, 40))
        new_item.description.setObjectName(f"item_{item_idx}_description")
        return new_item

    def add_to_layout(self):
        self.layout.addWidget(self.items_weight_label, 0, 1, 1, 1)
        self.layout.addWidget(self.items_name_label, 0, 0, 1, 1)
        self.layout.addWidget(self.items_count_label, 0, 2, 1, 1)
        self.layout.addWidget(self.items_description_label, 0, 3, 1, 1)

    def add_item(self):
        item_idx = len(self.items)
        new_item = self.create_new_item()
        self.items.append(new_item)
        for el_idx, element in enumerate(new_item.__dict__.values()):
            self.layout.addWidget(element, item_idx + 1, el_idx, 1, 1)
        self.update_container_size()

    def translate(self):
        _translate = QtCore.QCoreApplication.translate
        self.root.setTitle(_translate("MainWindow", "Items"))
        self.items_weight_label.setText(_translate("MainWindow", "Weight"))
        self.items_name_label.setText(_translate("MainWindow", "Item name"))
        self.items_count_label.setText(_translate("MainWindow", "Count"))
        self.items_description_label.setText(_translate("MainWindow", "Description"))

    def update_container_size(self):
        self.container.setGeometry(QtCore.QRect(10, 20, 561, 80 + len(self.items) * 40))
