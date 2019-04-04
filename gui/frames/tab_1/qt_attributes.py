from types import SimpleNamespace

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication

from core.character import Character
from gui.frames.qt_generic_classes import DefaultBox, BoxType
from gui.frames.qt_generic_functions import create_qlabel, create_qline_edit, add_multiple_elements_to_layout_by_row


class AttributesBox(BoxType, DefaultBox):
    char_core: Character

    def __init__(self, parent, position, size, char_core):
        self.char_core = char_core
        BoxType.__init__(self, parent=parent, position=position, size=size)
        self.attrs_names = ('str', 'dex', 'con', 'int', 'wis', 'cha')
        self.attrs_references = []
        self.head = SimpleNamespace()

        for attr in self.attrs_names:
            setattr(self, attr, SimpleNamespace())
            self.attrs_references.append(getattr(self, attr))

        self.qlabel_dict = dict(parent=self.container,
                                align=QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter,
                                )
        self.qlabel_header_dict = dict(parent=self.container, align=QtCore.Qt.AlignCenter, )
        self.qline_dict = dict(parent=self.container, )
        self.qline_dict_mod = dict(parent=self.container, str_format="{:+d}", enabled=False)

        self.generate_head_labels()
        self.generate_attributes_elements()
        self.add_to_layout()
        self.set_values_from_attributes()

    def generate_head_labels(self):
        elements = ['label', 'val', 'mod', 'temp_val', 'temp_mod']
        for element in elements:
            setattr(self.head, element, create_qlabel(**self.qlabel_header_dict))

    def generate_attributes_elements(self):
        for attr_reference, attr_name in zip(self.attrs_references, self.attrs_names):
            self._generate_attribute_elemenets(attr_reference, attr_name)

    def _generate_attribute_elemenets(self, attr_reference, attr_name):
        elements = ['label', 'val', 'mod', 'temp_val', 'temp_mod']
        for element in elements[1:]:
            if "mod" in element:
                setattr(attr_reference, element,
                        create_qline_edit(**self.qline_dict_mod))
            else:
                setattr(attr_reference, element, create_qline_edit(**self.qline_dict))
        setattr(attr_reference, 'label', create_qlabel(**self.qlabel_dict))

    def add_to_layout(self):
        elements = ['label', 'val', 'mod', 'temp_val', 'temp_mod']
        add_multiple_elements_to_layout_by_row(self.layout, [getattr(self.head, element) for element in elements])

        attributes_elements = [[getattr(attr, element) for element in elements] for attr in self.attrs_references]
        for idx, attribute_row in enumerate(attributes_elements):
            add_multiple_elements_to_layout_by_row(self.layout, attribute_row, row=idx + 1)

    def set_values_from_attributes(self):
        for attr in self.attrs_names:
            attr_core = getattr(self.char_core.attributes, attr)
            attr_gui = getattr(self, attr)
            attr_gui.val.setText(str(attr_core['value']))
            attr_gui.mod.setText(str(attr_core['mod']))

    def retranslate(self):
        self.root.setTitle(QApplication.translate("Attributes", "Attributes"))
        self.head.label.setText(QApplication.translate("Attributes", "Attr"))
        self.head.val.setText(QApplication.translate("Attributes", "Val"))
        self.head.mod.setText(QApplication.translate("Attributes", "Mod"))
        self.head.temp_val.setText(QApplication.translate("Attributes", "T. Val"))
        self.head.temp_mod.setText(QApplication.translate("Attributes", "T. Mod"))
        self.str.label.setText(QApplication.translate("Attributes", "STR"))
        self.dex.label.setText(QApplication.translate("Attributes", "DEX"))
        self.con.label.setText(QApplication.translate("Attributes", "CON"))
        self.int.label.setText(QApplication.translate("Attributes", "INT"))
        self.wis.label.setText(QApplication.translate("Attributes", "WIS"))
        self.cha.label.setText(QApplication.translate("Attributes", "CHA"))
