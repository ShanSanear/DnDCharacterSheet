from PyQt5 import QtWidgets, QtCore

from gui.boxes.qt_generic_classes import DefaultBox
from gui.boxes.qt_generic_functions import create_qline_edit, create_qlabel, add_multiple_elements_to_layout_by_row, \
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
        self.layout.setSpacing(10)
        self.layout.setContentsMargins(20, 10, 10, 20)
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
        qline_dict = dict(parent=self.container, )
        qline_dict_attr = dict(parent=self.container, enabled=False)
        qlabel_dict = dict(parent=self.container, )

        self.total_label = create_qlabel("attacks_total_label", **qlabel_dict)
        self.base_label = create_qlabel("attacks_base_label", **qlabel_dict)
        self.attr_mod_label = create_qlabel("attacks_attr_mod_label", **qlabel_dict)
        self.size_label = create_qlabel("attacks_size_label", **qlabel_dict)
        self.misc_label = create_qlabel("attacks_misc_label", **qlabel_dict)
        self.melee_label = create_qlabel("attacks_melee_label", **qlabel_dict)
        self.ranged_label = create_qlabel("attacks_ranged_label", **qlabel_dict)

        self.melee_total = create_qline_edit("attacks_melee_total", **qline_dict)
        self.melee_base = create_qline_edit("attacks_melee_base", **qline_dict)
        self.melee_attr_mod = create_qline_edit("attacks_melee_attr_mod", **qline_dict_attr)
        self.melee_size = create_qline_edit("attacks_melee_size", **qline_dict)
        self.melee_misc = create_qline_edit("attacks_melee_misc", **qline_dict)

        self.ranged_total = create_qline_edit("attacks_ranged_total", **qline_dict)
        self.ranged_base = create_qline_edit("attacks_ranged_base", **qline_dict)
        self.ranged_attr_mod = create_qline_edit("attacks_ranged_attr_mod", **qline_dict_attr)
        self.ranged_size = create_qline_edit("attacks_ranged_size", **qline_dict)
        self.ranged_misc = create_qline_edit("attacks_ranged_misc", **qline_dict)

        self.add_to_layout()
        self.translate("EN")
        self.set_default_values()
        self.root.setLayout(self.layout)

    def add_to_layout(self):
        # TODO not sure how to change those to fit some kind of pattern, if at all
        self.layout.addWidget(self.total_label, 0, 1, 1, 1)
        self.layout.addWidget(self.base_label, 0, 2, 1, 1)
        self.layout.addWidget(self.attr_mod_label, 0, 3, 1, 1)
        self.layout.addWidget(self.size_label, 0, 4, 1, 1)
        self.layout.addWidget(self.misc_label, 0, 5, 1, 1)

        first_row = [self.melee_label,
                     self.melee_total,
                     self.melee_base,
                     self.melee_attr_mod,
                     self.melee_size,
                     self.melee_misc, ]

        second_row = [self.ranged_label,
                      self.ranged_total,
                      self.ranged_base,
                      self.ranged_attr_mod,
                      self.ranged_size,
                      self.ranged_misc, ]

        add_multiple_elements_to_layout_by_row(self.layout, first_row, row=1)
        add_multiple_elements_to_layout_by_row(self.layout, second_row, row=2)

    def translate(self, language_ref):
        set_text_of_children(self, self.translate_reference[language_ref])

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
