from types import SimpleNamespace

from PyQt5 import QtWidgets, QtCore

from gui.frames.qt_generic_classes import ResizeableBox, DefaultBox
from gui.frames.qt_generic_functions import create_qlabel, create_qline_edit, create_push_button, \
    set_text_of_children, add_multiple_elements_to_layout_by_row
from gui.popups.feat_full_description import DescriptionDialog


class KnownSpellsBox(DefaultBox, ResizeableBox):
    def __init__(self, parent, position, size):
        self.parent = parent
        ResizeableBox.__init__(self, increase_width=0, increase_height=28)
        self.root = QtWidgets.QGroupBox(parent)
        self.root.setGeometry(QtCore.QRect(*position, *size))
        self.root.setObjectName("KnownSpellsBox")
        self.container = QtWidgets.QWidget(self.root)
        self.container.setObjectName("KnownSpellsQwidget")
        self.layout = QtWidgets.QGridLayout(self.container)
        self.layout.setObjectName("KnownSpellsLayout")
        self.add_new = create_push_button("add_new_feat", self.container, max_size=[20, None], text="+")
        self.add_new.clicked.connect(self.add_spell)

        self.spells = []
        qlabel_dict = dict(parent=self.container, max_size=(20, None))
        qlabel_dict_2 = dict(parent=self.container)

        self.lvl_label = create_qlabel("known_spells_lvl_label", **qlabel_dict)

        self.name_label = create_qlabel("known_spells_name_label", **qlabel_dict_2)

        self.description_button_label = create_qlabel("known_spells_description_label",
                                                      **qlabel_dict_2)
        self.short_description_label = create_qlabel("known_spells_short_description_label",
                                                     **qlabel_dict_2)

        self.translate_reference = {
            "EN": {
                "root": {
                    "title": "Known spells"
                },
                "lvl_label": "LVL",
                "name_label": "Spell name",
                "description_button_label": "Desc",
                "short_description_label": "DESC",
            }
        }
        self.translate_reference_new_element = {
            "EN": {
                "lvl": "10",
                "name": "Lorem ipsum",
                "short_description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
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
        new_spell.lvl = create_qline_edit(f"known_spells_{idx}_lvl", parent=self.container, max_size=[20, None], min_size=[None, 23])
        new_spell.name = create_qline_edit(f"known_spells_{idx}_name", parent=self.container, min_size=[None, 23])

        new_spell.short_description = create_qline_edit(f"known_spells_{idx}_description_field",
                                                        parent=self.container, min_size=[350, 23])
        new_spell.description_button = create_push_button(f"known_spells_{idx}_description_button",
                                                          parent=self.container, max_size=[20, None],
                                                          min_size=[None, 23],
                                                          function_on_clicked=self.show_description, args_on_clicked=new_spell, text="...")
        new_spell._full_description = ""

        set_text_of_children(new_spell, self.translate_reference_new_element["EN"])
        return new_spell

    def create_new_element(self):
        return self.create_spell()

    def add_spell(self):
        self.add_new_element(self.spells, self.layout, 1)

    def add_to_layout(self):
        add_multiple_elements_to_layout_by_row(self.layout, elements_to_add=[self.lvl_label, self.name_label,
                                                                             self.short_description_label,
                                                                             self.description_button_label])

    def show_description(self, spell):
        dialog = DescriptionDialog("Spell description", self.root, spell)
        dialog.show()

    def translate(self, language):
        set_text_of_children(self, self.translate_reference[language])

    def adding_missing_element(self):
        self.add_spell()
