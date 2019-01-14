from functools import partial

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QGroupBox, QFormLayout, QLabel, QComboBox, QScrollArea, \
    QVBoxLayout

import sys

from PyQt5.uic.properties import QtGui

from qt_gui.main_window import MainWindowUi

class MyApp(QMainWindow, MainWindowUi):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setup_ui(self)

    #        self.push_button.clicked.connect(self.do_stuff)
    #        self.basic_info_box.name.textChanged.connect(partial(self.changed_text, self.feats_box))

    def do_stuff(self):
        self.items_box.add_item()

    def changed_text(self, arg):
        print("Changed text")
        print(arg)


class Window(QtWidgets.QWidget):

    def __init__(self, val):
        super(Window, self).__init__()
        mygroupbox = QGroupBox('this is my groupbox')
        myform = QFormLayout()
        labellist = []
        combolist = []
        for i in range(val):
            labellist.append(QLabel('mylabel'))
            combolist.append(QComboBox())
            myform.addRow(labellist[i],combolist[i])
        mygroupbox.setLayout(myform)
        scroll = QScrollArea()
        scroll.setWidget(mygroupbox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(400)
        layout = QVBoxLayout(self)
        layout.addWidget(scroll)


def main1():
    app = QApplication(sys.argv)
    window = Window(25)
    window.setGeometry(500, 300, 300, 400)
    window.show()
    sys.exit(app.exec_())

def main():
    app = QApplication(sys.argv)
    form = MyApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
    #main1()

