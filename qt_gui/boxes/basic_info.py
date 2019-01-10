from PyQt5 import QtWidgets, QtCore, QtGui

from qt_gui.boxes.box import DefaultBox
from qt_gui.boxes.qt_generic_functions import create_qlabel, create_qline_edit


class BasicInfoBox(DefaultBox):
    def __init__(self, centralwidget):
        self.root = QtWidgets.QGroupBox(centralwidget)
        self.root.setGeometry(QtCore.QRect(10, 0, 811, 201))
        self.root.setObjectName("BasicInfoBox")
        self.container = QtWidgets.QWidget(self.root)
        self.container.setGeometry(QtCore.QRect(10, 20, 791, 162))
        self.container.setObjectName("gridLayoutWidget_2")
        self.layout = QtWidgets.QGridLayout(self.container)
        self.layout.setContentsMargins(9, 9, 9, 9)
        self.layout.setSpacing(6)
        self.layout.setObjectName("BasicInfoLayout")

        qlabel_dict_1 = dict(parent=self.container,
                             align=QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter,
                             min_size=(178, 16), )
        qlabel_dict_2 = dict(parent=self.container,
                             align=QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter,
                             min_size=(86, 16), )
        qline_dict_1 = dict(parent=self.container, min_size=(177, 23))
        qline_dict_2 = dict(parent=self.container, min_size=(85, 23))

        self.character_class_label = create_qlabel("character_class_label", **qlabel_dict_1)
        self.character_faith_label = create_qlabel("character_faith_label", **qlabel_dict_1)
        self.character_race_label = create_qlabel("character_race_label", **qlabel_dict_1)
        self.character_alignement_label = create_qlabel("character_alignement_label", **qlabel_dict_1)
        self.player_name_label = create_qlabel("player_name_label", **qlabel_dict_1)
        self.character_name_label = create_qlabel("character_name_label", **qlabel_dict_1)
        self.character_height_label = create_qlabel("character_height_label", **qlabel_dict_2)
        self.character_weight_label = create_qlabel("character_weight_label", **qlabel_dict_2)
        self.character_eyes_label = create_qlabel("character_eyes_label", **qlabel_dict_2)
        self.character_hair_label = create_qlabel("character_hair_label", **qlabel_dict_2)
        self.character_size_label = create_qlabel("character_size_label", **qlabel_dict_2)
        self.character_age_label = create_qlabel("character_age_label", **qlabel_dict_2)
        self.character_gender_label = create_qlabel("character_gender_label", **qlabel_dict_2)
        self.character_level_label = create_qlabel("character_level_label", **qlabel_dict_2)
        self.player_name_label.setObjectName("player_name_label")

        self.character_race = create_qline_edit("character_race", **qline_dict_1)
        self.character_alignement = create_qline_edit("character_alignement", **qline_dict_1)
        self.character_class = create_qline_edit("character_class", **qline_dict_1)
        self.character_faith = create_qline_edit("character_faith", **qline_dict_1)
        self.character_name = create_qline_edit("character_name", **qline_dict_2)
        self.character_height = create_qline_edit("character_height", **qline_dict_2)
        self.character_weight = create_qline_edit("character_weight", **qline_dict_2)
        self.character_hair = create_qline_edit("character_hair", **qline_dict_2)
        self.player_name = create_qline_edit("player_name", **qline_dict_2)
        self.character_eyes = create_qline_edit("character_eyes", **qline_dict_2)
        self.character_gender = create_qline_edit("character_gender", **qline_dict_2)
        self.character_age = create_qline_edit("character_age", **qline_dict_2)
        self.character_size = create_qline_edit("character_size", **qline_dict_2)
        self.character_level = create_qline_edit("character_level", **qline_dict_2)

        self.add_to_layout()
        self.translate()
        self.set_default()

    def add_to_layout(self):
        self.layout.addWidget(self.character_class_label, 2, 0, 1, 2)
        self.layout.addWidget(self.character_faith_label, 2, 6, 1, 2)
        self.layout.addWidget(self.character_race_label, 2, 2, 1, 2)
        self.layout.addWidget(self.character_alignement_label, 2, 4, 1, 2)
        self.layout.addWidget(self.character_race, 3, 2, 1, 2)
        self.layout.addWidget(self.character_alignement, 3, 4, 1, 2)
        self.layout.addWidget(self.character_class, 3, 0, 1, 2)
        self.layout.addWidget(self.character_faith, 3, 6, 1, 2)
        self.layout.addWidget(self.character_name_label, 0, 0, 1, 4)
        self.layout.addWidget(self.character_name, 1, 0, 1, 4)
        self.layout.addWidget(self.player_name_label, 0, 4, 1, 4)
        self.layout.addWidget(self.character_height_label, 4, 4, 1, 1)
        self.layout.addWidget(self.character_height, 5, 4, 1, 1)
        self.layout.addWidget(self.character_weight_label, 4, 5, 1, 1)
        self.layout.addWidget(self.character_weight, 5, 5, 1, 1)
        self.layout.addWidget(self.character_eyes_label, 4, 6, 1, 1)
        self.layout.addWidget(self.character_hair, 5, 7, 1, 1)
        self.layout.addWidget(self.player_name, 1, 4, 1, 4)
        self.layout.addWidget(self.character_eyes, 5, 6, 1, 1)
        self.layout.addWidget(self.character_hair_label, 4, 7, 1, 1)
        self.layout.addWidget(self.character_gender, 5, 3, 1, 1)
        self.layout.addWidget(self.character_age, 5, 2, 1, 1)
        self.layout.addWidget(self.character_size_label, 4, 1, 1, 1)
        self.layout.addWidget(self.character_size, 5, 1, 1, 1)
        self.layout.addWidget(self.character_age_label, 4, 2, 1, 1)
        self.layout.addWidget(self.character_gender_label, 4, 3, 1, 1)
        self.layout.addWidget(self.character_level, 5, 0, 1, 1)
        self.layout.addWidget(self.character_level_label, 4, 0, 1, 1)

    def translate(self):
        _translate = QtCore.QCoreApplication.translate
        self.root.setTitle(_translate("MainWindow", "Basic Info"))
        self.character_class_label.setText(_translate("MainWindow", "Class"))
        self.character_faith_label.setText(_translate("MainWindow", "Faith"))
        self.character_race_label.setText(_translate("MainWindow", "Race"))
        self.character_alignement_label.setText(_translate("MainWindow", "Alignement"))
        self.character_name_label.setText(_translate("MainWindow", "Character name"))
        self.player_name_label.setText(_translate("MainWindow", "Player name"))
        self.character_height_label.setText(_translate("MainWindow", "Height"))
        self.character_weight_label.setText(_translate("MainWindow", "Weight"))
        self.character_eyes_label.setText(_translate("MainWindow", "Eyes"))
        self.character_hair_label.setText(_translate("MainWindow", "Hair"))
        self.character_size_label.setText(_translate("MainWindow", "Size"))
        self.character_age_label.setText(_translate("MainWindow", "Age"))
        self.character_gender_label.setText(_translate("MainWindow", "Gender"))
        self.character_level_label.setText(_translate("MainWindow", "Level"))

    def set_default(self):
        self.character_race.setText("Lorem ipsum")
        self.character_alignement.setText("Lorem ipsum")
        self.character_class.setText("Lorem ipsum")
        self.character_faith.setText("Lorem ipsum")
        self.character_name.setText("Lorem ipsum")
        self.character_height.setText("10")
        self.character_weight.setText("10")
        self.character_hair.setText("Lorem ipsum")
        self.player_name.setText("Lorem ipsum")
        self.character_eyes.setText("Lorem ipsum")
        self.character_gender.setText("Lorem ipsum")
        self.character_age.setText("10")
        self.character_size.setText("Lorem ipsum")
        self.character_level.setText("10")

    def create_palette(self):
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        return palette
