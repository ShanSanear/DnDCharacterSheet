from types import SimpleNamespace

from PyQt5 import QtWidgets, QtCore

from gui.frames.qt_generic_classes import DefaultBox
from gui.frames.qt_generic_functions import create_qline_edit, create_qlabel, create_combo_box, \
    add_multiple_elements_to_layout_by_row, set_text_of_children
from gui.frames.tab_1.qt_weapon_statistics import WeaponStatisticsBox


class WeaponsBox(DefaultBox):
    # TODO - more than 3 choices for weapons
    # TODO Generalize melee/ranged weapon as classes / general function
    def __init__(self, parent, position, size, weapons_statistics_box: WeaponStatisticsBox):
        self.root = QtWidgets.QGroupBox(parent)
        self.root.setGeometry(QtCore.QRect(*position, *size))
        self.root.setObjectName("WeaponsBox")
        self.weapons_statistics_box = weapons_statistics_box

        self.melee_box = QtWidgets.QGroupBox(self.root)
        self.melee_box.setGeometry(QtCore.QRect(10, 60, 591, 161))
        self.melee_box.setMaximumSize(QtCore.QSize(591, 44444))
        self.melee_box.setObjectName("CurrentMeleeWeaponBox")
        self.melee_container = QtWidgets.QWidget(self.melee_box)
        self.melee_container.setGeometry(QtCore.QRect(11, 21, 571, 121))
        self.melee_container.setObjectName("layoutWidget3")
        self.melee_layout = QtWidgets.QGridLayout(self.melee_container)
        self.melee_layout.setContentsMargins(9, 9, 9, 9)
        self.melee_layout.setSpacing(6)
        self.melee_layout.setObjectName("MeleeWeapon")
        melee_weapon_qedit = dict(parent=self.melee_container,
                                  function_on_text_changed=self.save_melee_weapon,
                                  min_size=(0, 23), max_size=(138, 20))
        melee_weapon_qlabel = dict(parent=self.melee_container, max_size=(138, 16))
        self.melee_weapons = []
        self.ranged_weapons = []

        for _ in range(3):
            self.melee_weapons.append(self.create_melee_weapon())

        for _ in range(3):
            self.ranged_weapons.append(self.create_ranged_weapon())

        self.translate_reference = {
            "EN":
                {
                    "root": {
                        "title": "Weapons"
                    },
                    "melee_box": {
                        "title": "Currently chosen melee weapon"
                    },
                    "ranged_box": {
                        "title": "Currently chosen ranged weapon"
                    },
                    "melee_weapon_name_label": "Name",
                    "melee_weapon_attack_bonus_label": "Attack bonus",
                    "melee_weapon_damage_roll_label": "Damage roll",
                    "melee_weapon_crit_label": "Critical roll / multiplier",
                    "melee_weapon_special_label": "Special",
                    "melee_weapon_weight_label": "Weight",
                    "melee_weapon_size_label": "Size",
                    "melee_weapon_type_label": "Type",
                    "melee_choice": {
                        "choices": ["Melee weapon 1", "Melee weapon 2", "Melee weapon 3"]
                    },
                    "ranged_choice": {
                        "choices": ["Ranged weapon 1", "Ranged weapon 2", "Ranged weapon 3"]
                    },

                    "ranged_weapon_crit_label": "Critical roll / multiplier",
                    "ranged_weapon_damage_roll_label": "Damage roll",
                    "ranged_weapon_range_label": "Range",
                    "ranged_weapon_name_label": "Name",
                    "ranged_weapon_attack_bonus_label": "Attack bonus",
                    "ranged_weapon_special_label": "Special",
                    "ranged_weapon_ammo_label": "Ammo",
                    "ranged_weapon_weight_label": "Weight",
                    "ranged_weapon_size_label": "Size",
                    "ranged_weapon_type_label": "Type"}}

        self.current_melee = SimpleNamespace()

        self.current_melee.name = create_qline_edit("melee_weapon_name", args_on_text_changed=["name"],
                                                    **melee_weapon_qedit)
        self.current_melee.attack_bonus = create_qline_edit("melee_weapon_attack_bonus",
                                                            args_on_text_changed=["attack_bonus"],
                                                            **melee_weapon_qedit)
        self.current_melee.damage_roll = create_qline_edit("melee_weapon_damage_roll",
                                                           args_on_text_changed=["damage_roll"],
                                                           **melee_weapon_qedit)
        self.current_melee.crit = create_qline_edit("melee_weapon_crit",
                                                    args_on_text_changed=["crit"],
                                                    **melee_weapon_qedit)
        self.current_melee.special = create_qline_edit("melee_weapon_special",
                                                       args_on_text_changed=["special"],
                                                       **melee_weapon_qedit)
        self.current_melee.weight = create_qline_edit("melee_weapon_weight",
                                                      args_on_text_changed=["weight"],
                                                      **melee_weapon_qedit)
        self.current_melee.size = create_qline_edit("melee_weapon_size",
                                                    args_on_text_changed=["size"],
                                                    **melee_weapon_qedit)
        self.current_melee.type = create_qline_edit("melee_weapon_type",
                                                    args_on_text_changed=["type"],
                                                    **melee_weapon_qedit)

        self.melee_choice = create_combo_box("weapons_melee_choice", self.root, 3, min_size=[171, 22],
                                             function_on_index_changed=self.change_melee_weapon)
        self.melee_choice.move(20, 30)
        self.melee_weapon_name_label = create_qlabel("melee_weapon_name_label", **melee_weapon_qlabel)
        self.melee_weapon_attack_bonus_label = create_qlabel("melee_weapon_attack_bonus_label", **melee_weapon_qlabel)
        self.melee_weapon_damage_roll_label = create_qlabel("melee_weapon_damage_roll_label", **melee_weapon_qlabel)
        self.melee_weapon_crit_label = create_qlabel("melee_weapon_crit_label", **melee_weapon_qlabel)
        self.melee_weapon_special_label = create_qlabel("melee_weapon_special_label", **melee_weapon_qlabel)
        self.melee_weapon_weight_label = create_qlabel("melee_weapon_weight_label", **melee_weapon_qlabel)
        self.melee_weapon_size_label = create_qlabel("melee_weapon_size_label", **melee_weapon_qlabel)
        self.melee_weapon_type_label = create_qlabel("melee_weapon_type_label", **melee_weapon_qlabel)

        self.ranged_choice = create_combo_box("weapons_ranged_choice", self.root, 3, min_size=[171, 22],
                                              function_on_index_changed=self.change_ranged_weapon)
        self.ranged_choice.move(20, 230)

        self.ranged_box = QtWidgets.QGroupBox(self.root)
        self.ranged_box.setGeometry(QtCore.QRect(10, 260, 591, 151))
        self.ranged_box.setObjectName("CurrentRangedWeaponBox")
        self.ranged_container = QtWidgets.QWidget(self.ranged_box)
        self.ranged_container.setGeometry(QtCore.QRect(10, 20, 571, 111))
        self.ranged_container.setObjectName("gridLayoutWidget_17")
        self.ranged_layout = QtWidgets.QGridLayout(self.ranged_container)
        self.ranged_layout.setContentsMargins(9, 9, 9, 9)
        self.ranged_layout.setSpacing(6)
        self.ranged_layout.setObjectName("RangedWeapon")

        ranged_weapon_qlabel = dict(parent=self.ranged_container)
        ranged_weapon_qedit = dict(parent=self.ranged_container, min_size=(0, 23),
                                   function_on_text_changed=self.save_ranged_weapon)

        self.ranged_weapon_crit_label = create_qlabel("ranged_weapon_crit_label", **ranged_weapon_qlabel)
        self.ranged_weapon_damage_roll_label = create_qlabel("ranged_weapon_damage_roll_label", **ranged_weapon_qlabel)
        self.ranged_weapon_range_label = create_qlabel("ranged_weapon_range_label", **ranged_weapon_qlabel)
        self.ranged_weapon_name_label = create_qlabel("ranged_weapon_name_label", **ranged_weapon_qlabel)
        self.ranged_weapon_attack_bonus_label = create_qlabel("ranged_weapon_attack_bonus_label",
                                                              **ranged_weapon_qlabel)
        self.ranged_weapon_special_label = create_qlabel("ranged_weapon_special_label", **ranged_weapon_qlabel)
        self.ranged_weapon_ammo_label = create_qlabel("ranged_weapon_ammo_label", **ranged_weapon_qlabel)
        self.ranged_weapon_weight_label = create_qlabel("ranged_weapon_weight_label", **ranged_weapon_qlabel)
        self.ranged_weapon_size_label = create_qlabel("ranged_weapon_size_label", **ranged_weapon_qlabel)
        self.ranged_weapon_type_label = create_qlabel("ranged_weapon_type_label", **ranged_weapon_qlabel)

        self.current_ranged = SimpleNamespace()
        self.current_ranged.name = create_qline_edit("ranged_weapon_name", args_on_text_changed=["name"],
                                                     **ranged_weapon_qedit)
        self.current_ranged.attack_bonus = create_qline_edit("ranged_weapon_attack_bonus",
                                                             args_on_text_changed=["attack_bonus"],
                                                             **ranged_weapon_qedit)
        self.current_ranged.damage_roll = create_qline_edit("ranged_weapon_damage_roll",
                                                            args_on_text_changed=["damage_roll"],
                                                            **ranged_weapon_qedit)
        self.current_ranged.crit = create_qline_edit("ranged_weapon_crit",
                                                     args_on_text_changed=["crit"],
                                                     **ranged_weapon_qedit)
        self.current_ranged.range = create_qline_edit("ranged_weapon_range",
                                                      args_on_text_changed=["range"],
                                                      **ranged_weapon_qedit)
        self.current_ranged.special = create_qline_edit("ranged_weapon_special",
                                                        args_on_text_changed=["special"],
                                                        **ranged_weapon_qedit)
        self.current_ranged.ammo = create_qline_edit("ranged_weapon_ammo",
                                                     args_on_text_changed=["ammo"],
                                                     **ranged_weapon_qedit)
        self.current_ranged.weight = create_qline_edit("ranged_weapon_weight",
                                                       args_on_text_changed=["weight"],
                                                       **ranged_weapon_qedit)
        self.current_ranged.size = create_qline_edit("ranged_weapon_size",
                                                     args_on_text_changed=["size"],
                                                     **ranged_weapon_qedit)
        self.current_ranged.type = create_qline_edit("ranged_weapon_type",
                                                     args_on_text_changed=["type"],
                                                     **ranged_weapon_qedit)

        self.current_weapons = [self.current_melee, self.current_ranged]
        self.add_to_layout()
        self.translate("EN")
        self.change_melee_weapon()
        self.change_ranged_weapon()
        # self.root.setLayout(self.layout)

    def add_to_ranged_layout(self):
        first_row = [self.ranged_weapon_name_label, self.ranged_weapon_attack_bonus_label,
                     self.ranged_weapon_damage_roll_label, self.ranged_weapon_crit_label,
                     self.ranged_weapon_range_label, ]
        add_multiple_elements_to_layout_by_row(self.ranged_layout, first_row)

        second_row = [self.current_ranged.name, self.current_ranged.attack_bonus, self.current_ranged.damage_roll,
                      self.current_ranged.crit, self.current_ranged.range, ]
        add_multiple_elements_to_layout_by_row(self.ranged_layout, second_row, row=1)

        third_row = [self.ranged_weapon_special_label, self.ranged_weapon_ammo_label, self.ranged_weapon_weight_label,
                     self.ranged_weapon_size_label, self.ranged_weapon_type_label, ]
        add_multiple_elements_to_layout_by_row(self.ranged_layout, third_row, row=2)

        fourth_row = [self.current_ranged.special, self.current_ranged.ammo, self.current_ranged.weight,
                      self.current_ranged.size, self.current_ranged.type, ]
        add_multiple_elements_to_layout_by_row(self.ranged_layout, fourth_row, row=3)

    def add_to_melee_layout(self):
        first_row = [self.melee_weapon_name_label, self.melee_weapon_attack_bonus_label,
                     self.melee_weapon_damage_roll_label, self.melee_weapon_crit_label, ]
        add_multiple_elements_to_layout_by_row(self.melee_layout, first_row)

        second_row = [self.current_melee.name, self.current_melee.attack_bonus, self.current_melee.damage_roll,
                      self.current_melee.crit, ]
        add_multiple_elements_to_layout_by_row(self.melee_layout, second_row, row=1)

        third_row = [self.melee_weapon_special_label, self.melee_weapon_weight_label, self.melee_weapon_size_label,
                     self.melee_weapon_type_label]
        add_multiple_elements_to_layout_by_row(self.melee_layout, third_row, row=2)

        fourth_row = [self.current_melee.special, self.current_melee.weight, self.current_melee.size,
                      self.current_melee.type, ]
        add_multiple_elements_to_layout_by_row(self.melee_layout, fourth_row, row=3)

    def translate(self, language):
        set_text_of_children(self, self.translate_reference[language])

    def add_to_layout(self):
        self.add_to_melee_layout()
        self.add_to_ranged_layout()

    def create_melee_weapon(self):
        melee_weapon = SimpleNamespace()
        attributes = ["name", "attack_bonus", "damage_roll", "crit", "special", "weight", "size", "type"]
        for attribute in attributes:
            if attribute == "name":
                setattr(melee_weapon, attribute, "Dummy name")
            else:
                setattr(melee_weapon, attribute, "")
        return melee_weapon

    def create_ranged_weapon(self):
        ranged_weapon = SimpleNamespace()
        attributes = ["name", "attack_bonus", "damage_roll", "crit", "range",
                      "special", "ammo", "weight", "size", "type"]
        for attribute in attributes:
            if attribute == "name":
                setattr(ranged_weapon, attribute, "Dummy name")
            else:
                setattr(ranged_weapon, attribute, "")
        return ranged_weapon

    def change_melee_weapon(self):
        idx = self.melee_choice.currentIndex()
        chosen_weapon = self.melee_weapons[idx]
        for attribute, value in chosen_weapon.__dict__.items():
            obj_ref = getattr(self.current_melee, attribute)
            obj_ref.setText(value)

    def save_melee_weapon(self, attribute):
        idx = self.melee_choice.currentIndex()
        chosen_weapon = self.melee_weapons[idx]
        print("Chosen weapon before: %s" % chosen_weapon)
        new_val = getattr(self.current_melee, attribute).text()
        setattr(chosen_weapon, attribute, new_val)
        if attribute == "name":
            self.melee_choice.setItemText(idx, chosen_weapon.name)
        elif attribute == "damage_roll":
            self.weapons_statistics_box.melee_damage.setText(new_val)
        elif attribute == "crit":
            self.weapons_statistics_box.melee_crit.setText(new_val)
        elif attribute == "attack_bonus":
            try:
                val = int(new_val)
            except ValueError:
                val = 0
            self.weapons_statistics_box.bonus_from_melee = val
            self.weapons_statistics_box.set_values_for_melee()


        print("Chosen weapon after: %s" % chosen_weapon)


    def change_ranged_weapon(self):
        idx = self.ranged_choice.currentIndex()
        chosen_weapon = self.ranged_weapons[idx]
        for attribute, value in chosen_weapon.__dict__.items():
            obj_ref = getattr(self.current_ranged, attribute)
            obj_ref.setText(value)

    def save_ranged_weapon(self, attribute):
        idx = self.ranged_choice.currentIndex()
        chosen_weapon = self.ranged_weapons[idx]
        print("Chosen weapon before: %s" % chosen_weapon)
        new_val = getattr(self.current_ranged, attribute).text()
        setattr(chosen_weapon, attribute, new_val)
        if attribute == "name":
            self.ranged_choice.setItemText(idx, chosen_weapon.name)
        elif attribute == "damage_roll":
            self.weapons_statistics_box.ranged_damage.setText(new_val)
        elif attribute == "crit":
            self.weapons_statistics_box.ranged_crit.setText(new_val)
        elif attribute == "attack_bonus":
            try:
                val = int(new_val)
            except ValueError:
                val = 0
            self.weapons_statistics_box.bonus_from_ranged = val
            self.weapons_statistics_box.set_values_for_ranged()

        print("Chosen weapon after: %s" % chosen_weapon)
