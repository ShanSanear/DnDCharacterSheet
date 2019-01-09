from PyQt5 import QtWidgets, QtCore


class NotesBox:
    def __init__(self, centralwidget):
        self.NotesBox = QtWidgets.QGroupBox(centralwidget)
        self.NotesBox.setGeometry(QtCore.QRect(330, 200, 491, 231))
        self.NotesBox.setObjectName("NotesBox")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.NotesBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 471, 201))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.NotesLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.NotesLayout.setContentsMargins(9, 9, 9, 9)
        self.NotesLayout.setSpacing(6)
        self.NotesLayout.setObjectName("NotesLayout")
        self.notes_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.notes_label.setAlignment(QtCore.Qt.AlignCenter)
        self.notes_label.setObjectName("notes_label")
        self.NotesLayout.addWidget(self.notes_label)
        self.notes = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_2)
        self.notes.setObjectName("notes")
        self.NotesLayout.addWidget(self.notes)
        self.translate_notes_box()

    def translate_notes_box(self):
        _translate = QtCore.QCoreApplication.translate
        self.NotesBox.setTitle(_translate("MainWindow", "Notes"))
        self.notes_label.setText(_translate("MainWindow", "Notes"))
        self.notes.setPlainText(_translate("MainWindow",
                                           " Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sapien urna, egestas eu tempor at, pretium nec orci. In nec pharetra tellus. In malesuada erat tellus, eget efficitur elit convallis eu. Integer consectetur porttitor eros vitae sagittis. Vestibulum commodo suscipit varius. Nulla vitae fringilla velit. Mauris sagittis tellus urna. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Fusce in arcu justo.\n"
                                           "\n"
                                           "Mauris auctor, elit sed tristique maximus, libero quam feugiat dolor, in laoreet massa libero a tortor. Donec molestie pretium tempus. Integer lacinia magna lacus, nec volutpat felis condimentum id. Vivamus orci ante, gravida sed velit vel, venenatis pellentesque est. Maecenas laoreet laoreet ullamcorper. Phasellus rutrum felis non sapien aliquam semper. Morbi tempus, quam in luctus tempor, mauris neque faucibus libero, ut porta justo sem eu orci. Suspendisse consectetur sem ac neque mollis, sed iaculis tellus elementum. Nulla facilisis turpis vel sagittis pharetra. Donec nec odio pharetra, vestibulum lorem accumsan, tempus nulla. Donec blandit nisi in elit pulvinar, nec feugiat metus egestas. "))