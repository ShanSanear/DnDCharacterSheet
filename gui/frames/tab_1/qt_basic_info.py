from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

from gui.frames.qt_generic_classes import DefaultBox, BoxType
from gui.frames.qt_generic_functions import create_qlabel, create_qline_edit, add_multiple_elements_to_layout_by_row


class BasicInfoBox(BoxType, DefaultBox):
    def __init__(self, parent, position, size):
        BoxType.__init__(self, parent=parent, position=position, size=size)
        qlabel_dict_1 = dict(parent=self.container)
        qlabel_dict_2 = dict(parent=self.container)
        qline_dict_1 = dict(parent=self.container)  # min_size=(100, 23))
        qline_dict_2 = dict(parent=self.container, max_size=(40, None))  # min_size=(50, 23))

        self.class_label = create_qlabel(**qlabel_dict_1)
        self.faith_label = create_qlabel(**qlabel_dict_1)
        self.race_label = create_qlabel(**qlabel_dict_1)
        self.alignement_label = create_qlabel(**qlabel_dict_1)
        self.player_name_label = create_qlabel(**qlabel_dict_1)
        self.name_label = create_qlabel(**qlabel_dict_1)
        self.experience_label = create_qlabel(**qlabel_dict_1, align=Qt.AlignVCenter | Qt.AlignCenter)
        self.experience_divide_label = create_qlabel(**qlabel_dict_1, text="/")
        self.height_label = create_qlabel(**qlabel_dict_2)
        self.weight_label = create_qlabel(**qlabel_dict_2)
        self.eyes_label = create_qlabel(**qlabel_dict_2)
        self.hair_label = create_qlabel(**qlabel_dict_2)
        self.size_label = create_qlabel(**qlabel_dict_2)
        self.age_label = create_qlabel(**qlabel_dict_2)
        self.gender_label = create_qlabel(**qlabel_dict_2)
        self.level_label = create_qlabel(**qlabel_dict_2)

        self.race = create_qline_edit(**qline_dict_1)
        self.alignement = create_qline_edit(**qline_dict_1)
        self.char_class = create_qline_edit(**qline_dict_1)
        self.faith = create_qline_edit(**qline_dict_1)
        self.name = create_qline_edit(**qline_dict_1)
        self.current_experience = create_qline_edit(**qline_dict_1)
        self.next_experience = create_qline_edit(**qline_dict_1)
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
        self.retranslate()

    def add_to_layout(self):
        second_row_labels = [self.class_label, self.race_label, self.alignement_label, self.faith_label]
        second_row_input = [self.char_class, self.race, self.alignement, self.faith]
        third_row_labels_part_1 = [self.level_label, self.age_label, self.weight_label, self.height_label]
        third_row_labels_part_2 = [self.size_label, self.gender_label, self.eyes_label, self.hair_label]

        third_row_input_part_1 = [self.level, self.age, self.weight, self.height]
        third_row_input_part_2 = [self.size, self.gender, self.eyes, self.hair]

        elements = [[second_row_labels, 2], [second_row_input, 2]]
        add_multiple_elements_to_layout_by_row(self.layout, [self.name_label], width=4)
        add_multiple_elements_to_layout_by_row(self.layout, [self.player_name_label], start_column=4, width=2)
        add_multiple_elements_to_layout_by_row(self.layout, [self.experience_label], start_column=6, width=3)
        add_multiple_elements_to_layout_by_row(self.layout, [self.name], row=1, width=4)
        add_multiple_elements_to_layout_by_row(self.layout, [self.player_name], row=1, start_column=4, width=2)
        add_multiple_elements_to_layout_by_row(self.layout, [self.current_experience, self.experience_divide_label,
                                                             self.next_experience], row=1, start_column=6)
        for row_idx, [row_elements, width] in enumerate(elements):
            add_multiple_elements_to_layout_by_row(self.layout, row_elements, row=row_idx + 2, width=width)
        add_multiple_elements_to_layout_by_row(self.layout, [self.faith], start_column=6, row=3, width=3)

        add_multiple_elements_to_layout_by_row(self.layout, third_row_labels_part_1, row=4)
        add_multiple_elements_to_layout_by_row(self.layout, third_row_labels_part_2[:-1], row=4, start_column=4)
        add_multiple_elements_to_layout_by_row(self.layout, [third_row_labels_part_2[-1]], row=4, start_column=7,
                                               width=2)
        add_multiple_elements_to_layout_by_row(self.layout, third_row_input_part_1, row=5)
        add_multiple_elements_to_layout_by_row(self.layout, third_row_input_part_2[:-1], row=5, start_column=4)
        add_multiple_elements_to_layout_by_row(self.layout, [third_row_input_part_2[-1]], row=5, start_column=7,
                                               width=2)

    def retranslate(self):
        self.root.setTitle(QApplication.translate("BasicInfo", "Basic info"))
        self.class_label.setText(QApplication.translate("BasicInfo", "Class"))
        self.faith_label.setText(QApplication.translate("BasicInfo", "Faith"))
        self.race_label.setText(QApplication.translate("BasicInfo", "Race"))
        self.alignement_label.setText(QApplication.translate("BasicInfo", "Alignement"))
        self.player_name_label.setText(QApplication.translate("BasicInfo", "Player"))
        self.name_label.setText(QApplication.translate("BasicInfo", "Name"))
        self.height_label.setText(QApplication.translate("BasicInfo", "Height"))
        self.weight_label.setText(QApplication.translate("BasicInfo", "Weight"))
        self.experience_label.setText(QApplication.translate("BasicInfo", "Experience"))
        self.eyes_label.setText(QApplication.translate("BasicInfo", "Eyes"))
        self.hair_label.setText(QApplication.translate("BasicInfo", "Hair"))
        self.size_label.setText(QApplication.translate("BasicInfo", "Size"))
        self.age_label.setText(QApplication.translate("BasicInfo", "Age"))
        self.gender_label.setText(QApplication.translate("BasicInfo", "Gender"))
        self.level_label.setText(QApplication.translate("BasicInfo", "Level"))
