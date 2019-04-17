import logging
import sys
from functools import partial

from PyQt5.QtCore import QTranslator
from PyQt5.QtWidgets import QApplication, QMainWindow

from gui.frames.qt_menu_bar import MenuBar
from gui.multi_character_tabs import MulticharacterTabWidget
from gui.popups.qt_about_popup import AboutDialog
from gui.popups.qt_settings import SettingsWindow
from qt_gui import MyApp, config_logger


class MultiCharApp(QMainWindow):

    def __init__(self):
        super(MultiCharApp, self).__init__()
        self.main_tabs = MulticharacterTabWidget(self, MyApp)
        self.main_tabs.move(0, 20)
        self.main_tabs.currentChanged.connect(self.changed_tab)
        self.about_popup = AboutDialog("About", self)
        self.settings_window = SettingsWindow()
        self.trans = QTranslator(self)
        self.menu_bar = MenuBar(self)
        self.menu_bar.retranslate()
        self.main_tabs.setMinimumSize(1340, 1000)
        self.resize(1360, 1020)
        initial_char = self.main_tabs.widget(0)
        self.connect_menu_bar(initial_char)
        self.general_connect_menu_bar()

    def changed_tab(self, tab_idx):
        char = self.main_tabs.widget(tab_idx)
        self.disconnect_menu_bar()
        self.connect_menu_bar(char)

    def general_connect_menu_bar(self):
        self.menu_bar.language_menu.triggered.connect(partial(self.change_language,
                                                              self.menu_bar.change_language_en))
        self.menu_bar.about.triggered.connect(self.about_popup.show)
        self.menu_bar.open_settings.triggered.connect(self.settings_window.show)

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



def init_multi_gui():
    app = QApplication(sys.argv)
    app.setStyle("windowsvista")
    form = MultiCharApp()
    form.setWindowTitle("MultiCharacter Sheet")
    form.show()
    app.exec_()


def main():
    config_logger(logging.DEBUG)
    init_multi_gui()


if __name__ == '__main__':
    main()
