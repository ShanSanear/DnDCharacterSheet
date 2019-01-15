from PyQt5 import QtWidgets, QtCore

from qt_gui.boxes.box import DefaultBox
from qt_gui.boxes.qt_generic_functions import create_qline_edit, create_qlabel


class AttacksBox(DefaultBox):
    def __init__(self, parent, position, size):
        self.root = QtWidgets.QGroupBox(parent)
        self.root.setGeometry(QtCore.QRect(*position, *size))
        self.root.setObjectName("AttacksBox")
        self.container = QtWidgets.QWidget(self.root)
        self.container.setGeometry(QtCore.QRect(20, 20, 361, 91))
        self.container.setObjectName("layoutWidget1")
        self.layout = QtWidgets.QGridLayout(self.container)
        self.layout.setContentsMargins(9, 9, 9, 9)
        self.layout.setSpacing(6)
        self.layout.setObjectName("AttacksLayout")
        qline_dict = dict(parent=self.container, min_size=(39, 23), max_size=(167, 20))
        qlabel_dict = dict(parent=self.container, min_size=(39, 17), max_size=(16777215, 20))
        qlabel_sign_dict = dict(parent=self.container, min_size=(8, 10), max_size=(10, 20))

        self.total_label = create_qlabel("attacks_total_label", **qlabel_dict)
        self.base_label = create_qlabel("attacks_base_label", **qlabel_dict)
        self.attr_mod_label = create_qlabel("attacks_attr_mod_label", **qlabel_dict)
        self.size_label = create_qlabel("attacks_size_label", **qlabel_dict)
        self.misc_label = create_qlabel("attacks_misc_label", **qlabel_dict)
        self.melee_label = create_qlabel("attacks_melee_label", **qlabel_dict)
        self.ranged_label = create_qlabel("attacks_ranged_label", **qlabel_dict)

        self.melee_total = create_qline_edit("attacks_melee_total", **qline_dict)
        self.melee_base = create_qline_edit("attacks_melee_base", **qline_dict)
        self.melee_attr_mod = create_qline_edit("attacks_melee_attr_mod", **qline_dict)
        self.melee_size = create_qline_edit("attacks_melee_size", **qline_dict)
        self.melee_misc = create_qline_edit("attacks_melee_misc", **qline_dict)
        self.ranged_total = create_qline_edit("attacks_ranged_total", **qline_dict)
        self.ranged_base = create_qline_edit("attacks_ranged_base", **qline_dict)
        self.ranged_attr_mod = create_qline_edit("attacks_ranged_attr_mod", **qline_dict)
        self.ranged_size = create_qline_edit("attacks_ranged_size", **qline_dict)
        self.ranged_misc = create_qline_edit("attacks_ranged_misc", **qline_dict)

        self._eq_sign = create_qlabel("_eq_sign", **qlabel_sign_dict)
        self._plus_sign_16 = create_qlabel("_plus_sign_16", **qlabel_sign_dict)
        self._plus_sign_17 = create_qlabel("_plus_sign_17", **qlabel_sign_dict)
        self._plus_sign_18 = create_qlabel("_plus_sign_18", **qlabel_sign_dict)
        self._eq_sign_2 = create_qlabel("_eq_sign_2", **qlabel_sign_dict)
        self._plus_sign_19 = create_qlabel("_plus_sign_19", **qlabel_sign_dict)
        self._plus_sign_20 = create_qlabel("_plus_sign_20", **qlabel_sign_dict)
        self._plus_sign_21 = create_qlabel("_plus_sign_21", **qlabel_sign_dict)


        self.add_to_layout()
        self.translate()
        self.set_signs_labels()
        self.set_default_values()

    def add_to_layout(self):
        self.layout.addWidget(self.total_label, 0, 1, 1, 1)
        self.layout.addWidget(self.base_label, 0, 3, 1, 1)
        self.layout.addWidget(self.attr_mod_label, 0, 5, 1, 1)
        self.layout.addWidget(self.size_label, 0, 7, 1, 1)
        self.layout.addWidget(self.misc_label, 0, 9, 1, 1)
        self.layout.addWidget(self.melee_label, 1, 0, 1, 1)
        self.layout.addWidget(self.melee_total, 1, 1, 1, 1)
        self.layout.addWidget(self._eq_sign, 1, 2, 1, 1)
        self.layout.addWidget(self.melee_base, 1, 3, 1, 1)
        self.layout.addWidget(self._plus_sign_16, 1, 4, 1, 1)
        self.layout.addWidget(self.melee_attr_mod, 1, 5, 1, 1)
        self.layout.addWidget(self._plus_sign_17, 1, 6, 1, 1)
        self.layout.addWidget(self.melee_size, 1, 7, 1, 1)
        self.layout.addWidget(self._plus_sign_18, 1, 8, 1, 1)
        self.layout.addWidget(self.melee_misc, 1, 9, 1, 1)
        self.layout.addWidget(self.ranged_label, 2, 0, 1, 1)
        self.layout.addWidget(self.ranged_total, 2, 1, 1, 1)
        self.layout.addWidget(self._eq_sign_2, 2, 2, 1, 1)
        self.layout.addWidget(self.ranged_base, 2, 3, 1, 1)
        self.layout.addWidget(self._plus_sign_19, 2, 4, 1, 1)
        self.layout.addWidget(self.ranged_attr_mod, 2, 5, 1, 1)
        self.layout.addWidget(self._plus_sign_20, 2, 6, 1, 1)
        self.layout.addWidget(self.ranged_size, 2, 7, 1, 1)
        self.layout.addWidget(self._plus_sign_21, 2, 8, 1, 1)
        self.layout.addWidget(self.ranged_misc, 2, 9, 1, 1)

    def translate(self):
        _translate = QtCore.QCoreApplication.translate
        self.root.setTitle(_translate("MainWindow", "Attacks"))
        self.total_label.setText(_translate("MainWindow", "Total"))
        self.base_label.setText(_translate("MainWindow", "Base"))
        self.attr_mod_label.setText(_translate("MainWindow", "Attr mod"))
        self.size_label.setText(_translate("MainWindow", "Size"))
        self.misc_label.setText(_translate("MainWindow", "Misc"))
        self.melee_label.setText(_translate("MainWindow", "Melee"))
        self.ranged_label.setText(_translate("MainWindow", "Ranged"))

    def set_signs_labels(self):
        self._eq_sign.setText("=")
        self._plus_sign_16.setText("+")
        self._plus_sign_17.setText("+")
        self._plus_sign_18.setText("+")
        self._eq_sign_2.setText("=")
        self._plus_sign_19.setText("+")
        self._plus_sign_20.setText("+")
        self._plus_sign_21.setText("+")

    def set_default_values(self):
        self.melee_total.setText("10")
        self.melee_base.setText("10")
        self.melee_attr_mod.setText("10")
        self.melee_size.setText("10")
        self.melee_misc.setText("10")
        self.ranged_total.setText("10")
        self.ranged_base.setText("10")
        self.ranged_attr_mod.setText("10")
        self.ranged_size.setText("10")
        self.ranged_misc.setText("10")
