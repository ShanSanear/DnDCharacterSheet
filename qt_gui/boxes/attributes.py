from types import SimpleNamespace

from PyQt5 import QtWidgets, QtCore

from qt_gui.boxes.box import DefaultBox
from qt_gui.boxes.qt_generic_functions import create_qlabel, create_qline_edit, add_to_box_layout_by_row, \
    set_text_of_children


class AttributesBox(DefaultBox):
    def __init__(self, centralwidget, position, size):

        self.root = QtWidgets.QGroupBox(centralwidget)
        self.root.setGeometry(QtCore.QRect(*position, *size))
        self.root.setObjectName("AttributesBox")

        self.container = QtWidgets.QWidget(self.root)
        self.container.setObjectName("gridLayoutWidget")

        self.layout = QtWidgets.QGridLayout(self.container)
        # self.layout.setContentsMargins(9, 9, 9, 9)
        # self.layout.setSpacing(6)
        self.layout.setObjectName("AttributesLayout")

        self.attrs_names = ('str', 'dex', 'con', 'int', 'wis', 'cha')
        self.attrs_references = []
        self.head = SimpleNamespace()

        self.translate_reference = {
            "EN":
                {
                    "head": {
                        "label": "Attribute",
                        "val": "Value",
                        "mod": "Mod",
                        "temp_val": "Temp val",
                        "temp_mod": "Temp mod",
                    },
                    "str": {
                        "label": "STR"
                    },
                    "dex": {
                        "label": "DEX"
                    },
                    "con": {
                        "label": "CON"
                    },
                    "int": {
                        "label": "INT"
                    },
                    "wis": {
                        "label": "WIS"
                    },
                    "cha": {
                        "label": "CHA"
                    }
                }
        }
        attr_default = {"val": "10",
                        "mod": "0",
                        "temp_val": "10",
                        "temp_mod": "0", }

        self.default_attribute_values = dict(str=dict(attr_default), dex=dict(attr_default), con=dict(attr_default),
                                             int=dict(attr_default), wis=dict(attr_default), cha=dict(attr_default), )
        for attr in self.attrs_names:
            setattr(self, f"{attr}", SimpleNamespace())
            self.attrs_references.append(getattr(self, f"{attr}"))
        self.elements = ['label', 'val', 'mod', 'temp_val', 'temp_mod']


        self.qlabel_dict = dict(parent=self.container,
                                align=QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter,
                                )
        self.qlabel_header_dict = dict(parent=self.container, align=QtCore.Qt.AlignCenter, )
        self.qline_dict = dict(parent=self.container, min_size=(0, 23), )

        self.generate_head_labels()
        self.generate_attributes_elements()
        self.add_to_layout()
        self.translate("EN")
        self.set_default_values()
        self.root.setTitle("Attributes")
        self.root.setLayout(self.layout)

    def generate_head_labels(self):
        for element in self.elements:
            setattr(self.head, element, create_qlabel(f"attr_head_{element}", **self.qlabel_header_dict))

    def generate_attributes_elements(self):
        for attr_reference, attr_name in zip(self.attrs_references, self.attrs_names):
            self._generate_attribute_elemenets(attr_reference, attr_name)

    def _generate_attribute_elemenets(self, attr_reference, attr_name):
        for element in self.elements[1:]:
            setattr(attr_reference, element, create_qline_edit(f"attr_{attr_name}_{element}", **self.qline_dict))
        setattr(attr_reference, 'label', create_qlabel(f"attr_{attr_name}_label", **self.qlabel_dict))

    def add_to_layout(self):
        add_to_box_layout_by_row(self.layout, [getattr(self.head, element) for element in self.elements])

        attributes_elements = [[getattr(attr, element) for element in self.elements] for attr in self.attrs_references]
        for idx, attribute_row in enumerate(attributes_elements):
            add_to_box_layout_by_row(self.layout, attribute_row, row=idx + 1)

    def translate(self, language_ref):
        set_text_of_children(self, self.translate_reference[language_ref])

    def set_default_values(self):
        set_text_of_children(self, self.default_attribute_values)
