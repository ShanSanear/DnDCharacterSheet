import json
import logging
from functools import partial
from pathlib import Path

from PyQt5.QtWidgets import QFileDialog, QMessageBox

from gui.frames.qt_generic_functions import set_text_of_children
from gui.main_window import MainWindowUi


class MyApp(MainWindowUi):

    def __init__(self):
        MainWindowUi.__init__(self)
        self.character_file = ""
        self.tab_name = "New char"
        self.connect_attrs()

    def open_file(self):
        if self.character_file:
            proceed = QMessageBox.question(self,
                                           "Overwriting old data",
                                           "Opening new character file will overwrite all data in sheet. Continue?",
                                           QMessageBox.Yes, QMessageBox.No)
            if proceed == QMessageBox.No:
                return
        logging.info("Opening file")
        fname = QFileDialog.getOpenFileName(self.tabs, 'Open file', Path().cwd().as_posix(),
                                            "Character file (*.json)")[0]
        if not fname:
            logging.debug("No file opened.")
            return

        self.character_file = fname

        data_to_read = json.load(Path(fname).open())
        self._clean_character_sheet()
        try:
            set_text_of_children(self, data_to_read)
        except (AttributeError, TypeError, IndexError) as e:
            logging.error("Couldnt load file: %s. Error: %s", self.character_file, e)
            return
        logging.info("File opened: %s", fname)
        self.weapons_box.melee_weapons_box.update_choice_text()
        self.weapons_box.ranged_weapons_box.update_choice_text()

    def create_new_character(self):
        proceed = QMessageBox.question(self, "Continue?",
                                       "This will clear character sheet. Continue?", QMessageBox.Yes, QMessageBox.No)
        if proceed == QMessageBox.Yes:
            self._clean_character_sheet()

    def _clean_character_sheet(self):
        logging.debug("Cleaning character sheet")
        self.character_file = ""
        self.feats_box.set_default_state()
        self.known_spells_box.set_default_state()
        self.items_box.set_default_state()
        self.skills_box.set_default_state()
        self.weapons_box.melee_weapons_box.set_default_state()
        self.weapons_box.ranged_weapons_box.set_default_state()
        defaults_data = json.load(Path("data/defaults.json").open('r', encoding='utf-8'))
        set_text_of_children(self, defaults_data)

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


def config_logger(logging_level):
    logging.basicConfig(level=logging_level, style="%",
                        format="%(asctime)s %(levelname)s %(module)s %(funcName)s: %(lineno)d %(message)s",
                        datefmt="%H:%M:%S")
