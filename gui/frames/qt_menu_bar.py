from PyQt5 import QtWidgets, QtCore


class MenuBar:
    # TODO - function based widgets and labels
    # TODO - generalized translation
    # TODO - adding widgets by rows/columns
    # TODO - some basic tests of saving / loading files (probably in main file)
    def __init__(self, main_window):
        self.root = QtWidgets.QMenuBar(main_window)
        self.file_menu = QtWidgets.QMenu(self.root)
        self.about_menu = QtWidgets.QMenu(self.root)
        main_window.setMenuBar(self.root)
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
        self.translate_menu_bar()

    def translate_menu_bar(self):
        _translate = QtCore.QCoreApplication.translate
        self.file_menu.setTitle(_translate("MainWindow", "File"))
        self.about_menu.setTitle(_translate("MainWindow", "About"))
        self.new_character.setText(_translate("MainWindow", "New character..."))
        self.open_character.setText(_translate("MainWindow", "Open"))
        self.save_character.setText(_translate("MainWindow", "Save"))
        self.exit.setText(_translate("MainWindow", "Exit"))
