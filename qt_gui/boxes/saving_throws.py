from PyQt5 import QtWidgets, QtCore

from qt_gui.boxes.box import DefaultBox
from qt_gui.qt_line_edits import create_qlabel, create_qline_edit


class SavingThrowsBox(DefaultBox):
    def __init__(self, centralwidget):
        self.root = QtWidgets.QGroupBox(centralwidget)
        self.root.setGeometry(QtCore.QRect(1270, 0, 461, 150))
        self.root.setMinimumSize(QtCore.QSize(461, 0))
        self.root.setMaximumSize(QtCore.QSize(461, 150))
        self.root.setObjectName("SavingThrowsBox")
        self.container = QtWidgets.QWidget(self.root)
        self.container.setGeometry(QtCore.QRect(11, 21, 431, 121))
        self.container.setObjectName("layoutWidget2")
        self.layout = QtWidgets.QGridLayout(self.container)
        self.layout.setContentsMargins(9, 9, 9, 9)
        self.layout.setSpacing(6)
        self.layout.setObjectName("SavingThrowsLayout")
        qlabel_dict = dict(parent=self.container, min_size=(60, 20), max_size=(60, 23))
        qlabel_sign_dict = dict(parent=self.container, min_size=(8, 10), max_size=(8, 23))
        qline_dict = dict(parent=self.container, min_size=(60, 23))

        self.saving_throws_fortitude_total = create_qline_edit("saving_throws_fortitude_total", **qline_dict)
        self.saving_throws_fortitude_class_base = create_qline_edit("saving_throws_fortitude_class_base", **qline_dict)
        self.saving_throws_fortitude_attr_bonus = create_qline_edit("saving_throws_fortitude_attr_bonus", **qline_dict)
        self.saving_throws_fortitude_size_bonus = create_qline_edit("saving_throws_fortitude_size_bonus", **qline_dict)
        self.saving_throws_fortitude_misc_bonus = create_qline_edit("saving_throws_fortitude_misc_bonus", **qline_dict)
        self.saving_throws_reflex_label = create_qlabel("saving_throws_reflex_label", **qlabel_dict)
        self.saving_throws_reflex_total = create_qline_edit("saving_throws_reflex_total", **qline_dict)
        self.saving_throws_reflex_class_bonus = create_qline_edit("saving_throws_reflex_class_bonus", **qline_dict)
        self.saving_throws_reflex_attr_bonus = create_qline_edit("saving_throws_reflex_attr_bonus", **qline_dict)
        self.saving_throws_reflex_size_bonus = create_qline_edit("saving_throws_reflex_size_bonus", **qline_dict)
        self.saving_throws_reflex_misc_bonus = create_qline_edit("saving_throws_reflex_misc_bonus", **qline_dict)
        self.saving_throws_will_label = create_qlabel("saving_throws_will_label", **qlabel_dict)
        self.saving_throws_will_total = create_qline_edit("saving_throws_will_total", **qline_dict)
        self.saving_throws_will_class_bonus = create_qline_edit("saving_throws_will_class_bonus", **qline_dict)
        self.saving_throws_will_attr_bonus = create_qline_edit("saving_throws_will_attr_bonus", **qline_dict)
        self.saving_throws_will_size_bonus = create_qline_edit("saving_throws_will_size_bonus", **qline_dict)
        self.saving_throws_will_misc_bonus = create_qline_edit("saving_throws_will_misc_bonus", **qline_dict)
        self.saving_throws_total_label = create_qlabel("saving_throws_total_label", **qlabel_dict)
        self.saving_throws_class_base_label = create_qlabel("saving_throws_class_base_label", **qlabel_dict)
        self.saving_throws_attr_bonus_label = create_qlabel("saving_throws_attr_bonus_label", **qlabel_dict)
        self.saving_throws_size_bonus_label = create_qlabel("saving_throws_size_bonus_label", **qlabel_dict)
        self.saving_throws_misc_bonus_label = create_qlabel("saving_throws_misc_bonus_label", **qlabel_dict)
        self.saving_throws_fortitude_label = create_qlabel("saving_throws_fortitude_label", **qlabel_dict)
        self._eq_sign_4 = create_qlabel("_eq_sign_4", **qlabel_sign_dict)
        self._plus_sign = create_qlabel("_plus_sign", **qlabel_sign_dict)
        self._plus_sign_4 = create_qlabel("_plus_sign_4", **qlabel_sign_dict)
        self._plus_sign_7 = create_qlabel("_plus_sign_7", **qlabel_sign_dict)
        self._eq_sign_5 = create_qlabel("_eq_sign_5", **qlabel_sign_dict)
        self._plus_sign_2 = create_qlabel("_plus_sign_2", **qlabel_sign_dict)
        self._plus_sign_5 = create_qlabel("_plus_sign_5", **qlabel_sign_dict)
        self._plus_sign_8 = create_qlabel("_plus_sign_8", **qlabel_sign_dict)
        self._eq_sign_6 = create_qlabel("_eq_sign_6", **qlabel_sign_dict)
        self._plus_sign_3 = create_qlabel("_plus_sign_3", **qlabel_sign_dict)
        self._plus_sign_6 = create_qlabel("_plus_sign_6", **qlabel_sign_dict)
        self._plus_sign_9 = create_qlabel("_plus_sign_9", **qlabel_sign_dict)

        self.add_to_layout()
        self.translate()
        self.set_signs_labels()
        self.set_default()

    def add_to_layout(self):
        self.layout.addWidget(self.saving_throws_will_misc_bonus, 3, 9, 1, 1)
        self.layout.addWidget(self.saving_throws_total_label, 0, 1, 1, 1)
        self.layout.addWidget(self.saving_throws_class_base_label, 0, 3, 1, 1)
        self.layout.addWidget(self.saving_throws_attr_bonus_label, 0, 5, 1, 1)
        self.layout.addWidget(self.saving_throws_size_bonus_label, 0, 7, 1, 1)
        self.layout.addWidget(self.saving_throws_misc_bonus_label, 0, 9, 1, 1)
        self.layout.addWidget(self.saving_throws_fortitude_label, 1, 0, 1, 1)
        self.layout.addWidget(self.saving_throws_fortitude_total, 1, 1, 1, 1)
        self.layout.addWidget(self._eq_sign_4, 1, 2, 1, 1)
        self.layout.addWidget(self.saving_throws_fortitude_class_base, 1, 3, 1, 1)
        self.layout.addWidget(self._plus_sign, 1, 4, 1, 1)
        self.layout.addWidget(self.saving_throws_fortitude_attr_bonus, 1, 5, 1, 1)
        self.layout.addWidget(self._plus_sign_4, 1, 6, 1, 1)
        self.layout.addWidget(self.saving_throws_fortitude_size_bonus, 1, 7, 1, 1)
        self.layout.addWidget(self._plus_sign_7, 1, 8, 1, 1)
        self.layout.addWidget(self.saving_throws_fortitude_misc_bonus, 1, 9, 1, 1)
        self.layout.addWidget(self.saving_throws_reflex_label, 2, 0, 1, 1)
        self.layout.addWidget(self.saving_throws_reflex_total, 2, 1, 1, 1)
        self.layout.addWidget(self._eq_sign_5, 2, 2, 1, 1)
        self.layout.addWidget(self.saving_throws_reflex_class_bonus, 2, 3, 1, 1)
        self.layout.addWidget(self._plus_sign_2, 2, 4, 1, 1)
        self.layout.addWidget(self.saving_throws_reflex_attr_bonus, 2, 5, 1, 1)
        self.layout.addWidget(self._plus_sign_5, 2, 6, 1, 1)
        self.layout.addWidget(self.saving_throws_reflex_size_bonus, 2, 7, 1, 1)
        self.layout.addWidget(self._plus_sign_8, 2, 8, 1, 1)
        self.layout.addWidget(self.saving_throws_reflex_misc_bonus, 2, 9, 1, 1)
        self.layout.addWidget(self.saving_throws_will_label, 3, 0, 1, 1)
        self.layout.addWidget(self.saving_throws_will_total, 3, 1, 1, 1)
        self.layout.addWidget(self._eq_sign_6, 3, 2, 1, 1)
        self.layout.addWidget(self.saving_throws_will_class_bonus, 3, 3, 1, 1)
        self.layout.addWidget(self._plus_sign_3, 3, 4, 1, 1)
        self.layout.addWidget(self.saving_throws_will_attr_bonus, 3, 5, 1, 1)
        self.layout.addWidget(self._plus_sign_6, 3, 6, 1, 1)
        self.layout.addWidget(self.saving_throws_will_size_bonus, 3, 7, 1, 1)
        self.layout.addWidget(self._plus_sign_9, 3, 8, 1, 1)

    def translate(self):
        _translate = QtCore.QCoreApplication.translate
        self.root.setTitle(_translate("MainWindow", "Saving throws"))
        self.saving_throws_total_label.setText(_translate("MainWindow", "Total"))
        self.saving_throws_class_base_label.setText(_translate("MainWindow", "Class Base"))
        self.saving_throws_attr_bonus_label.setText(_translate("MainWindow", "Attr"))
        self.saving_throws_size_bonus_label.setText(_translate("MainWindow", "Size"))
        self.saving_throws_misc_bonus_label.setText(_translate("MainWindow", "Misc"))
        self.saving_throws_fortitude_label.setText(_translate("MainWindow", "Fortitude"))
        self.saving_throws_reflex_label.setText(_translate("MainWindow", "Reflex"))
        self.saving_throws_will_label.setText(_translate("MainWindow", "Will"))

    def set_signs_labels(self):
        self._eq_sign_4.setText("=")
        self._plus_sign.setText("+")
        self._plus_sign_4.setText("+")
        self._plus_sign_7.setText("+")
        self._eq_sign_5.setText("=")
        self._plus_sign_2.setText("+")
        self._plus_sign_5.setText("+")
        self._plus_sign_8.setText("+")
        self._eq_sign_6.setText("=")
        self._plus_sign_3.setText("+")
        self._plus_sign_6.setText("+")
        self._plus_sign_9.setText("+")

    def set_default(self):
        self.saving_throws_fortitude_total.setText("10")
        self.saving_throws_fortitude_class_base.setText("10")
        self.saving_throws_fortitude_attr_bonus.setText("10")
        self.saving_throws_fortitude_size_bonus.setText("10")
        self.saving_throws_fortitude_misc_bonus.setText("10")
        self.saving_throws_reflex_total.setText("10")
        self.saving_throws_reflex_class_bonus.setText("10")
        self.saving_throws_reflex_attr_bonus.setText("10")
        self.saving_throws_reflex_size_bonus.setText("10")
        self.saving_throws_reflex_misc_bonus.setText("10")
        self.saving_throws_will_total.setText("10")
        self.saving_throws_will_class_bonus.setText("10")
        self.saving_throws_will_attr_bonus.setText("10")
        self.saving_throws_will_size_bonus.setText("10")
        self.saving_throws_will_misc_bonus.setText("10")
