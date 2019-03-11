from PyQt5 import QtWidgets

from gui.frames.qt_generic_functions import set_text_of_children


class MenuBar:
    def __init__(self, main_window):
        self.root = QtWidgets.QMenuBar(main_window)
        self.file_menu = QtWidgets.QMenu(self.root)
        self.about_menu = QtWidgets.QMenu(self.root)
        main_window.setMenuBar(self.root)
        # TODO NEW CHARACTER - 10S ATTRIBUTES

        self.new_character = QtWidgets.QAction(main_window)
        self.open_character = QtWidgets.QAction(main_window)
        self.save_character = QtWidgets.QAction(main_window)
        self.exit = QtWidgets.QAction(main_window)
        self.file_menu.addAction(self.new_character)
        self.file_menu.addAction(self.open_character)
        self.file_menu.addAction(self.save_character)
        self.file_menu.addAction(self.exit)
        self.root.addAction(self.file_menu.menuAction())
        self.root.addAction(self.about_menu.menuAction())
        self.translate_reference = {
            "EN": {
                "file_menu": {"title": "File"},
                "about_menu": {"title": "About"},
                "new_character": "New character...",
                "open_character": "Open",
                "save_character": "Save",
                "exit": "Exit",
            }
        }
        self.translate("EN")

    def translate(self, language):
        set_text_of_children(self, self.translate_reference[language])
