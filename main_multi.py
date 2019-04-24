import logging
import sys
from functools import partial

from PyQt5.QtCore import QSettings, QTimerEvent
from PyQt5.QtWidgets import QApplication, QMessageBox

from gui.constants import OPENED_CHARACTERS_COUNT, LAST_OPENED_CHARACTER_FILE, ASK_ABOUT_LOADING, AUTOSAVE_INTERVAL
from gui.frames.qt_menu_bar import MenuBar
from gui.main_window_wrapper import MainWindowWrapper
from gui.multi_character_tabs import MulticharacterTabWidget
from gui.qt_gui import SingleCharCore
from utils.console_logging import config_logger


class MultiCharApp(MainWindowWrapper):

    def __init__(self):
        default_size = [1380, 860]
        MainWindowWrapper.__init__(self, default_size)
        self.settings = QSettings("settings.ini", QSettings.IniFormat, None)
        self.settings.setFallbacksEnabled(False)
        self.main_tabs = MulticharacterTabWidget(self, SingleCharCore)
        self.main_tabs.move(0, 20)
        self.main_tabs.currentChanged.connect(self.changed_tab)
        self.menu_bar = MenuBar(self)
        self.menu_bar.retranslate()
        self.general_connect_menu_bar()
        self.setCentralWidget(self.main_tabs)
        self.chars_count = self.settings.value(OPENED_CHARACTERS_COUNT, 0, type=int)
        self.autosave_interval = self.settings.value(AUTOSAVE_INTERVAL, 5, type=int) * 60000  # 60k ms = 1 min
        self.ask_about_loading_last = self.settings.value(ASK_ABOUT_LOADING, False, type=bool)
        self.autosave_timer_id = self.startTimer(self.autosave_interval)
        self.restore_settings()
        self.settings_window.buttons_box.accepted.connect(self.setting_new_autosave_interval)

    def changed_tab(self, tab_idx):
        char = self.main_tabs.get_character(tab_idx)
        self.disconnect_menu_bar()
        self.connect_menu_bar(char)

    def general_connect_menu_bar(self):
        self.common_connect_menu_bar()
        self.menu_bar.language_menu.triggered.connect(partial(self.change_language,
                                                              self.menu_bar.change_language_en))

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

    def change_language(self, english_language_action):
        logging.debug("Changing language")
        language = "EN" if english_language_action.isChecked() else "PL"
        tabs_count = self.main_tabs.count()
        if language == "PL":
            self.trans.load("data/languages/eng-pl")
            QApplication.instance().installTranslator(self.trans)
        else:
            QApplication.instance().removeTranslator(self.trans)
        for char_idx in range(tabs_count):
            char = self.main_tabs.widget(char_idx)
            char.retranslate()
        self.menu_bar.retranslate()

    def restore_settings(self):
        self.restore_window_settings()
        self.chars_restore()
        self.connect_menu_bar(self.main_tabs.get_character(0))

    def chars_restore(self):
        if self.ask_about_loading_last and self.chars_count:
            proceed = QMessageBox.question(self.container,
                                           QApplication.translate("Open last",
                                                                  "Opening last file"),
                                           QApplication.translate("Open last",
                                                                  "Do you want to open last opened file?"),
                                           QMessageBox.Yes | QMessageBox.No)
            if proceed == QMessageBox.Yes:
                self.restore_opened_characters()
            else:
                self.main_tabs.add_char_tab()
        elif not self.chars_count:
            self.main_tabs.add_char_tab()
        else:
            self.restore_opened_characters()

    def restore_opened_characters(self):
        for idx in range(self.chars_count):
            logging.debug("Adding character tab at idx: %d", idx)
            self.main_tabs.add_char_tab()
            char_file_key = f'{LAST_OPENED_CHARACTER_FILE}_{idx}'
            char_file_path = self.settings.value(char_file_key, '')
            logging.debug("Character file path to load: %s", char_file_path)
            if char_file_path:
                char: SingleCharCore = self.main_tabs.get_character(idx)
                char.open_selected_file(char_file_path)

    def timerEvent(self, a0: 'QTimerEvent') -> None:
        self.save_characters()

    def save_characters(self):
        characters = self.main_tabs.get_character_list()
        for char in characters:
            char: SingleCharCore
            char.backup_char_file()

    def setting_new_autosave_interval(self):
        logging.debug("Checking if autosave value changed")
        tmp = self.settings.value(AUTOSAVE_INTERVAL, 5, type=int)
        if tmp != self.autosave_interval * 60000:
            self.autosave_interval = tmp * 60000
            logging.debug("New autosave interval: %d", self.autosave_interval)
            self._set_new_autosave_timer()

    def _set_new_autosave_timer(self):
        logging.debug("Setting new autosave timer")
        self.killTimer(self.autosave_timer_id)
        self.autosave_timer_id = self.startTimer(self.autosave_interval)


def init_multi_gui():
    app = QApplication(sys.argv)
    form = MultiCharApp()
    logging.debug("Post init size: %s", form.size())
    form.setWindowTitle("MultiCharacter Sheet")
    form.show()
    app.exec_()


def main():
    config_logger(logging.DEBUG)
    init_multi_gui()


if __name__ == '__main__':
    main()
