from PyQt5 import QtWidgets, QtCore

from qt_gui.boxes.qt_generic_classes import DefaultBox


class FeatsBox(DefaultBox):
    # TODO - function based widgets and labels
    # TODO - generalized adding feats
    # TODO - generalized translation
    # TODO - adding widgets by rows/columns
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
        self.feat_description_field_label = QtWidgets.QLabel(self.container)
        self.feat_name_label.setObjectName("feat_name_label")
        self.feat_description_label = QtWidgets.QLabel(self.container)
        self.feat_description_label.setObjectName("feat_description_label")
        self.add_feat()

        self.add_to_layout()
        self.translate()
        self.root.setLayout(self.layout)

    def add_feat(self):
        self.feat_1_name = QtWidgets.QLineEdit(self.container)
        self.feat_1_name.setMinimumSize(QtCore.QSize(0, 23))
        self.feat_1_name.setMaximumWidth(150)
        self.feat_1_name.setObjectName("feat_1_name")

        self.feat_1_description_edit = QtWidgets.QLineEdit(self.container)
        self.feat_1_description_edit.setMinimumSize(QtCore.QSize(0, 23))
        self.feat_1_description_edit.setObjectName("feat_1_description_edit")

        self.feat_1_description_button = QtWidgets.QPushButton(self.container)
        self.feat_1_description_button.setObjectName("feat_1_description_button")
        self.feat_1_description_button.setMaximumWidth(20)

    def translate(self):
        _translate = QtCore.QCoreApplication.translate
        self.root.setTitle(_translate("MainWindow", "Feats / Powers / Special abilities"))
        self.feat_1_name.setText(_translate("MainWindow", "Lorem ipsum"))
        self.feat_description_label.setText(_translate("MainWindow", "Desc"))
        self.feat_description_field_label.setText(_translate("MainWindow", "Desc"))
        self.feat_1_description_button.setText(_translate("MainWindow", "..."))
        self.feat_name_label.setText(_translate("MainWindow", "Feat name"))
        self.feat_1_description_edit.setText(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sapien urna, egestas eu tempor at, pretium nec orci. In nec pharetra tellus")

    def add_to_layout(self):
        self.layout.addWidget(self.feat_1_name, 1, 0, 1, 1)
        self.layout.addWidget(self.feat_1_description_edit, 1, 1, 1, 1)
        self.layout.addWidget(self.feat_1_description_button, 1, 2, 1, 1)

        self.layout.addWidget(self.feat_name_label, 0, 0, 1, 1)
        self.layout.addWidget(self.feat_description_label, 0, 1, 1, 1)
        self.layout.addWidget(self.feat_description_field_label, 0, 2, 1, 1)
