from PyQt5 import QtCore

from core.character import Character
from gui.frames.qt_generic_classes import DefaultBox, BoxType
from gui.frames.qt_generic_functions import create_qlabel, create_qline_edit, update_texts, \
    add_multiple_elements_to_layout_by_row, set_text_of_children


class SavingThrowsBox(BoxType, DefaultBox):
    char_core: Character
    def __init__(self, parent, position, size, char_core):
        self.char_core = char_core
        BoxType.__init__(self, parent=parent, position=position, size=size)
        self.translate_reference = {
            "EN":
                {"total_label": "Total",
                 "class_base_label": "Base",
                 "attr_bonus_label": "Attr",
                 "size_bonus_label": "Size",
                 "misc_bonus_label": "Misc",
                 "fortitude_label": "Fortitude",
                 "reflex_label": "Reflex",
                 "will_label": "Will"}}
        qlabel_dict = dict(parent=self.container)
        qlabel_dict_centered = dict(parent=self.container, align=QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        qline_dict_disabled = dict(parent=self.container, min_size=(15, 23), enabled=False)
        qline_update_fortitude = dict(parent=self.container, min_size=(15, 23),
                                      function_on_text_changed=self._update_fortitude_text)
        qline_update_reflex = dict(parent=self.container, min_size=(15, 23),
                                   function_on_text_changed=self._update_reflex_text)
        qline_update_will = dict(parent=self.container, min_size=(15, 23),
                                 function_on_text_changed=self._update_will_text)

        self.fortitude_total = create_qline_edit(str_format="{:+d}", **qline_dict_disabled)
        self.fortitude_class_bonus = create_qline_edit(**qline_update_fortitude)
        self.fortitude_attr_bonus = create_qline_edit(**qline_dict_disabled)
        self.fortitude_size_bonus = create_qline_edit(**qline_update_fortitude)
        self.fortitude_misc_bonus = create_qline_edit(**qline_update_fortitude)

        self.reflex_total = create_qline_edit(str_format="{:+d}", **qline_dict_disabled)
        self.reflex_class_bonus = create_qline_edit(**qline_update_reflex)
        self.reflex_attr_bonus = create_qline_edit(**qline_dict_disabled)
        self.reflex_size_bonus = create_qline_edit(**qline_update_reflex)
        self.reflex_misc_bonus = create_qline_edit(**qline_update_reflex)

        self.will_total = create_qline_edit(str_format="{:+d}", **qline_dict_disabled)
        self.will_class_bonus = create_qline_edit(**qline_update_will)
        self.will_attr_bonus = create_qline_edit(**qline_dict_disabled)
        self.will_size_bonus = create_qline_edit(**qline_update_will)
        self.will_misc_bonus = create_qline_edit(**qline_update_will)

        self.fortitude_label = create_qlabel(align=QtCore.Qt.AlignRight, **qlabel_dict)
        self.reflex_label = create_qlabel(align=QtCore.Qt.AlignRight, **qlabel_dict)
        self.will_label = create_qlabel(align=QtCore.Qt.AlignRight, **qlabel_dict)

        self.total_label = create_qlabel(**qlabel_dict_centered)
        self.class_base_label = create_qlabel(**qlabel_dict_centered)
        self.attr_bonus_label = create_qlabel(**qlabel_dict_centered)
        self.size_bonus_label = create_qlabel(**qlabel_dict_centered)
        self.misc_bonus_label = create_qlabel(**qlabel_dict_centered)

        self.add_to_layout()
        self.translate("EN")
        self.set_values_from_attributes()

    def add_to_layout(self):
        first_row = [self.total_label, self.class_base_label, self.attr_bonus_label, self.size_bonus_label,
                     self.misc_bonus_label]
        add_multiple_elements_to_layout_by_row(self.layout, first_row, start_column=1)

        second_row = [self.fortitude_label, self.fortitude_total, self.fortitude_class_bonus, self.fortitude_attr_bonus,
                      self.fortitude_size_bonus, self.fortitude_misc_bonus]
        add_multiple_elements_to_layout_by_row(self.layout, second_row, row=1)

        third_row = [self.reflex_label, self.reflex_total, self.reflex_class_bonus, self.reflex_attr_bonus,
                     self.reflex_size_bonus, self.reflex_misc_bonus]
        add_multiple_elements_to_layout_by_row(self.layout, third_row, row=2)

        fourth_row = [self.will_label, self.will_total, self.will_class_bonus, self.will_attr_bonus,
                      self.will_size_bonus, self.will_misc_bonus]
        add_multiple_elements_to_layout_by_row(self.layout, fourth_row, row=3)

    def translate(self, language):
        set_text_of_children(self, self.translate_reference[language])

    def set_values_from_attributes(self):
        self.reflex_attr_bonus.setText(str(self.char_core.attributes.dex['mod']))
        self.will_attr_bonus.setText(str(self.char_core.attributes.wis['mod']))
        self.fortitude_attr_bonus.setText(str(self.char_core.attributes.con['mod']))
        self.update_saving_throws_texts()

    def update_saving_throws_texts(self):
        self._update_fortitude_text()
        self._update_reflex_text()
        self._update_will_text()

    def _update_fortitude_text(self):
        update_texts(self, to_set="fortitude_total", to_get_from=["fortitude_class_bonus", "fortitude_attr_bonus",
                                                                  "fortitude_size_bonus", "fortitude_misc_bonus"])

    def _update_reflex_text(self):
        update_texts(self, to_set="reflex_total", to_get_from=["reflex_class_bonus", "reflex_attr_bonus",
                                                               "reflex_size_bonus", "reflex_misc_bonus"])

    def _update_will_text(self):
        update_texts(self, to_set="will_total", to_get_from=["will_class_bonus", "will_attr_bonus",
                                                             "will_size_bonus", "will_misc_bonus"])
