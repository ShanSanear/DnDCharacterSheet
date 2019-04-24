import logging
import sys
from functools import partial

from PyQt5.QtCore import QTimerEvent
from PyQt5.QtWidgets import QApplication, QMessageBox

from gui.constants import AUTOSAVE_INTERVAL, LAST_OPENED_CHARACTER_FILE, APP_LANGUAGE, ASK_ABOUT_LOADING
from gui.main_window_wrapper import MainWindowWrapper
from gui.qt_gui import SingleCharCore, config_logger


class SingleCharApp(SingleCharCore, MainWindowWrapper):
    def __init__(self):
        default_size = (1360, 860)
        MainWindowWrapper.__init__(self, default_size)
        SingleCharCore.__init__(self)
        self.connect_menu_bar()
        self.setCentralWidget(self.container)
        self.load_predefined_language()
        self.autosave_interval = self.settings.value(AUTOSAVE_INTERVAL, 1, type=int) * 60000  # 60k ms = 1 min
        self.ask_about_loading_last = self.settings.value(ASK_ABOUT_LOADING, False, type=bool)
        self.autosave_timer_id = self.startTimer(self.autosave_interval)
        self.restore_settings()
        self.settings_window.buttons_box.accepted.connect(self.setting_new_autosave_interval)
        self.load_last_saved()

    def load_predefined_language(self):
        language = self.settings.value(APP_LANGUAGE, 'PL', type=str)
        if language == 'PL':
            self._set_lang_pl()
            self.menu_bar.change_language_pl.setChecked(True)
        else:
            self._set_lang_en()
            self.menu_bar.change_language_en.setChecked(True)
        self.retranslate()
        self.menu_bar.retranslate()

    def load_last_saved(self):
        self.character_file = self.get_character_file()
        if self.character_file:
            if self.ask_about_loading_last:
                proceed = QMessageBox.question(self.container,
                                               QApplication.translate("Open last",
                                                                      "Opening last file"),
                                               QApplication.translate("Open last",
                                                                      "Do you want to open last opened file?"),
                                               QMessageBox.Yes | QMessageBox.No)
                if proceed == QMessageBox.Yes:
                    self.open_selected_file(self.character_file)
            else:
                self.open_selected_file(self.character_file)

    def get_character_file(self):
        char_file = self.settings.value(LAST_OPENED_CHARACTER_FILE, '', type=str)
        logging.debug("Char file: %s", char_file)
        return char_file

    def setting_new_autosave_interval(self):
        logging.debug("Checking if autosave value changed")
        tmp = self.settings.value(AUTOSAVE_INTERVAL, 1, type=int) * 60000
        if tmp != self.autosave_interval:
            self.autosave_interval = tmp
            self._set_new_autosave_timer()

    def _set_new_autosave_timer(self):
        logging.debug("Setting new autosave timer")
        self.killTimer(self.autosave_timer_id)
        self.autosave_timer_id = self.startTimer(self.autosave_interval)

    def connect_menu_bar(self):
        self.common_connect_menu_bar()
        self.menu_bar.open_character.triggered.connect(self.open_file)
        self.menu_bar.save_character_as.triggered.connect(self.save_file_as)
        self.menu_bar.save_character.triggered.connect(self.save_file)
        self.menu_bar.new_character.triggered.connect(self.create_new_character)
        self.menu_bar.language_menu.triggered.connect(partial(self.change_language,
                                                              self.menu_bar.change_language_en))

    def change_language(self, english_language_action):
        logging.debug("Changing language")
        language = "EN" if english_language_action.isChecked() else "PL"
        if language == "PL":
            self._set_lang_pl()
        else:
            self._set_lang_en()

        self.settings.setValue(APP_LANGUAGE, language)
        self.settings.sync()
        self.retranslate()

    def _set_lang_en(self):
        QApplication.instance().removeTranslator(self.trans)
        logging.debug("Setting to english")

    def _set_lang_pl(self):
        self.trans.load("data/languages/eng-pl")
        QApplication.instance().installTranslator(self.trans)
        logging.debug("Setting to polish")

    def restore_settings(self):
        self.restore_window_settings()

    def timerEvent(self, a0: 'QTimerEvent') -> None:
        logging.debug("Timer event")
        self.backup_char_file()


def init_gui():
    app = QApplication(sys.argv)
    app.setStyle("windowsvista")
    form = SingleCharApp()
    form.show()
    form.setWindowTitle("Character Sheet")
    app.exec_()


def main():
    config_logger(logging.DEBUG)
    init_gui()


if __name__ == '__main__':
    main()
