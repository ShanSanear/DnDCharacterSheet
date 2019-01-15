from PyQt5 import QtWidgets, QtCore

from qt_gui.boxes.box import DefaultBox


class SkillsBox(DefaultBox):
    # TODO - interclass skills need additional checkbox
    # TODO - function based widgets and labels
    # TODO - adding single skill using function, similar to items
    # TODO - generalized translation
    # TODO - adding widgets by rows/columns
    def __init__(self, parent, position, size):
        self.root = QtWidgets.QGroupBox(parent)
        self.root.setGeometry(QtCore.QRect(*position, *size))
        self.root.setObjectName("SkillsBox")
        self.container = QtWidgets.QWidget(self.root)
        self.container.setObjectName("gridLayoutWidget_5")
        self.layout = QtWidgets.QGridLayout(self.container)
        self.layout.setContentsMargins(9, 9, 9, 9)
        self.layout.setSpacing(6)
        self.root.setMaximumHeight(100)
        self.layout.setObjectName("SkillsLayout")
        self.skills_cross_class_label = QtWidgets.QLabel(self.container)
        self.skills_cross_class_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.skills_cross_class_label.setAlignment(QtCore.Qt.AlignCenter)
        self.skills_cross_class_label.setObjectName("skills_description_label")
        self.skills_1_cross_class_checkbox = QtWidgets.QCheckBox(self.container)
        self.skills_1_cross_class_checkbox.setObjectName("skills_1_description_button")
        self.skills_1_cross_class_checkbox.setMaximumWidth(20)
        self.skills_1_misc_mod = QtWidgets.QLineEdit(self.container)
        self.skills_1_misc_mod.setMinimumSize(QtCore.QSize(0, 23))
        self.skills_1_misc_mod.setMaximumSize(QtCore.QSize(54, 20))
        self.skills_1_misc_mod.setAlignment(QtCore.Qt.AlignCenter)
        self.skills_1_misc_mod.setObjectName("skills_1_misc_mod")
        self.skills_1_attr_mod = QtWidgets.QLineEdit(self.container)
        self.skills_1_attr_mod.setEnabled(False)
        self.skills_1_attr_mod.setMinimumSize(QtCore.QSize(0, 23))
        self.skills_1_attr_mod.setMaximumSize(QtCore.QSize(54, 20))
        self.skills_1_attr_mod.setAutoFillBackground(False)
        self.skills_1_attr_mod.setAlignment(QtCore.Qt.AlignCenter)
        self.skills_1_attr_mod.setReadOnly(True)
        self.skills_1_attr_mod.setObjectName("skills_1_attr_mod")
        self.skills_1_rank = QtWidgets.QLineEdit(self.container)
        self.skills_1_rank.setMinimumSize(QtCore.QSize(0, 23))
        self.skills_1_rank.setMaximumSize(QtCore.QSize(54, 20))
        self.skills_1_rank.setAlignment(QtCore.Qt.AlignCenter)
        self.skills_1_rank.setObjectName("skills_1_rank")
        self.skills_1_total = QtWidgets.QLineEdit(self.container)
        self.skills_1_total.setMinimumSize(QtCore.QSize(0, 23))
        self.skills_1_total.setMaximumSize(QtCore.QSize(54, 20))
        self.skills_1_total.setAlignment(QtCore.Qt.AlignCenter)
        self.skills_1_total.setObjectName("skills_1_total")
        self.skills_1_skill_name = QtWidgets.QLineEdit(self.container)
        self.skills_1_skill_name.setMinimumSize(QtCore.QSize(0, 23))
        self.skills_1_skill_name.setObjectName("skills_1_skill_name")
        self.skills_rank_label = QtWidgets.QLabel(self.container)
        self.skills_rank_label.setMaximumSize(QtCore.QSize(54, 20))
        self.skills_rank_label.setAlignment(QtCore.Qt.AlignCenter)
        self.skills_rank_label.setObjectName("skills_rank_label")
        self.skills_attr_mod_label = QtWidgets.QLabel(self.container)
        self.skills_attr_mod_label.setMaximumSize(QtCore.QSize(54, 20))
        self.skills_attr_mod_label.setAlignment(QtCore.Qt.AlignCenter)
        self.skills_attr_mod_label.setObjectName("skills_attr_mod_label")
        self.skills_misc_label = QtWidgets.QLabel(self.container)
        self.skills_misc_label.setMaximumSize(QtCore.QSize(54, 20))
        self.skills_misc_label.setAlignment(QtCore.Qt.AlignCenter)
        self.skills_misc_label.setObjectName("skills_misc_label")
        self.skills_1_attr_choice = QtWidgets.QComboBox(self.container)
        self.skills_1_attr_choice.setMaximumSize(QtCore.QSize(69, 20))
        self.skills_1_attr_choice.setObjectName("skills_1_attr_choice")
        self.skills_1_attr_choice.addItem("")
        self.skills_1_attr_choice.addItem("")
        self.skills_1_attr_choice.addItem("")
        self.skills_1_attr_choice.addItem("")
        self.skills_1_attr_choice.addItem("")
        self.skills_1_attr_choice.addItem("")
        self.skills_skill_name_label = QtWidgets.QLabel(self.container)
        self.skills_skill_name_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.skills_skill_name_label.setObjectName("skills_skill_name_label")
        self.skills_attr_choice_label = QtWidgets.QLabel(self.container)
        self.skills_attr_choice_label.setMaximumSize(QtCore.QSize(69, 20))
        self.skills_attr_choice_label.setAlignment(QtCore.Qt.AlignCenter)
        self.skills_attr_choice_label.setObjectName("skills_attr_choice_label")
        self.skills_total_label = QtWidgets.QLabel(self.container)
        self.skills_total_label.setMaximumSize(QtCore.QSize(54, 20))
        self.skills_total_label.setAlignment(QtCore.Qt.AlignCenter)
        self.skills_total_label.setObjectName("skills_total_label")

        self.add_to_layout()
        self.translate()
        self.set_default()
        self.root.setLayout(self.layout)

    def add_to_layout(self):
        self.layout.addWidget(self.skills_cross_class_label, 0, 6, 1, 1)
        self.layout.addWidget(self.skills_1_cross_class_checkbox, 1, 6, 1, 1)
        self.layout.addWidget(self.skills_1_misc_mod, 1, 5, 1, 1)
        self.layout.addWidget(self.skills_1_attr_mod, 1, 3, 1, 1)
        self.layout.addWidget(self.skills_1_rank, 1, 4, 1, 1)
        self.layout.addWidget(self.skills_1_total, 1, 2, 1, 1)
        self.layout.addWidget(self.skills_1_skill_name, 1, 0, 1, 1)
        self.layout.addWidget(self.skills_rank_label, 0, 4, 1, 1)
        self.layout.addWidget(self.skills_attr_mod_label, 0, 3, 1, 1)
        self.layout.addWidget(self.skills_misc_label, 0, 5, 1, 1)
        self.layout.addWidget(self.skills_1_attr_choice, 1, 1, 1, 1)
        self.layout.addWidget(self.skills_skill_name_label, 0, 0, 1, 1)
        self.layout.addWidget(self.skills_attr_choice_label, 0, 1, 1, 1)
        self.layout.addWidget(self.skills_total_label, 0, 2, 1, 1)

    def translate(self):
        _translate = QtCore.QCoreApplication.translate
        self.root.setTitle(_translate("MainWindow", "Skills"))
        self.skills_cross_class_label.setText(_translate("MainWindow", "CC"))
        self.skills_1_cross_class_checkbox.setText(_translate("MainWindow", "..."))
        self.skills_rank_label.setText(_translate("MainWindow", "Rank"))
        self.skills_attr_mod_label.setText(_translate("MainWindow", "Attr mod"))
        self.skills_misc_label.setText(_translate("MainWindow", "Misc"))
        self.skills_skill_name_label.setText(_translate("MainWindow", "Skill name"))
        self.skills_attr_choice_label.setText(_translate("MainWindow", "Attr"))
        self.skills_total_label.setText(_translate("MainWindow", "Total"))
        self.skills_1_attr_choice.setItemText(0, _translate("MainWindow", "STR"))
        self.skills_1_attr_choice.setItemText(1, _translate("MainWindow", "DEX"))
        self.skills_1_attr_choice.setItemText(2, _translate("MainWindow", "CON"))
        self.skills_1_attr_choice.setItemText(3, _translate("MainWindow", "INT"))
        self.skills_1_attr_choice.setItemText(4, _translate("MainWindow", "WIS"))
        self.skills_1_attr_choice.setItemText(5, _translate("MainWindow", "CHA"))

    def set_default(self):
        self.skills_1_misc_mod.setText("10")
        self.skills_1_attr_mod.setText("10")
        self.skills_1_rank.setText("10")
        self.skills_1_total.setText("10")
        self.skills_1_skill_name.setText("Spostrzegawczosc")
