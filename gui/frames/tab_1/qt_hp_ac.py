from PyQt5.QtWidgets import QApplication

from core.character import Character
from gui.frames.qt_generic_classes import DefaultBox, BoxType
from gui.frames.qt_generic_functions import create_qlabel, create_qline_edit, add_element_to_layout, \
    add_multiple_elements_to_layout_by_row, update_texts


class HpAcBox(BoxType, DefaultBox):
    char_core: Character

    def __init__(self, parent, position, size, char_core):
        self.char_core = char_core
        BoxType.__init__(self, parent=parent, position=position, size=size, defaults=True)
        qline_editable = dict(parent=self.container, function_on_text_changed=self._update_ac)
        self.hp_total_label = create_qlabel(self.container)
        self.hp_hp_wounds_current_hp_label = create_qlabel(self.container)
        self.hp_label = create_qlabel(self.container)
        self.hp_total = create_qline_edit(self.container)
        self.ac_label = create_qlabel(self.container)
        self.hp_dice_label = create_qlabel(self.container)
        self.hp_dice = create_qline_edit(self.container)
        self.ac_total = create_qline_edit(self.container, enabled=False)
        self.ac_base = create_qline_edit(**qline_editable)
        self.ac_armor_bonus = create_qline_edit(enabled=False, **qline_editable)
        self.ac_dex_bonus = create_qline_edit(self.container, enabled=False)
        self.ac_size_bonus = create_qline_edit(**qline_editable)
        self.ac_misc_bonus = create_qline_edit(**qline_editable)
        self.ac_total_label = create_qlabel(self.container)

        self.ac_base_bonus_label = create_qlabel(self.container)
        self.ac_armor_bonus_label = create_qlabel(self.container)
        self.ac_dex_bonus_label = create_qlabel(self.container)
        self.ac_size_bonus_label = create_qlabel(self.container)
        self.ac_misc_bonus_label = create_qlabel(self.container)
        self.hp_hp_wounds_current_hp = create_qline_edit(self.container)
        self.hp_contusion = create_qline_edit(self.container)
        self.contusion_label = create_qlabel(self.container)

        self.add_to_layout()
        self.set_values_from_attributes()

    def add_to_layout(self):
        add_element_to_layout(self.layout, self.hp_total_label, 0, 1, 1, 1)
        add_element_to_layout(self.layout, self.hp_hp_wounds_current_hp_label, 0, 2, 1, 2)
        self.layout.addWidget(self.hp_hp_wounds_current_hp, 1, 2, 1, 2)
        add_element_to_layout(self.layout, self.contusion_label, 0, 4, 1, 2)
        add_element_to_layout(self.layout, self.hp_dice_label, 0, 6, 1, 2)

        add_element_to_layout(self.layout, self.hp_label, 1, 0, 1, 1)
        add_element_to_layout(self.layout, self.hp_total, 1, 1, 1, 1)
        add_element_to_layout(self.layout, self.hp_contusion, 1, 4, 1, 2)
        add_element_to_layout(self.layout, self.hp_dice, 1, 6, 1, 1)

        third_row = [self.ac_label, self.ac_total, self.ac_base,
                     self.ac_armor_bonus, self.ac_dex_bonus, self.ac_size_bonus, self.ac_misc_bonus]
        add_multiple_elements_to_layout_by_row(self.layout, third_row, row=2)

        fourth_row = [self.ac_total_label, self.ac_base_bonus_label, self.ac_armor_bonus_label,
                      self.ac_dex_bonus_label, self.ac_size_bonus_label,
                      self.ac_misc_bonus_label, ]
        add_multiple_elements_to_layout_by_row(self.layout, fourth_row, start_column=1, row=3)

    def set_values_from_attributes(self):
        self.ac_dex_bonus.setText(str(self.char_core.attributes.dex['mod']))
        self._update_ac()

    def _update_ac(self):
        update_texts(self, "ac_total",
                     ["ac_base", "ac_armor_bonus", "ac_size_bonus", "ac_misc_bonus", "ac_dex_bonus"])

    def retranslate(self):
        self.root.setTitle(QApplication.translate("HpAc" "HP / AC"))
        self.hp_total_label.setText(QApplication.translate("HpAc" "Total"))
        self.hp_hp_wounds_current_hp_label.setText(QApplication.translate("HpAc" "Wounds"))
        self.hp_label.setText(QApplication.translate("HpAc" "HP"))
        self.ac_label.setText(QApplication.translate("HpAc" "AC"))
        self.ac_total_label.setText(QApplication.translate("HpAc" "Total"))
        self.ac_base_bonus_label.setText(QApplication.translate("HpAc" "Base"))
        self.ac_armor_bonus_label.setText(QApplication.translate("HpAc" "Armor"))
        self.ac_dex_bonus_label.setText(QApplication.translate("HpAc" "Dex"))
        self.ac_size_bonus_label.setText(QApplication.translate("HpAc" "Size"))
        self.ac_misc_bonus_label.setText(QApplication.translate("HpAc", "Misc"))
        self.hp_dice_label.setText(QApplication.translate("HpAc" "Dice"))
        self.contusion_label.setText(QApplication.translate("HpAc" "Contusion"))
