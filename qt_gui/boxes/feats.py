from PyQt5 import QtWidgets, QtCore


class FeatsBox:
    def __init__(self, centralwidget):
        self.FeatsBox = QtWidgets.QGroupBox(centralwidget)
        self.FeatsBox.setGeometry(QtCore.QRect(630, 700, 191, 491))
        self.FeatsBox.setObjectName("FeatsBox")
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.FeatsBox)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(10, 20, 171, 61))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.FeatsLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.FeatsLayout.setContentsMargins(9, 9, 9, 9)
        self.FeatsLayout.setSpacing(6)
        self.FeatsLayout.setObjectName("FeatsLayout")

        self.feat_1_name = QtWidgets.QLineEdit(self.gridLayoutWidget_6)
        self.feat_1_name.setMinimumSize(QtCore.QSize(0, 23))
        self.feat_1_name.setObjectName("feat_1_name")
        self.feat_description_label = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.feat_description_label.setObjectName("feat_description_label")
        self.feat_1_description_button = QtWidgets.QPushButton(self.gridLayoutWidget_6)
        self.feat_1_description_button.setObjectName("feat_1_description_button")
        self.feat_name_label = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.feat_name_label.setObjectName("feat_name_label")

        self.FeatsLayout.addWidget(self.feat_1_name, 1, 0, 1, 1)
        self.FeatsLayout.addWidget(self.feat_description_label, 0, 1, 1, 1)
        self.FeatsLayout.addWidget(self.feat_1_description_button, 1, 1, 1, 1)
        self.FeatsLayout.addWidget(self.feat_name_label, 0, 0, 1, 1)

    def translate_feats_box(self):
        _translate = QtCore.QCoreApplication.translate
        self.FeatsBox.setTitle(_translate("MainWindow", "Feats"))
        self.feat_1_name.setText(_translate("MainWindow", "Lorem ipsum"))
        self.feat_description_label.setText(_translate("MainWindow", "Description"))
        self.feat_1_description_button.setText(_translate("MainWindow", "DESC"))
        self.feat_name_label.setText(_translate("MainWindow", "Feat name"))