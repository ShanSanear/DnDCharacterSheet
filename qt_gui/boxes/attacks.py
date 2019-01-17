from PyQt5 import QtWidgets, QtCore

from qt_gui.boxes.qt_generic_classes import DefaultBox
from qt_gui.boxes.qt_generic_functions import create_qline_edit, create_qlabel, add_multiple_elements_to_layout_by_row, \
    set_text_of_children


class AttacksBox(DefaultBox):
    def __init__(self, parent, position, size):
        self.root = QtWidgets.QGroupBox(parent)
        self.root.setGeometry(QtCore.QRect(*position, *size))
        self.root.setObjectName("AttacksBox")
        self.container = QtWidgets.QWidget(self.root)
        self.container.setObjectName("layoutWidget1")
        self.layout = QtWidgets.QGridLayout(self.container)
        self.layout.setObjectName("AttacksLayout")
        self.translate_reference = {
            "EN":
                {
                    "total_label": "Total",
                    "base_label": "Base",
                    "attr_mod_label": "Attr mod",
                    "size_label": "Size",
                    "misc_label": "Misc",
                    "melee_label": "Melee",
                    "ranged_label": "Ranged",
                }
        }
        qline_dict = dict(parent=self.container, )  # min_size=(39, 23), max_size=(167, 20))
        qlabel_dict = dict(parent=self.container, )  # min_size=(39, 17), max_size=(16777215, 20))
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
        self.translate("EN")
        self.set_signs_labels()
        self.set_default_values()
        self.root.setLayout(self.layout)

    def add_to_layout(self):
        # TODO not sure how to change those to fit some kind of pattern, if at all
        self.layout.addWidget(self.total_label, 0, 1, 1, 1)
        self.layout.addWidget(self.base_label, 0, 3, 1, 1)
        self.layout.addWidget(self.attr_mod_label, 0, 5, 1, 1)
        self.layout.addWidget(self.size_label, 0, 7, 1, 1)
        self.layout.addWidget(self.misc_label, 0, 9, 1, 1)

        first_row = [self.melee_label,
                     self.melee_total,
                     self._eq_sign,
                     self.melee_base,
                     self._plus_sign_16,
                     self.melee_attr_mod,
                     self._plus_sign_17,
                     self.melee_size,
                     self._plus_sign_18,
                     self.melee_misc, ]

        second_row = [self.ranged_label,
                      self.ranged_total,
                      self._eq_sign_2,
                      self.ranged_base,
                      self._plus_sign_19,
                      self.ranged_attr_mod,
                      self._plus_sign_20,
                      self.ranged_size,
                      self._plus_sign_21,
                      self.ranged_misc, ]

        add_multiple_elements_to_layout_by_row(self.layout, first_row, row=1)
        add_multiple_elements_to_layout_by_row(self.layout, second_row, row=2)

    def translate(self, language_ref):
        set_text_of_children(self, self.translate_reference[language_ref])

    def set_signs_labels(self):
        # TODO not sure how to bite this one
        self._eq_sign.setText("=")
        self._plus_sign_16.setText("+")
        self._plus_sign_17.setText("+")
        self._plus_sign_18.setText("+")
        self._eq_sign_2.setText("=")
        self._plus_sign_19.setText("+")
        self._plus_sign_20.setText("+")
        self._plus_sign_21.setText("+")

    def set_default_values(self):
        defaults = {"melee_total": "10",
                    "melee_base": "10",
                    "melee_attr_mod": "10",
                    "melee_size": "10",
                    "melee_misc": "10",
                    "ranged_total": "10",
                    "ranged_base": "10",
                    "ranged_attr_mod": "10",
                    "ranged_size": "10",
                    "ranged_misc": "10", }
        set_text_of_children(self, defaults)
        self.root.setTitle("Attacks")
