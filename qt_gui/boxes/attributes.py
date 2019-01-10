from PyQt5 import QtWidgets, QtCore

from qt_gui.boxes.box import DefaultBox
from qt_gui.boxes.qt_generic_functions import create_qlabel, create_qline_edit, add_to_box_layout_by_row, \
    add_to_box_layout_by_column


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

        self.head_name = create_qlabel("attr_head_name", **qlabel_header_dict)
        self.head_val = create_qlabel("attr_head_val", **qlabel_header_dict)
        self.head_mod = create_qlabel("Attr_head_mod", **qlabel_header_dict)
        self.head_temp_val = create_qlabel("attr_head_temp_val", **qlabel_header_dict)
        self.head_temp_mod = create_qlabel("attr_head_temp_mod", **qlabel_header_dict)

        self.str_label = create_qlabel("attr_str_label", **qlabel_dict)
        self.dex_label = create_qlabel("attr_dex_label", **qlabel_dict)
        self.con_label = create_qlabel("attr_con_label", **qlabel_dict)
        self.int_label = create_qlabel("attr_int_label", **qlabel_dict)
        self.wis_label = create_qlabel("attr_wis_label", **qlabel_dict)
        self.cha_label = create_qlabel("attr_cha_label", **qlabel_dict)

        self.str_val = create_qline_edit("attr_str_val", **qline_dict)
        self.str_mod = create_qline_edit("attr_str_mod", **qline_dict)
        self.str_temp_val = create_qline_edit("attr_str_temp_val", **qline_dict)
        self.str_temp_mod = create_qline_edit("attr_str_temp_mod", **qline_dict)

        self.dex_val = create_qline_edit("attr_dex_val", **qline_dict)
        self.dex_mod = create_qline_edit("attr_dex_mod", **qline_dict)
        self.dex_temp_val = create_qline_edit("attr_dex_temp_val", **qline_dict)
        self.dex_temp_mod = create_qline_edit("attr_dex_temp_mod", **qline_dict)

        self.con_val = create_qline_edit("attr_con_val", **qline_dict)
        self.con_mod = create_qline_edit("attr_con_mod", **qline_dict)
        self.con_temp_val = create_qline_edit("attr_con_temp_val", **qline_dict)
        self.con_temp_mod = create_qline_edit("attr_con_temp_mod", **qline_dict)

        self.int_val = create_qline_edit("attr_int_val", **qline_dict)
        self.int_mod = create_qline_edit("attr_int_mod", **qline_dict)
        self.int_temp_val = create_qline_edit("attr_int_temp_val", **qline_dict)
        self.int_temp_mod = create_qline_edit("attr_int_temp_mod", **qline_dict)

        self.wis_val = create_qline_edit("attr_wis_val", **qline_dict)
        self.wis_mod = create_qline_edit("attr_wis_mod", **qline_dict)
        self.wis_temp_val = create_qline_edit("attr_wis_temp_val", **qline_dict)
        self.wis_temp_mod = create_qline_edit("attr_wis_temp_mod", **qline_dict)

        self.cha_val = create_qline_edit("attr_cha_val", **qline_dict)
        self.cha_mod = create_qline_edit("attr_cha_mod", **qline_dict)
        self.cha_temp_val = create_qline_edit("attr_cha_temp_val", **qline_dict)
        self.cha_temp_mod = create_qline_edit("attr_cha_temp_mod", **qline_dict)

        self.add_to_layout()
        self.translate()
        self.set_default_values()

    def add_to_layout(self):
        header = [self.head_name, self.head_val, self.head_mod,
                  self.head_temp_val, self.head_temp_mod]
        add_to_box_layout_by_row(self.layout, header)

        attrs = ('str', 'dex', 'con', 'int', 'wis', 'cha')
        stats_column = [getattr(self, f'{x}_label') for x in attrs]
        add_to_box_layout_by_column(self.layout, stats_column, start_row=1)

        elements = [lambda x: f'{x}_val', lambda x: f'{x}_mod',
                    lambda x: f'{x}_temp_val', lambda x: f'{x}_temp_mod']
        attributes_lines = [[getattr(self, e(attr)) for e in elements] for attr in attrs]
        for idx, attribute_line in enumerate(attributes_lines):
            add_to_box_layout_by_row(self.layout, attribute_line, row=idx + 1, start_column=1)

    def translate(self):
        _translate = QtCore.QCoreApplication.translate
        self.root.setTitle(_translate("MainWindow", "Attributes"))

        self.head_name.setText(_translate("MainWindow", "Atrribute"))
        self.head_val.setText(_translate("MainWindow", "Value"))
        self.head_mod.setText(_translate("MainWindow", "Mod"))
        self.head_temp_val.setText(_translate("MainWindow", "Temp val"))
        self.head_temp_mod.setText(_translate("MainWindow", "Temp mod"))

        self.int_label.setText(_translate("MainWindow", "INT"))
        self.dex_label.setText(_translate("MainWindow", "DEX"))
        self.con_label.setText(_translate("MainWindow", "CON"))
        self.wis_label.setText(_translate("MainWindow", "WIS"))
        self.str_label.setText(_translate("MainWindow", "STR"))
        self.cha_label.setText(_translate("MainWindow", "CHA"))

    def set_default_values(self):
        self.str_val.setText("10")
        self.dex_val.setText("10")
        self.int_temp_mod.setText("10")
        self.con_temp_mod.setText("10")
        self.con_val.setText("10")
        self.con_mod.setText("10")
        self.con_temp_val.setText("10")
        self.wis_mod.setText("10")
        self.wis_temp_mod.setText("10")
        self.wis_temp_val.setText("10")
        self.dex_mod.setText("10")
        self.dex_temp_val.setText("10")
        self.dex_temp_mod.setText("10")
        self.wis_val.setText("10")
        self.int_temp_val.setText("10")
        self.int_mod.setText("10")
        self.int_val.setText("10")
        self.str_temp_mod.setText("10")
        self.str_mod.setText("10")
        self.str_temp_val.setText("10")
        self.cha_val.setText("10")
        self.cha_mod.setText("10")
        self.cha_temp_val.setText("10")
        self.cha_temp_mod.setText("10")
