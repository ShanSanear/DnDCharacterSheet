from PyQt5 import QtWidgets, QtCore

from qt_gui.boxes.box import DefaultBox


class HpAcBox(DefaultBox):
    def __init__(self, parent, position, size):
        self.root = QtWidgets.QGroupBox(parent)
        self.root.setGeometry(QtCore.QRect(*position, *size))
        self.root.setMaximumSize(QtCore.QSize(2000, 2000))
        self.root.setObjectName("HpAcBox")
        self.container = QtWidgets.QWidget(self.root)
        self.container.setObjectName("layoutWidget")
        self.layout = QtWidgets.QGridLayout(self.container)
        self.layout.setObjectName("HpAcLayout")
        self.hp_ac_hp_total_label = QtWidgets.QLabel(self.container)
        self.hp_ac_hp_total_label.setMinimumSize(QtCore.QSize(0, 23))
        self.hp_ac_hp_total_label.setMaximumSize(QtCore.QSize(100000, 23))
        self.hp_ac_hp_total_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hp_ac_hp_total_label.setObjectName("hp_ac_hp_total_label")
        self.hp_ac_hp_hp_wounds_current_hp_label = QtWidgets.QLabel(self.container)
        self.hp_ac_hp_hp_wounds_current_hp_label.setMinimumSize(QtCore.QSize(0, 23))
        self.hp_ac_hp_hp_wounds_current_hp_label.setMaximumSize(QtCore.QSize(140, 23))
        self.hp_ac_hp_hp_wounds_current_hp_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hp_ac_hp_hp_wounds_current_hp_label.setObjectName("hp_ac_hp_hp_wounds_current_hp_label")
        self.hp_ac_hp_label = QtWidgets.QLabel(self.container)
        self.hp_ac_hp_label.setMaximumSize(QtCore.QSize(14, 23))
        self.hp_ac_hp_label.setObjectName("hp_ac_hp_label")
        self.hp_ac_hp_total = QtWidgets.QLineEdit(self.container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hp_ac_hp_total.sizePolicy().hasHeightForWidth())
        self.hp_ac_hp_total.setSizePolicy(sizePolicy)
        self.hp_ac_hp_total.setMinimumSize(QtCore.QSize(0, 23))
        self.hp_ac_hp_total.setMaximumSize(QtCore.QSize(1000, 23))
        self.hp_ac_hp_total.setBaseSize(QtCore.QSize(200, 0))
        self.hp_ac_hp_total.setObjectName("hp_ac_hp_total")
        self.hp_ac_ac_label = QtWidgets.QLabel(self.container)
        self.hp_ac_ac_label.setMaximumSize(QtCore.QSize(14, 23))
        self.hp_ac_ac_label.setObjectName("hp_ac_ac_label")
        self.hp_ac_ac_total = QtWidgets.QLineEdit(self.container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hp_ac_ac_total.sizePolicy().hasHeightForWidth())
        self.hp_ac_ac_total.setSizePolicy(sizePolicy)
        self.hp_ac_ac_total.setMinimumSize(QtCore.QSize(0, 23))
        self.hp_ac_ac_total.setMaximumSize(QtCore.QSize(1000, 23))
        self.hp_ac_ac_total.setObjectName("hp_ac_ac_total")
        self._eq_sign_3 = QtWidgets.QLabel(self.container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._eq_sign_3.sizePolicy().hasHeightForWidth())
        self._eq_sign_3.setSizePolicy(sizePolicy)
        self._eq_sign_3.setMinimumSize(QtCore.QSize(10, 0))
        self._eq_sign_3.setMaximumSize(QtCore.QSize(10, 23))
        self._eq_sign_3.setAlignment(QtCore.Qt.AlignCenter)
        self._eq_sign_3.setObjectName("_eq_sign_3")
        self.hp_ac_ac_base = QtWidgets.QLineEdit(self.container)
        self.hp_ac_ac_base.setMinimumSize(QtCore.QSize(0, 23))
        self.hp_ac_ac_base.setMaximumSize(QtCore.QSize(26, 23))
        self.hp_ac_ac_base.setAlignment(QtCore.Qt.AlignCenter)
        self.hp_ac_ac_base.setObjectName("hp_ac_ac_base")
        self._plus_sign_12 = QtWidgets.QLabel(self.container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._plus_sign_12.sizePolicy().hasHeightForWidth())
        self._plus_sign_12.setSizePolicy(sizePolicy)
        self._plus_sign_12.setMinimumSize(QtCore.QSize(10, 0))
        self._plus_sign_12.setMaximumSize(QtCore.QSize(10, 23))
        self._plus_sign_12.setAlignment(QtCore.Qt.AlignCenter)
        self._plus_sign_12.setObjectName("_plus_sign_12")
        self.hp_ac_ac_armor_bonus = QtWidgets.QLineEdit(self.container)
        self.hp_ac_ac_armor_bonus.setMinimumSize(QtCore.QSize(0, 23))
        self.hp_ac_ac_armor_bonus.setMaximumSize(QtCore.QSize(27, 23))
        self.hp_ac_ac_armor_bonus.setAlignment(QtCore.Qt.AlignCenter)
        self.hp_ac_ac_armor_bonus.setObjectName("hp_ac_ac_armor_bonus")
        self._plus_sign_11 = QtWidgets.QLabel(self.container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._plus_sign_11.sizePolicy().hasHeightForWidth())
        self._plus_sign_11.setSizePolicy(sizePolicy)
        self._plus_sign_11.setMinimumSize(QtCore.QSize(10, 0))
        self._plus_sign_11.setMaximumSize(QtCore.QSize(10, 23))
        self._plus_sign_11.setAlignment(QtCore.Qt.AlignCenter)
        self._plus_sign_11.setObjectName("_plus_sign_11")
        self.hp_ac_ac_shield_bonus = QtWidgets.QLineEdit(self.container)
        self.hp_ac_ac_shield_bonus.setMinimumSize(QtCore.QSize(0, 23))
        self.hp_ac_ac_shield_bonus.setMaximumSize(QtCore.QSize(27, 23))
        self.hp_ac_ac_shield_bonus.setAlignment(QtCore.Qt.AlignCenter)
        self.hp_ac_ac_shield_bonus.setObjectName("hp_ac_ac_shield_bonus")
        self._plus_sign_13 = QtWidgets.QLabel(self.container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._plus_sign_13.sizePolicy().hasHeightForWidth())
        self._plus_sign_13.setSizePolicy(sizePolicy)
        self._plus_sign_13.setMinimumSize(QtCore.QSize(10, 0))
        self._plus_sign_13.setMaximumSize(QtCore.QSize(10, 23))
        self._plus_sign_13.setAlignment(QtCore.Qt.AlignCenter)
        self._plus_sign_13.setObjectName("_plus_sign_13")
        self.hp_ac_ac_dex_bonus = QtWidgets.QLineEdit(self.container)
        self.hp_ac_ac_dex_bonus.setMinimumSize(QtCore.QSize(0, 23))
        self.hp_ac_ac_dex_bonus.setMaximumSize(QtCore.QSize(27, 23))
        self.hp_ac_ac_dex_bonus.setAlignment(QtCore.Qt.AlignCenter)
        self.hp_ac_ac_dex_bonus.setObjectName("hp_ac_ac_dex_bonus")
        self._plus_sign_14 = QtWidgets.QLabel(self.container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._plus_sign_14.sizePolicy().hasHeightForWidth())
        self._plus_sign_14.setSizePolicy(sizePolicy)
        self._plus_sign_14.setMinimumSize(QtCore.QSize(10, 0))
        self._plus_sign_14.setMaximumSize(QtCore.QSize(10, 23))
        self._plus_sign_14.setAlignment(QtCore.Qt.AlignCenter)
        self._plus_sign_14.setObjectName("_plus_sign_14")
        self.hp_ac_ac_size_bonus = QtWidgets.QLineEdit(self.container)
        self.hp_ac_ac_size_bonus.setMinimumSize(QtCore.QSize(0, 23))
        self.hp_ac_ac_size_bonus.setMaximumSize(QtCore.QSize(27, 23))
        self.hp_ac_ac_size_bonus.setAlignment(QtCore.Qt.AlignCenter)
        self.hp_ac_ac_size_bonus.setObjectName("hp_ac_ac_size_bonus")
        self._plus_sign_15 = QtWidgets.QLabel(self.container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._plus_sign_15.sizePolicy().hasHeightForWidth())
        self._plus_sign_15.setSizePolicy(sizePolicy)
        self._plus_sign_15.setMinimumSize(QtCore.QSize(10, 0))
        self._plus_sign_15.setMaximumSize(QtCore.QSize(10, 23))
        self._plus_sign_15.setAlignment(QtCore.Qt.AlignCenter)
        self._plus_sign_15.setObjectName("_plus_sign_15")
        self.hp_ac_ac_misc_bonus = QtWidgets.QLineEdit(self.container)
        self.hp_ac_ac_misc_bonus.setMinimumSize(QtCore.QSize(0, 23))
        self.hp_ac_ac_misc_bonus.setMaximumSize(QtCore.QSize(26, 23))
        self.hp_ac_ac_misc_bonus.setAlignment(QtCore.Qt.AlignCenter)
        self.hp_ac_ac_misc_bonus.setObjectName("hp_ac_ac_misc_bonus")
        self.hp_ac_ac_total_label = QtWidgets.QLabel(self.container)
        self.hp_ac_ac_total_label.setMinimumSize(QtCore.QSize(0, 23))
        self.hp_ac_ac_total_label.setMaximumSize(QtCore.QSize(1000, 23))
        self.hp_ac_ac_total_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hp_ac_ac_total_label.setObjectName("hp_ac_ac_total_label")
        self.hp_ac_ac_base_bonus_label = QtWidgets.QLabel(self.container)
        self.hp_ac_ac_base_bonus_label.setMinimumSize(QtCore.QSize(0, 23))
        self.hp_ac_ac_base_bonus_label.setMaximumSize(QtCore.QSize(26, 23))
        self.hp_ac_ac_base_bonus_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hp_ac_ac_base_bonus_label.setObjectName("hp_ac_ac_base_bonus_label")
        self.hp_ac_ac_armor_bonus_label = QtWidgets.QLabel(self.container)
        self.hp_ac_ac_armor_bonus_label.setMinimumSize(QtCore.QSize(0, 23))
        self.hp_ac_ac_armor_bonus_label.setMaximumSize(QtCore.QSize(27, 23))
        self.hp_ac_ac_armor_bonus_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hp_ac_ac_armor_bonus_label.setObjectName("hp_ac_ac_armor_bonus_label")
        self.hp_ac_ac_shield_bonus_label = QtWidgets.QLabel(self.container)
        self.hp_ac_ac_shield_bonus_label.setMinimumSize(QtCore.QSize(0, 23))
        self.hp_ac_ac_shield_bonus_label.setMaximumSize(QtCore.QSize(27, 23))
        self.hp_ac_ac_shield_bonus_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hp_ac_ac_shield_bonus_label.setObjectName("hp_ac_ac_shield_bonus_label")
        self.hp_ac_ac_dex_bonus_label = QtWidgets.QLabel(self.container)
        self.hp_ac_ac_dex_bonus_label.setMinimumSize(QtCore.QSize(0, 23))
        self.hp_ac_ac_dex_bonus_label.setMaximumSize(QtCore.QSize(27, 23))
        self.hp_ac_ac_dex_bonus_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hp_ac_ac_dex_bonus_label.setObjectName("hp_ac_ac_dex_bonus_label")
        self.hp_ac_ac_size_bonus_label = QtWidgets.QLabel(self.container)
        self.hp_ac_ac_size_bonus_label.setMinimumSize(QtCore.QSize(0, 23))
        self.hp_ac_ac_size_bonus_label.setMaximumSize(QtCore.QSize(27, 23))
        self.hp_ac_ac_size_bonus_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hp_ac_ac_size_bonus_label.setObjectName("hp_ac_ac_size_bonus_label")
        self.hp_ac_ac_misc_bonus_label = QtWidgets.QLabel(self.container)
        self.hp_ac_ac_misc_bonus_label.setMinimumSize(QtCore.QSize(0, 23))
        self.hp_ac_ac_misc_bonus_label.setMaximumSize(QtCore.QSize(26, 23))
        self.hp_ac_ac_misc_bonus_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hp_ac_ac_misc_bonus_label.setObjectName("hp_ac_ac_misc_bonus_label")
        self.hp_ac_hp_hp_wounds_current_hp = QtWidgets.QLineEdit(self.container)
        self.hp_ac_hp_hp_wounds_current_hp.setMinimumSize(QtCore.QSize(0, 23))
        self.hp_ac_hp_hp_wounds_current_hp.setMaximumSize(QtCore.QSize(140, 23))
        self.hp_ac_hp_hp_wounds_current_hp.setAlignment(QtCore.Qt.AlignCenter)
        self.hp_ac_hp_hp_wounds_current_hp.setObjectName("hp_ac_hp_hp_wounds_current_hp")
        self.hp_ac_hp_contusion = QtWidgets.QLineEdit(self.container)
        self.hp_ac_hp_contusion.setMinimumSize(QtCore.QSize(0, 23))
        self.hp_ac_hp_contusion.setMaximumSize(QtCore.QSize(140, 23))
        self.hp_ac_hp_contusion.setAlignment(QtCore.Qt.AlignCenter)
        self.hp_ac_hp_contusion.setObjectName("hp_ac_hp_contusion")
        self.hp_ac_contusion_label = QtWidgets.QLabel(self.container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hp_ac_contusion_label.sizePolicy().hasHeightForWidth())
        self.hp_ac_contusion_label.setSizePolicy(sizePolicy)
        self.hp_ac_contusion_label.setMinimumSize(QtCore.QSize(0, 23))
        self.hp_ac_contusion_label.setMaximumSize(QtCore.QSize(140, 23))
        self.hp_ac_contusion_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hp_ac_contusion_label.setObjectName("hp_ac_contusion_label")

        self.add_to_layout()
        self.translate()
        self.root.setLayout(self.layout)

    def add_to_layout(self):
        self.layout.addWidget(self.hp_ac_hp_total_label, 0, 1, 1, 1)
        self.layout.addWidget(self.hp_ac_hp_hp_wounds_current_hp_label, 0, 3, 1, 5)
        self.layout.addWidget(self.hp_ac_hp_label, 1, 0, 1, 1)
        self.layout.addWidget(self.hp_ac_hp_total, 1, 1, 1, 1)
        self.layout.addWidget(self.hp_ac_ac_label, 2, 0, 1, 1)
        self.layout.addWidget(self.hp_ac_ac_total, 2, 1, 1, 1)
        self.layout.addWidget(self._eq_sign_3, 2, 2, 1, 1)
        self.layout.addWidget(self.hp_ac_ac_base, 2, 3, 1, 1)
        self.layout.addWidget(self._plus_sign_12, 2, 4, 1, 1)
        self.layout.addWidget(self.hp_ac_ac_armor_bonus, 2, 5, 1, 1)
        self.layout.addWidget(self._plus_sign_11, 2, 6, 1, 1)
        self.layout.addWidget(self.hp_ac_ac_shield_bonus, 2, 7, 1, 1)
        self.layout.addWidget(self._plus_sign_13, 2, 8, 1, 1)
        self.layout.addWidget(self.hp_ac_ac_dex_bonus, 2, 9, 1, 1)
        self.layout.addWidget(self._plus_sign_14, 2, 10, 1, 1)
        self.layout.addWidget(self.hp_ac_ac_size_bonus, 2, 11, 1, 1)
        self.layout.addWidget(self._plus_sign_15, 2, 12, 1, 1)
        self.layout.addWidget(self.hp_ac_ac_misc_bonus, 2, 13, 1, 1)
        self.layout.addWidget(self.hp_ac_ac_total_label, 3, 1, 1, 1)
        self.layout.addWidget(self.hp_ac_ac_base_bonus_label, 3, 3, 1, 1)
        self.layout.addWidget(self.hp_ac_ac_armor_bonus_label, 3, 5, 1, 1)
        self.layout.addWidget(self.hp_ac_ac_shield_bonus_label, 3, 7, 1, 1)
        self.layout.addWidget(self.hp_ac_ac_dex_bonus_label, 3, 9, 1, 1)
        self.layout.addWidget(self.hp_ac_ac_size_bonus_label, 3, 11, 1, 1)
        self.layout.addWidget(self.hp_ac_ac_misc_bonus_label, 3, 13, 1, 1)
        self.layout.addWidget(self.hp_ac_hp_hp_wounds_current_hp, 1, 3, 1, 5)
        self.layout.addWidget(self.hp_ac_hp_contusion, 1, 9, 1, 5)
        self.layout.addWidget(self.hp_ac_contusion_label, 0, 9, 1, 5)

    def translate(self):
        _translate = QtCore.QCoreApplication.translate
        self.root.setTitle(_translate("MainWindow", "HP / AC"))
        self.hp_ac_hp_total_label.setText(_translate("MainWindow", "Total"))
        self.hp_ac_hp_hp_wounds_current_hp_label.setText(_translate("MainWindow", "Wounds / Current HP"))
        self.hp_ac_hp_label.setText(_translate("MainWindow", "HP"))
        self.hp_ac_hp_total.setText(_translate("MainWindow", "10"))
        self.hp_ac_ac_label.setText(_translate("MainWindow", "AC"))
        self.hp_ac_ac_total.setText(_translate("MainWindow", "10"))
        self._eq_sign_3.setText(_translate("MainWindow", "="))
        self.hp_ac_ac_base.setText(_translate("MainWindow", "10"))
        self._plus_sign_12.setText(_translate("MainWindow", "+"))
        self.hp_ac_ac_armor_bonus.setText(_translate("MainWindow", "10"))
        self._plus_sign_11.setText(_translate("MainWindow", "+"))
        self.hp_ac_ac_shield_bonus.setText(_translate("MainWindow", "10"))
        self._plus_sign_13.setText(_translate("MainWindow", "+"))
        self.hp_ac_ac_dex_bonus.setText(_translate("MainWindow", "10"))
        self._plus_sign_14.setText(_translate("MainWindow", "+"))
        self.hp_ac_ac_size_bonus.setText(_translate("MainWindow", "10"))
        self._plus_sign_15.setText(_translate("MainWindow", "+"))
        self.hp_ac_ac_misc_bonus.setText(_translate("MainWindow", "10"))
        self.hp_ac_ac_total_label.setText(_translate("MainWindow", "Total"))
        self.hp_ac_ac_base_bonus_label.setText(_translate("MainWindow", "Base"))
        self.hp_ac_ac_armor_bonus_label.setText(_translate("MainWindow", "Armor"))
        self.hp_ac_ac_shield_bonus_label.setText(_translate("MainWindow", "Shield"))
        self.hp_ac_ac_dex_bonus_label.setText(_translate("MainWindow", "Dex"))
        self.hp_ac_ac_size_bonus_label.setText(_translate("MainWindow", "Size"))
        self.hp_ac_ac_misc_bonus_label.setText(_translate("MainWindow", "Misc"))
        self.hp_ac_hp_hp_wounds_current_hp.setText(_translate("MainWindow", "10/10"))
        self.hp_ac_hp_contusion.setText(_translate("MainWindow", "10"))
        self.hp_ac_contusion_label.setText(_translate("MainWindow", "Contusion"))