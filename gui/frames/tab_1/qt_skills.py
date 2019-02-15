import logging
from types import SimpleNamespace

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QScrollArea, QSizePolicy, QVBoxLayout

from core.character import Character
from gui.frames.qt_generic_classes import DefaultBox, ResizeableBox
from gui.frames.qt_generic_functions import create_combo_box, create_qline_edit, set_text_of_children, create_qlabel, \
    add_multiple_elements_to_layout_by_row, update_texts, create_push_button, create_checkbox, get_float_from_widget


class SkillsBox(DefaultBox, ResizeableBox):
    char_core: Character

    def __init__(self, parent, position, size, char_core):
        # TODO - scrollbar after achieving certain height

        self.translate_reference = {
            "EN": {
                "root": {
                     "title": "Skills"
                },
                "cross_class_label": "CC",
                "rank_label": "Rank",
                "attr_mod_label": "Mod",
                "misc_label": "Misc",
                "skill_name_label": "Skill name",
                "attr_choice_label": "Attr",
                "total_label": "Total",
                "used_skill_points_label": "Used skill points:"
            }
        }
        self._map_choice_to_attr = {
            0: "str",
            1: "dex",
            2: "con",
            3: "int",
            4: "wis",
            5: "cha",
        }

        self.char_core = char_core
        self.parent = parent
        self.root = QtWidgets.QGroupBox(self.parent)
        self.root.setGeometry(QtCore.QRect(*position, *size))
        self.root.setObjectName("SkillsBox")
        smaller_size = [size[0] * 0.95, size[1] * 0.95]
        self.main_widget = QtWidgets.QWidget(self.parent)
        self.scrollarea = QScrollArea(self.main_widget)
        self.main_widget.setGeometry(QtCore.QRect(*position, *size))
        self.scrollarea.setFixedHeight(smaller_size[1])
        self.scrollarea.setFixedWidth(smaller_size[0])
        self.scrollarea.setWidgetResizable(True)
        self.scrollarea.move(10, 10)
        self.container = QtWidgets.QWidget(self.parent)
        self.container.setGeometry(QtCore.QRect(*position, *smaller_size))
        # self.scrollarea.setAutoFillBackground(False)
        self.container.setObjectName("gridLayoutWidget_5")
        self.layout = QtWidgets.QGridLayout(self.container)
        self.layout.setSpacing(10)
        self.add_new = create_push_button("add_new_feat", self.container, min_size=[20, 20], max_size=[20, 20], text="+")
        self.layout.setObjectName("SkillsLayout")
        self.skills = []
        ResizeableBox.__init__(self, elements_list=self.skills, row_offset=1, increase_width=0, increase_height=28,
                               last_row_column=7)
        self.skill_name_label = create_qlabel("skills_skill_name_label", self.container, max_size=(69, 20))
        self.attr_choice_label = create_qlabel("skills_attr_choice_label", self.container, align=QtCore.Qt.AlignCenter,
                                               max_size=(69, 20))
        self.total_label = create_qlabel("skills_total_label", self.container, align=QtCore.Qt.AlignCenter,
                                         max_size=(69, 20))
        self.attr_mod_label = create_qlabel("skills_attr_mod_label", self.container, align=QtCore.Qt.AlignCenter,
                                            max_size=(69, 20))
        self.rank_label = create_qlabel("skills_rank_label", self.container, align=QtCore.Qt.AlignCenter,
                                        max_size=(69, 20))
        self.misc_label = create_qlabel("skills_misc_label", self.container, align=QtCore.Qt.AlignCenter,
                                        max_size=(69, 20))
        self.cross_class_label = create_qlabel("skills_description_label", self.container, align=QtCore.Qt.AlignCenter,
                                               max_size=(69, 20))
        self.used_skill_points_label = create_qlabel("skills_total_rank_label", self.container,
                                                     align=QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter,
                                                     max_size=(None, 20))
        self.total_rank_calc = create_qline_edit("skills_total_rank_calc", self.container, enabled=False,
                                                 align=QtCore.Qt.AlignCenter, max_size=[30, None], is_float=True)
        self.labels = [self.skill_name_label, self.attr_choice_label, self.total_label, self.attr_mod_label,
                       self.rank_label, self.misc_label, self.cross_class_label, ]
        self.last_row = [self.add_new, self.used_skill_points_label, self.total_rank_calc]
        self.add_to_layout()
        self.add_skill = self.add_new_element
        self.add_new.clicked.connect(self.add_skill)
        for _ in range(15):
            self.add_skill()

        self.add_to_layout()
        self.translate("EN")
        self.set_values_from_attributes()
        self.scrollarea.setWidget(self.container)
        self.layout_All = QVBoxLayout(self.main_widget)
        self.layout_All.addWidget(self.scrollarea)

    def update_size(self):
        pass

    def create_new_skill(self):
        new_skill = SimpleNamespace()
        skill_idx = len(self.skills)
        new_skill.name = create_qline_edit(f"skills{skill_idx}skill_name", self.container,
                                                 min_size=(150, None), function_on_unfocused=self.sort_elements)
        new_skill.name.setText(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
            "Praesent sapien urna, egestas eu tempor at, pretium nec orci.")
        new_skill.attr_choice = create_combo_box(name=f"skills{skill_idx}attr_choice", parent=self.container,
                                                 number_of_choices=6,
                                                 choices_text=("STR", "DEX", "CON", "INT", "WIS", "CHA"),
                                                 function_on_index_changed=self._set_attr_val_for_skill,
                                                 args_on_index_changed=[new_skill], max_size=(69, 20), )

        qdict = dict(parent=self.container, align=QtCore.Qt.AlignCenter, max_size=[30, None], )
        new_skill.total = create_qline_edit(f"skills{skill_idx}total", enabled=False, str_format="{:+d}", **qdict)
        new_skill.attr_mod = create_qline_edit(f"skills{skill_idx}attr_mod", **qdict, enabled=False)
        new_skill.rank = create_qline_edit(f"skills{skill_idx}rank", function_on_text_changed=self._update_skill,
                                           args_on_text_changed=[new_skill], **qdict)

        new_skill.misc_mod = create_qline_edit(f"skills_{skill_idx}_misc_mod",
                                               function_on_text_changed=self._update_skill,
                                               args_on_text_changed=[new_skill], **qdict)

        new_skill.cross_class_checkbox = create_checkbox(f"skills{skill_idx}description_button", self.container,
                                                         function_on_toggle=self.calculate_ranks)
        new_skill.delete_skill = create_push_button("item_delete", self.container, min_size=[20, 20],
                                                    max_size=[20, 20], text="-",
                                                    function_on_clicked=self._remove_element, args_on_clicked=new_skill)

        return new_skill

    def create_new_element(self):
        return self.create_new_skill()


    def add_to_layout(self):
        add_multiple_elements_to_layout_by_row(self.layout, self.labels)

    def translate(self, language):
        set_text_of_children(self, self.translate_reference[language])

    def calculate_ranks(self):
        total_ranks = 0
        for skill in self.skills:
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
        for skill in self.skills:
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
