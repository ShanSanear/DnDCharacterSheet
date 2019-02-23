from PyQt5 import QtCore

from gui.frames.qt_generic_classes import DefaultBox, BoxType
from gui.frames.qt_generic_functions import create_qlabel, create_qline_edit, set_text_of_children, \
    add_multiple_elements_to_layout_by_column


class SpellsPerDayBox(BoxType, DefaultBox):
    # TODO - function based widgets and labels
    # TODO - generalized translation
    # TODO - adding widgets by rows/columns
    def __init__(self, parent, position, size):
        BoxType.__init__(self, parent=parent, position=position, size=size, defaults=True)
        self.translation_reference = {"EN": {
            "root": {"title": "Spells per day / Spells DC"},
            "level_label": "Lvl", "per_day_label": "/Day", "extra_spells_label": "Extra", "base_spell_dc_label": "DC",
            "_num_0": "0", "_num_1": "1", "_num_2": "2", "_num_3": "3", "_num_4": "4", "_num_5": "5", "_num_6": "6",
            "_num_7": "7", "_num_8": "8", "_num_9": "9", }}

        qline_dict = dict(parent=self.container, min_size=(0, 23), align=QtCore.Qt.AlignCenter)
        qlabel_dict = dict(parent=self.container, align=QtCore.Qt.AlignCenter)

        self.level_label = create_qlabel(**qlabel_dict)
        self.per_day_label = create_qlabel(**qlabel_dict)
        self.extra_spells_label = create_qlabel(**qlabel_dict)
        self.base_spell_dc_label = create_qlabel(**qlabel_dict)

        self.dc_lvl_0 = create_qline_edit(**qline_dict)
        self.spells_per_day_lvl_0 = create_qline_edit(**qline_dict)

        self.dc_lvl_1 = create_qline_edit(**qline_dict)

        self.extra_spells_lvl_0 = create_qline_edit(**qline_dict)

        self.extra_spells_lvl_1 = create_qline_edit(**qline_dict)

        self.spells_per_day_lvl_2 = create_qline_edit(**qline_dict)

        self.dc_lvl_2 = create_qline_edit(**qline_dict)

        self.spells_per_day_lvl_1 = create_qline_edit(**qline_dict)

        self.spells_per_day_lvl_5 = create_qline_edit(**qline_dict)

        self.extra_spells_lvl_2 = create_qline_edit(**qline_dict)

        self.dc_lvl_3 = create_qline_edit(**qline_dict)

        self.spells_per_day_lvl_4 = create_qline_edit(**qline_dict)

        self.extra_spells_lvl_3 = create_qline_edit(**qline_dict)

        self.dc_lvl_6 = create_qline_edit(**qline_dict)

        self.extra_spells_lvl_4 = create_qline_edit(**qline_dict)

        self.dc_lvl_5 = create_qline_edit(**qline_dict)

        self.spells_per_day_lvl_3 = create_qline_edit(**qline_dict)

        self.dc_lvl_4 = create_qline_edit(**qline_dict)

        self.extra_spells_lvl_8 = create_qline_edit(**qline_dict)

        self.extra_spells_lvl_5 = create_qline_edit(**qline_dict)

        self.dc_lvl_8 = create_qline_edit(**qline_dict)

        self.dc_lvl_7 = create_qline_edit(**qline_dict)

        self.extra_spells_lvl_7 = create_qline_edit(**qline_dict)

        self.extra_spells_lvl_6 = create_qline_edit(**qline_dict)

        self.spells_per_day_lvl_7 = create_qline_edit(**qline_dict)

        self.spells_per_day_lvl_6 = create_qline_edit(**qline_dict)

        self.spells_per_day_lvl_8 = create_qline_edit(**qline_dict)
        self.dc_lvl_9 = create_qline_edit(**qline_dict)
        self.spells_per_day_lvl_9 = create_qline_edit(**qline_dict)
        self.extra_spells_lvl_9 = create_qline_edit(**qline_dict)

        self._num_0 = create_qlabel(**qlabel_dict)
        self._num_1 = create_qlabel(**qlabel_dict)
        self._num_2 = create_qlabel(**qlabel_dict)
        self._num_3 = create_qlabel(**qlabel_dict)
        self._num_4 = create_qlabel(**qlabel_dict)
        self._num_5 = create_qlabel(**qlabel_dict)
        self._num_6 = create_qlabel(**qlabel_dict)
        self._num_7 = create_qlabel(**qlabel_dict)
        self._num_8 = create_qlabel(**qlabel_dict)
        self._num_9 = create_qlabel(**qlabel_dict)

        self.add_to_layout()
        self.translate("EN")

    def add_to_layout(self):
        first_column = [self.base_spell_dc_label, self.dc_lvl_0, self.dc_lvl_1, self.dc_lvl_2, self.dc_lvl_3,
                        self.dc_lvl_4, self.dc_lvl_5, self.dc_lvl_6, self.dc_lvl_7, self.dc_lvl_8, self.dc_lvl_9]
        add_multiple_elements_to_layout_by_column(layout=self.layout, elements_to_add=first_column, column=0)

        second_column = [self.level_label, self._num_0, self._num_1, self._num_2, self._num_3, self._num_4, self._num_5,
                         self._num_6, self._num_7, self._num_8, self._num_9, ]
        add_multiple_elements_to_layout_by_column(layout=self.layout, elements_to_add=second_column, column=1)

        third_column = [self.per_day_label, self.spells_per_day_lvl_0, self.spells_per_day_lvl_1,
                        self.spells_per_day_lvl_2, self.spells_per_day_lvl_3, self.spells_per_day_lvl_4,
                        self.spells_per_day_lvl_5, self.spells_per_day_lvl_6, self.spells_per_day_lvl_7,
                        self.spells_per_day_lvl_8, self.spells_per_day_lvl_9]
        add_multiple_elements_to_layout_by_column(layout=self.layout, elements_to_add=third_column, column=2)

        fourth_column = [self.extra_spells_label, self.extra_spells_lvl_0, self.extra_spells_lvl_1,
                         self.extra_spells_lvl_2, self.extra_spells_lvl_3, self.extra_spells_lvl_4,
                         self.extra_spells_lvl_5, self.extra_spells_lvl_6, self.extra_spells_lvl_7,
                         self.extra_spells_lvl_8, self.extra_spells_lvl_9]
        add_multiple_elements_to_layout_by_column(layout=self.layout, elements_to_add=fourth_column, column=3)

    def translate(self, language):
        set_text_of_children(self, self.translation_reference[language])
