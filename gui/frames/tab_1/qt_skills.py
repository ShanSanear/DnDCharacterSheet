import logging
from types import SimpleNamespace

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication

from core.character import Character
from gui.frames.qt_generic_classes import ScrollableBox
from gui.frames.qt_generic_functions import create_combo_box, create_qline_edit, create_qlabel, \
    add_multiple_elements_to_layout_by_row, update_texts, create_push_button, create_checkbox, get_float_from_widget


class SkillsBox(ScrollableBox):
    char_core: Character

    def __init__(self, parent, position, size, char_core):
        base_size = [size[0], 110]
        height_increment = 29
        max_height = size[1]
        ScrollableBox.__init__(self, parent=parent, position=position, base_size=base_size, max_height=max_height,
                               original_size=size,
                               height_increment=height_increment, row_offset=1, last_row_column=7)
        self._map_choice_to_attr = {0: "str", 1: "dex", 2: "con", 3: "int", 4: "wis", 5: "cha"}

        self.char_core = char_core
        self.add_new = create_push_button("add_new_feat", self.container, min_size=[20, 20], max_size=[20, 20], text="+")
        self.skill_name_label = create_qlabel(self.container, max_size=(69, None))
        self.attr_choice_label = create_qlabel(self.container, align=QtCore.Qt.AlignCenter,
                                               max_size=(69, None))
        self.total_label = create_qlabel(self.container, align=QtCore.Qt.AlignCenter,
                                         max_size=(69, None))
        self.attr_mod_label = create_qlabel(self.container, align=QtCore.Qt.AlignCenter,
                                            max_size=(69, None))
        self.rank_label = create_qlabel(self.container, align=QtCore.Qt.AlignCenter,
                                        max_size=(69, None))
        self.misc_label = create_qlabel(self.container, align=QtCore.Qt.AlignCenter,
                                        max_size=(69, None))
        self.cross_class_label = create_qlabel(self.container, align=QtCore.Qt.AlignCenter,
                                               max_size=(69, None))
        self.used_skill_points_label = create_qlabel(self.container,
                                                     align=QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter, )
        self.total_rank_calc = create_qline_edit(self.container, enabled=False,
                                                 align=QtCore.Qt.AlignCenter, max_size=[30, None], is_float=True)
        self.labels = [self.skill_name_label, self.attr_choice_label, self.total_label, self.attr_mod_label,
                       self.rank_label, self.misc_label, self.cross_class_label, ]
        self.last_row = [self.add_new, self.used_skill_points_label, self.total_rank_calc]
        self.add_to_layout()
        self.add_skill = self.add_new_element
        self.add_new.clicked.connect(self.add_skill)
        self.add_skill()

        self.add_to_layout()
        self.set_values_from_attributes()


    def create_new_skill(self):
        new_skill = SimpleNamespace()
        new_skill.name = create_qline_edit(self.container, min_size=(150, None),
                                           function_on_unfocused=self.sort_elements)
        new_skill.attr_choice = create_combo_box(parent=self.container,
                                                 number_of_choices=6,
                                                 choices_text=("STR", "DEX", "CON", "INT", "WIS", "CHA"),
                                                 function_on_index_changed=self._set_attr_val_for_skill,
                                                 args_on_index_changed=[new_skill], max_size=(69, None), )

        qdict = dict(parent=self.container, align=QtCore.Qt.AlignCenter, max_size=[30, None], min_size=[None, 23])
        new_skill.total = create_qline_edit(enabled=False, str_format="{:+d}", **qdict)
        new_skill.attr_mod = create_qline_edit(**qdict, enabled=False)
        new_skill.rank = create_qline_edit(function_on_text_changed=self._update_skill,
                                           args_on_text_changed=[new_skill], **qdict)

        new_skill.misc_mod = create_qline_edit(function_on_text_changed=self._update_skill,
                                               args_on_text_changed=[new_skill], **qdict)

        new_skill.cross_class_checkbox = create_checkbox(self.container, function_on_toggle=self.calculate_ranks)
        new_skill.delete_skill = create_push_button("item_delete", self.container, min_size=[20, 20],
                                                    max_size=[20, 20], text="-",
                                                    function_on_clicked=self._remove_element, args_on_clicked=new_skill)

        return new_skill

    def create_new_element(self):
        self.increase_height()
        return self.create_new_skill()


    def add_to_layout(self):
        add_multiple_elements_to_layout_by_row(self.layout, self.labels)


    def calculate_ranks(self):
        total_ranks = 0
        for skill in self.elements_list:
            rank_value = get_float_from_widget(skill.rank, 0)
            if skill.cross_class_checkbox.isChecked():
                rank_value *= 2
            total_ranks += rank_value
        logging.debug("Total ranks: %d", total_ranks)
        self.total_rank_calc.setText(str(total_ranks))

    def add_last_row(self):
        self.layout.addWidget(self.add_new, len(self.elements_list) + 1, self.last_row_column, 1, 1)
        self.layout.addWidget(self.used_skill_points_label, len(self.elements_list) + 1, 1, 1, 3)
        self.layout.addWidget(self.total_rank_calc, len(self.elements_list) + 1, 4, 1, 1)

    def set_values_from_attributes(self):
        for skill in self.elements_list:
            self._set_attr_val_for_skill(skill)

    def _set_attr_val_for_skill(self, skill):
        chosen_attr_idx = skill.attr_choice.currentIndex()
        attr_name = self._map_choice_to_attr[chosen_attr_idx]
        attr_ref_core = getattr(self.char_core.attributes, attr_name)
        skill.attr_mod.setText(str(attr_ref_core['mod']))
        self._update_skill(skill)

    def _update_skill(self, skill):
        update_texts(skill, to_set="total", to_get_from=["attr_mod", "rank", "misc_mod"],
                     with_decimal_point=True)
        self.calculate_ranks()

    def retranslate(self):
        self.root.setTitle(QApplication.translate("Skills", "Skills"))
        self.cross_class_label.setText(QApplication.translate("Skills", "CC"))
        self.rank_label.setText(QApplication.translate("Skills", "Rank"))
        self.attr_mod_label.setText(QApplication.translate("Skills", "Mod"))
        self.misc_label.setText(QApplication.translate("Skills", "Misc"))
        self.skill_name_label.setText(QApplication.translate("Skills", "Skill name"))
        self.attr_choice_label.setText(QApplication.translate("Skills", "Attr"))
        self.total_label.setText(QApplication.translate("Skills", "Total"))
        self.used_skill_points_label.setText(QApplication.translate("Skills", "Used skill points:"))
        for skill in self.elements_list:
            for idx, attr_name in enumerate(("STR", "DEX", "CON", "INT", "WIS", "CHA")):
                skill.attr_choice.setItemText(idx, QApplication.translate("Attributes", attr_name))
