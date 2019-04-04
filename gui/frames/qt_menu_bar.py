from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QActionGroup, QApplication


class MenuBar:
    def __init__(self, main_window):
        self.root = QtWidgets.QMenuBar(main_window)
        self.file_menu = QtWidgets.QMenu(self.root)
        self.help_menu = QtWidgets.QMenu(self.root)
        self.language_menu = QtWidgets.QMenu(self.root)
        main_window.setMenuBar(self.root)
        self.new_character = QtWidgets.QAction(main_window)
        self.open_character = QtWidgets.QAction(main_window)
        self.save_character = QtWidgets.QAction(main_window)
        self.save_character_as = QtWidgets.QAction(main_window)
        self.new_character.setShortcut("Ctrl+n")
        self.open_character.setShortcut("Ctrl+o")
        self.save_character.setShortcut("Ctrl+s")
        self.language_action_group = QActionGroup(main_window, exclusive=True)
        self.change_language_en = QtWidgets.QAction(main_window, checkable=True)
        self.change_language_pl = QtWidgets.QAction(main_window, checkable=True)
        self.about = QtWidgets.QAction(main_window)
        self.help_menu.addAction(self.about)
        self.language_action_group.addAction(self.change_language_en)
        self.language_action_group.addAction(self.change_language_pl)
        self.change_language_en.setChecked(True)
        self.exit = QtWidgets.QAction(main_window)
        self.file_menu.addAction(self.new_character)
        self.file_menu.addAction(self.open_character)
        self.file_menu.addAction(self.save_character)
        self.file_menu.addAction(self.save_character_as)
        self.file_menu.addAction(self.exit)
        self.language_menu.addAction(self.change_language_en)
        self.language_menu.addAction(self.change_language_pl)
        self.root.addAction(self.file_menu.menuAction())
        self.root.addAction(self.language_menu.menuAction())
        self.root.addAction(self.help_menu.menuAction())
        self.translate_reference = {
            "EN": {
                "file_menu": {"title": "File"},
                "help_menu": {"title": "Help"},
                "language_menu": {"title": "Language"},
                "new_character": "New character...",
                "open_character": "Open",
                "save_character": "Save",
                "save_character_as": "Save as...",
                "change_language_en": "English",
                "change_language_pl": "polski",
                "about": "About",
                "exit": "Exit",
            }
        }
        self.change_language_en.setText("English")
        self.change_language_pl.setText("polski")

    def retranslate(self):
        self.file_menu.setTitle(QApplication.translate("Menu", "File"))
        self.help_menu.setTitle(QApplication.translate("Menu", "Help"))
        self.language_menu.setTitle(QApplication.translate("Menu", "Language"))
        self.new_character.setText(QApplication.translate("Menu", "New character..."))
        self.open_character.setText(QApplication.translate("Menu", "Open"))
        self.save_character.setText(QApplication.translate("Menu", "Save"))
        self.save_character_as.setText(QApplication.translate("Menu", "Save as..."))
        self.exit.setText(QApplication.translate("Menu", "Exit"))
