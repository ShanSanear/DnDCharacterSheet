import json
import sys
from pathlib import Path

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog

from qt_gui.boxes.qt_generic_functions import set_text_of_children
from qt_gui.main_window import MainWindowUi


class MyApp(QMainWindow, MainWindowUi):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setup_ui(self)

        # self.push_button.clicked.connect(self.do_stuff)
        # self.basic_info_box.name.textChanged.connect(partial(self.changed_text, self.feats_box))
        self.menu_bar.open_character.triggered.connect(self.open_file)
        self.menu_bar.save_character.triggered.connect(self.save_file)
        self.menu_bar.new_character.triggered.connect(self.save_file)
        self.character_file = ""

    def do_stuff(self):
        d = {
            "items": [
                {
                    "name": "Item 1 name",
                    "weight": "19",
                    "count": "3",
                    "description": "onomatopeja",
                },
                {
                    "name": "Item 2 name",
                    "weight": "222",
                    "count": "2",
                    "description": "onomatopeja 2",
                },
                {
                    "name": "Item 3 name",
                    "weight": "222",
                    "count": "2",
                    "description": "onomatopeja 3",
                },
                {
                    "name": "Item 4 name",
                    "weight": "444",
                    "count": "4",
                    "description": "onomatopeja 4",
                },
                {
                    "name": "Item 5 name",
                    "weight": "555",
                    "count": "5",
                    "description": "onomatopeja 5",
                },

            ]
        }
        set_text_of_children(self.items_box, d)

    def changed_text(self, arg):
        print("Changed text")
        print(arg)

    def open_file(self):
        print("Opening file")
        fname = QFileDialog.getOpenFileName(self.central_widget, 'Open file', Path().cwd().as_posix(),
                                            "Character file (*.json)")[0]
        self.character_file = fname
        print(fname)
        data_to_read = json.load(Path(fname).open())
        set_text_of_children(self, data_to_read)

    def save_file(self):
        print("Saving file")
        data_to_save = {"basic_info_box": self.basic_info_box.get_dict_repr(),
                        "feats_box": self.feats_box.get_dict_repr(), "items_box": self.items_box.get_dict_repr(),
                        "feats_box_2": self.feats_box_2.get_dict_repr(),
                        "known_spells_box": self.known_spells_box.get_dict_repr(),
                        "languages_box": self.languages_box.get_dict_repr(),
                        "notes_box": self.notes_box.get_dict_repr(),
                        "attacks_box": self.attacks_box.get_dict_repr(),
                        "hp_ac_box": self.hp_ac_box.get_dict_repr(),
                        "saving_throws_box": self.saving_throws_box.get_dict_repr(),
                        "number_of_spells_box" : self.number_of_spells_box.get_dict_repr(),
                        "spells_per_day_box" : self.spells_per_day_box.get_dict_repr(),
                        "skills_box" : self.skills_box.get_dict_repr(),
                        "attributes_box" : self.attributes_box.get_dict_repr(),
                        "armor_items_box" : self.armor_items_box.get_dict_repr(),
                        "weapons_box" : self.weapons_box.get_dict_repr(),
                        }
        new_file = QFileDialog.getSaveFileName(self.central_widget, "Save file", Path().cwd().as_posix(),
                                               "Character file (*.json)")[0]
        if new_file:
            json.dump(data_to_save, Path(new_file).open('w'), indent=4)
        else:
            print("No file selected")
        self.character_file = new_file
        print(new_file)


def main():
    app = QApplication(sys.argv)
    form = MyApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
    # main1()
