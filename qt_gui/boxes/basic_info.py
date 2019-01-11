from PyQt5 import QtWidgets, QtCore, QtGui

from qt_gui.boxes.box import DefaultBox
from qt_gui.boxes.qt_generic_functions import create_qlabel, create_qline_edit, add_to_box_layout_by_row, \
    set_text_of_children


class BasicInfoBox(DefaultBox):
    def __init__(self, centralwidget):
        self.root = QtWidgets.QGroupBox(centralwidget)
        self.root.setGeometry(QtCore.QRect(10, 0, 811, 201))
        self.root.setObjectName("BasicInfoBox")
        self.container = QtWidgets.QWidget(self.root)
        self.container.setGeometry(QtCore.QRect(10, 20, 791, 162))
        self.container.setObjectName("gridLayoutWidget_2")
        self.layout = QtWidgets.QGridLayout(self.container)
        self.layout.setContentsMargins(9, 9, 9, 9)
        self.layout.setSpacing(6)
        self.layout.setObjectName("BasicInfoLayout")
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
                    "eyes_label": "Eyes",
                    "hair_label": "Hair",
                    "size_label": "Size",
                    "age_label": "Age",
                    "gender_label": "Gender",
                    "level_label": "Level",
                }
        }
        self.default_values = {
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
        }

        qlabel_dict_1 = dict(parent=self.container,
                             align=QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter,
                             min_size=(178, 16), )
        qlabel_dict_2 = dict(parent=self.container,
                             align=QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter,
                             min_size=(86, 16), )
        qline_dict_1 = dict(parent=self.container, min_size=(177, 23))
        qline_dict_2 = dict(parent=self.container, min_size=(85, 23))

        self.class_label = create_qlabel("character_class_label", **qlabel_dict_1)
        self.faith_label = create_qlabel("character_faith_label", **qlabel_dict_1)
        self.race_label = create_qlabel("character_race_label", **qlabel_dict_1)
        self.alignement_label = create_qlabel("character_alignement_label", **qlabel_dict_1)
        self.player_name_label = create_qlabel("player_name_label", **qlabel_dict_1)
        self.name_label = create_qlabel("character_name_label", **qlabel_dict_1)
        self.height_label = create_qlabel("character_height_label", **qlabel_dict_2)
        self.weight_label = create_qlabel("character_weight_label", **qlabel_dict_2)
        self.eyes_label = create_qlabel("character_eyes_label", **qlabel_dict_2)
        self.hair_label = create_qlabel("character_hair_label", **qlabel_dict_2)
        self.size_label = create_qlabel("character_size_label", **qlabel_dict_2)
        self.age_label = create_qlabel("character_age_label", **qlabel_dict_2)
        self.gender_label = create_qlabel("character_gender_label", **qlabel_dict_2)
        self.level_label = create_qlabel("character_level_label", **qlabel_dict_2)

        self.race = create_qline_edit("character_race", **qline_dict_1)
        self.alignement = create_qline_edit("character_alignement", **qline_dict_1)
        self.char_class = create_qline_edit("character_class", **qline_dict_1)
        self.faith = create_qline_edit("character_faith", **qline_dict_1)
        self.name = create_qline_edit("character_name", **qline_dict_2)
        self.height = create_qline_edit("character_height", **qline_dict_2)
        self.weight = create_qline_edit("character_weight", **qline_dict_2)
        self.hair = create_qline_edit("character_hair", **qline_dict_2)
        self.player_name = create_qline_edit("player_name", **qline_dict_2)
        self.eyes = create_qline_edit("character_eyes", **qline_dict_2)
        self.gender = create_qline_edit("character_gender", **qline_dict_2)
        self.age = create_qline_edit("character_age", **qline_dict_2)
        self.size = create_qline_edit("character_size", **qline_dict_2)
        self.level = create_qline_edit("character_level", **qline_dict_2)

        self.add_to_layout()
        self.translate("EN")
        self.set_default()
        self.root.setTitle("Basic Info")

    def add_to_layout(self):
        first_row_labels = [self.name_label, self.player_name_label]
        add_to_box_layout_by_row(self.layout, first_row_labels, row=0, width=4)

        first_row_input = [self.name, self.player_name]
        add_to_box_layout_by_row(self.layout, first_row_input, row=1, width=4)

        second_row_labels = [self.class_label, self.race_label, self.alignement_label, self.faith_label]
        add_to_box_layout_by_row(self.layout, second_row_labels, row=2, width=2)

        second_row_input = [self.char_class, self.race, self.alignement, self.faith]
        add_to_box_layout_by_row(self.layout, second_row_input, row=3, width=2)

        third_row_labels = [self.level_label, self.size_label, self.age_label, self.gender_label, self.height_label,
                            self.weight_label, self.eyes_label, self.hair_label]
        add_to_box_layout_by_row(self.layout, third_row_labels, row=4)

        third_row_input = [self.level, self.size, self.age, self.gender, self.height, self.weight, self.eyes, self.hair]
        add_to_box_layout_by_row(self.layout, third_row_input, row=5)

    def translate(self, language_ref):
        set_text_of_children(self, self.translate_reference[language_ref])

    def set_default(self):
        set_text_of_children(self, self.default_values)
