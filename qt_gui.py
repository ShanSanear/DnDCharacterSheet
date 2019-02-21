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

        self.menu_bar.open_character.triggered.connect(self.open_file)
        self.menu_bar.save_character.triggered.connect(self.save_file)
        self.menu_bar.new_character.triggered.connect(self.save_file)
        self.character_file = ""
        self.connect_attrs()

    def open_file(self):
        logging.info("Opening file")
        fname = QFileDialog.getOpenFileName(self.tabs, 'Open file', Path().cwd().as_posix(),
                                            "Character file (*.json)")[0]
        self.character_file = fname
        logging.info("File opened: %s", fname)
        data_to_read = json.load(Path(fname).open())
        set_text_of_children(self, data_to_read)

    def save_file(self):
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
        new_file = QFileDialog.getSaveFileName(self.tabs, "Save file", Path().cwd().as_posix(),
                                               "Character file (*.json)")[0]
        if new_file:
            logging.info("File name: %s", new_file)
            json.dump(data_to_save, Path(new_file).open('w'), indent=4)
        else:
            logging.info("No file selected")
        self.character_file = new_file

    def connect_attrs(self):
        for attr in self.attributes_box.__dict__:
            if attr in ['str', 'dex', 'con', 'int', 'wis', 'cha']:
                attr_box_reference = getattr(self.attributes_box, attr)
                attr_box_reference.val.textChanged.connect(partial(self.changed_attributes, attr_box_reference, attr))

    def changed_attributes(self, attr_box_reference, attr_name):
        self.char_core.attributes.set_attribute(attr_name, attr_box_reference.val.text())
        attr_ref_core = getattr(self.char_core.attributes, attr_name)
        attr_box_reference.mod.setText(str(attr_ref_core["mod"]))
        self.combat_box.set_values_from_attributes()
        self.saving_throws_box.set_values_from_attributes()
        self.hp_ac_box.set_values_from_attributes()
        self.skills_box.set_values_from_attributes()
        self.items_box.set_values_from_attributes()


def init_gui():
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_EnableHighDpiScaling)
    form = MyApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    init_gui()
    # main1()
