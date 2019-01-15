from PyQt5 import QtWidgets, QtCore

from qt_gui.boxes.qt_generic_functions import create_qlabel, create_qline_edit


class KnownSpellsBox:
    # TODO - generalized adding known spells
    # TODO - generalized translation
    # TODO - adding widgets by rows/columns
    def __init__(self, parent, position, size):
        self.root = QtWidgets.QGroupBox(parent)
        self.root.setGeometry(QtCore.QRect(*position, *size))
        self.root.setObjectName("KnownSpellsBox")
        self.container = QtWidgets.QWidget(self.root)
        self.container.setGeometry(QtCore.QRect(10, 20, 561, 61))
        self.container.setObjectName("gridLayoutWidget_11")
        self.layout = QtWidgets.QGridLayout(self.container)
        self.layout.setContentsMargins(9, 9, 9, 9)
        self.layout.setSpacing(6)
        self.layout.setObjectName("KnownSpellsLayout")
        qline_dict = dict(parent=self.container, min_size=(0, 23), max_size=(20, 16777215))
        qline_dict_2 = dict(parent=self.container, min_size=(0, 23))
        qlabel_dict = dict(parent=self.container, max_size=(20, 16777215))
        qlabel_dict_2 = dict(parent=self.container)

        self.known_spells_lvl_label_1 = create_qlabel("known_spells_lvl_label_1", **qlabel_dict)
        self.known_spells_lvl_label_2 = create_qlabel("known_spells_lvl_label_2", **qlabel_dict)

        self.known_spells_name_label_1 = create_qlabel("known_spells_name_label_1", **qlabel_dict_2)
        self.known_spells_name_label_2 = create_qlabel("known_spells_name_label_2", **qlabel_dict_2)

        self.known_spells_description_label_1 = create_qlabel("known_spells_description_label_1", **qlabel_dict_2)
        self.known_spells_description_label_2 = create_qlabel("known_spells_description_label_2", **qlabel_dict_2)

        self.known_spells_1_lvl = create_qline_edit("known_spells_1_lvl", **qline_dict)
        self.known_spells_2_lvl = create_qline_edit("known_spells_2_lvl", **qline_dict)
        self.known_spells_1_name = create_qline_edit("known_spells_1_name", **qline_dict_2)
        self.known_spells_2_name = create_qline_edit("known_spells_2_name", **qline_dict_2)

        self.known_spells_1_description_button = QtWidgets.QPushButton(self.container)
        self.known_spells_1_description_button.setObjectName("known_spells_1_description_button")
        self.known_spells_2_description_button = QtWidgets.QPushButton(self.container)
        self.known_spells_2_description_button.setObjectName("known_spells_2_description_button")
        self.add_to_layout()
        self.translate()

    def add_to_layout(self):
        self.layout.addWidget(self.known_spells_2_description_button, 1, 5, 1, 1)
        self.layout.addWidget(self.known_spells_1_lvl, 1, 1, 1, 1)
        self.layout.addWidget(self.known_spells_2_lvl, 1, 4, 1, 1)
        self.layout.addWidget(self.known_spells_1_name, 1, 0, 1, 1)
        self.layout.addWidget(self.known_spells_name_label_2, 0, 3, 1, 1)
        self.layout.addWidget(self.known_spells_lvl_label_1, 0, 1, 1, 1)
        self.layout.addWidget(self.known_spells_lvl_label_2, 0, 4, 1, 1)
        self.layout.addWidget(self.known_spells_name_label_1, 0, 0, 1, 1)
        self.layout.addWidget(self.known_spells_description_label_1, 0, 2, 1, 1)
        self.layout.addWidget(self.known_spells_description_label_2, 0, 5, 1, 1)
        self.layout.addWidget(self.known_spells_2_name, 1, 3, 1, 1)
        self.layout.addWidget(self.known_spells_1_description_button, 1, 2, 1, 1)

    def translate(self):
        _translate = QtCore.QCoreApplication.translate
        self.root.setTitle(_translate("MainWindow", "Known Spells"))
        self.known_spells_2_description_button.setText(_translate("MainWindow", "DESC"))
        self.known_spells_1_lvl.setText(_translate("MainWindow", "10"))
        self.known_spells_2_lvl.setText(_translate("MainWindow", "10"))
        self.known_spells_1_name.setText(_translate("MainWindow", "Lorem ipsum"))
        self.known_spells_name_label_2.setText(_translate("MainWindow", "Spell name"))
        self.known_spells_lvl_label_1.setText(_translate("MainWindow", "LVL"))
        self.known_spells_lvl_label_2.setText(_translate("MainWindow", "LVL"))
        self.known_spells_name_label_1.setText(_translate("MainWindow", "Spell name"))
        self.known_spells_description_label_1.setText(_translate("MainWindow", "Description"))
        self.known_spells_description_label_2.setText(_translate("MainWindow", "Description"))
        self.known_spells_2_name.setText(_translate("MainWindow", "Lorem ipsum"))
        self.known_spells_1_description_button.setText(_translate("MainWindow", "DESC"))