from types import SimpleNamespace

from PyQt5 import QtWidgets, QtCore

from qt_gui.boxes.qt_generic_classes import ResizeableBox
from qt_gui.boxes.qt_generic_functions import create_qlabel, create_qline_edit, create_push_button, \
    set_text_of_children, add_multiple_elements_to_layout_by_row


class KnownSpellsBox(ResizeableBox):
    def __init__(self, parent, position, size):
        ResizeableBox.__init__(self, increase_width=0, increase_height=30)
        self.root = QtWidgets.QGroupBox(parent)
        self.root.setGeometry(QtCore.QRect(*position, *size))
        self.root.setObjectName("KnownSpellsBox")
        self.container = QtWidgets.QWidget(self.root)
        self.container.setObjectName("KnownSpellsQwidget")
        self.layout = QtWidgets.QGridLayout(self.container)
        self.layout.setObjectName("KnownSpellsLayout")

        self.spells = []
        qlabel_dict = dict(parent=self.container, max_size=(20, 16777215))
        qlabel_dict_2 = dict(parent=self.container)

        self.lvl_label = create_qlabel("known_spells_lvl_label_1", **qlabel_dict)

        self.name_label = create_qlabel("known_spells_name_label_1", **qlabel_dict_2)

        self.description_button_label = create_qlabel("known_spells_description_label_1",
                                                      **qlabel_dict_2)
        self.description_field_label = create_qlabel("known_spells_description_field_label_1",
                                                     **qlabel_dict_2)

        self.translate_reference = {
            "EN": {
                "lvl_label": "LVL",
                "name_label": "Spell name",
                "description_button_label": "Desc",
                "description_field_label": "DESC",
            }
        }
        self.translate_reference_new_element = {
            "EN": {
                "lvl": "10",
                "name": "Lorem ipsum",
                "description_field": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                                     "Praesent sapien urna, egestas eu tempor at, pretium nec orci. "
                                     "In nec pharetra tellus. In malesuada erat tellus, "
                                     "eget efficitur elit convallis eu."
            }
        }

        for _ in range(15):
            self.add_spell()

        self.add_to_layout()
        self.translate("EN")

        self.root.setLayout(self.layout)

    def create_spell(self):
        idx = len(self.spells)
        new_spell = SimpleNamespace()
        new_spell.lvl = create_qline_edit(f"known_spells_{idx}_lvl", parent=self.container, max_size=[20, None])
        new_spell.name = create_qline_edit(f"known_spells_{idx}_name", parent=self.container,)

        new_spell.description_field = create_qline_edit(f"known_spells_{idx}_description_field",
                                                        parent=self.container, min_size=[350, 23])
        new_spell.description_button = create_push_button(f"known_spells_{idx}_description_button",
                                                          parent=self.container, max_size=[20, None])

        set_text_of_children(new_spell, self.translate_reference_new_element["EN"])
        return new_spell

    def create_new_element(self):
        return self.create_spell()

    def add_spell(self):
        self.add_new_element(self.spells, self.layout, 1)

    def add_to_layout(self):
        add_multiple_elements_to_layout_by_row(self.layout, elements_to_add=[self.lvl_label, self.name_label,
                                                                             self.description_field_label,
                                                                             self.description_button_label])

    def translate(self, language):
        set_text_of_children(self, self.translate_reference[language])

    def update_container_size(self):
        root_width = self.root.width()
        root_height = self.root.height()
        container_width = self.container.width()
        container_height = self.container.height()
        self.root.setMinimumSize(QtCore.QSize(root_width, root_height + 30))
        self.container.setMinimumSize(QtCore.QSize(container_width, container_height + 30))
