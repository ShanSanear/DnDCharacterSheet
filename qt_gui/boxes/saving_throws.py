from PyQt5 import QtWidgets, QtCore


class SavingThrowsBox:
    def __init__(self, centralwidget):
        self.SavingThrowsBox = QtWidgets.QGroupBox(centralwidget)
        self.SavingThrowsBox.setGeometry(QtCore.QRect(1270, 0, 461, 150))
        self.SavingThrowsBox.setMinimumSize(QtCore.QSize(461, 0))
        self.SavingThrowsBox.setMaximumSize(QtCore.QSize(461, 150))
        self.SavingThrowsBox.setObjectName("SavingThrowsBox")
        self.layoutWidget2 = QtWidgets.QWidget(self.SavingThrowsBox)
        self.layoutWidget2.setGeometry(QtCore.QRect(11, 21, 431, 121))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.SavingThrowsLayout = QtWidgets.QGridLayout(self.layoutWidget2)
        self.SavingThrowsLayout.setContentsMargins(9, 9, 9, 9)
        self.SavingThrowsLayout.setSpacing(6)
        self.SavingThrowsLayout.setObjectName("SavingThrowsLayout")
        self.saving_throws_total_label = QtWidgets.QLabel(self.layoutWidget2)
        self.saving_throws_total_label.setMinimumSize(QtCore.QSize(60, 21))
        self.saving_throws_total_label.setMaximumSize(QtCore.QSize(60, 23))
        self.saving_throws_total_label.setAlignment(QtCore.Qt.AlignCenter)
        self.saving_throws_total_label.setObjectName("saving_throws_total_label")
        self.saving_throws_class_base_label = QtWidgets.QLabel(self.layoutWidget2)
        self.saving_throws_class_base_label.setMinimumSize(QtCore.QSize(60, 20))
        self.saving_throws_class_base_label.setMaximumSize(QtCore.QSize(60, 23))
        self.saving_throws_class_base_label.setAlignment(QtCore.Qt.AlignCenter)
        self.saving_throws_class_base_label.setObjectName("saving_throws_class_base_label")
        self.saving_throws_attr_bonus_label = QtWidgets.QLabel(self.layoutWidget2)
        self.saving_throws_attr_bonus_label.setMinimumSize(QtCore.QSize(59, 20))
        self.saving_throws_attr_bonus_label.setMaximumSize(QtCore.QSize(59, 23))
        self.saving_throws_attr_bonus_label.setAlignment(QtCore.Qt.AlignCenter)
        self.saving_throws_attr_bonus_label.setObjectName("saving_throws_attr_bonus_label")
        self.saving_throws_size_bonus_label = QtWidgets.QLabel(self.layoutWidget2)
        self.saving_throws_size_bonus_label.setMinimumSize(QtCore.QSize(60, 20))
        self.saving_throws_size_bonus_label.setMaximumSize(QtCore.QSize(60, 23))
        self.saving_throws_size_bonus_label.setAlignment(QtCore.Qt.AlignCenter)
        self.saving_throws_size_bonus_label.setObjectName("saving_throws_size_bonus_label")
        self.saving_throws_misc_bonus_label = QtWidgets.QLabel(self.layoutWidget2)
        self.saving_throws_misc_bonus_label.setMinimumSize(QtCore.QSize(60, 20))
        self.saving_throws_misc_bonus_label.setMaximumSize(QtCore.QSize(60, 23))
        self.saving_throws_misc_bonus_label.setAlignment(QtCore.Qt.AlignCenter)
        self.saving_throws_misc_bonus_label.setObjectName("saving_throws_misc_bonus_label")
        self.saving_throws_fortitude_label = QtWidgets.QLabel(self.layoutWidget2)
        self.saving_throws_fortitude_label.setMinimumSize(QtCore.QSize(44, 20))
        self.saving_throws_fortitude_label.setMaximumSize(QtCore.QSize(44, 23))
        self.saving_throws_fortitude_label.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.saving_throws_fortitude_label.setObjectName("saving_throws_fortitude_label")
        self.saving_throws_fortitude_total = QtWidgets.QLineEdit(self.layoutWidget2)
        self.saving_throws_fortitude_total.setMinimumSize(QtCore.QSize(60, 23))
        self.saving_throws_fortitude_total.setMaximumSize(QtCore.QSize(60, 23))
        self.saving_throws_fortitude_total.setObjectName("saving_throws_fortitude_total")
        self._eq_sign_4 = QtWidgets.QLabel(self.layoutWidget2)
        self._eq_sign_4.setMinimumSize(QtCore.QSize(8, 10))
        self._eq_sign_4.setMaximumSize(QtCore.QSize(8, 23))
        self._eq_sign_4.setAlignment(QtCore.Qt.AlignCenter)
        self._eq_sign_4.setObjectName("_eq_sign_4")
        self.saving_throws_fortitude_class_base = QtWidgets.QLineEdit(self.layoutWidget2)
        self.saving_throws_fortitude_class_base.setMinimumSize(QtCore.QSize(60, 23))
        self.saving_throws_fortitude_class_base.setMaximumSize(QtCore.QSize(60, 23))
        self.saving_throws_fortitude_class_base.setObjectName("saving_throws_fortitude_class_base")
        self._plus_sign = QtWidgets.QLabel(self.layoutWidget2)
        self._plus_sign.setMinimumSize(QtCore.QSize(8, 10))
        self._plus_sign.setMaximumSize(QtCore.QSize(8, 23))
        self._plus_sign.setAlignment(QtCore.Qt.AlignCenter)
        self._plus_sign.setObjectName("_plus_sign")
        self.saving_throws_fortitude_attr_bonus = QtWidgets.QLineEdit(self.layoutWidget2)
        self.saving_throws_fortitude_attr_bonus.setMinimumSize(QtCore.QSize(59, 23))
        self.saving_throws_fortitude_attr_bonus.setMaximumSize(QtCore.QSize(59, 23))
        self.saving_throws_fortitude_attr_bonus.setObjectName("saving_throws_fortitude_attr_bonus")
        self._plus_sign_4 = QtWidgets.QLabel(self.layoutWidget2)
        self._plus_sign_4.setMinimumSize(QtCore.QSize(8, 10))
        self._plus_sign_4.setMaximumSize(QtCore.QSize(8, 23))
        self._plus_sign_4.setAlignment(QtCore.Qt.AlignCenter)
        self._plus_sign_4.setObjectName("_plus_sign_4")
        self.saving_throws_fortitude_size_bonus = QtWidgets.QLineEdit(self.layoutWidget2)
        self.saving_throws_fortitude_size_bonus.setMinimumSize(QtCore.QSize(60, 23))
        self.saving_throws_fortitude_size_bonus.setMaximumSize(QtCore.QSize(60, 23))
        self.saving_throws_fortitude_size_bonus.setObjectName("saving_throws_fortitude_size_bonus")
        self._plus_sign_7 = QtWidgets.QLabel(self.layoutWidget2)
        self._plus_sign_7.setMinimumSize(QtCore.QSize(8, 10))
        self._plus_sign_7.setMaximumSize(QtCore.QSize(8, 23))
        self._plus_sign_7.setAlignment(QtCore.Qt.AlignCenter)
        self._plus_sign_7.setObjectName("_plus_sign_7")
        self.saving_throws_fortitude_misc_bonus = QtWidgets.QLineEdit(self.layoutWidget2)
        self.saving_throws_fortitude_misc_bonus.setMinimumSize(QtCore.QSize(60, 23))
        self.saving_throws_fortitude_misc_bonus.setMaximumSize(QtCore.QSize(60, 23))
        self.saving_throws_fortitude_misc_bonus.setObjectName("saving_throws_fortitude_misc_bonus")
        self.saving_throws_reflex_label = QtWidgets.QLabel(self.layoutWidget2)
        self.saving_throws_reflex_label.setMinimumSize(QtCore.QSize(44, 20))
        self.saving_throws_reflex_label.setMaximumSize(QtCore.QSize(44, 23))
        self.saving_throws_reflex_label.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.saving_throws_reflex_label.setObjectName("saving_throws_reflex_label")
        self.saving_throws_reflex_total = QtWidgets.QLineEdit(self.layoutWidget2)
        self.saving_throws_reflex_total.setMinimumSize(QtCore.QSize(60, 23))
        self.saving_throws_reflex_total.setMaximumSize(QtCore.QSize(60, 23))
        self.saving_throws_reflex_total.setObjectName("saving_throws_reflex_total")
        self._eq_sign_5 = QtWidgets.QLabel(self.layoutWidget2)
        self._eq_sign_5.setMinimumSize(QtCore.QSize(8, 10))
        self._eq_sign_5.setMaximumSize(QtCore.QSize(8, 23))
        self._eq_sign_5.setAlignment(QtCore.Qt.AlignCenter)
        self._eq_sign_5.setObjectName("_eq_sign_5")
        self.saving_throws_reflex_class_bonus = QtWidgets.QLineEdit(self.layoutWidget2)
        self.saving_throws_reflex_class_bonus.setMinimumSize(QtCore.QSize(60, 23))
        self.saving_throws_reflex_class_bonus.setMaximumSize(QtCore.QSize(60, 23))
        self.saving_throws_reflex_class_bonus.setObjectName("saving_throws_reflex_class_bonus")
        self._plus_sign_2 = QtWidgets.QLabel(self.layoutWidget2)
        self._plus_sign_2.setMinimumSize(QtCore.QSize(8, 10))
        self._plus_sign_2.setMaximumSize(QtCore.QSize(8, 23))
        self._plus_sign_2.setAlignment(QtCore.Qt.AlignCenter)
        self._plus_sign_2.setObjectName("_plus_sign_2")
        self.saving_throws_reflex_attr_bonus = QtWidgets.QLineEdit(self.layoutWidget2)
        self.saving_throws_reflex_attr_bonus.setMinimumSize(QtCore.QSize(59, 23))
        self.saving_throws_reflex_attr_bonus.setMaximumSize(QtCore.QSize(59, 23))
        self.saving_throws_reflex_attr_bonus.setObjectName("saving_throws_reflex_attr_bonus")
        self._plus_sign_5 = QtWidgets.QLabel(self.layoutWidget2)
        self._plus_sign_5.setMinimumSize(QtCore.QSize(8, 10))
        self._plus_sign_5.setMaximumSize(QtCore.QSize(8, 23))
        self._plus_sign_5.setAlignment(QtCore.Qt.AlignCenter)
        self._plus_sign_5.setObjectName("_plus_sign_5")
        self.saving_throws_reflex_size_bonus = QtWidgets.QLineEdit(self.layoutWidget2)
        self.saving_throws_reflex_size_bonus.setMinimumSize(QtCore.QSize(60, 23))
        self.saving_throws_reflex_size_bonus.setMaximumSize(QtCore.QSize(60, 23))
        self.saving_throws_reflex_size_bonus.setObjectName("saving_throws_reflex_size_bonus")
        self._plus_sign_8 = QtWidgets.QLabel(self.layoutWidget2)
        self._plus_sign_8.setMinimumSize(QtCore.QSize(8, 10))
        self._plus_sign_8.setMaximumSize(QtCore.QSize(8, 23))
        self._plus_sign_8.setAlignment(QtCore.Qt.AlignCenter)
        self._plus_sign_8.setObjectName("_plus_sign_8")
        self.saving_throws_reflex_misc_bonus = QtWidgets.QLineEdit(self.layoutWidget2)
        self.saving_throws_reflex_misc_bonus.setMinimumSize(QtCore.QSize(60, 23))
        self.saving_throws_reflex_misc_bonus.setMaximumSize(QtCore.QSize(60, 23))
        self.saving_throws_reflex_misc_bonus.setObjectName("saving_throws_reflex_misc_bonus")
        self.saving_throws_will_label = QtWidgets.QLabel(self.layoutWidget2)
        self.saving_throws_will_label.setMinimumSize(QtCore.QSize(44, 23))
        self.saving_throws_will_label.setMaximumSize(QtCore.QSize(44, 23))
        self.saving_throws_will_label.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.saving_throws_will_label.setObjectName("saving_throws_will_label")
        self.saving_throws_will_total = QtWidgets.QLineEdit(self.layoutWidget2)
        self.saving_throws_will_total.setMinimumSize(QtCore.QSize(60, 23))
        self.saving_throws_will_total.setMaximumSize(QtCore.QSize(60, 23))
        self.saving_throws_will_total.setObjectName("saving_throws_will_total")
        self._eq_sign_6 = QtWidgets.QLabel(self.layoutWidget2)
        self._eq_sign_6.setMinimumSize(QtCore.QSize(8, 10))
        self._eq_sign_6.setMaximumSize(QtCore.QSize(8, 23))
        self._eq_sign_6.setAlignment(QtCore.Qt.AlignCenter)
        self._eq_sign_6.setObjectName("_eq_sign_6")
        self.saving_throws_will_class_bonus = QtWidgets.QLineEdit(self.layoutWidget2)
        self.saving_throws_will_class_bonus.setMinimumSize(QtCore.QSize(60, 23))
        self.saving_throws_will_class_bonus.setMaximumSize(QtCore.QSize(60, 23))
        self.saving_throws_will_class_bonus.setObjectName("saving_throws_will_class_bonus")
        self._plus_sign_3 = QtWidgets.QLabel(self.layoutWidget2)
        self._plus_sign_3.setMinimumSize(QtCore.QSize(8, 10))
        self._plus_sign_3.setMaximumSize(QtCore.QSize(8, 23))
        self._plus_sign_3.setAlignment(QtCore.Qt.AlignCenter)
        self._plus_sign_3.setObjectName("_plus_sign_3")
        self.saving_throws_will_attr_bonus = QtWidgets.QLineEdit(self.layoutWidget2)
        self.saving_throws_will_attr_bonus.setMinimumSize(QtCore.QSize(59, 23))
        self.saving_throws_will_attr_bonus.setMaximumSize(QtCore.QSize(59, 23))
        self.saving_throws_will_attr_bonus.setObjectName("saving_throws_will_attr_bonus")
        self._plus_sign_6 = QtWidgets.QLabel(self.layoutWidget2)
        self._plus_sign_6.setMinimumSize(QtCore.QSize(8, 10))
        self._plus_sign_6.setMaximumSize(QtCore.QSize(8, 23))
        self._plus_sign_6.setAlignment(QtCore.Qt.AlignCenter)
        self._plus_sign_6.setObjectName("_plus_sign_6")
        self.saving_throws_will_size_bonus = QtWidgets.QLineEdit(self.layoutWidget2)
        self.saving_throws_will_size_bonus.setMinimumSize(QtCore.QSize(60, 23))
        self.saving_throws_will_size_bonus.setMaximumSize(QtCore.QSize(60, 23))
        self.saving_throws_will_size_bonus.setObjectName("saving_throws_will_size_bonus")
        self._plus_sign_9 = QtWidgets.QLabel(self.layoutWidget2)
        self._plus_sign_9.setMinimumSize(QtCore.QSize(8, 10))
        self._plus_sign_9.setMaximumSize(QtCore.QSize(8, 23))
        self._plus_sign_9.setAlignment(QtCore.Qt.AlignCenter)
        self._plus_sign_9.setObjectName("_plus_sign_9")
        self.saving_throws_will_misc_bonus = QtWidgets.QLineEdit(self.layoutWidget2)
        self.saving_throws_will_misc_bonus.setMinimumSize(QtCore.QSize(60, 23))
        self.saving_throws_will_misc_bonus.setMaximumSize(QtCore.QSize(60, 23))
        self.saving_throws_will_misc_bonus.setObjectName("saving_throws_will_misc_bonus")
        self.SavingThrowsLayout.addWidget(self.saving_throws_will_misc_bonus, 3, 9, 1, 1)

        self.SavingThrowsLayout.addWidget(self.saving_throws_total_label, 0, 1, 1, 1)
        self.SavingThrowsLayout.addWidget(self.saving_throws_class_base_label, 0, 3, 1, 1)
        self.SavingThrowsLayout.addWidget(self.saving_throws_attr_bonus_label, 0, 5, 1, 1)
        self.SavingThrowsLayout.addWidget(self.saving_throws_size_bonus_label, 0, 7, 1, 1)
        self.SavingThrowsLayout.addWidget(self.saving_throws_misc_bonus_label, 0, 9, 1, 1)
        self.SavingThrowsLayout.addWidget(self.saving_throws_fortitude_label, 1, 0, 1, 1)
        self.SavingThrowsLayout.addWidget(self.saving_throws_fortitude_total, 1, 1, 1, 1)
        self.SavingThrowsLayout.addWidget(self._eq_sign_4, 1, 2, 1, 1)
        self.SavingThrowsLayout.addWidget(self.saving_throws_fortitude_class_base, 1, 3, 1, 1)
        self.SavingThrowsLayout.addWidget(self._plus_sign, 1, 4, 1, 1)
        self.SavingThrowsLayout.addWidget(self.saving_throws_fortitude_attr_bonus, 1, 5, 1, 1)
        self.SavingThrowsLayout.addWidget(self._plus_sign_4, 1, 6, 1, 1)
        self.SavingThrowsLayout.addWidget(self.saving_throws_fortitude_size_bonus, 1, 7, 1, 1)
        self.SavingThrowsLayout.addWidget(self._plus_sign_7, 1, 8, 1, 1)
        self.SavingThrowsLayout.addWidget(self.saving_throws_fortitude_misc_bonus, 1, 9, 1, 1)
        self.SavingThrowsLayout.addWidget(self.saving_throws_reflex_label, 2, 0, 1, 1)
        self.SavingThrowsLayout.addWidget(self.saving_throws_reflex_total, 2, 1, 1, 1)
        self.SavingThrowsLayout.addWidget(self._eq_sign_5, 2, 2, 1, 1)
        self.SavingThrowsLayout.addWidget(self.saving_throws_reflex_class_bonus, 2, 3, 1, 1)
        self.SavingThrowsLayout.addWidget(self._plus_sign_2, 2, 4, 1, 1)
        self.SavingThrowsLayout.addWidget(self.saving_throws_reflex_attr_bonus, 2, 5, 1, 1)
        self.SavingThrowsLayout.addWidget(self._plus_sign_5, 2, 6, 1, 1)
        self.SavingThrowsLayout.addWidget(self.saving_throws_reflex_size_bonus, 2, 7, 1, 1)
        self.SavingThrowsLayout.addWidget(self._plus_sign_8, 2, 8, 1, 1)
        self.SavingThrowsLayout.addWidget(self.saving_throws_reflex_misc_bonus, 2, 9, 1, 1)
        self.SavingThrowsLayout.addWidget(self.saving_throws_will_label, 3, 0, 1, 1)
        self.SavingThrowsLayout.addWidget(self.saving_throws_will_total, 3, 1, 1, 1)
        self.SavingThrowsLayout.addWidget(self._eq_sign_6, 3, 2, 1, 1)
        self.SavingThrowsLayout.addWidget(self.saving_throws_will_class_bonus, 3, 3, 1, 1)
        self.SavingThrowsLayout.addWidget(self._plus_sign_3, 3, 4, 1, 1)
        self.SavingThrowsLayout.addWidget(self.saving_throws_will_attr_bonus, 3, 5, 1, 1)
        self.SavingThrowsLayout.addWidget(self._plus_sign_6, 3, 6, 1, 1)
        self.SavingThrowsLayout.addWidget(self.saving_throws_will_size_bonus, 3, 7, 1, 1)
        self.SavingThrowsLayout.addWidget(self._plus_sign_9, 3, 8, 1, 1)

        self.translate_saving_throws_box()

    def translate_saving_throws_box(self):
        _translate = QtCore.QCoreApplication.translate
        self.SavingThrowsBox.setTitle(_translate("MainWindow", "Saving throws"))
        self.saving_throws_total_label.setText(_translate("MainWindow", "Total"))
        self.saving_throws_class_base_label.setText(_translate("MainWindow", "Class Base"))
        self.saving_throws_attr_bonus_label.setText(_translate("MainWindow", "Attr"))
        self.saving_throws_size_bonus_label.setText(_translate("MainWindow", "Size"))
        self.saving_throws_misc_bonus_label.setText(_translate("MainWindow", "Misc"))
        self.saving_throws_fortitude_label.setText(_translate("MainWindow", "Fortitude"))
        self.saving_throws_fortitude_total.setText(_translate("MainWindow", "10"))
        self._eq_sign_4.setText(_translate("MainWindow", "="))
        self.saving_throws_fortitude_class_base.setText(_translate("MainWindow", "10"))
        self._plus_sign.setText(_translate("MainWindow", "+"))
        self.saving_throws_fortitude_attr_bonus.setText(_translate("MainWindow", "10"))
        self._plus_sign_4.setText(_translate("MainWindow", "+"))
        self.saving_throws_fortitude_size_bonus.setText(_translate("MainWindow", "10"))
        self._plus_sign_7.setText(_translate("MainWindow", "+"))
        self.saving_throws_fortitude_misc_bonus.setText(_translate("MainWindow", "10"))
        self.saving_throws_reflex_label.setText(_translate("MainWindow", "Reflex"))
        self.saving_throws_reflex_total.setText(_translate("MainWindow", "10"))
        self._eq_sign_5.setText(_translate("MainWindow", "="))
        self.saving_throws_reflex_class_bonus.setText(_translate("MainWindow", "10"))
        self._plus_sign_2.setText(_translate("MainWindow", "+"))
        self.saving_throws_reflex_attr_bonus.setText(_translate("MainWindow", "10"))
        self._plus_sign_5.setText(_translate("MainWindow", "+"))
        self.saving_throws_reflex_size_bonus.setText(_translate("MainWindow", "10"))
        self._plus_sign_8.setText(_translate("MainWindow", "+"))
        self.saving_throws_reflex_misc_bonus.setText(_translate("MainWindow", "10"))
        self.saving_throws_will_label.setText(_translate("MainWindow", "Will"))
        self.saving_throws_will_total.setText(_translate("MainWindow", "10"))
        self._eq_sign_6.setText(_translate("MainWindow", "="))
        self.saving_throws_will_class_bonus.setText(_translate("MainWindow", "10"))
        self._plus_sign_3.setText(_translate("MainWindow", "+"))
        self.saving_throws_will_attr_bonus.setText(_translate("MainWindow", "10"))
        self._plus_sign_6.setText(_translate("MainWindow", "+"))
        self.saving_throws_will_size_bonus.setText(_translate("MainWindow", "10"))
        self._plus_sign_9.setText(_translate("MainWindow", "+"))
        self.saving_throws_will_misc_bonus.setText(_translate("MainWindow", "10"))