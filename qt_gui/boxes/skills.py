from types import SimpleNamespace

from PyQt5 import QtWidgets, QtCore

from qt_gui.boxes.qt_generic_classes import DefaultBox


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
        self.skills = []

        self.create_labels()
        for _ in range(10):
            self.add_skill()

        self.add_to_layout()
        self.translate()
        self.set_default()
        self.root.setLayout(self.layout)

    def create_new_skill(self):
        new_skill = SimpleNamespace()
        skill_idx = len(self.skills)
        new_skill.skill_name = QtWidgets.QLineEdit(self.container)
        new_skill.skill_name.setMinimumSize(QtCore.QSize(0, 23))
        new_skill.skill_name.setObjectName(f"skills{skill_idx}skill_name")
        new_skill.skill_name.setText(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sapien urna, egestas eu tempor at, pretium nec orci.")

        new_skill.attr_choice = QtWidgets.QComboBox(self.container)
        new_skill.attr_choice.setMaximumSize(QtCore.QSize(69, 20))
        new_skill.attr_choice.setObjectName(f"skills{skill_idx}attr_choice")
        new_skill.attr_choice.addItem("STR")
        new_skill.attr_choice.addItem("DEX")
        new_skill.attr_choice.addItem("CON")
        new_skill.attr_choice.addItem("INT")
        new_skill.attr_choice.addItem("WIS")
        new_skill.attr_choice.addItem("CHA")
        new_skill.attr_choice.setItemText(0, "STR")
        new_skill.total = QtWidgets.QLineEdit(self.container)
        new_skill.total.setMinimumSize(QtCore.QSize(0, 23))
        new_skill.total.setMaximumSize(QtCore.QSize(54, 20))
        new_skill.total.setAlignment(QtCore.Qt.AlignCenter)
        new_skill.total.setObjectName(f"skills{skill_idx}total")
        new_skill.total.setText("10")

        new_skill.attr_mod = QtWidgets.QLineEdit(self.container)
        new_skill.attr_mod.setEnabled(False)
        new_skill.attr_mod.setMinimumSize(QtCore.QSize(0, 23))
        new_skill.attr_mod.setMaximumSize(QtCore.QSize(54, 20))
        new_skill.attr_mod.setAutoFillBackground(False)
        new_skill.attr_mod.setAlignment(QtCore.Qt.AlignCenter)
        new_skill.attr_mod.setReadOnly(True)
        new_skill.attr_mod.setObjectName(f"skills{skill_idx}attr_mod")
        new_skill.attr_mod.setText("10")

        new_skill.rank = QtWidgets.QLineEdit(self.container)
        new_skill.rank.setMinimumSize(QtCore.QSize(0, 23))
        new_skill.rank.setMaximumSize(QtCore.QSize(54, 20))
        new_skill.rank.setAlignment(QtCore.Qt.AlignCenter)
        new_skill.rank.setObjectName(f"skills{skill_idx}rank")
        new_skill.rank.setText("10")

        new_skill.misc_mod = QtWidgets.QLineEdit(self.container)
        new_skill.misc_mod.setMinimumSize(QtCore.QSize(0, 23))
        new_skill.misc_mod.setMaximumSize(QtCore.QSize(54, 20))
        new_skill.misc_mod.setAlignment(QtCore.Qt.AlignCenter)
        new_skill.misc_mod.setObjectName(f"skills_{skill_idx}_misc_mod")
        new_skill.misc_mod.setText("10")

        new_skill.cross_class_checkbox = QtWidgets.QCheckBox(self.container)
        new_skill.cross_class_checkbox.setObjectName(f"skills{skill_idx}description_button")

        return new_skill

    def add_skill(self):
        skill_idx = len(self.skills)
        new_skill = self.create_new_skill()
        self.skills.append(new_skill)
        for el_idx, element in enumerate(new_skill.__dict__.values()):
            self.layout.addWidget(element, skill_idx + 1, el_idx, 1, 1)
        self.update_container_size()

    def create_labels(self):
        self.skills_cross_class_label = QtWidgets.QLabel(self.container)
        self.skills_cross_class_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.skills_cross_class_label.setAlignment(QtCore.Qt.AlignCenter)
        self.skills_cross_class_label.setObjectName("skills_description_label")
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

    def add_to_layout(self):
        self.layout.addWidget(self.skills_cross_class_label, 0, 6, 1, 1)
        self.layout.addWidget(self.skills_rank_label, 0, 4, 1, 1)
        self.layout.addWidget(self.skills_attr_mod_label, 0, 3, 1, 1)
        self.layout.addWidget(self.skills_misc_label, 0, 5, 1, 1)
        self.layout.addWidget(self.skills_skill_name_label, 0, 0, 1, 1)
        self.layout.addWidget(self.skills_attr_choice_label, 0, 1, 1, 1)
        self.layout.addWidget(self.skills_total_label, 0, 2, 1, 1)

    def translate(self):
        _translate = QtCore.QCoreApplication.translate
        self.root.setTitle(_translate("MainWindow", "Skills"))
        self.skills_cross_class_label.setText(_translate("MainWindow", "CC"))
        self.skills_rank_label.setText(_translate("MainWindow", "Rank"))
        self.skills_attr_mod_label.setText(_translate("MainWindow", "Attr mod"))
        self.skills_misc_label.setText(_translate("MainWindow", "Misc"))
        self.skills_skill_name_label.setText(_translate("MainWindow", "Skill name"))
        self.skills_attr_choice_label.setText(_translate("MainWindow", "Attr"))
        self.skills_total_label.setText(_translate("MainWindow", "Total"))

    def set_default(self):
        pass

    def update_container_size(self):
        root_width = self.root.width()
        root_height = self.root.height()
        container_width = self.container.width()
        container_height = self.container.height()
        self.root.setMinimumSize(QtCore.QSize(root_width, root_height + 40))
        self.container.setMinimumSize(QtCore.QSize(container_width, container_height + 40))
