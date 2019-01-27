from types import SimpleNamespace

from PyQt5 import QtWidgets, QtCore

from gui.frames.qt_generic_classes import DefaultBox, ResizeableBox
from gui.frames.qt_generic_functions import create_combo_box, create_qline_edit, set_text_of_children, create_qlabel, \
    add_multiple_elements_to_layout_by_row


class SkillsBox(DefaultBox, ResizeableBox):
    def __init__(self, parent, position, size):
        ResizeableBox.__init__(self, increase_width=-0, increase_height=28)
        self.root = QtWidgets.QGroupBox(parent)
        self.root.setGeometry(QtCore.QRect(*position, *size))
        self.root.setObjectName("SkillsBox")
        self.container = QtWidgets.QWidget(self.root)
        self.container.setGeometry(QtCore.QRect(10, 10, size[0] - 10, size[1] - 10))
        self.container.setObjectName("gridLayoutWidget_5")
        self.layout = QtWidgets.QGridLayout(self.container)
        self.layout.setObjectName("SkillsLayout")
        self.skills = []
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
            }
        }
        self.create_labels()
        for _ in range(15):
            self.add_skill()

        self.add_to_layout()
        self.translate("EN")
        self.root.setLayout(self.layout)

    def create_new_skill(self):
        new_skill = SimpleNamespace()
        skill_idx = len(self.skills)
        new_skill.skill_name = create_qline_edit(f"skills{skill_idx}skill_name", self.container,
                                                 align=QtCore.Qt.AlignCenter, min_size=(150, None))
        new_skill.skill_name.setText(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
            "Praesent sapien urna, egestas eu tempor at, pretium nec orci.")
        new_skill.attr_choice = create_combo_box(f"skills{skill_idx}attr_choice", self.container,
                                                 number_of_choices=6,
                                                 choices_text=("STR", "DEX", "CON", "INT", "WIS", "CHA"),
                                                 max_size=(69, 20))
        qdict = dict(parent=self.container, align=QtCore.Qt.AlignCenter, max_size=[30, None])
        new_skill.total = create_qline_edit(f"skills{skill_idx}total", **qdict)

        new_skill.attr_mod = create_qline_edit(f"skills{skill_idx}attr_mod", **qdict, enabled=False)
        new_skill.rank = create_qline_edit(f"skills{skill_idx}rank", **qdict)

        new_skill.misc_mod = create_qline_edit(f"skills_{skill_idx}_misc_mod", **qdict)

        new_skill.cross_class_checkbox = QtWidgets.QCheckBox(self.container)
        new_skill.cross_class_checkbox.setObjectName(f"skills{skill_idx}description_button")


        return new_skill

    def add_skill(self):
        self.add_new_element(elements_list=self.skills, layout=self.layout, row_offset=1)

    def create_new_element(self):
        return self.create_new_skill()

    def create_labels(self):
        self.skill_name_label = create_qlabel("skills_skill_name_label", self.container)
        self.attr_choice_label = create_qlabel("skills_attr_choice_label", self.container, align=QtCore.Qt.AlignCenter)
        self.total_label = create_qlabel("skills_total_label", self.container, align=QtCore.Qt.AlignCenter)
        self.attr_mod_label = create_qlabel("skills_attr_mod_label", self.container, align=QtCore.Qt.AlignCenter)
        self.rank_label = create_qlabel("skills_rank_label", self.container, align=QtCore.Qt.AlignCenter)
        self.misc_label = create_qlabel("skills_misc_label", self.container, align=QtCore.Qt.AlignCenter)
        self.cross_class_label = create_qlabel("skills_description_label", self.container, align=QtCore.Qt.AlignCenter)
        self.add_to_layout()

    def add_to_layout(self):
        labels = [self.skill_name_label, self.attr_choice_label, self.total_label, self.attr_mod_label,
                  self.rank_label, self.misc_label, self.cross_class_label, ]
        add_multiple_elements_to_layout_by_row(self.layout, labels)

    def translate(self, language):
        set_text_of_children(self, self.translate_reference[language])
