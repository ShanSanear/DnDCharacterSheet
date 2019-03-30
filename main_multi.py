import json
import logging
import sys
from functools import partial
from pathlib import Path

from PyQt5.QtWidgets import QApplication, QMainWindow

from gui.frames.qt_generic_functions import set_text_of_children
from gui.frames.qt_menu_bar import MenuBar
from gui.multi_character_tabs import MulticharacterTabWidget
from gui.popups.qt_about_popup import AboutDialog
from qt_gui import MyApp, config_logger


class MultiCharApp(QMainWindow):

    def __init__(self):
        super(MultiCharApp, self).__init__()
        self.main_tabs = MulticharacterTabWidget(self, MyApp)
        self.main_tabs.move(0, 20)
        self.main_tabs.currentChanged.connect(self.changed_tab)
        self.about_popup = AboutDialog("About", self)
        self.menu_bar = MenuBar(self)
        self.main_tabs.setMinimumSize(1340, 1000)
        self.resize(1360, 1020)
        initial_char = self.main_tabs.widget(0)
        self.connect_menu_bar(initial_char)

    def changed_tab(self, tab_idx):
        char = self.main_tabs.widget(tab_idx)
        self.disconnect_menu_bar()
        self.connect_menu_bar(char)

    def disconnect_menu_bar(self):
        try:
            self.menu_bar.open_character.disconnect()
            self.menu_bar.save_character.disconnect()
            self.menu_bar.save_character_as.disconnect()
            self.menu_bar.new_character.disconnect()
            self.menu_bar.language_menu.disconnect()
        except TypeError:
            pass

    def connect_menu_bar(self, char):
        self.menu_bar.open_character.triggered.connect(char.open_file)
        self.menu_bar.save_character_as.triggered.connect(char.save_file_as)
        self.menu_bar.save_character.triggered.connect(char.save_file)
        self.menu_bar.new_character.triggered.connect(char.create_new_character)
        self.menu_bar.language_menu.triggered.connect(partial(self.change_language,
                                                              self.menu_bar.change_language_en))

    def change_language(self, english_language_action):
        logging.debug("Changing language")
        language_data = json.load(Path("data/languages.json").open(encoding='utf-8'))
        language = "EN" if english_language_action.isChecked() else "PL"
        menu_bar_language_data = language_data["menu_bar"][language]
        tabs_count = self.main_tabs.count()
        for char_idx in range(tabs_count):
            char = self.main_tabs.widget(char_idx)
            set_text_of_children(char, language_data[language])
        set_text_of_children(self, menu_bar_language_data)


def init_multi_gui():
    app = QApplication(sys.argv)
    form = MultiCharApp()
    form.show()
    app.exec_()


def main():
    config_logger(logging.DEBUG)
    init_multi_gui()


if __name__ == '__main__':
    main()
