import json
import logging
import sys
from functools import partial
from pathlib import Path

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QFileDialog

from gui.frames.qt_generic_functions import set_text_of_children
from gui.main_window import MainWindowUi


class MyApp(MainWindowUi):
    def __init__(self):
        MainWindowUi.__init__(self)
        self.character_file = ""

    def open_file(self):
        logging.info("Opening file")
        fname = QFileDialog.getOpenFileName(self.tabs, 'Open file', Path().cwd().as_posix(),
                                            "Character file (*.json)")[0]
        if not fname:
            logging.debug("No file opened.")
            return

        self.character_file = fname

        data_to_read = json.load(Path(fname).open())
        set_text_of_children(self, data_to_read)
        logging.info("File opened: %s", fname)
        self.weapons_box.melee_weapons_box.update_choice_text()
        self.weapons_box.ranged_weapons_box.update_choice_text()

    def create_new_character(self):
        # TODO Logic and data for this
        logging.debug("Cleaning character sheet")


    def save_file(self):
        if not self.character_file:
            self.save_file_as()
        else:
            self._save_file()

    def save_file_as(self):
        logging.debug("Saving file as...")
        default_path = Path().cwd()
        if self.character_file:
            default_path = default_path / self.character_file
        default_path = default_path.as_posix()
        new_file = QFileDialog.getSaveFileName(self.tabs, "Save file", default_path,
                                               "Character file (*.json)")[0]
        if not new_file:
            logging.info("No file selected")
            return
        logging.info("File name: %s", new_file)
        self.character_file = new_file
        self._save_file()

    def _save_file(self):
        logging.info("Saving file")
        data_to_save = {"basic_info_box": self.basic_info_box.get_dict_repr(),
                        "feats_box": self.feats_box.get_dict_repr(), "items_box": self.items_box.get_dict_repr(),
                        "known_spells_box": self.known_spells_box.get_dict_repr(),
                        "languages_box": self.languages_box.get_dict_repr(),
                        "notes_box": self.notes_box.get_dict_repr(),
                        "combat_box": self.combat_box.get_dict_repr(),
                        "hp_ac_box": self.hp_ac_box.get_dict_repr(),
                        "saving_throws_box": self.saving_throws_box.get_dict_repr(),
                        "number_of_spells_box": self.number_of_spells_box.get_dict_repr(),
                        "spells_per_day_box": self.spells_per_day_box.get_dict_repr(),
                        "skills_box": self.skills_box.get_dict_repr(),
                        "attributes_box": self.attributes_box.get_dict_repr(),
                        "armor_items_box": self.armor_items_box.get_dict_repr(),
                        "weapons_box": self.weapons_box.get_dict_repr(),
                        }
        json.dump(data_to_save, Path(self.character_file).open('w'), indent=4)
        logging.debug("Saved character to file: %s", self.character_file)


    def connect_attrs(self):
        for attr in self.attributes_box.__dict__:
            if attr in ['str', 'dex', 'con', 'int', 'wis', 'cha']:
                attr_from_qt_attrs = getattr(self.attributes_box, attr)
                attr_from_qt_attrs.val.textChanged.connect(partial(self.changed_attributes, attr_from_qt_attrs, attr))
                attr_from_qt_attrs.temp_val.textChanged.connect(
                    partial(self.changed_temp_attributes, attr_from_qt_attrs, attr))

    def changed_attributes(self, attr_from_qt_attrs, attr_name):
        self.char_core.attributes.set_attribute(f"base_{attr_name}", attr_from_qt_attrs.val.text())
        base_attr_ref = getattr(self.char_core.attributes, f"base_{attr_name}")
        attr_from_qt_attrs.mod.setText(str(base_attr_ref["mod"]))
        self._setting_values_from_attributes()

    def changed_temp_attributes(self, attr_from_qt_attrs, attr_name):
        value = attr_from_qt_attrs.temp_val.text()
        self.char_core.attributes.set_temp_attribute(attr_name, value)
        attr_ref_core = getattr(self.char_core.attributes, attr_name)
        if value and not value.strip() == '0':
            attr_from_qt_attrs.temp_mod.setText(str(attr_ref_core["mod"]))
        else:
            attr_from_qt_attrs.temp_mod.setText("")
            self.changed_attributes(attr_from_qt_attrs, attr_name)
        self._setting_values_from_attributes()

    def _setting_values_from_attributes(self):
        self.combat_box.set_values_from_attributes()
        self.saving_throws_box.set_values_from_attributes()
        self.hp_ac_box.set_values_from_attributes()
        self.skills_box.set_values_from_attributes()
        self.items_box.set_values_from_attributes()

    def change_language(self):
        logging.debug("Changing language")
        language_data = json.load(Path("data/languages.json").open(encoding='utf-8'))
        # TODO FULL armors translation
        if self.menu_bar.change_language_en.isChecked():
            set_text_of_children(self, language_data["EN"])
        else:
            set_text_of_children(self, language_data["PL"])



class SingleCharApp(MyApp):
    def __init__(self):
        super(SingleCharApp, self).__init__()
        self.menu_bar.open_character.triggered.connect(self.open_file)
        self.menu_bar.save_character_as.triggered.connect(self.save_file_as)
        self.menu_bar.save_character.triggered.connect(self.save_file)
        self.menu_bar.new_character.triggered.connect(self.create_new_character)
        self.menu_bar.language_menu.triggered.connect(self.change_language)
        self.connect_attrs()
        self.dump_weapons_box_json()

    def dump_weapons_box_json(self):
        d = {
            "weapons_box": {
                "ranged_weapons_box": self.weapons_box.ranged_weapons_box.translate_reference["EN"],
                "melee_weapons_box": self.weapons_box.melee_weapons_box.translate_reference["EN"]
            }

        }
        json.dump(d, Path("test.json").open('w', encoding='utf-8', newline='\n'), indent=4)




def init_gui():
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_EnableHighDpiScaling)
    form = SingleCharApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    init_gui()
    # main1()
