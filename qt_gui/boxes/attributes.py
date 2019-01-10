from PyQt5 import QtWidgets, QtCore

from qt_gui.boxes.box import DefaultBox
from qt_gui.boxes.qt_line_edits import create_qlabel, create_qline_edit


class AttributesBox(DefaultBox):
    def __init__(self, centralwidget):
        self.root = QtWidgets.QGroupBox(centralwidget)
        self.root.setGeometry(QtCore.QRect(10, 200, 311, 231))
        self.root.setObjectName("AttributesBox")

        self.container = QtWidgets.QWidget(self.root)
        self.container.setGeometry(QtCore.QRect(20, 20, 285, 201))
        self.container.setObjectName("gridLayoutWidget")

        self.layout = QtWidgets.QGridLayout(self.container)
        self.layout.setContentsMargins(9, 9, 9, 9)
        self.layout.setSpacing(6)
        self.layout.setObjectName("AttributesLayout")

        qlabel_dict = dict(parent=self.container,
                           align=QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter,
                           )
        qlabel_header_dict = dict(parent=self.container, align=QtCore.Qt.AlignCenter, )
        qline_dict = dict(parent=self.container, min_size=(0, 23), )

        self.attr_head_name = create_qlabel("attr_head_name", **qlabel_header_dict)
        self.attr_head_val = create_qlabel("attr_head_val", **qlabel_header_dict)
        self.Attr_head_mod = create_qlabel("Attr_head_mod", **qlabel_header_dict)
        self.attr_head_temp_val = create_qlabel("attr_head_temp_val", **qlabel_header_dict)
        self.attr_head_temp_mod = create_qlabel("attr_head_temp_mod", **qlabel_header_dict)

        self.attr_str_label = create_qlabel("attr_str_label", **qlabel_dict)
        self.attr_dex_label = create_qlabel("attr_dex_label", **qlabel_dict)
        self.attr_con_label = create_qlabel("attr_con_label", **qlabel_dict)
        self.attr_int_label = create_qlabel("attr_int_label", **qlabel_dict)
        self.attr_wis_label = create_qlabel("attr_wis_label", **qlabel_dict)
        self.attr_cha_label = create_qlabel("attr_cha_label", **qlabel_dict)

        self.attr_str_val = create_qline_edit("attr_str_val", **qline_dict)
        self.attr_str_mod = create_qline_edit("attr_str_mod", **qline_dict)
        self.attr_str_temp_val = create_qline_edit("attr_str_temp_val", **qline_dict)
        self.attr_str_temp_mod = create_qline_edit("attr_str_temp_mod", **qline_dict)

        self.attr_dex_val = create_qline_edit("attr_dex_val", **qline_dict)
        self.attr_dex_mod = create_qline_edit("attr_dex_mod", **qline_dict)
        self.attr_dex_temp_val = create_qline_edit("attr_dex_temp_val", **qline_dict)
        self.attr_dex_temp_mod = create_qline_edit("attr_dex_temp_mod", **qline_dict)

        self.attr_con_val = create_qline_edit("attr_con_val", **qline_dict)
        self.attr_con_mod = create_qline_edit("attr_con_mod", **qline_dict)
        self.attr_con_temp_val = create_qline_edit("attr_con_temp_val", **qline_dict)
        self.attr_con_temp_mod = create_qline_edit("attr_con_temp_mod", **qline_dict)

        self.attr_int_val = create_qline_edit("attr_int_val", **qline_dict)
        self.attr_int_mod = create_qline_edit("attr_int_mod", **qline_dict)
        self.attr_int_temp_val = create_qline_edit("attr_int_temp_val", **qline_dict)
        self.attr_int_temp_mod = create_qline_edit("attr_int_temp_mod", **qline_dict)

        self.attr_wis_val = create_qline_edit("attr_wis_val", **qline_dict)
        self.attr_wis_mod = create_qline_edit("attr_wis_mod", **qline_dict)
        self.attr_wis_temp_val = create_qline_edit("attr_wis_temp_val", **qline_dict)
        self.attr_wis_temp_mod = create_qline_edit("attr_wis_temp_mod", **qline_dict)

        self.attr_cha_val = create_qline_edit("attr_cha_val", **qline_dict)
        self.attr_cha_mod = create_qline_edit("attr_cha_mod", **qline_dict)
        self.attr_cha_temp_val = create_qline_edit("attr_cha_temp_val", **qline_dict)
        self.attr_cha_temp_mod = create_qline_edit("attr_cha_temp_mod", **qline_dict)

        self.add_to_layout()
        self.translate()
        self.set_default_values()

    def add_to_layout(self):
        self.layout.addWidget(self.attr_head_name, 0, 0, 1, 1)
        self.layout.addWidget(self.Attr_head_mod, 0, 2, 1, 1)
        self.layout.addWidget(self.attr_head_temp_mod, 0, 4, 1, 1)
        self.layout.addWidget(self.attr_head_temp_val, 0, 3, 1, 1)
        self.layout.addWidget(self.attr_head_val, 0, 1, 1, 1)

        self.layout.addWidget(self.attr_str_label, 1, 0, 1, 1)
        self.layout.addWidget(self.attr_dex_label, 2, 0, 1, 1)
        self.layout.addWidget(self.attr_con_label, 3, 0, 1, 1)
        self.layout.addWidget(self.attr_int_label, 4, 0, 1, 1)
        self.layout.addWidget(self.attr_wis_label, 5, 0, 1, 1)
        self.layout.addWidget(self.attr_cha_label, 6, 0, 1, 1)

        self.layout.addWidget(self.attr_str_val, 1, 1, 1, 1)
        self.layout.addWidget(self.attr_str_mod, 1, 2, 1, 1)
        self.layout.addWidget(self.attr_str_temp_val, 1, 3, 1, 1)
        self.layout.addWidget(self.attr_str_temp_mod, 1, 4, 1, 1)

        self.layout.addWidget(self.attr_dex_val, 2, 1, 1, 1)
        self.layout.addWidget(self.attr_dex_mod, 2, 2, 1, 1)
        self.layout.addWidget(self.attr_dex_temp_val, 2, 3, 1, 1)
        self.layout.addWidget(self.attr_dex_temp_mod, 2, 4, 1, 1)

        self.layout.addWidget(self.attr_con_val, 3, 1, 1, 1)
        self.layout.addWidget(self.attr_con_mod, 3, 2, 1, 1)
        self.layout.addWidget(self.attr_con_temp_mod, 3, 4, 1, 1)
        self.layout.addWidget(self.attr_con_temp_val, 3, 3, 1, 1)

        self.layout.addWidget(self.attr_int_val, 4, 1, 1, 1)
        self.layout.addWidget(self.attr_int_mod, 4, 2, 1, 1)
        self.layout.addWidget(self.attr_int_temp_mod, 4, 4, 1, 1)
        self.layout.addWidget(self.attr_int_temp_val, 4, 3, 1, 1)

        self.layout.addWidget(self.attr_wis_val, 5, 1, 1, 1)
        self.layout.addWidget(self.attr_wis_mod, 5, 2, 1, 1)
        self.layout.addWidget(self.attr_wis_temp_mod, 5, 4, 1, 1)
        self.layout.addWidget(self.attr_wis_temp_val, 5, 3, 1, 1)

        self.layout.addWidget(self.attr_cha_val, 6, 1, 1, 1)
        self.layout.addWidget(self.attr_cha_mod, 6, 2, 1, 1)
        self.layout.addWidget(self.attr_cha_temp_val, 6, 3, 1, 1)
        self.layout.addWidget(self.attr_cha_temp_mod, 6, 4, 1, 1)

    def translate(self):
        _translate = QtCore.QCoreApplication.translate
        self.root.setTitle(_translate("MainWindow", "Attributes"))
        self.attr_head_name.setText(_translate("MainWindow", "Atrribute"))
        self.attr_int_label.setText(_translate("MainWindow", "INT"))
        self.Attr_head_mod.setText(_translate("MainWindow", "Mod"))
        self.attr_head_temp_mod.setText(_translate("MainWindow", "Temp mod"))
        self.attr_dex_label.setText(_translate("MainWindow", "DEX"))
        self.attr_head_temp_val.setText(_translate("MainWindow", "Temp val"))
        self.attr_con_label.setText(_translate("MainWindow", "CON"))
        self.attr_head_val.setText(_translate("MainWindow", "Value"))
        self.attr_wis_label.setText(_translate("MainWindow", "WIS"))
        self.attr_str_label.setText(_translate("MainWindow", "STR"))
        self.attr_cha_label.setText(_translate("MainWindow", "CHA"))

    def set_default_values(self):
        self.attr_str_val.setText("10")
        self.attr_dex_val.setText("10")
        self.attr_int_temp_mod.setText("10")
        self.attr_con_temp_mod.setText("10")
        self.attr_con_val.setText("10")
        self.attr_con_mod.setText("10")
        self.attr_con_temp_val.setText("10")
        self.attr_wis_mod.setText("10")
        self.attr_wis_temp_mod.setText("10")
        self.attr_wis_temp_val.setText("10")
        self.attr_dex_mod.setText("10")
        self.attr_dex_temp_val.setText("10")
        self.attr_dex_temp_mod.setText("10")
        self.attr_wis_val.setText("10")
        self.attr_int_temp_val.setText("10")
        self.attr_int_mod.setText("10")
        self.attr_int_val.setText("10")
        self.attr_str_temp_mod.setText("10")
        self.attr_str_mod.setText("10")
        self.attr_str_temp_val.setText("10")
        self.attr_cha_val.setText("10")
        self.attr_cha_mod.setText("10")
        self.attr_cha_temp_val.setText("10")
        self.attr_cha_temp_mod.setText("10")
