from PyQt5 import QtWidgets, QtCore

from qt_gui.boxes.qt_line_edits import create_qlabel, create_qline_edit


class InitiativeSpeedBox:
    def __init__(self, centralwidget):
        self.root = QtWidgets.QGroupBox(centralwidget)
        self.root.setGeometry(QtCore.QRect(1430, 290, 271, 121))
        self.root.setObjectName("InitiativeSpeedBox")
        self.container = QtWidgets.QWidget(self.root)
        self.container.setGeometry(QtCore.QRect(10, 20, 261, 91))
        self.container.setObjectName("gridLayoutWidget_7")
        self.layout = QtWidgets.QGridLayout(self.container)
        self.layout.setContentsMargins(9, 9, 9, 9)
        self.layout.setSpacing(6)
        self.layout.setObjectName("InitiativeSpeedLayout")
        qline_dict = dict(parent=self.container, min_size=(0, 23), max_size=(10000, 20))
        qlabel_dict = dict(parent=self.container)
        qlabel_eq_sign_dict = dict(parent=self.container, min_size=(8, 20), max_size=(1000, 20),
                                   align=QtCore.Qt.AlignCenter)
        qlabel_plus_sign_dict = dict(parent=self.container, min_size=(8, 10), max_size=(10, 10))

        self.initiative_speed_total_label = create_qlabel("initiative_speed_total_label", **qlabel_dict)
        self.initiative_speed_initiative_misc_bonus_label = create_qlabel(
            "initiative_speed_initiative_misc_bonus_label", **qlabel_dict)
        self.initiative_speed_initiative_dex_bonus_label = create_qlabel("initiative_speed_initiative_dex_bonus_label",
                                                                         **qlabel_dict)
        self.initiative_speed_initiative_label = create_qlabel("initiative_speed_initiative_label", **qlabel_dict)
        self.initiative_speed_speed_label = create_qlabel("initiative_speed_speed_label", **qlabel_plus_sign_dict)
        self.initiative_speed_speed_armor_type_label = create_qlabel("initiative_speed_speed_armor_type_label",
                                                                     **qlabel_dict)

        self._eq_sign_7 = create_qlabel("_eq_sign_7", **qlabel_eq_sign_dict)
        self._plus_sign_10 = create_qlabel("_plus_sign_10", **qlabel_dict)

        self.initiative_speed_initiative_total = create_qline_edit("initiative_speed_initiative_total", **qline_dict)
        self.initiative_speed_initiative_misc_bonus = create_qline_edit("initiative_speed_initiative_misc_bonus",
                                                                        **qline_dict)
        self.initiative_speed_initiative_dex_bonus = create_qline_edit("initiative_speed_initiative_dex_bonus",
                                                                       **qline_dict)
        self.initiative_speed_speed_total = create_qline_edit("initiative_speed_speed_total", **qline_dict)
        self.initiative_speed_speed_armor_type = create_qline_edit("initiative_speed_speed_armor_type", **qline_dict)

        self.layout.addWidget(self.initiative_speed_initiative_total, 1, 1, 1, 1)
        self.layout.addWidget(self._eq_sign_7, 1, 2, 1, 1)
        self.layout.addWidget(self.initiative_speed_total_label, 0, 1, 1, 1)
        self.layout.addWidget(self.initiative_speed_initiative_misc_bonus, 1, 5, 1, 1)
        self.layout.addWidget(self.initiative_speed_initiative_dex_bonus, 1, 3, 1, 1)
        self.layout.addWidget(self.initiative_speed_initiative_misc_bonus_label, 0, 5, 1, 1)
        self.layout.addWidget(self.initiative_speed_initiative_dex_bonus_label, 0, 3, 1, 1)
        self.layout.addWidget(self.initiative_speed_initiative_label, 1, 0, 1, 1)
        self.layout.addWidget(self._plus_sign_10, 1, 4, 1, 1)
        self.layout.addWidget(self.initiative_speed_speed_label, 2, 0, 1, 1)
        self.layout.addWidget(self.initiative_speed_speed_total, 2, 1, 1, 1)
        self.layout.addWidget(self.initiative_speed_speed_armor_type_label, 2, 2, 1, 1)
        self.layout.addWidget(self.initiative_speed_speed_armor_type, 2, 3, 1, 3)

        self.translate_initiative_speed_box()

    def translate_initiative_speed_box(self):
        _translate = QtCore.QCoreApplication.translate
        self.root.setTitle(_translate("MainWindow", "Initiative and speed"))
        self.initiative_speed_initiative_total.setText(_translate("MainWindow", "10"))
        self._eq_sign_7.setText(_translate("MainWindow", "="))
        self.initiative_speed_total_label.setText(_translate("MainWindow", "Total"))
        self.initiative_speed_initiative_misc_bonus.setText(_translate("MainWindow", "10"))
        self.initiative_speed_initiative_dex_bonus.setText(_translate("MainWindow", "10"))
        self.initiative_speed_initiative_misc_bonus_label.setText(_translate("MainWindow", "Misc"))
        self.initiative_speed_initiative_dex_bonus_label.setText(_translate("MainWindow", "Dex"))
        self.initiative_speed_initiative_label.setText(_translate("MainWindow", "Init."))
        self._plus_sign_10.setText(_translate("MainWindow", "+"))
        self.initiative_speed_speed_label.setText(_translate("MainWindow", "Speed"))
        self.initiative_speed_speed_total.setText(_translate("MainWindow", "10"))
        self.initiative_speed_speed_armor_type_label.setText(_translate("MainWindow", "Armor"))
        self.initiative_speed_speed_armor_type.setText(_translate("MainWindow", "Lorem ipsum"))