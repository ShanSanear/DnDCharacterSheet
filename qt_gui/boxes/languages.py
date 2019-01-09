from PyQt5 import QtWidgets, QtCore


class LanguagesBox:
    def __init__(self, centralwidget):
        self.LanguagesBox = QtWidgets.QGroupBox(centralwidget)
        self.LanguagesBox.setGeometry(QtCore.QRect(630, 440, 191, 251))
        self.LanguagesBox.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.LanguagesBox.setObjectName("LanguagesBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.LanguagesBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 171, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.LanguagesLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.LanguagesLayout.setContentsMargins(9, 9, 9, 9)
        self.LanguagesLayout.setSpacing(6)
        self.LanguagesLayout.setObjectName("LanguagesLayout")
        self.known_languages_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.known_languages_label.setAlignment(QtCore.Qt.AlignCenter)
        self.known_languages_label.setObjectName("known_languages_label")
        self.LanguagesLayout.addWidget(self.known_languages_label)
        self.known_languages = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.known_languages.setObjectName("known_languages")
        self.LanguagesLayout.addWidget(self.known_languages)
        self.translate_languages_box()

    def translate_languages_box(self):
        _translate = QtCore.QCoreApplication.translate
        self.LanguagesBox.setTitle(_translate("MainWindow", "Languages"))
        self.known_languages_label.setText(_translate("MainWindow", "Known Languages"))
        self.known_languages.setPlainText(_translate("MainWindow",
                                                     " Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sapien urna, egestas eu tempor at, pretium nec orci. In nec pharetra tellus. In malesuada erat tellus, eget efficitur elit convallis eu. Integer consectetur porttitor eros vitae sagittis. Vestibulum commodo suscipit varius. Nulla vitae fringilla velit. Mauris sagittis tellus urna. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Fusce in arcu justo.\n"
                                                     "\n"
                                                     "Mauris auctor, elit sed tristique maximus, libero quam feugiat dolor, in laoreet massa libero a tortor. Donec molestie pretium tempus. Integer lacinia magna lacus, nec volutpat felis condimentum id. Vivamus orci ante, gravida sed velit vel, venenatis pellentesque est. Maecenas laoreet laoreet ullamcorper. Phasellus rutrum felis non sapien aliquam semper. Morbi tempus, quam in luctus tempor, mauris neque faucibus libero, ut porta justo sem eu orci. Suspendisse consectetur sem ac neque mollis, sed iaculis tellus elementum. Nulla facilisis turpis vel sagittis pharetra. Donec nec odio pharetra, vestibulum lorem accumsan, tempus nulla. Donec blandit nisi in elit pulvinar, nec feugiat metus egestas. "))