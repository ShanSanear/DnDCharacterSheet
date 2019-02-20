from PyQt5 import QtWidgets, QtCore

from gui.frames.qt_generic_classes import DefaultBox
from gui.frames.qt_generic_functions import create_qlabel, create_qline_edit, add_multiple_elements_to_layout_by_row, \
    set_text_of_children


class BasicInfoBox(DefaultBox):
    def __init__(self, parent, position, size):
        self.root = QtWidgets.QGroupBox(parent)

        self.root.setGeometry(QtCore.QRect(*position, *size))
        self.container = QtWidgets.QWidget(self.root)

        self.layout = QtWidgets.QGridLayout(self.container)
        self.layout.setSpacing(10)
        self.layout.setContentsMargins(20, 10, 10, 20)
        self.translate_reference = {
            "EN":
                {
                    "class_label": "Class",
                    "faith_label": "Faith",
                    "race_label": "Race",
                    "alignement_label": "Alignement",
                    "player_name_label": "Player",
                    "name_label": "Name",
                    "height_label": "Height",
                    "weight_label": "Weight",
                    "experience_label": "Experience",
                    "eyes_label": "Eyes",
                    "hair_label": "Hair",
                    "size_label": "Size",
                    "age_label": "Age",
                    "gender_label": "Gender",
                    "level_label": "Level",
                }
        }
        qlabel_dict_1 = dict(parent=self.container,
                             )
        qlabel_dict_2 = dict(parent=self.container,
                             )
        qline_dict_1 = dict(parent=self.container, )  # min_size=(100, 23))
        qline_dict_2 = dict(parent=self.container, max_size=(40, None))  # min_size=(50, 23))

        # TODO - in a long shot - generalize it
        self.class_label = create_qlabel(**qlabel_dict_1)
        self.faith_label = create_qlabel(**qlabel_dict_1)
        self.race_label = create_qlabel(**qlabel_dict_1)
        self.alignement_label = create_qlabel(**qlabel_dict_1)
        self.player_name_label = create_qlabel(**qlabel_dict_1)
        self.name_label = create_qlabel(**qlabel_dict_1)
        self.experience_label = create_qlabel(**qlabel_dict_1)
        self.height_label = create_qlabel(**qlabel_dict_2)
        self.weight_label = create_qlabel(**qlabel_dict_2)
        self.eyes_label = create_qlabel(**qlabel_dict_2)
        self.hair_label = create_qlabel(**qlabel_dict_2)
        self.size_label = create_qlabel(**qlabel_dict_2)
        self.age_label = create_qlabel(**qlabel_dict_2)
        self.gender_label = create_qlabel(**qlabel_dict_2)
        self.level_label = create_qlabel(**qlabel_dict_2)

        # TODO - in a long shot - generalize it
        self.race = create_qline_edit(**qline_dict_1)
        self.alignement = create_qline_edit(**qline_dict_1)
        self.char_class = create_qline_edit(**qline_dict_1)
        self.faith = create_qline_edit(**qline_dict_1)
        self.name = create_qline_edit(**qline_dict_1)
        self.experience = create_qline_edit(**qline_dict_1)
        self.height = create_qline_edit(**qline_dict_2)
        self.weight = create_qline_edit(**qline_dict_2)
        self.hair = create_qline_edit(**qline_dict_1)
        self.player_name = create_qline_edit(**qline_dict_1)
        self.eyes = create_qline_edit(**qline_dict_1)
        self.gender = create_qline_edit(**qline_dict_1)
        self.age = create_qline_edit(**qline_dict_2)
        self.size = create_qline_edit(**qline_dict_1)
        self.level = create_qline_edit(**qline_dict_2)

        self.add_to_layout()
        self.translate("EN")
        self.set_default()
        self.root.setTitle("Basic Info")
        self.root.setLayout(self.layout)

    def add_to_layout(self):
        second_row_labels = [self.class_label, self.race_label, self.alignement_label, self.faith_label]
        second_row_input = [self.char_class, self.race, self.alignement, self.faith]
        third_row_labels_part_1 = [self.level_label, self.age_label, self.weight_label, self.height_label]
        third_row_labels_part_2 = [self.size_label, self.gender_label, self.eyes_label, self.hair_label]

        third_row_input_part_1 = [self.level, self.age, self.weight, self.height]
        third_row_input_part_2 = [self.size, self.gender, self.eyes, self.hair]

        elements = [[second_row_labels, 2], [second_row_input, 2]]
        add_multiple_elements_to_layout_by_row(self.layout, [self.name_label], width=4)
        add_multiple_elements_to_layout_by_row(self.layout, [self.player_name_label, self.experience_label], start_column=4, width=2)
        add_multiple_elements_to_layout_by_row(self.layout, [self.name], row=1, width=4)
        add_multiple_elements_to_layout_by_row(self.layout, [self.player_name, self.experience], row=1, start_column=4, width=2)
        for row_idx, [row_elements, width] in enumerate(elements):
            add_multiple_elements_to_layout_by_row(self.layout, row_elements, row=row_idx + 2, width=width)

        add_multiple_elements_to_layout_by_row(self.layout, third_row_labels_part_1, row=4)
        add_multiple_elements_to_layout_by_row(self.layout, third_row_labels_part_2, row=4, start_column=4)
        add_multiple_elements_to_layout_by_row(self.layout, third_row_input_part_1, row=5)
        add_multiple_elements_to_layout_by_row(self.layout, third_row_input_part_2, row=5, start_column=4)

    def translate(self, language_ref):
        set_text_of_children(self, self.translate_reference[language_ref])

    def set_default(self):
        default_values = {
            "race": "Lorem ipsum",
            "alignement": "Lorem ipsum",
            "char_class": "Lorem ipsum",
            "faith": "Lorem ipsum",
            "name": "Lorem ipsum",
            "height": "10",
            "weight": "10",
            "hair": "Lorem ipsum",
            "player_name": "Lorem ipsum",
            "eyes": "Lorem ipsum",
            "gender": "Lorem ipsum",
            "age": "10",
            "size": "Lorem ipsum",
            "level": "10",
            "experience": "0/1000",
        }
        set_text_of_children(self, default_values)
