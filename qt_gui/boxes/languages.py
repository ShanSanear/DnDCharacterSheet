from PyQt5 import QtWidgets, QtCore

from qt_gui.boxes.box import DefaultBox


class LanguagesBox(DefaultBox):
    def __init__(self, centralwidget):
        self.root = QtWidgets.QGroupBox(centralwidget)
        self.root.setGeometry(QtCore.QRect(630, 440, 191, 251))
        self.root.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.root.setObjectName("LanguagesBox")
        self.container = QtWidgets.QWidget(self.root)
        self.container.setGeometry(QtCore.QRect(10, 20, 171, 211))
        self.container.setObjectName("verticalLayoutWidget")
        self.layout = QtWidgets.QVBoxLayout(self.container)
        self.layout.setContentsMargins(9, 9, 9, 9)
        self.layout.setSpacing(0)
        self.layout.setObjectName("LanguagesLayout")
        self.known_languages_label = QtWidgets.QLabel(self.container)
        self.known_languages_label.setAlignment(QtCore.Qt.AlignCenter)
        self.known_languages_label.setObjectName("known_languages_label")
        self.layout.addWidget(self.known_languages_label)
        self.known_languages = QtWidgets.QPlainTextEdit(self.container)
        self.known_languages.setObjectName("known_languages")
        self.add_to_layout()
        self.translate()
        self.set_default()

    def add_to_layout(self):
        self.layout.addWidget(self.known_languages)

    def translate(self):
        _translate = QtCore.QCoreApplication.translate
        self.root.setTitle(_translate("MainWindow", "Languages"))
        self.known_languages_label.setText(_translate("MainWindow", "Known Languages"))

    def set_default(self):
        _translate = QtCore.QCoreApplication.translate
        self.known_languages.setPlainText(_translate("MainWindow",
                                                     " Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sapien urna, egestas eu tempor at, pretium nec orci. In nec pharetra tellus. In malesuada erat tellus, eget efficitur elit convallis eu. Integer consectetur porttitor eros vitae sagittis. Vestibulum commodo suscipit varius. Nulla vitae fringilla velit. Mauris sagittis tellus urna. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Fusce in arcu justo.\n"
                                                     "\n"
                                                     "Mauris auctor, elit sed tristique maximus, libero quam feugiat dolor, in laoreet massa libero a tortor. Donec molestie pretium tempus. Integer lacinia magna lacus, nec volutpat felis condimentum id. Vivamus orci ante, gravida sed velit vel, venenatis pellentesque est. Maecenas laoreet laoreet ullamcorper. Phasellus rutrum felis non sapien aliquam semper. Morbi tempus, quam in luctus tempor, mauris neque faucibus libero, ut porta justo sem eu orci. Suspendisse consectetur sem ac neque mollis, sed iaculis tellus elementum. Nulla facilisis turpis vel sagittis pharetra. Donec nec odio pharetra, vestibulum lorem accumsan, tempus nulla. Donec blandit nisi in elit pulvinar, nec feugiat metus egestas. "))
