from PyQt5 import QtCore

from core.character import Character
from gui.frames.qt_generic_classes import DefaultBox, BoxType
from gui.frames.qt_generic_functions import create_qline_edit, create_qlabel, add_multiple_elements_to_layout_by_row, \
    set_text_of_children


class WeaponStatisticsBox(BoxType, DefaultBox):
    char_core: Character

    def __init__(self, parent, position, size, char_core):
        self.char_core = char_core
        BoxType.__init__(self, parent=parent, position=position, size=size)
        self.bonus_from_melee = 0
        self.bonus_from_ranged = 0
        self.translate_reference = {
            "EN":
                {
                    "root": {"title": "Current weapon statistics"},
                    "attack_bonus_label": "Att. bonus", "damage_label": "Dmg",
                    "range_label": "Range", "melee_range": "1 m", "crit_label": "Crit",
                    "melee_label": "Melee", "ranged_label": "Ranged",
                    "weapon_name_label": "Weapon name"}}
        qline_dict = dict(parent=self.container, enabled=False)
        qlabel_dict = dict(parent=self.container)
        qlabel_dict_centered = dict(parent=self.container, align=QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)

        self.weapon_name_label = create_qlabel(**qlabel_dict)
        self.attack_bonus_label = create_qlabel(**qlabel_dict_centered)
        self.damage_label = create_qlabel(**qlabel_dict_centered)
        self.crit_label = create_qlabel(**qlabel_dict_centered)
        self.range_label = create_qlabel(**qlabel_dict_centered)

        self.melee_label = create_qlabel(align=QtCore.Qt.AlignRight, **qlabel_dict)
        self.melee_name = create_qline_edit(min_size=[90, None],
                                            parent=self.container, enabled=False)
        self.melee_attack_bonus = create_qline_edit(max_size=[50, None],
                                                    str_format="{:+d}", **qline_dict)
        self.melee_damage = create_qline_edit(max_size=[60, None], **qline_dict)
        self.melee_crit = create_qline_edit(parent=self.container, max_size=[60, None],
                                            min_size=[50, None], enabled=False)
        self.melee_range = create_qline_edit(parent=self.container,
                                             max_size=[50, None],
                                             enabled=False)

        self.ranged_label = create_qlabel(align=QtCore.Qt.AlignRight, **qlabel_dict)
        self.ranged_name = create_qline_edit(min_size=[90, None],
                                             parent=self.container, enabled=False)
        self.ranged_attack_bonus = create_qline_edit(max_size=[50, None],
                                                     str_format="{:+d}", **qline_dict)
        self.ranged_damage = create_qline_edit(max_size=[60, None], **qline_dict)
        self.ranged_crit = create_qline_edit(parent=self.container, max_size=[60, None],
                                             min_size=[50, None], enabled=False)
        self.ranged_range = create_qline_edit(parent=self.container, max_size=[50, None],
                                              enabled=False)

        self.add_to_layout()
        self.translate("EN")

    def add_to_layout(self):
        first_row = [self.weapon_name_label, self.attack_bonus_label, self.damage_label, self.crit_label,
                     self.range_label]
        add_multiple_elements_to_layout_by_row(layout=self.layout, elements_to_add=first_row, start_column=1)

        second_row = [self.melee_label, self.melee_name, self.melee_attack_bonus, self.melee_damage, self.melee_crit,
                      self.melee_range]
        add_multiple_elements_to_layout_by_row(layout=self.layout, elements_to_add=second_row, row=1)

        third_row = [self.ranged_label, self.ranged_name, self.ranged_attack_bonus, self.ranged_damage,
                     self.ranged_crit,
                     self.ranged_range]
        add_multiple_elements_to_layout_by_row(layout=self.layout, elements_to_add=third_row, row=2)

    def translate(self, language):
        set_text_of_children(self, self.translate_reference[language])
