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
        self.items_count = 0
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

    def create_item_row(self, item_idx):
        item_name = QtWidgets.QLineEdit(self.container)
        item_name.setMinimumSize(QtCore.QSize(0, 23))
        item_name.setObjectName(f"item_{item_idx}_name")
        item_weight = QtWidgets.QLineEdit(self.container)
        item_weight.setMinimumSize(QtCore.QSize(0, 23))
        item_weight.setMaximumSize(QtCore.QSize(50, 16777215))
        item_weight.setObjectName(f"item_{item_idx}_weight")
        item_count = QtWidgets.QLineEdit(self.container)
        item_count.setMinimumSize(QtCore.QSize(0, 23))
        item_count.setMaximumSize(QtCore.QSize(40, 16777215))
        item_count.setObjectName(f"item_{item_idx}_count")
        item_description = QtWidgets.QPlainTextEdit(self.container)
        item_description.setMaximumSize(QtCore.QSize(16777215, 40))
        item_description.setObjectName(f"item_{item_idx}_description")
        return [item_name, item_weight, item_count, item_description]

    def add_to_layout(self):
        self.layout.addWidget(self.items_weight_label, 0, 1, 1, 1)
        self.layout.addWidget(self.items_name_label, 0, 0, 1, 1)
        self.layout.addWidget(self.items_count_label, 0, 2, 1, 1)
        self.layout.addWidget(self.items_description_label, 0, 3, 1, 1)

    def add_item(self):
        new_item = self.create_item_row(self.items_count)
        self.items.append(new_item)
        for el_idx, element in enumerate(new_item):
            self.layout.addWidget(element, self.items_count + 1, el_idx, 1, 1)
        self.items_count += 1
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
