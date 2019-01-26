from types import SimpleNamespace

from PyQt5 import QtWidgets, QtCore

from qt_gui.boxes.qt_generic_classes import DefaultBox
from qt_gui.boxes.qt_generic_functions import create_qlabel, create_qline_edit, add_multiple_elements_to_layout_by_row, \
    set_text_of_children


class AttributesBox(DefaultBox):
    def __init__(self, parent, position, size):

        self.root = QtWidgets.QGroupBox(parent)
        self.root.setGeometry(QtCore.QRect(*position, *size))
        self.root.setObjectName("AttributesBox")

        self.container = QtWidgets.QWidget(self.root)
        self.container.setObjectName("gridLayoutWidget")

        self.layout = QtWidgets.QGridLayout(self.container)
        self.layout.setObjectName("AttributesLayout")
        #self.layout.setContentsMargins(8,8,8,8)
        self.layout.setSpacing(10)
        self.layout.setContentsMargins(20, 10, 10, 20)

        self.attrs_names = ('str', 'dex', 'con', 'int', 'wis', 'cha')
        self.attrs_references = []
        self.head = SimpleNamespace()

        self.translate_reference = {
            "EN":
                {
                    "head": {
                        "label": "Attr",
                        "val": "Val",
                        "mod": "Mod",
                        "temp_val": "Tmp val",
                        "temp_mod": "Tmp mod",
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
        for attr in self.attrs_names:
            setattr(self, attr, SimpleNamespace())
            self.attrs_references.append(getattr(self, attr))
        self.elements = ['label', 'val', 'mod', 'temp_val', 'temp_mod']

        self.qlabel_dict = dict(parent=self.container,
                                align=QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter,
                                )
        self.qlabel_header_dict = dict(parent=self.container, align=QtCore.Qt.AlignCenter, )
        self.qline_dict = dict(parent=self.container,)
        self.qline_dict_mod = dict(parent=self.container, enabled=False)

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
            if "mod" in element:
                setattr(attr_reference, element, create_qline_edit(f"attr_{attr_name}_{element}", **self.qline_dict_mod))
            else:
                setattr(attr_reference, element, create_qline_edit(f"attr_{attr_name}_{element}", **self.qline_dict))
        setattr(attr_reference, 'label', create_qlabel(f"attr_{attr_name}_label", **self.qlabel_dict))

    def add_to_layout(self):
        add_multiple_elements_to_layout_by_row(self.layout, [getattr(self.head, element) for element in self.elements])

        attributes_elements = [[getattr(attr, element) for element in self.elements] for attr in self.attrs_references]
        for idx, attribute_row in enumerate(attributes_elements):
            add_multiple_elements_to_layout_by_row(self.layout, attribute_row, row=idx + 1)

    def translate(self, language_ref):
        set_text_of_children(self, self.translate_reference[language_ref])

    def set_default_values(self):
        attr_default = {"val": "10",
                        "mod": "0",
                        "temp_val": "10",
                        "temp_mod": "0", }

        default_attribute_values = dict(str=dict(attr_default), dex=dict(attr_default), con=dict(attr_default),
                                        int=dict(attr_default), wis=dict(attr_default), cha=dict(attr_default), )
        set_text_of_children(self, default_attribute_values)
