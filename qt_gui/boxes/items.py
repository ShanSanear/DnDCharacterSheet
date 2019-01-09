from PyQt5 import QtWidgets, QtCore


class ItemsBox:
    def __init__(self, centralwidget):
        self.root = QtWidgets.QGroupBox(centralwidget)
        self.root.setGeometry(QtCore.QRect(840, 900, 581, 291))
        self.root.setObjectName("ItemsBox")
        self.container = QtWidgets.QWidget(self.root)
        self.container.setGeometry(QtCore.QRect(10, 20, 561, 80))
        self.container.setObjectName("gridLayoutWidget_8")
        self.layout = QtWidgets.QGridLayout(self.container)
        self.layout.setContentsMargins(9, 9, 9, 9)
        self.layout.setSpacing(6)
        self.layout.setObjectName("ItemsLayout")
        self.items_weight_label = QtWidgets.QLabel(self.container)
        self.items_weight_label.setMaximumSize(QtCore.QSize(50, 16777215))
        self.items_weight_label.setAlignment(QtCore.Qt.AlignCenter)
        self.items_weight_label.setObjectName("items_weight_label")
        self.layout.addWidget(self.items_weight_label, 0, 1, 1, 1)
        self.item_1_name = QtWidgets.QLineEdit(self.container)
        self.item_1_name.setMinimumSize(QtCore.QSize(0, 23))
        self.item_1_name.setObjectName("item_1_name")
        self.layout.addWidget(self.item_1_name, 2, 0, 1, 1)
        self.item_1_weight = QtWidgets.QLineEdit(self.container)
        self.item_1_weight.setMinimumSize(QtCore.QSize(0, 23))
        self.item_1_weight.setMaximumSize(QtCore.QSize(50, 16777215))
        self.item_1_weight.setObjectName("item_1_weight")
        self.layout.addWidget(self.item_1_weight, 2, 1, 1, 1)
        self.items_name_label = QtWidgets.QLabel(self.container)
        self.items_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.items_name_label.setObjectName("items_name_label")
        self.layout.addWidget(self.items_name_label, 0, 0, 1, 1)
        self.item_1_count = QtWidgets.QLineEdit(self.container)
        self.item_1_count.setMinimumSize(QtCore.QSize(0, 23))
        self.item_1_count.setMaximumSize(QtCore.QSize(40, 16777215))
        self.item_1_count.setObjectName("item_1_count")
        self.layout.addWidget(self.item_1_count, 2, 2, 1, 1)
        self.item_1_description = QtWidgets.QPlainTextEdit(self.container)
        self.item_1_description.setMaximumSize(QtCore.QSize(16777215, 40))
        self.item_1_description.setObjectName("item_1_description")
        self.layout.addWidget(self.item_1_description, 2, 3, 1, 1)
        self.items_count_label = QtWidgets.QLabel(self.container)
        self.items_count_label.setMaximumSize(QtCore.QSize(40, 16777215))
        self.items_count_label.setAlignment(QtCore.Qt.AlignCenter)
        self.items_count_label.setObjectName("items_count_label")
        self.layout.addWidget(self.items_count_label, 0, 2, 1, 1)
        self.items_description_label = QtWidgets.QLabel(self.container)
        self.items_description_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.items_description_label.setAlignment(QtCore.Qt.AlignCenter)
        self.items_description_label.setIndent(0)
        self.items_description_label.setObjectName("items_description_label")
        self.layout.addWidget(self.items_description_label, 0, 3, 1, 1)
        self.translate_items_box()

    def translate_items_box(self):
        _translate = QtCore.QCoreApplication.translate
        self.root.setTitle(_translate("MainWindow", "Items"))
        self.items_weight_label.setText(_translate("MainWindow", "Weight"))
        self.item_1_name.setText(_translate("MainWindow", "Lorem ipsum"))
        self.item_1_weight.setText(_translate("MainWindow", "10"))
        self.items_name_label.setText(_translate("MainWindow", "Item name"))
        self.item_1_count.setText(_translate("MainWindow", "10"))
        self.item_1_description.setPlainText(_translate("MainWindow",
                                                        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sapien urna, egestas eu tempor at, pretium nec orci. In nec pharetra tellus. In malesuada erat tellus, eget efficitur elit convallis eu. Integer consectetur porttitor eros vitae sagittis. Vestibulum commodo suscipit varius. Nulla vitae fringilla velit. Mauris sagittis tellus urna. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Fusce in arcu justo."))
        self.items_count_label.setText(_translate("MainWindow", "Count"))
        self.items_description_label.setText(_translate("MainWindow", "Description"))