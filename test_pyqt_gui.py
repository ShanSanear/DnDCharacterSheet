from functools import partial

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication

import sys

from qt_gui.main_window import MainWindowUi

class MyApp(QMainWindow, MainWindowUi):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setup_ui(self)
        self.pushButton.clicked.connect(self.do_stuff)
        self.character_name.textChanged.connect(partial(self.changed_text, self.FeatsBox))

    def do_stuff(self):
        print("Doing stuff")

    def changed_text(self, arg):
        print("Changed text")
        print(arg)


if __name__ == '__main__':
    # pyuic5 input -o output for converting ui files
    app = QApplication(sys.argv)
    form = MyApp()
    form.show()
    app.exec_()
