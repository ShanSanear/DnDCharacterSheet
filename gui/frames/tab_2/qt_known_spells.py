import logging
from types import SimpleNamespace

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QScrollArea, QVBoxLayout

from gui.frames.qt_generic_classes import ResizeableBox, DefaultBox
from gui.frames.qt_generic_functions import create_qlabel, create_qline_edit, create_push_button, \
    set_text_of_children, add_multiple_elements_to_layout_by_row
from gui.popups.qt_full_description import DescriptionDialog


class KnownSpellsBox(DefaultBox, ResizeableBox):
    def __init__(self, parent, position, size):
        # TODO - scrollbar after achieving certain height
        self.parent = parent
        self.root = QtWidgets.QGroupBox(parent)
        self.root.setGeometry(QtCore.QRect(*position, *size))
        smaller_size = [size[0] - 20, size[1] - 40]
        self.main_widget = QtWidgets.QWidget(self.parent)
        self.main_widget.setStyleSheet("QScrollArea {background-color: #D8D8D8}")
        self.scrollarea = QScrollArea(self.main_widget)
        self.scrollarea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.main_widget.setGeometry(QtCore.QRect(*position, *size))
        self.scrollarea.setFixedHeight(smaller_size[1])
        self.scrollarea.setFixedWidth(smaller_size[0])
        self.scrollarea.setWidgetResizable(True)
        self.scrollarea.move(10, 10)
        self.container = QtWidgets.QWidget(self.main_widget)
        self.layout = QtWidgets.QGridLayout(self.container)
        self.add_new = create_push_button("add_new_feat", self.container, min_size=[20, 20],
                                          max_size=[20, 20], text="+")
        self.last_row = [self.add_new]

        self.spells = []
        qlabel_dict = dict(parent=self.container, max_size=(20, None))
        qlabel_dict_2 = dict(parent=self.container)

        self.lvl_label = create_qlabel(**qlabel_dict)

        self.name_label = create_qlabel(**qlabel_dict_2)

        self.description_button_label = create_qlabel(**qlabel_dict_2)
        self.short_description_label = create_qlabel(**qlabel_dict_2)

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
        self.labels = [self.lvl_label, self.name_label, self.short_description_label, self.description_button_label]
        ResizeableBox.__init__(self, elements_list=self.spells, row_offset=1, increase_width=0, increase_height=28,
                               last_row_column=4)
        self.add_spell = self.add_new_element
        self.add_new.clicked.connect(self.add_spell)
        for _ in range(19):
            self.add_spell()

        self.add_to_layout()
        self.translate("EN")

        self.scrollarea.setWidget(self.container)
        self.layout_All = QVBoxLayout(self.main_widget)
        self.layout_All.addWidget(self.scrollarea)


    def create_spell(self):
        idx = len(self.spells)
        new_spell = SimpleNamespace()
        new_spell.lvl = create_qline_edit(parent=self.container, max_size=[20, None],
                                          min_size=[None, 23], function_on_unfocused=self.sort_elements)
        new_spell.name = create_qline_edit(parent=self.container, min_size=[120, 23],
                                           function_on_unfocused=self.sort_elements)

        new_spell.short_description = create_qline_edit(parent=self.container, min_size=[250, 23])
        new_spell.description_button = create_push_button(f"known_spells_{idx}_description_button",
                                                          parent=self.container, min_size=[20, 20], max_size=[20, 20],
                                                          function_on_clicked=self.show_description,
                                                          args_on_clicked=new_spell, text="...")
        new_spell._full_description = ""
        new_spell.delete_spell = create_push_button("item_delete", self.container, min_size=[20, 20], max_size=[20, 20], text="-",
                                                    function_on_clicked=self._remove_element, args_on_clicked=new_spell)

        set_text_of_children(new_spell, self.translate_reference_new_element["EN"])
        return new_spell

    def create_new_element(self):
        return self.create_spell()

    def update_size(self):
        pass

    def add_to_layout(self):
        add_multiple_elements_to_layout_by_row(self.layout, elements_to_add=self.labels)

    def show_description(self, spell):
        dialog = DescriptionDialog("Spell description", self.root, spell)
        dialog.show()

    def translate(self, language):
        set_text_of_children(self, self.translate_reference[language])
