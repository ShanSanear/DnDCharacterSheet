from PyQt5 import QtWidgets, QtCore


class MenuBar:
    def __init__(self, main_window):
        self.root = QtWidgets.QMenuBar(main_window)
        self.root.setGeometry(QtCore.QRect(0, 0, 1748, 21))
        self.root.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.root)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.root)
        self.menuAbout.setObjectName("menuAbout")
        main_window.setMenuBar(self.root)
        self.actionNew_character = QtWidgets.QAction(main_window)
        self.actionNew_character.setObjectName("actionNew_character")
        self.actionOpen_character = QtWidgets.QAction(main_window)
        self.actionOpen_character.setObjectName("actionOpen_character")
        self.actionSave = QtWidgets.QAction(main_window)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(main_window)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionNew_character)
        self.menuFile.addAction(self.actionOpen_character)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.root.addAction(self.menuFile.menuAction())
        self.root.addAction(self.menuAbout.menuAction())
        self.translate_menu_bar()

    def translate_menu_bar(self):
        _translate = QtCore.QCoreApplication.translate
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionNew_character.setText(_translate("MainWindow", "New character..."))
        self.actionOpen_character.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
