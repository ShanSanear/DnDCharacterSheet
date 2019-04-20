import logging
import sys
from functools import partial

from PyQt5.QtWidgets import QApplication, QMainWindow

from gui.common_window import CommonWindow
from gui.qt_gui import MyApp, config_logger


class SingleCharApp(MyApp, CommonWindow, QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        MyApp.__init__(self)
        CommonWindow.__init__(self)
        self.connect_menu_bar()
        self.resize(1360, 860)

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
            self.trans.load("data/languages/eng-pl")
            QApplication.instance().installTranslator(self.trans)
            logging.debug("Setting to polish")
        else:
            QApplication.instance().removeTranslator(self.trans)
            logging.debug("Setting to english")
        self.retranslate()


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
