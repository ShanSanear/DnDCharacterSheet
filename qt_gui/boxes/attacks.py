from PyQt5 import QtWidgets, QtCore

from qt_gui.boxes.box import DefaultBox


class AttacksBox(DefaultBox):
    def __init__(self, centralwidget):
        self.root = QtWidgets.QGroupBox(centralwidget)
        self.root.setGeometry(QtCore.QRect(840, 160, 391, 121))
        self.root.setObjectName("AttacksBox")
        self.container = QtWidgets.QWidget(self.root)
        self.container.setGeometry(QtCore.QRect(20, 20, 361, 91))
        self.container.setObjectName("layoutWidget1")
        self.layout = QtWidgets.QGridLayout(self.container)
        self.layout.setContentsMargins(9, 9, 9, 9)
        self.layout.setSpacing(6)
        self.layout.setObjectName("AttacksLayout")
        self.attacks_total_label = QtWidgets.QLabel(self.container)
        self.attacks_total_label.setMinimumSize(QtCore.QSize(39, 17))
        self.attacks_total_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.attacks_total_label.setAlignment(QtCore.Qt.AlignCenter)
        self.attacks_total_label.setObjectName("attacks_total_label")
        self.attacks_base_label = QtWidgets.QLabel(self.container)
        self.attacks_base_label.setMinimumSize(QtCore.QSize(39, 17))
        self.attacks_base_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.attacks_base_label.setAlignment(QtCore.Qt.AlignCenter)
        self.attacks_base_label.setObjectName("attacks_base_label")
        self.attacks_attr_mod_label = QtWidgets.QLabel(self.container)
        self.attacks_attr_mod_label.setMinimumSize(QtCore.QSize(40, 17))
        self.attacks_attr_mod_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.attacks_attr_mod_label.setAlignment(QtCore.Qt.AlignCenter)
        self.attacks_attr_mod_label.setObjectName("attacks_attr_mod_label")
        self.attacks_size_label = QtWidgets.QLabel(self.container)
        self.attacks_size_label.setMinimumSize(QtCore.QSize(39, 17))
        self.attacks_size_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.attacks_size_label.setAlignment(QtCore.Qt.AlignCenter)
        self.attacks_size_label.setObjectName("attacks_size_label")
        self.attacks_misc_label = QtWidgets.QLabel(self.container)
        self.attacks_misc_label.setMinimumSize(QtCore.QSize(39, 17))
        self.attacks_misc_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.attacks_misc_label.setAlignment(QtCore.Qt.AlignCenter)
        self.attacks_misc_label.setObjectName("attacks_misc_label")
        self.attacks_melee_label = QtWidgets.QLabel(self.container)
        self.attacks_melee_label.setMinimumSize(QtCore.QSize(37, 20))
        self.attacks_melee_label.setMaximumSize(QtCore.QSize(47, 20))
        self.attacks_melee_label.setObjectName("attacks_melee_label")
        self.attacks_melee_total = QtWidgets.QLineEdit(self.container)
        self.attacks_melee_total.setMinimumSize(QtCore.QSize(39, 23))
        self.attacks_melee_total.setMaximumSize(QtCore.QSize(167, 20))
        self.attacks_melee_total.setObjectName("attacks_melee_total")
        self._eq_sign = QtWidgets.QLabel(self.container)
        self._eq_sign.setMinimumSize(QtCore.QSize(8, 10))
        self._eq_sign.setMaximumSize(QtCore.QSize(10, 20))
        self._eq_sign.setAlignment(QtCore.Qt.AlignCenter)
        self._eq_sign.setObjectName("_eq_sign")
        self.attacks_melee_base = QtWidgets.QLineEdit(self.container)
        self.attacks_melee_base.setMinimumSize(QtCore.QSize(39, 23))
        self.attacks_melee_base.setMaximumSize(QtCore.QSize(167, 20))
        self.attacks_melee_base.setObjectName("attacks_melee_base")
        self._plus_sign_16 = QtWidgets.QLabel(self.container)
        self._plus_sign_16.setMinimumSize(QtCore.QSize(8, 10))
        self._plus_sign_16.setMaximumSize(QtCore.QSize(10, 20))
        self._plus_sign_16.setAlignment(QtCore.Qt.AlignCenter)
        self._plus_sign_16.setObjectName("_plus_sign_16")
        self.attacks_melee_attr_mod = QtWidgets.QLineEdit(self.container)
        self.attacks_melee_attr_mod.setMinimumSize(QtCore.QSize(40, 23))
        self.attacks_melee_attr_mod.setMaximumSize(QtCore.QSize(167, 20))
        self.attacks_melee_attr_mod.setObjectName("attacks_melee_attr_mod")
        self._plus_sign_17 = QtWidgets.QLabel(self.container)
        self._plus_sign_17.setMinimumSize(QtCore.QSize(8, 10))
        self._plus_sign_17.setMaximumSize(QtCore.QSize(10, 20))
        self._plus_sign_17.setAlignment(QtCore.Qt.AlignCenter)
        self._plus_sign_17.setObjectName("_plus_sign_17")
        self.attacks_melee_size = QtWidgets.QLineEdit(self.container)
        self.attacks_melee_size.setMinimumSize(QtCore.QSize(39, 23))
        self.attacks_melee_size.setMaximumSize(QtCore.QSize(167, 20))
        self.attacks_melee_size.setObjectName("attacks_melee_size")
        self._plus_sign_18 = QtWidgets.QLabel(self.container)
        self._plus_sign_18.setMinimumSize(QtCore.QSize(8, 10))
        self._plus_sign_18.setMaximumSize(QtCore.QSize(10, 20))
        self._plus_sign_18.setAlignment(QtCore.Qt.AlignCenter)
        self._plus_sign_18.setObjectName("_plus_sign_18")
        self.attacks_melee_misc = QtWidgets.QLineEdit(self.container)
        self.attacks_melee_misc.setMinimumSize(QtCore.QSize(39, 23))
        self.attacks_melee_misc.setMaximumSize(QtCore.QSize(167, 20))
        self.attacks_melee_misc.setObjectName("attacks_melee_misc")
        self.attacks_ranged_label = QtWidgets.QLabel(self.container)
        self.attacks_ranged_label.setMinimumSize(QtCore.QSize(37, 20))
        self.attacks_ranged_label.setMaximumSize(QtCore.QSize(47, 20))
        self.attacks_ranged_label.setObjectName("attacks_ranged_label")
        self.attacks_ranged_total = QtWidgets.QLineEdit(self.container)
        self.attacks_ranged_total.setMinimumSize(QtCore.QSize(39, 23))
        self.attacks_ranged_total.setMaximumSize(QtCore.QSize(167, 20))
        self.attacks_ranged_total.setObjectName("attacks_ranged_total")
        self._eq_sign_2 = QtWidgets.QLabel(self.container)
        self._eq_sign_2.setMinimumSize(QtCore.QSize(8, 10))
        self._eq_sign_2.setMaximumSize(QtCore.QSize(10, 20))
        self._eq_sign_2.setAlignment(QtCore.Qt.AlignCenter)
        self._eq_sign_2.setObjectName("_eq_sign_2")
        self.attacks_ranged_base = QtWidgets.QLineEdit(self.container)
        self.attacks_ranged_base.setMinimumSize(QtCore.QSize(39, 23))
        self.attacks_ranged_base.setMaximumSize(QtCore.QSize(167, 20))
        self.attacks_ranged_base.setObjectName("attacks_ranged_base")
        self._plus_sign_19 = QtWidgets.QLabel(self.container)
        self._plus_sign_19.setMinimumSize(QtCore.QSize(8, 10))
        self._plus_sign_19.setMaximumSize(QtCore.QSize(10, 20))
        self._plus_sign_19.setAlignment(QtCore.Qt.AlignCenter)
        self._plus_sign_19.setObjectName("_plus_sign_19")
        self.attacks_ranged_attr_mod = QtWidgets.QLineEdit(self.container)
        self.attacks_ranged_attr_mod.setMinimumSize(QtCore.QSize(40, 23))
        self.attacks_ranged_attr_mod.setMaximumSize(QtCore.QSize(167, 20))
        self.attacks_ranged_attr_mod.setObjectName("attacks_ranged_attr_mod")
        self._plus_sign_20 = QtWidgets.QLabel(self.container)
        self._plus_sign_20.setMinimumSize(QtCore.QSize(8, 10))
        self._plus_sign_20.setMaximumSize(QtCore.QSize(10, 20))
        self._plus_sign_20.setAlignment(QtCore.Qt.AlignCenter)
        self._plus_sign_20.setObjectName("_plus_sign_20")
        self.attacks_ranged_size = QtWidgets.QLineEdit(self.container)
        self.attacks_ranged_size.setMinimumSize(QtCore.QSize(39, 23))
        self.attacks_ranged_size.setMaximumSize(QtCore.QSize(167, 20))
        self.attacks_ranged_size.setObjectName("attacks_ranged_size")
        self._plus_sign_21 = QtWidgets.QLabel(self.container)
        self._plus_sign_21.setMinimumSize(QtCore.QSize(8, 10))
        self._plus_sign_21.setMaximumSize(QtCore.QSize(10, 20))
        self._plus_sign_21.setAlignment(QtCore.Qt.AlignCenter)
        self._plus_sign_21.setObjectName("_plus_sign_21")
        self.attacks_ranged_misc = QtWidgets.QLineEdit(self.container)
        self.attacks_ranged_misc.setMinimumSize(QtCore.QSize(39, 23))
        self.attacks_ranged_misc.setMaximumSize(QtCore.QSize(167, 20))
        self.attacks_ranged_misc.setObjectName("attacks_ranged_misc")

        self.add_to_layout()
        self.translate()
        self.set_signs_labels()
        self.set_default_values()

    def add_to_layout(self):
        self.layout.addWidget(self.attacks_total_label, 0, 1, 1, 1)
        self.layout.addWidget(self.attacks_base_label, 0, 3, 1, 1)
        self.layout.addWidget(self.attacks_attr_mod_label, 0, 5, 1, 1)
        self.layout.addWidget(self.attacks_size_label, 0, 7, 1, 1)
        self.layout.addWidget(self.attacks_misc_label, 0, 9, 1, 1)
        self.layout.addWidget(self.attacks_melee_label, 1, 0, 1, 1)
        self.layout.addWidget(self.attacks_melee_total, 1, 1, 1, 1)
        self.layout.addWidget(self._eq_sign, 1, 2, 1, 1)
        self.layout.addWidget(self.attacks_melee_base, 1, 3, 1, 1)
        self.layout.addWidget(self._plus_sign_16, 1, 4, 1, 1)
        self.layout.addWidget(self.attacks_melee_attr_mod, 1, 5, 1, 1)
        self.layout.addWidget(self._plus_sign_17, 1, 6, 1, 1)
        self.layout.addWidget(self.attacks_melee_size, 1, 7, 1, 1)
        self.layout.addWidget(self._plus_sign_18, 1, 8, 1, 1)
        self.layout.addWidget(self.attacks_melee_misc, 1, 9, 1, 1)
        self.layout.addWidget(self.attacks_ranged_label, 2, 0, 1, 1)
        self.layout.addWidget(self.attacks_ranged_total, 2, 1, 1, 1)
        self.layout.addWidget(self._eq_sign_2, 2, 2, 1, 1)
        self.layout.addWidget(self.attacks_ranged_base, 2, 3, 1, 1)
        self.layout.addWidget(self._plus_sign_19, 2, 4, 1, 1)
        self.layout.addWidget(self.attacks_ranged_attr_mod, 2, 5, 1, 1)
        self.layout.addWidget(self._plus_sign_20, 2, 6, 1, 1)
        self.layout.addWidget(self.attacks_ranged_size, 2, 7, 1, 1)
        self.layout.addWidget(self._plus_sign_21, 2, 8, 1, 1)
        self.layout.addWidget(self.attacks_ranged_misc, 2, 9, 1, 1)

    def translate(self):
        _translate = QtCore.QCoreApplication.translate
        self.root.setTitle(_translate("MainWindow", "Attacks"))
        self.attacks_total_label.setText(_translate("MainWindow", "Total"))
        self.attacks_base_label.setText(_translate("MainWindow", "Base"))
        self.attacks_attr_mod_label.setText(_translate("MainWindow", "Attr mod"))
        self.attacks_size_label.setText(_translate("MainWindow", "Size"))
        self.attacks_misc_label.setText(_translate("MainWindow", "Misc"))
        self.attacks_melee_label.setText(_translate("MainWindow", "Melee"))
        self.attacks_ranged_label.setText(_translate("MainWindow", "Ranged"))

    def set_signs_labels(self):
        _translate = QtCore.QCoreApplication.translate
        self._eq_sign.setText(_translate("MainWindow", "="))
        self._plus_sign_16.setText(_translate("MainWindow", "+"))
        self._plus_sign_17.setText(_translate("MainWindow", "+"))
        self._plus_sign_18.setText(_translate("MainWindow", "+"))
        self._eq_sign_2.setText(_translate("MainWindow", "="))
        self._plus_sign_19.setText(_translate("MainWindow", "+"))
        self._plus_sign_20.setText(_translate("MainWindow", "+"))
        self._plus_sign_21.setText(_translate("MainWindow", "+"))

    def set_default_values(self):
        _translate = QtCore.QCoreApplication.translate
        self.attacks_melee_total.setText(_translate("MainWindow", "10"))
        self.attacks_melee_base.setText(_translate("MainWindow", "10"))
        self.attacks_melee_attr_mod.setText(_translate("MainWindow", "10"))
        self.attacks_melee_size.setText(_translate("MainWindow", "10"))
        self.attacks_melee_misc.setText(_translate("MainWindow", "10"))
        self.attacks_ranged_total.setText(_translate("MainWindow", "10"))
        self.attacks_ranged_base.setText(_translate("MainWindow", "10"))
        self.attacks_ranged_attr_mod.setText(_translate("MainWindow", "10"))
        self.attacks_ranged_size.setText(_translate("MainWindow", "10"))
        self.attacks_ranged_misc.setText(_translate("MainWindow", "10"))
