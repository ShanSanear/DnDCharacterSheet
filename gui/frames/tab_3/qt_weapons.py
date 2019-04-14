import logging
from types import SimpleNamespace

from PyQt5 import QtCore
from PyQt5.QtWidgets import QGroupBox, QWidget, QVBoxLayout, QComboBox, QApplication

from gui.frames.qt_generic_classes import DefaultBox, BoxType
from gui.frames.qt_generic_functions import create_qline_edit, create_qlabel, create_combo_box, \
    add_multiple_elements_to_layout_by_row, create_push_button, try_to_get_float
from gui.frames.tab_1.qt_weapon_statistics import WeaponStatisticsBox
from gui.frames.tab_2.qt_items import ItemsBox


class Weapons(BoxType, DefaultBox):
    choice: QComboBox

    def __init__(self, parent, position, size, weapons_statistics_box, label_dict, weapon_attributes, ):
        self.main_widget = QWidget(parent)
        self.main_widget.setGeometry(QtCore.QRect(*position, *size))
        logging.debug("Position: %s, class: %s", position, self.__class__)
        logging.debug("Size: %s, class: %s", size, self.__class__)
        inner_position = [10, 60]
        inner_size = [size[0] - 20, size[1] - 60]
        logging.debug("Inner position: %s, class: %s", inner_position, self.__class__)
        logging.debug("Inner size: %s, class: %s", inner_size, self.__class__)
        BoxType.__init__(self, parent=self.main_widget, position=inner_position, size=inner_size, defaults=False)
        self.weapon_attributes = weapon_attributes
        self.weapons_statistics_box = weapons_statistics_box
        self.qedit_dict = dict(parent=self.container,
                               function_on_text_changed=self.save_weapon,
                               min_size=(0, 23), max_size=(138, 20))
        label_dict.update(dict(parent=self.container))
        self.name_label = create_qlabel(**label_dict)
        self.attack_bonus_label = create_qlabel(**label_dict)
        self.damage_roll_label = create_qlabel(**label_dict)
        self.crit_label = create_qlabel(**label_dict)
        self.special_label = create_qlabel(**label_dict)
        self.weight_label = create_qlabel(**label_dict)
        self.size_label = create_qlabel(**label_dict)
        self.type_label = create_qlabel(**label_dict)

        self.weapons = []
        self.choice = create_combo_box(parent=self.main_widget, number_of_choices=1, min_size=[171, 22],
                                       max_size=[None, 22], function_on_index_changed=self.change_weapon)
        self.choice.move(20, 20)
        self.add = create_push_button("melee_add", parent=self.main_widget, text="+", max_size=[24, 24],
                                      function_on_clicked=self.add_new_element)
        self.add.move(200, 20)
        self.remove = create_push_button("melee_remove", parent=self.main_widget, text="-", max_size=[24, 24],
                                         function_on_clicked=self._remove_weapon)
        self.remove.move(230, 20)
        self.current_weapon = SimpleNamespace()
        self.first_row_label = []
        self.first_row_edit = []
        self.second_row_label = []
        self.second_row_edit = []
        self.total_weight = 0

    def create_current_weapon(self):
        self.current_weapon.name = create_qline_edit(args_on_text_changed=["name"],
                                                     function_on_unfocused=self._sort_weapon_by_name,
                                                     **self.qedit_dict)
        self.current_weapon.attack_bonus = create_qline_edit(args_on_text_changed=["attack_bonus"], **self.qedit_dict)
        self.current_weapon.damage_roll = create_qline_edit(args_on_text_changed=["damage_roll"], **self.qedit_dict)
        self.current_weapon.crit = create_qline_edit(args_on_text_changed=["crit"], **self.qedit_dict)
        self.current_weapon.special = create_qline_edit(args_on_text_changed=["special"], **self.qedit_dict)
        self.current_weapon.weight = create_qline_edit(args_on_text_changed=["weight"], **self.qedit_dict)
        self.current_weapon.size = create_qline_edit(args_on_text_changed=["size"], **self.qedit_dict)
        self.current_weapon.type = create_qline_edit(args_on_text_changed=["type"], **self.qedit_dict)

    def save_weapon(self, attribute):
        pass

    def update_choice_text(self):
        for idx, weapon in enumerate(self.weapons):
            self.choice.setItemText(idx, weapon.name)

    def create_weapon(self):
        weapon = SimpleNamespace()
        for attribute in self.weapon_attributes:
            if attribute == "name":
                setattr(weapon, attribute, "Dummy name")
            else:
                setattr(weapon, attribute, "")
        return weapon

    def add_new_element(self):
        logging.debug("Adding new weapon")
        new_weapon = self.create_weapon()
        new_name_count = sum(["New weapon" in weapon.name for weapon in self.weapons])
        new_name = f"New weapon {new_name_count}"
        new_weapon.name = new_name
        self.weapons.append(new_weapon)
        self.choice.addItem(new_name)
        self.choice.setCurrentIndex(len(self.weapons) - 1)

    def add_to_layout(self):
        add_multiple_elements_to_layout_by_row(self.layout, self.first_row_label)
        add_multiple_elements_to_layout_by_row(self.layout, self.first_row_edit, row=1)
        add_multiple_elements_to_layout_by_row(self.layout, self.second_row_label, row=2)
        add_multiple_elements_to_layout_by_row(self.layout, self.second_row_edit, row=3)

    def change_weapon(self):
        idx = self.choice.currentIndex()
        chosen_weapon = self.weapons[idx]
        for attribute, value in chosen_weapon.__dict__.items():
            obj_ref = getattr(self.current_weapon, attribute)
            obj_ref.setText(value)

    def _sort_weapon_by_name(self):
        chosen_weapon = self.weapons[self.choice.currentIndex()]
        self.weapons = sorted(self.weapons, key=lambda x: x.name)
        for idx, weapon in enumerate(self.weapons):
            if chosen_weapon == weapon:
                self.choice.setCurrentIndex(idx)

    def _remove_weapon(self):
        idx = self.choice.currentIndex()
        if idx == 0 and len(self.weapons) == 1:
            logging.warning("At least one weapon needs to be provided")
            return
        del self.weapons[idx]
        self.choice.removeItem(idx)
        self.choice.setCurrentIndex(0)
        self._sort_weapon_by_name()

    def update_total_weight(self):
        pass

    def set_default_state(self):
        count = self.choice.count()
        for idx in reversed(range(count)):
            self.choice.removeItem(idx)
        self.weapons = []
        self.add_new_element()

    def retranslate(self):
        self.name_label.setText(QApplication.translate("Weapons", "Name"))
        self.attack_bonus_label.setText(QApplication.translate("Weapons", "Attack bonus"))
        self.damage_roll_label.setText(QApplication.translate("Weapons", "Damage roll"))
        self.crit_label.setText(QApplication.translate("Weapons", "Critical roll / multiplier"))
        self.special_label.setText(QApplication.translate("Weapons", "Special"))
        self.weight_label.setText(QApplication.translate("Weapons", "Weight"))
        self.size_label.setText(QApplication.translate("Weapons", "Size"))
        self.type_label.setText(QApplication.translate("Weapons", "Type"))


class MeleeWeapon(Weapons):
    def __init__(self, parent, position, size, weapons_statistics_box: WeaponStatisticsBox, items_box: ItemsBox):
        weapon_attributes = ["name", "attack_bonus", "damage_roll", "crit", "special", "weight", "size", "type"]
        melee_weapon_qlabel = dict(max_size=(138, 16))
        super(MeleeWeapon, self).__init__(parent=parent, position=position, size=size,
                                          label_dict=melee_weapon_qlabel, weapons_statistics_box=weapons_statistics_box,
                                          weapon_attributes=weapon_attributes)
        self.items_box = items_box
        self.create_current_weapon()
        self.fill_row_lists()
        self.add_to_layout()
        self.weapons.append(self.create_weapon())
        self.change_weapon()
        self._sort_weapon_by_name()

    def fill_row_lists(self):
        self.first_row_label = [self.name_label, self.attack_bonus_label, self.damage_roll_label, self.crit_label]
        self.first_row_edit = [self.current_weapon.name, self.current_weapon.attack_bonus,
                               self.current_weapon.damage_roll, self.current_weapon.crit, ]
        self.second_row_label = [self.special_label, self.weight_label, self.size_label, self.type_label]
        self.second_row_edit = [self.current_weapon.special, self.current_weapon.weight,
                                self.current_weapon.size, self.current_weapon.type, ]

    def update_total_weight(self):
        total_weight = 0
        for weapon in self.weapons:
            total_weight += try_to_get_float(weapon.weight, 0)
        self.items_box.melee_weapons_weight = total_weight
        self.items_box.calculate_weight()

    def save_weapon(self, attribute):
        idx = self.choice.currentIndex()
        chosen_weapon = self.weapons[idx]
        logging.debug("Chosen weapon before: %s", chosen_weapon)
        new_val = getattr(self.current_weapon, attribute).text()
        setattr(chosen_weapon, attribute, new_val)
        if attribute == "name":
            self.weapons_statistics_box.melee_name.setText(new_val)
            self.choice.setItemText(idx, new_val)
        elif attribute == "damage_roll":
            self.weapons_statistics_box.melee_damage.setText(new_val)
        elif attribute == "crit":
            self.weapons_statistics_box.melee_crit.setText(new_val)
        elif attribute == "attack_bonus":
            self.weapons_statistics_box.melee_attack_bonus.setText(new_val)
        elif attribute == "weight":
            self.update_total_weight()
        self.update_choice_text()

    def retranslate(self):
        super(MeleeWeapon, self).retranslate()
        self.root.setTitle(QApplication.translate("Weapons", "Currently chose melee weapon"))


class RangedWeapon(Weapons):
    def __init__(self, parent, position, size, weapons_statistics_box: WeaponStatisticsBox, items_box: ItemsBox):
        weapon_attributes = ["name", "attack_bonus", "damage_roll", "crit", "range",
                             "special", "ammo", "weight", "size", "type"]
        ranged_weapon_qlabel = {}
        super(RangedWeapon, self).__init__(parent=parent, position=position, size=size,
                                           label_dict=ranged_weapon_qlabel,
                                           weapons_statistics_box=weapons_statistics_box,
                                           weapon_attributes=weapon_attributes)
        self.range_label = create_qlabel(**ranged_weapon_qlabel)
        self.ammo_label = create_qlabel(**ranged_weapon_qlabel)
        self.items_box = items_box
        self.create_current_weapon()
        self.fill_row_lists()
        self.add_to_layout()
        self.weapons.append(self.create_weapon())
        self.change_weapon()
        self._sort_weapon_by_name()

    def create_current_weapon(self):
        super(RangedWeapon, self).create_current_weapon()
        ranged_weapon_qedit = dict(parent=self.container, min_size=(0, 23),
                                   function_on_text_changed=self.save_weapon)
        self.current_weapon.range = create_qline_edit(args_on_text_changed=["range"],
                                                      **ranged_weapon_qedit)
        self.current_weapon.ammo = create_qline_edit(args_on_text_changed=["ammo"],
                                                     **ranged_weapon_qedit)

    def fill_row_lists(self):
        self.first_row_label = [self.name_label, self.attack_bonus_label, self.damage_roll_label, self.crit_label,
                                self.range_label]
        self.first_row_edit = [self.current_weapon.name, self.current_weapon.attack_bonus,
                               self.current_weapon.damage_roll, self.current_weapon.crit, self.current_weapon.range]
        self.second_row_label = [self.special_label, self.ammo_label, self.weight_label,
                                 self.size_label, self.type_label]
        self.second_row_edit = [self.current_weapon.special, self.current_weapon.ammo, self.current_weapon.weight,
                                self.current_weapon.size, self.current_weapon.type, ]

    def update_total_weight(self):
        total_weight = 0
        for weapon in self.weapons:
            total_weight += try_to_get_float(weapon.weight, 0)
        self.items_box.ranged_weapons_weight = total_weight
        self.items_box.calculate_weight()

    def save_weapon(self, attribute):
        idx = self.choice.currentIndex()
        chosen_weapon = self.weapons[idx]
        logging.debug("Chosen weapon before: %s", chosen_weapon)
        new_val = getattr(self.current_weapon, attribute).text()
        setattr(chosen_weapon, attribute, new_val)
        if attribute == "name":
            self.weapons_statistics_box.ranged_name.setText(new_val)
        elif attribute == "damage_roll":
            self.weapons_statistics_box.ranged_damage.setText(new_val)
        elif attribute == "crit":
            self.weapons_statistics_box.ranged_crit.setText(new_val)
        elif attribute == "attack_bonus":
            self.weapons_statistics_box.ranged_attack_bonus.setText(new_val)
        elif attribute == "range":
            self.weapons_statistics_box.ranged_range.setText(new_val)
        elif attribute == "weight":
            self.update_total_weight()
        self.update_choice_text()

    def retranslate(self):
        super(RangedWeapon, self).retranslate()
        self.root.setTitle(QApplication.translate("Weapons", "Currently chosen ranged weapon"))
        self.ammo_label.setText(QApplication.translate("Weapons", "Ammo"))
        self.range_label.setText(QApplication.translate("Weapons", "Range"))


class WeaponsBox:
    def __init__(self, parent, position, size, weapons_statistics_box: WeaponStatisticsBox, items_box: ItemsBox):
        self.root = QGroupBox(parent)
        self.root.setGeometry(QtCore.QRect(*position, *size))
        self.container = QWidget(self.root)
        self.container.setGeometry(QtCore.QRect(*position, size[0], size[1] / 2))
        self.layout = QVBoxLayout(self.root)

        box_size = [size[0], size[1] / 2 - 20]
        self.melee_weapons_box = MeleeWeapon(parent=self.root, position=[0, 0], size=box_size,
                                             weapons_statistics_box=weapons_statistics_box, items_box=items_box)
        self.ranged_weapons_box = RangedWeapon(parent=self.root, position=[0, size[1] / 2], size=box_size,
                                               weapons_statistics_box=weapons_statistics_box, items_box=items_box)

    def get_dict_repr(self):
        return {"melee_weapons_box": self.melee_weapons_box.get_dict_repr(),
                "ranged_weapons_box": self.ranged_weapons_box.get_dict_repr()}

    def retranslate(self):
        self.root.setTitle(QApplication.translate("Weapons", "Weapons"))
        self.melee_weapons_box.retranslate()
        self.ranged_weapons_box.retranslate()
