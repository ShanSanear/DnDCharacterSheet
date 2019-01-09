from PyQt5 import QtWidgets, QtCore


class MenuBar:
    def __init__(self, main_window):
        self.menuBar = QtWidgets.QMenuBar(main_window)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1748, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menuBar)
        self.menuAbout.setObjectName("menuAbout")
        main_window.setMenuBar(self.menuBar)
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
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())
        self.translate_menu_bar()

    def translate_menu_bar(self):
        _translate = QtCore.QCoreApplication.translate
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionNew_character.setText(_translate("MainWindow", "New character..."))
        self.actionOpen_character.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
