from PyQt5 import QtWidgets, QtCore

from core.character import Character
from gui.frames.qt_generic_classes import DefaultBox
from gui.frames.qt_generic_functions import create_qlabel, create_qline_edit, update_texts


class SavingThrowsBox(DefaultBox):
    char_core: Character

    # TODO Column labels centered
    # TODO - generalized translation
    # TODO - adding widgets by rows/columns
    def __init__(self, parent, position, size, char_core):
        self.char_core = char_core
        self.root = QtWidgets.QGroupBox(parent)
        self.root.setGeometry(QtCore.QRect(*position, *size))
        self.root.setObjectName("SavingThrowsBox")
        self.container = QtWidgets.QWidget(self.root)
        self.container.setObjectName("layoutWidget2")
        self.layout = QtWidgets.QGridLayout(self.container)
        self.layout.setObjectName("SavingThrowsLayout")
        self.layout.setContentsMargins(20, 10, 10, 20)
        self.layout.setSpacing(10)
        qlabel_dict = dict(parent=self.container,)
        qline_dict_disabled = dict(parent=self.container, min_size=(15, 23), enabled=False)
        qline_update_fortitude = dict(parent=self.container, min_size=(15, 23),
                                      function_on_text_changed=self._update_fortitude_text)
        qline_update_reflex = dict(parent=self.container, min_size=(15, 23),
                                   function_on_text_changed=self._update_reflex_text)
        qline_update_will = dict(parent=self.container, min_size=(15, 23),
                                 function_on_text_changed=self._update_will_text)

        self.fortitude_total = create_qline_edit("fortitude_total", str_format="{:+d}", **qline_dict_disabled)
        self.fortitude_class_bonus = create_qline_edit("fortitude_class_base", **qline_update_fortitude)
        self.fortitude_attr_bonus = create_qline_edit("fortitude_attr_bonus", **qline_dict_disabled)
        self.fortitude_size_bonus = create_qline_edit("fortitude_size_bonus", **qline_update_fortitude)
        self.fortitude_misc_bonus = create_qline_edit("fortitude_misc_bonus", **qline_update_fortitude)

        self.reflex_total = create_qline_edit("reflex_total", str_format="{:+d}", **qline_dict_disabled)
        self.reflex_class_bonus = create_qline_edit("reflex_class_bonus", **qline_update_reflex)
        self.reflex_attr_bonus = create_qline_edit("reflex_attr_bonus", **qline_dict_disabled)
        self.reflex_size_bonus = create_qline_edit("reflex_size_bonus", **qline_update_reflex)
        self.reflex_misc_bonus = create_qline_edit("reflex_misc_bonus", **qline_update_reflex)

        self.will_total = create_qline_edit("will_total", str_format="{:+d}", **qline_dict_disabled)
        self.will_class_bonus = create_qline_edit("will_class_bonus", **qline_update_will)
        self.will_attr_bonus = create_qline_edit("will_attr_bonus", **qline_dict_disabled)
        self.will_size_bonus = create_qline_edit("will_size_bonus", **qline_update_will)
        self.will_misc_bonus = create_qline_edit("will_misc_bonus", **qline_update_will)

        self.reflex_label = create_qlabel("reflex_label", align=QtCore.Qt.AlignRight, **qlabel_dict)
        self.will_label = create_qlabel("will_label", align=QtCore.Qt.AlignRight,**qlabel_dict)
        self.total_label = create_qlabel("total_label", align=QtCore.Qt.AlignRight,**qlabel_dict)
        self.class_base_label = create_qlabel("class_base_label", **qlabel_dict)
        self.attr_bonus_label = create_qlabel("attr_bonus_label", **qlabel_dict)
        self.size_bonus_label = create_qlabel("size_bonus_label", **qlabel_dict)
        self.misc_bonus_label = create_qlabel("misc_bonus_label", **qlabel_dict)
        self.fortitude_label = create_qlabel("fortitude_label", **qlabel_dict)

        self.add_to_layout()
        self.translate()
        self.set_default()
        self.root.setLayout(self.layout)
        self.set_values_from_attributes()

    def add_to_layout(self):
        self.layout.addWidget(self.will_misc_bonus, 3, 9, 1, 1)
        self.layout.addWidget(self.total_label, 0, 1, 1, 1)
        self.layout.addWidget(self.class_base_label, 0, 3, 1, 1)
        self.layout.addWidget(self.attr_bonus_label, 0, 5, 1, 1)
        self.layout.addWidget(self.size_bonus_label, 0, 7, 1, 1)
        self.layout.addWidget(self.misc_bonus_label, 0, 9, 1, 1)
        self.layout.addWidget(self.fortitude_label, 1, 0, 1, 1)
        self.layout.addWidget(self.fortitude_total, 1, 1, 1, 1)
        self.layout.addWidget(self.fortitude_class_bonus, 1, 3, 1, 1)
        self.layout.addWidget(self.fortitude_attr_bonus, 1, 5, 1, 1)
        self.layout.addWidget(self.fortitude_size_bonus, 1, 7, 1, 1)
        self.layout.addWidget(self.fortitude_misc_bonus, 1, 9, 1, 1)
        self.layout.addWidget(self.reflex_label, 2, 0, 1, 1)
        self.layout.addWidget(self.reflex_total, 2, 1, 1, 1)
        self.layout.addWidget(self.reflex_class_bonus, 2, 3, 1, 1)
        self.layout.addWidget(self.reflex_attr_bonus, 2, 5, 1, 1)
        self.layout.addWidget(self.reflex_size_bonus, 2, 7, 1, 1)
        self.layout.addWidget(self.reflex_misc_bonus, 2, 9, 1, 1)
        self.layout.addWidget(self.will_label, 3, 0, 1, 1)
        self.layout.addWidget(self.will_total, 3, 1, 1, 1)
        self.layout.addWidget(self.will_class_bonus, 3, 3, 1, 1)
        self.layout.addWidget(self.will_attr_bonus, 3, 5, 1, 1)
        self.layout.addWidget(self.will_size_bonus, 3, 7, 1, 1)

    def translate(self):
        _translate = QtCore.QCoreApplication.translate
        self.root.setTitle(_translate("MainWindow", "Saving throws"))
        self.total_label.setText(_translate("MainWindow", "Total"))
        self.class_base_label.setText(_translate("MainWindow", "Base"))
        self.attr_bonus_label.setText(_translate("MainWindow", "Attr"))
        self.size_bonus_label.setText(_translate("MainWindow", "Size"))
        self.misc_bonus_label.setText(_translate("MainWindow", "Misc"))
        self.fortitude_label.setText(_translate("MainWindow", "Fortitude"))
        self.reflex_label.setText(_translate("MainWindow", "Reflex"))
        self.will_label.setText(_translate("MainWindow", "Will"))

    def set_default(self):
        self.fortitude_total.setText("10")
        self.fortitude_class_bonus.setText("10")
        self.fortitude_attr_bonus.setText("10")
        self.fortitude_size_bonus.setText("10")
        self.fortitude_misc_bonus.setText("10")
        self.reflex_total.setText("10")
        self.reflex_class_bonus.setText("10")
        self.reflex_attr_bonus.setText("10")
        self.reflex_size_bonus.setText("10")
        self.reflex_misc_bonus.setText("10")
        self.will_total.setText("10")
        self.will_class_bonus.setText("10")
        self.will_attr_bonus.setText("10")
        self.will_size_bonus.setText("10")
        self.will_misc_bonus.setText("10")

    def set_values_from_attributes(self):
        self.reflex_attr_bonus.setText(str(self.char_core.attributes.dex['mod']))
        self.will_attr_bonus.setText(str(self.char_core.attributes.wis['mod']))
        self.fortitude_attr_bonus.setText(str(self.char_core.attributes.con['mod']))
        self.update_saving_throws_texts()

    def update_saving_throws_texts(self):
        self._update_fortitude_text()
        self._update_reflex_text()
        self._update_will_text()

    def _update_fortitude_text(self):
        update_texts(self, "fortitude_total", ["fortitude_class_bonus", "fortitude_attr_bonus",
                                               "fortitude_size_bonus", "fortitude_misc_bonus"])

    def _update_reflex_text(self):
        update_texts(self, "reflex_total", ["reflex_class_bonus", "reflex_attr_bonus",
                                            "reflex_size_bonus", "reflex_misc_bonus"])

    def _update_will_text(self):
        update_texts(self, "will_total", ["will_class_bonus", "will_attr_bonus",
                                          "will_size_bonus", "will_misc_bonus"])
