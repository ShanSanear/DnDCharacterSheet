from PyQt5 import QtWidgets, QtCore

from qt_gui.boxes.box import DefaultBox


class FeatsBox(DefaultBox):
    def __init__(self, parent, position, size):
        self.root = QtWidgets.QGroupBox(parent)
        self.root.setGeometry(QtCore.QRect(*position, *size))
        self.root.setObjectName("FeatsBox")
        self.container = QtWidgets.QWidget(self.root)
        self.container.setObjectName("gridLayoutWidget_6")
        self.layout = QtWidgets.QGridLayout(self.container)
        self.layout.setObjectName("FeatsLayout")
        self.feat_name_label = QtWidgets.QLabel(self.container)
        self.feat_name_label.setObjectName("feat_name_label")

        self.add_feat()

        self.add_to_layout()
        self.translate()
        self.root.setLayout(self.layout)

    def add_to_layout(self):
        self.layout.addWidget(self.feat_1_name, 1, 0, 1, 1)
        self.layout.addWidget(self.feat_description_label, 0, 1, 1, 1)
        self.layout.addWidget(self.feat_1_description_button, 1, 1, 1, 1)
        self.layout.addWidget(self.feat_name_label, 0, 0, 1, 1)

    def translate(self):
        _translate = QtCore.QCoreApplication.translate
        self.root.setTitle(_translate("MainWindow", "Feats"))
        self.feat_1_name.setText(_translate("MainWindow", "Lorem ipsum"))
        self.feat_description_label.setText(_translate("MainWindow", "Description"))
        self.feat_1_description_button.setText(_translate("MainWindow", "DESC"))
        self.feat_name_label.setText(_translate("MainWindow", "Feat name"))

    def add_feat(self):
        self.feat_1_name = QtWidgets.QLineEdit(self.container)
        self.feat_1_name.setMinimumSize(QtCore.QSize(0, 23))
        self.feat_1_name.setObjectName("feat_1_name")
        self.feat_description_label = QtWidgets.QLabel(self.container)
        self.feat_description_label.setObjectName("feat_description_label")
        self.feat_1_description_button = QtWidgets.QPushButton(self.container)
        self.feat_1_description_button.setObjectName("feat_1_description_button")
