from PyQt5 import QtWidgets, QtCore

from qt_gui.qt_line_edits import create_qlabel, create_qline_edit


class KnownSpellsBox:
    def __init__(self, centralwidget):
        self.KnownSpellsBox = QtWidgets.QGroupBox(centralwidget)
        self.KnownSpellsBox.setGeometry(QtCore.QRect(840, 670, 581, 101))
        self.KnownSpellsBox.setObjectName("KnownSpellsBox")
        self.gridLayoutWidget_11 = QtWidgets.QWidget(self.KnownSpellsBox)
        self.gridLayoutWidget_11.setGeometry(QtCore.QRect(10, 20, 561, 61))
        self.gridLayoutWidget_11.setObjectName("gridLayoutWidget_11")
        self.KnownSpellsLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_11)
        self.KnownSpellsLayout.setContentsMargins(9, 9, 9, 9)
        self.KnownSpellsLayout.setSpacing(6)
        self.KnownSpellsLayout.setObjectName("KnownSpellsLayout")
        qline_dict = dict(parent=self.gridLayoutWidget_11, min_size=(0, 23), max_size=(20, 16777215))
        qline_dict_2 = dict(parent=self.gridLayoutWidget_11, min_size=(0, 23))
        qlabel_dict = dict(parent=self.gridLayoutWidget_11, max_size=(20, 16777215))
        qlabel_dict_2 = dict(parent=self.gridLayoutWidget_11)

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

        self.known_spells_1_description_button = QtWidgets.QPushButton(self.gridLayoutWidget_11)
        self.known_spells_1_description_button.setObjectName("known_spells_1_description_button")
        self.known_spells_2_description_button = QtWidgets.QPushButton(self.gridLayoutWidget_11)
        self.known_spells_2_description_button.setObjectName("known_spells_2_description_button")

        self.KnownSpellsLayout.addWidget(self.known_spells_2_description_button, 1, 5, 1, 1)
        self.KnownSpellsLayout.addWidget(self.known_spells_1_lvl, 1, 1, 1, 1)
        self.KnownSpellsLayout.addWidget(self.known_spells_2_lvl, 1, 4, 1, 1)
        self.KnownSpellsLayout.addWidget(self.known_spells_1_name, 1, 0, 1, 1)
        self.KnownSpellsLayout.addWidget(self.known_spells_name_label_2, 0, 3, 1, 1)
        self.KnownSpellsLayout.addWidget(self.known_spells_lvl_label_1, 0, 1, 1, 1)
        self.KnownSpellsLayout.addWidget(self.known_spells_lvl_label_2, 0, 4, 1, 1)
        self.KnownSpellsLayout.addWidget(self.known_spells_name_label_1, 0, 0, 1, 1)
        self.KnownSpellsLayout.addWidget(self.known_spells_description_label_1, 0, 2, 1, 1)
        self.KnownSpellsLayout.addWidget(self.known_spells_description_label_2, 0, 5, 1, 1)
        self.KnownSpellsLayout.addWidget(self.known_spells_2_name, 1, 3, 1, 1)
        self.KnownSpellsLayout.addWidget(self.known_spells_1_description_button, 1, 2, 1, 1)
        self.translate_known_spells_box()

    def translate_known_spells_box(self):
        _translate = QtCore.QCoreApplication.translate
        self.KnownSpellsBox.setTitle(_translate("MainWindow", "Known Spells"))
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