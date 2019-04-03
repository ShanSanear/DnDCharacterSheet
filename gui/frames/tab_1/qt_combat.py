from PyQt5 import QtCore

from core.character import Character
from gui.frames.qt_generic_classes import DefaultBox, BoxType
from gui.frames.qt_generic_functions import create_qline_edit, create_qlabel, add_multiple_elements_to_layout_by_row, \
    set_text_of_children, update_texts


class CombatBox(BoxType, DefaultBox):
    char_core: Character

    def __init__(self, parent, position, size, char_core):
        self.char_core = char_core
        BoxType.__init__(self, parent=parent, position=position, size=size)
        self.translate_reference = {
            "EN":
                {
                    "root": {
                        "title": "Combat"
                    },
                    "total_label": "Total",
                    "base_label": "Base",
                    "attr_mod_label": "Attr mod",
                    "size_label": "Size",
                    "misc_label": "Misc",
                    "melee_label": "Melee",
                    "ranged_label": "Ranged",
                    "initiative_misc_bonus_label": "Misc",
                    "initiative_dex_bonus_label": "Dex",
                    "initiative_label": "Initiative",
                    "speed_label": "Speed",
                    "total_label_init": "Total",
                    "attacks_type_label": "Type",
                }
        }
        qline_dict_disabled = dict(parent=self.container, enabled=False)
        qline_dict_ranged = dict(parent=self.container, function_on_text_changed=self._update_ranged_attack)
        qline_dict_melee = dict(parent=self.container, function_on_text_changed=self._update_melee_attack)
        qlabel_dict = dict(parent=self.container, )
        qlabel_dict_centered = dict(parent=self.container, align=QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        qline_update = dict(parent=self.container, function_on_text_changed=self._update_initiative)

        self.attacks_type_label = create_qlabel(**qlabel_dict_centered)
        self.total_label = create_qlabel(**qlabel_dict_centered)
        self.base_label = create_qlabel(**qlabel_dict_centered)
        self.attr_mod_label = create_qlabel(**qlabel_dict_centered)
        self.size_label = create_qlabel(**qlabel_dict_centered)
        self.misc_label = create_qlabel(**qlabel_dict_centered)
        self.melee_label = create_qlabel(align=QtCore.Qt.AlignRight, **qlabel_dict)
        self.ranged_label = create_qlabel(align=QtCore.Qt.AlignRight, **qlabel_dict)

        self.melee_total = create_qline_edit(str_format="{:+d}", **qline_dict_disabled)
        self.melee_base = create_qline_edit(**qline_dict_melee)
        self.melee_attr_mod = create_qline_edit(**qline_dict_disabled)
        self.melee_size = create_qline_edit(**qline_dict_melee)
        self.melee_misc = create_qline_edit(**qline_dict_melee)

        self.ranged_total = create_qline_edit(str_format="{:+d}", **qline_dict_disabled)
        self.ranged_base = create_qline_edit(**qline_dict_ranged)
        self.ranged_attr_mod = create_qline_edit(**qline_dict_disabled)
        self.ranged_size = create_qline_edit(**qline_dict_ranged)
        self.ranged_misc = create_qline_edit(**qline_dict_ranged)

        self.total_label_init = create_qlabel(**qlabel_dict_centered)
        self.initiative_misc_bonus_label = create_qlabel(**qlabel_dict_centered)
        self.initiative_dex_bonus_label = create_qlabel(**qlabel_dict_centered)
        self.initiative_label = create_qlabel(align=QtCore.Qt.AlignRight, parent=self.container)
        self.speed_label = create_qlabel(align=QtCore.Qt.AlignRight, parent=self.container)

        self.initiative_total = create_qline_edit(parent=self.container, str_format="{:+d}",
                                                  enabled=False)
        self.initiative_misc_bonus = create_qline_edit(**qline_update)
        self.initiative_dex_bonus = create_qline_edit(parent=self.container, enabled=False)
        self.speed_total = create_qline_edit(parent=self.container)

        self.labels = [self.attacks_type_label, self.total_label, self.base_label, self.attr_mod_label,
                       self.size_label, self.misc_label]

        self.add_to_layout()
        self.translate("EN")
        self.set_values_from_attributes()

    def add_to_layout(self):
        add_multiple_elements_to_layout_by_row(self.layout, self.labels)

        first_row = [self.melee_label, self.melee_total, self.melee_base, self.melee_attr_mod, self.melee_size,
                     self.melee_misc, ]
        add_multiple_elements_to_layout_by_row(self.layout, first_row, row=1)

        second_row = [self.ranged_label, self.ranged_total, self.ranged_base, self.ranged_attr_mod, self.ranged_size,
                      self.ranged_misc, ]
        add_multiple_elements_to_layout_by_row(self.layout, second_row, row=2)

        third_row = [self.total_label_init, self.initiative_dex_bonus_label, self.initiative_misc_bonus_label]
        add_multiple_elements_to_layout_by_row(self.layout, third_row, row=3, start_column=1)

        fourth_row = [self.initiative_label, self.initiative_total, self.initiative_dex_bonus,
                      self.initiative_misc_bonus]
        add_multiple_elements_to_layout_by_row(self.layout, fourth_row, row=4)

        fith_row = [self.speed_label, self.speed_total]
        add_multiple_elements_to_layout_by_row(self.layout, fith_row, row=5)

    def translate(self, language):
        set_text_of_children(self, self.translate_reference[language])

    def set_values_from_attributes(self):
        self.melee_attr_mod.setText(str(self.char_core.attributes.str['mod']))
        self.ranged_attr_mod.setText(str(self.char_core.attributes.dex['mod']))
        self._update_melee_attack()
        self._update_ranged_attack()
        self.initiative_dex_bonus.setText(str(self.char_core.attributes.dex['mod']))
        self._update_initiative()

    def _update_ranged_attack(self):
        update_texts(root_object=self, to_set="ranged_total",
                     to_get_from=["ranged_base", "ranged_attr_mod", "ranged_size", "ranged_misc"])

    def _update_melee_attack(self):
        update_texts(root_object=self, to_set="melee_total",
                     to_get_from=["melee_base", "melee_attr_mod", "melee_size", "melee_misc"])

    def _update_initiative(self):
        update_texts(root_object=self, to_set="initiative_total",
                     to_get_from=["initiative_misc_bonus", "initiative_dex_bonus"])
