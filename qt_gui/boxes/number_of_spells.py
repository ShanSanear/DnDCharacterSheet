from PyQt5 import QtWidgets, QtCore

from qt_gui.boxes.qt_generic_functions import create_qlabel, create_qline_edit

from qt_gui.boxes.box import DefaultBox


class NumberOfSpellsBox(DefaultBox):
    def __init__(self, centralwidget):
        self.root = QtWidgets.QGroupBox(centralwidget)
        self.root.setGeometry(QtCore.QRect(840, 560, 581, 131))
        self.root.setObjectName("NumberOfSpellsBox")
        self.container = QtWidgets.QWidget(self.root)
        self.container.setGeometry(QtCore.QRect(10, 20, 561, 91))
        self.container.setObjectName("gridLayoutWidget_10")
        self.layout = QtWidgets.QGridLayout(self.container)
        self.layout.setContentsMargins(9, 9, 9, 9)
        self.layout.setSpacing(6)
        self.layout.setObjectName("NumberOfSpellsLayout")

        qline_dict = dict(parent=self.container, min_size=(0, 23))
        qline_dict_2 = dict(parent=self.container, align=QtCore.Qt.AlignCenter)

        self.number_of_spells_0th_label = create_qlabel("number_of_spells_0th_label",
                                                        parent=self.container)
        self.number_of_spells_1st_label = create_qlabel("number_of_spells_1st_label",
                                                        parent=self.container)
        self.number_of_spells_2nd_label = create_qlabel("number_of_spells_2nd_label",
                                                        parent=self.container)
        self.number_of_spells_3rd_label = create_qlabel("number_of_spells_3rd_label",
                                                        parent=self.container)
        self.number_of_spells_4th_label = create_qlabel("number_of_spells_4th_label",
                                                        parent=self.container)
        self.number_of_spells_5th_label = create_qlabel("number_of_spells_5th_label",
                                                        parent=self.container)
        self.number_of_spells_6th_label = create_qlabel("number_of_spells_6th_label",
                                                        parent=self.container)
        self.number_of_spells_7th_label = create_qlabel("number_of_spells_7th_label",
                                                        parent=self.container)
        self.number_of_spells_8th_label = create_qlabel("number_of_spells_8th_label",
                                                        parent=self.container)
        self.number_of_spells_9th_label = create_qlabel("number_of_spells_9th_label",
                                                        parent=self.container)
        self.number_of_spells_known_number_of_spells_label = create_qlabel(
            "number_of_spells_known_number_of_spells_label", **qline_dict_2)

        self.number_of_spells_0 = create_qline_edit("number_of_spells_0", **qline_dict)
        self.number_of_spells_1 = create_qline_edit("number_of_spells_1", **qline_dict)
        self.number_of_spells_2 = create_qline_edit("number_of_spells_2", **qline_dict)
        self.number_of_spells_3 = create_qline_edit("number_of_spells_3", **qline_dict)
        self.number_of_spells_4 = create_qline_edit("number_of_spells_4", **qline_dict)
        self.number_of_spells_5 = create_qline_edit("number_of_spells_5", **qline_dict)
        self.number_of_spells_6 = create_qline_edit("number_of_spells_6", **qline_dict)
        self.number_of_spells_7 = create_qline_edit("number_of_spells_7", **qline_dict)
        self.number_of_spells_8 = create_qline_edit("number_of_spells_8", **qline_dict)
        self.number_of_spells_9 = create_qline_edit("number_of_spells_9", **qline_dict)

        self.add_to_layout()
        self.translate()

    def add_to_layout(self):
        self.layout.addWidget(self.number_of_spells_0th_label, 1, 0, 1, 1)
        self.layout.addWidget(self.number_of_spells_0, 1, 1, 1, 1)
        self.layout.addWidget(self.number_of_spells_1st_label, 1, 2, 1, 1)
        self.layout.addWidget(self.number_of_spells_1, 1, 3, 1, 1)
        self.layout.addWidget(self.number_of_spells_2nd_label, 1, 4, 1, 1)
        self.layout.addWidget(self.number_of_spells_2, 1, 5, 1, 1)
        self.layout.addWidget(self.number_of_spells_3rd_label, 1, 6, 1, 1)
        self.layout.addWidget(self.number_of_spells_3, 1, 7, 1, 1)
        self.layout.addWidget(self.number_of_spells_4th_label, 1, 8, 1, 1)
        self.layout.addWidget(self.number_of_spells_4, 1, 9, 1, 1)
        self.layout.addWidget(self.number_of_spells_5th_label, 2, 0, 1, 1)
        self.layout.addWidget(self.number_of_spells_5, 2, 1, 1, 1)
        self.layout.addWidget(self.number_of_spells_6th_label, 2, 2, 1, 1)
        self.layout.addWidget(self.number_of_spells_6, 2, 3, 1, 1)
        self.layout.addWidget(self.number_of_spells_7th_label, 2, 4, 1, 1)
        self.layout.addWidget(self.number_of_spells_7, 2, 5, 1, 1)
        self.layout.addWidget(self.number_of_spells_8th_label, 2, 6, 1, 1)
        self.layout.addWidget(self.number_of_spells_8, 2, 7, 1, 1)
        self.layout.addWidget(self.number_of_spells_9th_label, 2, 8, 1, 1)
        self.layout.addWidget(self.number_of_spells_9, 2, 9, 1, 1)
        self.layout.addWidget(self.number_of_spells_known_number_of_spells_label, 0, 2, 1, 6)

    def translate(self):
        _translate = QtCore.QCoreApplication.translate
        self.root.setTitle(_translate("MainWindow", "Number of spells"))
        self.number_of_spells_0th_label.setText(_translate("MainWindow", "0th lvl"))
        self.number_of_spells_1.setText(_translate("MainWindow", "10"))
        self.number_of_spells_4th_label.setText(_translate("MainWindow", "4th lvl"))
        self.number_of_spells_4.setText(_translate("MainWindow", "10"))
        self.number_of_spells_2nd_label.setText(_translate("MainWindow", "2nd lvl"))
        self.number_of_spells_2.setText(_translate("MainWindow", "10"))
        self.number_of_spells_3rd_label.setText(_translate("MainWindow", "3rd lvl"))
        self.number_of_spells_3.setText(_translate("MainWindow", "10"))
        self.number_of_spells_0.setText(_translate("MainWindow", "10"))
        self.number_of_spells_1st_label.setText(_translate("MainWindow", "1st lvl"))
        self.number_of_spells_5th_label.setText(_translate("MainWindow", "5th lvl"))
        self.number_of_spells_5.setText(_translate("MainWindow", "10"))
        self.number_of_spells_6.setText(_translate("MainWindow", "10"))
        self.number_of_spells_7.setText(_translate("MainWindow", "10"))
        self.number_of_spells_8.setText(_translate("MainWindow", "10"))
        self.number_of_spells_9.setText(_translate("MainWindow", "10"))
        self.number_of_spells_6th_label.setText(_translate("MainWindow", "6th lvl"))
        self.number_of_spells_7th_label.setText(_translate("MainWindow", "7th lvl"))
        self.number_of_spells_8th_label.setText(_translate("MainWindow", "8th lvl"))
        self.number_of_spells_9th_label.setText(_translate("MainWindow", "9th lvl"))
        self.number_of_spells_known_number_of_spells_label.setText(
            _translate("MainWindow", "Known number of spells (Warlock / Bard)"))