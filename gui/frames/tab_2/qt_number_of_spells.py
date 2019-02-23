from PyQt5 import QtCore

from gui.frames.qt_generic_classes import DefaultBox, BoxType
from gui.frames.qt_generic_functions import create_qlabel, create_qline_edit, set_text_of_children, \
    add_multiple_elements_to_layout_by_row, add_element_to_layout


class NumberOfSpellsBox(BoxType, DefaultBox):
    def __init__(self, parent, position, size):
        BoxType.__init__(self, parent=parent, position=position, size=size, defaults=True)
        self.translate_reference = {"EN": {"root": {"title": "Number of spells"},
                                           "number_of_spells_0th_label": "0th lvl",
                                           "number_of_spells_4th_label": "4th lvl",
                                           "number_of_spells_2nd_label": "2nd lvl",
                                           "number_of_spells_3rd_label": "3rd lvl",
                                           "number_of_spells_1st_label": "1st lvl",
                                           "number_of_spells_5th_label": "5th lvl",
                                           "number_of_spells_6th_label": "6th lvl",
                                           "number_of_spells_7th_label": "7th lvl",
                                           "number_of_spells_8th_label": "8th lvl",
                                           "number_of_spells_9th_label": "9th lvl",
                                           "known_spells_title": "Known number of spells (Warlock / Bard)"}}


        self.number_of_spells_0th_label = create_qlabel(parent=self.container)
        self.number_of_spells_1st_label = create_qlabel(parent=self.container)
        self.number_of_spells_2nd_label = create_qlabel(parent=self.container)
        self.number_of_spells_3rd_label = create_qlabel(parent=self.container)
        self.number_of_spells_4th_label = create_qlabel(parent=self.container)
        self.number_of_spells_5th_label = create_qlabel(parent=self.container)
        self.number_of_spells_6th_label = create_qlabel(parent=self.container)
        self.number_of_spells_7th_label = create_qlabel(parent=self.container)
        self.number_of_spells_8th_label = create_qlabel(parent=self.container)
        self.number_of_spells_9th_label = create_qlabel(parent=self.container)
        self.known_spells_title = create_qlabel(parent=self.container, align=QtCore.Qt.AlignCenter)

        self.number_of_spells_0 = create_qline_edit(parent=self.container)
        self.number_of_spells_1 = create_qline_edit(parent=self.container)
        self.number_of_spells_2 = create_qline_edit(parent=self.container)
        self.number_of_spells_3 = create_qline_edit(parent=self.container)
        self.number_of_spells_4 = create_qline_edit(parent=self.container)
        self.number_of_spells_5 = create_qline_edit(parent=self.container)
        self.number_of_spells_6 = create_qline_edit(parent=self.container)
        self.number_of_spells_7 = create_qline_edit(parent=self.container)
        self.number_of_spells_8 = create_qline_edit(parent=self.container)
        self.number_of_spells_9 = create_qline_edit(parent=self.container)

        self.add_to_layout()
        self.translate("EN")
        self.root.setLayout(self.layout)

    def add_to_layout(self):
        add_element_to_layout(self.layout, self.known_spells_title, 0, 2, 1, 6)

        first_row = [self.number_of_spells_0th_label, self.number_of_spells_0, self.number_of_spells_1st_label,
                     self.number_of_spells_1, self.number_of_spells_2nd_label, self.number_of_spells_2,
                     self.number_of_spells_3rd_label, self.number_of_spells_3, self.number_of_spells_4th_label,
                     self.number_of_spells_4]
        add_multiple_elements_to_layout_by_row(self.layout, first_row, row=1)

        second_row = [self.number_of_spells_5th_label, self.number_of_spells_5, self.number_of_spells_6th_label,
                      self.number_of_spells_6, self.number_of_spells_7th_label, self.number_of_spells_7,
                      self.number_of_spells_8th_label, self.number_of_spells_8, self.number_of_spells_9th_label,
                      self.number_of_spells_9]
        add_multiple_elements_to_layout_by_row(self.layout, second_row, row=2)

    def translate(self, language):
        set_text_of_children(self, self.translate_reference[language])
