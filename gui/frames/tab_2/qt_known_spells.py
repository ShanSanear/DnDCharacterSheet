from types import SimpleNamespace

from PyQt5.QtWidgets import QApplication

from gui.frames.qt_generic_classes import ScrollableBox
from gui.frames.qt_generic_functions import create_qlabel, create_qline_edit, create_push_button, \
    add_multiple_elements_to_layout_by_row
from gui.popups.qt_full_description import DescriptionDialog


class KnownSpellsBox(ScrollableBox):
    def __init__(self, parent, position, size):
        base_size = [size[0], 100]
        height_increment = 29
        max_height = size[1]
        ScrollableBox.__init__(self, parent=parent, position=position, base_size=base_size, max_height=max_height,
                               original_size=size,
                               height_increment=height_increment, row_offset=1, last_row_column=3)
        qlabel_dict = dict(parent=self.container, max_size=(20, None))
        qlabel_dict_2 = dict(parent=self.container)

        self.lvl_label = create_qlabel(**qlabel_dict)

        self.name_label = create_qlabel(**qlabel_dict_2)

        self.description_button_label = create_qlabel(**qlabel_dict_2)
        self.short_description_label = create_qlabel(**qlabel_dict_2)

        self.labels = [self.lvl_label, self.name_label, self.short_description_label, self.description_button_label]
        self.add_spell = self.add_new_element
        self.add_new.clicked.connect(self.add_spell)
        self.add_spell()

        self.add_to_layout()


    def create_spell(self):
        idx = len(self.elements_list)
        new_spell = SimpleNamespace()
        new_spell.lvl = create_qline_edit(parent=self.container, max_size=[20, None], min_size=[None, 23])
        new_spell.name = create_qline_edit(parent=self.container, min_size=[120, 23])

        new_spell.short_description = create_qline_edit(parent=self.container, min_size=[250, 23])
        new_spell.description_button = create_push_button(f"known_spells_{idx}_description_button",
                                                          parent=self.container, min_size=[20, 20], max_size=[20, 20],
                                                          function_on_clicked=self.show_description,
                                                          args_on_clicked=new_spell, text="...")
        new_spell._full_description = ""
        new_spell.delete_spell = create_push_button("item_delete", self.container, min_size=[20, 20],
                                                    max_size=[20, 20], text="-",
                                                    function_on_clicked=self._remove_element, args_on_clicked=new_spell)

        return new_spell

    def create_new_element(self):
        self.increase_height()
        return self.create_spell()

    def add_to_layout(self):
        add_multiple_elements_to_layout_by_row(self.layout, elements_to_add=self.labels)

    def show_description(self, spell):
        dialog = DescriptionDialog(QApplication.translate("KnownLanguage", "Spell description"), self.root, spell)
        dialog.show()

    def retranslate(self):
        self.root.setTitle(QApplication.translate("KnownLanguage", "Known spells"))
        self.lvl_label.setText(QApplication.translate("KnownLanguage", "LVL"))
        self.name_label.setText(QApplication.translate("KnownLanguage", "Spell name"))
        self.description_button_label.setText(QApplication.translate("KnownLanguage", "Desc"))
        self.short_description_label.setText(QApplication.translate("KnownLanguage", "DESC"))
