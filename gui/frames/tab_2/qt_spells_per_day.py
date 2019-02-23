from PyQt5 import QtCore

from gui.frames.qt_generic_classes import DefaultBox, BoxType
from gui.frames.qt_generic_functions import create_qlabel, create_qline_edit, set_text_of_children


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
        self.layout.addWidget(self._num_0, 1, 1, 1, 1)
        self.layout.addWidget(self._num_1, 2, 1, 1, 1)
        self.layout.addWidget(self._num_2, 3, 1, 1, 1)
        self.layout.addWidget(self._num_3, 4, 1, 1, 1)
        self.layout.addWidget(self._num_4, 5, 1, 1, 1)
        self.layout.addWidget(self._num_5, 6, 1, 1, 1)
        self.layout.addWidget(self._num_6, 7, 1, 1, 1)
        self.layout.addWidget(self._num_7, 8, 1, 1, 1)
        self.layout.addWidget(self._num_8, 9, 1, 1, 1)
        self.layout.addWidget(self._num_9, 10, 1, 1, 1)
        self.layout.addWidget(self.dc_lvl_0, 1, 0, 1, 1)
        self.layout.addWidget(self.level_label, 0, 1, 1, 1)
        self.layout.addWidget(self.per_day_label, 0, 2, 1, 1)
        self.layout.addWidget(self.extra_spells_label, 0, 3, 1, 1)
        self.layout.addWidget(self.spells_per_day_lvl_0, 1, 2, 1, 1)
        self.layout.addWidget(self.dc_lvl_1, 2, 0, 1, 1)
        self.layout.addWidget(self.extra_spells_lvl_0, 1, 3, 1, 1)
        self.layout.addWidget(self.extra_spells_lvl_1, 2, 3, 1, 1)
        self.layout.addWidget(self.spells_per_day_lvl_2, 3, 2, 1, 1)
        self.layout.addWidget(self.dc_lvl_2, 3, 0, 1, 1)
        self.layout.addWidget(self.spells_per_day_lvl_1, 2, 2, 1, 1)
        self.layout.addWidget(self.spells_per_day_lvl_5, 6, 2, 1, 1)
        self.layout.addWidget(self.extra_spells_lvl_2, 3, 3, 1, 1)
        self.layout.addWidget(self.dc_lvl_3, 4, 0, 1, 1)
        self.layout.addWidget(self.spells_per_day_lvl_4, 5, 2, 1, 1)
        self.layout.addWidget(self.extra_spells_lvl_3, 4, 3, 1, 1)
        self.layout.addWidget(self.dc_lvl_6, 7, 0, 1, 1)
        self.layout.addWidget(self.extra_spells_lvl_4, 5, 3, 1, 1)
        self.layout.addWidget(self.dc_lvl_5, 6, 0, 1, 1)
        self.layout.addWidget(self.spells_per_day_lvl_3, 4, 2, 1, 1)
        self.layout.addWidget(self.dc_lvl_4, 5, 0, 1, 1)
        self.layout.addWidget(self.extra_spells_lvl_8, 9, 3, 1, 1)
        self.layout.addWidget(self.extra_spells_lvl_5, 6, 3, 1, 1)
        self.layout.addWidget(self.dc_lvl_8, 9, 0, 1, 1)
        self.layout.addWidget(self.dc_lvl_7, 8, 0, 1, 1)
        self.layout.addWidget(self.extra_spells_lvl_7, 8, 3, 1, 1)
        self.layout.addWidget(self.extra_spells_lvl_6, 7, 3, 1, 1)
        self.layout.addWidget(self.spells_per_day_lvl_7, 8, 2, 1, 1)
        self.layout.addWidget(self.spells_per_day_lvl_6, 7, 2, 1, 1)
        self.layout.addWidget(self.spells_per_day_lvl_8, 9, 2, 1, 1)
        self.layout.addWidget(self.base_spell_dc_label, 0, 0, 1, 1)
        self.layout.addWidget(self.spells_per_day_lvl_9, 10, 2, 1, 1)
        self.layout.addWidget(self.dc_lvl_9, 10, 0, 1, 1)
        self.layout.addWidget(self.extra_spells_lvl_9, 10, 3, 1, 1)

    def translate(self, language):
        set_text_of_children(self, self.translation_reference[language])
