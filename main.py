import logging
import sys
from functools import partial

from PyQt5.QtWidgets import QApplication

from gui.frames.qt_menu_bar import MenuBar
from gui.popups.qt_about_popup import AboutDialog
from qt_gui import MyApp, config_logger


class SingleCharApp(MyApp):
    def __init__(self):
        super(SingleCharApp, self).__init__()
        self.about_popup = AboutDialog("About", self)
        self.menu_bar = MenuBar(self)
        self.connect_menu_bar()

    def connect_menu_bar(self):
        self.menu_bar.open_character.triggered.connect(self.open_file)
        self.menu_bar.save_character_as.triggered.connect(self.save_file_as)
        self.menu_bar.save_character.triggered.connect(self.save_file)
        self.menu_bar.new_character.triggered.connect(self.create_new_character)
        self.menu_bar.language_menu.triggered.connect(partial(self.change_language,
                                                              self.menu_bar.change_language_en))
        self.menu_bar.about.triggered.connect(self.about_popup.show)

    def change_language(self, english_language_action):
        logging.debug("Changing language")
        # language_data = json.load(Path("data/languages.json").open(encoding='utf-8'))
        language = "EN" if english_language_action.isChecked() else "PL"
        # menu_bar_language_data = language_data["menu_bar"][language]
        # set_text_of_children(self, language_data[language])
        # set_text_of_children(self, menu_bar_language_data)
        if language == "PL":
            self.trans.load("eng-pl")
            QApplication.instance().installTranslator(self.trans)
            logging.debug("Setting to polish")
        else:
            QApplication.instance().removeTranslator(self.trans)
            logging.debug("Setting to english")
        self.retranslate()

def init_gui():
    app = QApplication(sys.argv)
    form = SingleCharApp()
    form.show()
    app.exec_()


def main():
    config_logger(logging.DEBUG)
    init_gui()


if __name__ == '__main__':
    main()