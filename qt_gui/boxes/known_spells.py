from types import SimpleNamespace

from PyQt5 import QtWidgets, QtCore

from qt_gui.boxes.qt_generic_functions import create_qlabel, create_qline_edit


class KnownSpellsBox:
    # TODO - generalized adding known spells
    # TODO - generalized translation
    # TODO - adding widgets by rows/columns
    def __init__(self, parent, position, size):
        self.root = QtWidgets.QGroupBox(parent)
        self.root.setGeometry(QtCore.QRect(*position, *size))
        self.root.setObjectName("KnownSpellsBox")
        self.container = QtWidgets.QWidget(self.root)
        self.container.setObjectName("gridLayoutWidget_11")
        self.layout = QtWidgets.QGridLayout(self.container)
        self.layout.setObjectName("KnownSpellsLayout")

        self.spells = []
        qlabel_dict = dict(parent=self.container, max_size=(20, 16777215))
        qlabel_dict_2 = dict(parent=self.container)

        self.known_spells_lvl_label = create_qlabel("known_spells_lvl_label_1", **qlabel_dict)

        self.known_spells_name_label = create_qlabel("known_spells_name_label_1", **qlabel_dict_2)

        self.known_spells_description_button_label = create_qlabel("known_spells_description_label_1",
                                                                   **qlabel_dict_2)
        self.known_spells_description_field_label = create_qlabel("known_spells_description_field_label_1",
                                                                  **qlabel_dict_2)

        for _ in range(15):
            self.add_spell()
        self.add_to_layout()
        self.translate()
        self.root.setLayout(self.layout)

    def create_spell(self):
        qline_dict = dict(parent=self.container, max_size=(20, 16777215))
        qline_dict_2 = dict(parent=self.container, min_size=(0, 10))
        new_spell = SimpleNamespace()
        new_spell.lvl = create_qline_edit("known_spells_1_lvl", **qline_dict)
        new_spell.lvl.setText("10")
        new_spell.name = create_qline_edit("known_spells_1_name", **qline_dict_2)
        new_spell.name.setText("Lorem ipsum")
        new_spell.description_field = QtWidgets.QLineEdit(self.container)
        new_spell.description_field.setObjectName("known_spells_1_description_field")
        new_spell.description_field.setMinimumSize(QtCore.QSize(350, 23))
        new_spell.description_field.setText(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sapien urna, egestas eu tempor at, pretium nec orci. In nec pharetra tellus. In malesuada erat tellus, eget efficitur elit convallis eu.")
        new_spell.description_button = QtWidgets.QPushButton(self.container)
        new_spell.description_button.setObjectName("known_spells_1_description_button")
        new_spell.description_button.setMaximumWidth(20)
        new_spell.description_button.setText("...")
        return new_spell

    def add_spell(self):
        spell_idx = len(self.spells)
        new_spell = self.create_spell()
        self.spells.append(new_spell)
        for el_idx, element in enumerate(new_spell.__dict__.values()):
            self.layout.addWidget(element, spell_idx + 1, el_idx, 1, 1)
        self.update_container_size()

    def add_to_layout(self):
        self.layout.addWidget(self.known_spells_lvl_label, 0, 0, 1, 1)
        self.layout.addWidget(self.known_spells_name_label, 0, 1, 1, 1)
        self.layout.addWidget(self.known_spells_description_field_label, 0, 2, 1, 1)
        self.layout.addWidget(self.known_spells_description_button_label, 0, 3, 1, 1)

        # self.layout.addWidget(self.known_spells_1_lvl, 1, 0, 1, 1)
        # self.layout.addWidget(self.known_spells_1_name, 1, 1, 1, 1)
        # self.layout.addWidget(self.known_spells_1_description_field, 1, 2, 1, 1)
        # self.layout.addWidget(self.known_spells_1_description_button, 1, 3, 1, 1)

    def translate(self):
        _translate = QtCore.QCoreApplication.translate
        self.root.setTitle(_translate("MainWindow", "Known Spells"))
        self.known_spells_lvl_label.setText(_translate("MainWindow", "LVL"))
        self.known_spells_name_label.setText(_translate("MainWindow", "Spell name"))
        self.known_spells_description_button_label.setText(_translate("MainWindow", "Desc"))
        self.known_spells_description_field_label.setText("DESC")
        # self.known_spells_1_lvl.setText(_translate("MainWindow", "10"))
        # self.known_spells_1_name.setText(_translate("MainWindow", "Oczyszczenie jedzenia i wody"))
        # self.known_spells_1_description_button.setText(_translate("MainWindow", "..."))
        # self.known_spells_1_description_field.setText(
        #     " Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sapien urna, egestas eu tempor at, pretium nec orci. In nec pharetra tellus. In malesuada erat tellus, eget efficitur elit convallis eu. Integer consectetur porttitor eros vitae sagittis. Vestibulum commodo suscipit varius. Nulla vitae fringilla velit. Mauris sagittis tellus urna. Class aptent tac")

    def update_container_size(self):
        root_width = self.root.width()
        root_height = self.root.height()
        container_width = self.container.width()
        container_height = self.container.height()
        self.root.setMinimumSize(QtCore.QSize(root_width, root_height + 30))
        self.container.setMinimumSize(QtCore.QSize(container_width, container_height + 30))
