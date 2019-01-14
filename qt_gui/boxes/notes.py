from PyQt5 import QtWidgets, QtCore

from qt_gui.boxes.box import DefaultBox


class NotesBox(DefaultBox):
    def __init__(self, centralwidget, position, size):
        self.root = QtWidgets.QGroupBox(centralwidget)
        self.root.setGeometry(QtCore.QRect(*position, *size))
        self.root.setObjectName("NotesBox")
        self.container = QtWidgets.QWidget(self.root)
        self.container.setObjectName("verticalLayoutWidget_2")
        self.layout = QtWidgets.QVBoxLayout(self.container)
        self.layout.setObjectName("NotesLayout")
        self.notes_label = QtWidgets.QLabel(self.container)
        self.notes_label.setAlignment(QtCore.Qt.AlignCenter)
        self.notes_label.setObjectName("notes_label")
        self.layout.addWidget(self.notes_label)
        self.notes = QtWidgets.QPlainTextEdit(self.container)
        self.notes.setObjectName("notes")
        self.translate()
        self.add_to_layout()
        self.root.setLayout(self.layout)

    def add_to_layout(self):
        self.layout.addWidget(self.notes)

    def translate(self):
        _translate = QtCore.QCoreApplication.translate
        self.root.setTitle(_translate("MainWindow", "Notes"))
        self.notes_label.setText(_translate("MainWindow", "Notes"))
        self.notes.setPlainText(_translate("MainWindow",
                                           " Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sapien urna, egestas eu tempor at, pretium nec orci. In nec pharetra tellus. In malesuada erat tellus, eget efficitur elit convallis eu. Integer consectetur porttitor eros vitae sagittis. Vestibulum commodo suscipit varius. Nulla vitae fringilla velit. Mauris sagittis tellus urna. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Fusce in arcu justo.\n"
                                           "\n"
                                           "Mauris auctor, elit sed tristique maximus, libero quam feugiat dolor, in laoreet massa libero a tortor. Donec molestie pretium tempus. Integer lacinia magna lacus, nec volutpat felis condimentum id. Vivamus orci ante, gravida sed velit vel, venenatis pellentesque est. Maecenas laoreet laoreet ullamcorper. Phasellus rutrum felis non sapien aliquam semper. Morbi tempus, quam in luctus tempor, mauris neque faucibus libero, ut porta justo sem eu orci. Suspendisse consectetur sem ac neque mollis, sed iaculis tellus elementum. Nulla facilisis turpis vel sagittis pharetra. Donec nec odio pharetra, vestibulum lorem accumsan, tempus nulla. Donec blandit nisi in elit pulvinar, nec feugiat metus egestas. "))