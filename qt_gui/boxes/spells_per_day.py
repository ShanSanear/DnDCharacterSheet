from PyQt5 import QtWidgets, QtCore

from qt_gui.boxes.qt_line_edits import create_qlabel, create_qline_edit, numeric_label
from qt_gui.boxes.box import DefaultBox


class SpellsPerDayBox(DefaultBox):
    def __init__(self, centralwidget):
        self.root = QtWidgets.QGroupBox(centralwidget)
        self.root.setGeometry(QtCore.QRect(1430, 560, 271, 631))
        self.root.setObjectName("SpellsPerDayBox")
        self.container = QtWidgets.QWidget(self.root)
        self.container.setGeometry(QtCore.QRect(10, 20, 251, 321))
        self.container.setObjectName("gridLayoutWidget_9")
        self.layout = QtWidgets.QGridLayout(self.container)
        self.layout.setContentsMargins(9, 9, 9, 9)
        self.layout.setSpacing(6)
        self.layout.setObjectName("SpellsPerDayLayout")

        qline_dict = dict(parent=self.container, min_size=(0, 23), align=QtCore.Qt.AlignCenter)
        qlabel_dict = dict(parent=self.container, align=QtCore.Qt.AlignCenter)

        self.spells_per_day_level_label = create_qlabel("spells_per_day_level_label", **qlabel_dict)
        self.spells_per_day_spells_per_day_label = create_qlabel("spells_per_day_spells_per_day_label",
                                                                 **qlabel_dict)
        self.spells_per_day_extra_spells = create_qlabel("spells_per_day_extra_spells", **qlabel_dict)
        self.spells_per_day_base_spell_dc = create_qlabel("spells_per_day_base_spell_dc", **qlabel_dict)

        self.spells_per_day_dc_lvl_0 = create_qline_edit("spells_per_day_dc_lvl_0", **qline_dict)
        self.spells_per_day_spells_per_day_lvl_0 = create_qline_edit("spells_per_day_spells_per_day_lvl_0",
                                                                     **qline_dict)

        self.spells_per_day_dc_lvl_1 = create_qline_edit("spells_per_day_dc_lvl_1", **qline_dict)

        self.spells_per_day_extra_spells_lvl_0 = create_qline_edit("spells_per_day_extra_spells_lvl_0",
                                                                   **qline_dict)

        self.spells_per_day_extra_spells_lvl_1 = create_qline_edit("spells_per_day_extra_spells_lvl_1",
                                                                   **qline_dict)

        self.spells_per_day_spells_per_day_lvl_2 = create_qline_edit("spells_per_day_spells_per_day_lvl_2",
                                                                     **qline_dict)

        self.spells_per_day_dc_lvl_2 = create_qline_edit("spells_per_day_dc_lvl_2", **qline_dict)

        self.spells_per_day_spells_per_day_lvl_1 = create_qline_edit("spells_per_day_spells_per_day_lvl_1",
                                                                     **qline_dict)

        self.spells_per_day_spells_per_day_lvl_5 = create_qline_edit("spells_per_day_spells_per_day_lvl_5",
                                                                     **qline_dict)

        self.spells_per_day_extra_spells_lvl_2 = create_qline_edit("spells_per_day_extra_spells_lvl_2",
                                                                   **qline_dict)

        self.spells_per_day_dc_lvl_3 = create_qline_edit("spells_per_day_dc_lvl_3", **qline_dict)

        self.spells_per_day_spells_per_day_lvl_4 = create_qline_edit("spells_per_day_spells_per_day_lvl_4",
                                                                     **qline_dict)

        self.spells_per_day_extra_spells_lvl_3 = create_qline_edit("spells_per_day_extra_spells_lvl_3",
                                                                   **qline_dict)

        self.spells_per_day_dc_lvl_6 = create_qline_edit("spells_per_day_dc_lvl_6", **qline_dict)

        self.spells_per_day_extra_spells_lvl_4 = create_qline_edit("spells_per_day_extra_spells_lvl_4",
                                                                   **qline_dict)

        self.spells_per_day_dc_lvl_5 = create_qline_edit("spells_per_day_dc_lvl_5", **qline_dict)

        self.spells_per_day_spells_per_day_lvl_3 = create_qline_edit("spells_per_day_spells_per_day_lvl_3",
                                                                     **qline_dict)

        self.spells_per_day_dc_lvl_4 = create_qline_edit("spells_per_day_dc_lvl_4", **qline_dict)

        self.spells_per_day_extra_spells_lvl_8 = create_qline_edit("spells_per_day_extra_spells_lvl_8",
                                                                   **qline_dict)

        self.spells_per_day_extra_spells_lvl_5 = create_qline_edit("spells_per_day_extra_spells_lvl_5",
                                                                   **qline_dict)

        self.spells_per_day_dc_lvl_8 = create_qline_edit("spells_per_day_dc_lvl_8", **qline_dict)

        self.spells_per_day_dc_lvl_7 = create_qline_edit("spells_per_day_dc_lvl_7", **qline_dict)

        self.spells_per_day_extra_spells_lvl_7 = create_qline_edit("spells_per_day_extra_spells_lvl_7",
                                                                   **qline_dict)

        self.spells_per_day_extra_spells_lvl_6 = create_qline_edit("spells_per_day_extra_spells_lvl_6",
                                                                   **qline_dict)

        self.spells_per_day_spells_per_day_lvl_7 = create_qline_edit("spells_per_day_spells_per_day_lvl_7",
                                                                     **qline_dict)

        self.spells_per_day_spells_per_day_lvl_6 = create_qline_edit("spells_per_day_spells_per_day_lvl_6",
                                                                     **qline_dict)

        self.spells_per_day_spells_per_day_lvl_8 = create_qline_edit("spells_per_day_spells_per_day_lvl_8",
                                                                     **qline_dict)
        self.spells_per_day_dc_lvl_9 = create_qline_edit("spells_per_day_dc_lvl_9", **qline_dict)
        self.spells_per_day_spells_per_day_lvl_9 = create_qline_edit("spells_per_day_spells_per_day_lvl_9",
                                                                     **qline_dict)
        self.spells_per_day_extra_spells_lvl_9 = create_qline_edit("spells_per_day_extra_spells_lvl_9",
                                                                   **qline_dict)

        self._num_0 = numeric_label("_num_0", **qlabel_dict)
        self._num_1 = numeric_label("_num_1", **qlabel_dict)
        self._num_2 = numeric_label("_num_2", **qlabel_dict)
        self._num_3 = numeric_label("_num_3", **qlabel_dict)
        self._num_4 = numeric_label("_num_4", **qlabel_dict)
        self._num_5 = numeric_label("_num_5", **qlabel_dict)
        self._num_6 = numeric_label("_num_6", **qlabel_dict)
        self._num_7 = numeric_label("_num_7", **qlabel_dict)
        self._num_8 = numeric_label("_num_8", **qlabel_dict)
        self._num_9 = numeric_label("_num_9", **qlabel_dict)

        self.add_to_layout()
        self.translate()

    def add_to_layout(self):
        self.layout.addWidget(self._num_0, 1, 1, 1, 1)
        self.layout.addWidget(self._num_1, 2, 1, 1, 1)
        self.layout.addWidget(self._num_2, 3, 1, 1, 1)
        self.layout.addWidget(self._num_3, 4, 1, 1, 1)
        self.layout.addWidget(self._num_4, 5, 1, 1, 1)
        self.layout.addWidget(self._num_5, 6, 1, 1, 1)
        self.layout.addWidget(self._num_6, 7, 1, 1, 1)
        self.layout.addWidget(self._num_7, 8, 1, 1, 1)
        self.layout.addWidget(self._num_8, 9, 1, 1, 1)
        self.layout.addWidget(self._num_9, 10, 1, 1, 1)
        self.layout.addWidget(self.spells_per_day_dc_lvl_0, 1, 0, 1, 1)
        self.layout.addWidget(self.spells_per_day_level_label, 0, 1, 1, 1)
        self.layout.addWidget(self.spells_per_day_spells_per_day_label, 0, 2, 1, 1)
        self.layout.addWidget(self.spells_per_day_extra_spells, 0, 3, 1, 1)
        self.layout.addWidget(self.spells_per_day_spells_per_day_lvl_0, 1, 2, 1, 1)
        self.layout.addWidget(self.spells_per_day_dc_lvl_1, 2, 0, 1, 1)
        self.layout.addWidget(self.spells_per_day_extra_spells_lvl_0, 1, 3, 1, 1)
        self.layout.addWidget(self.spells_per_day_extra_spells_lvl_1, 2, 3, 1, 1)
        self.layout.addWidget(self.spells_per_day_spells_per_day_lvl_2, 3, 2, 1, 1)
        self.layout.addWidget(self.spells_per_day_dc_lvl_2, 3, 0, 1, 1)
        self.layout.addWidget(self.spells_per_day_spells_per_day_lvl_1, 2, 2, 1, 1)
        self.layout.addWidget(self.spells_per_day_spells_per_day_lvl_5, 6, 2, 1, 1)
        self.layout.addWidget(self.spells_per_day_extra_spells_lvl_2, 3, 3, 1, 1)
        self.layout.addWidget(self.spells_per_day_dc_lvl_3, 4, 0, 1, 1)
        self.layout.addWidget(self.spells_per_day_spells_per_day_lvl_4, 5, 2, 1, 1)
        self.layout.addWidget(self.spells_per_day_extra_spells_lvl_3, 4, 3, 1, 1)
        self.layout.addWidget(self.spells_per_day_dc_lvl_6, 7, 0, 1, 1)
        self.layout.addWidget(self.spells_per_day_extra_spells_lvl_4, 5, 3, 1, 1)
        self.layout.addWidget(self.spells_per_day_dc_lvl_5, 6, 0, 1, 1)
        self.layout.addWidget(self.spells_per_day_spells_per_day_lvl_3, 4, 2, 1, 1)
        self.layout.addWidget(self.spells_per_day_dc_lvl_4, 5, 0, 1, 1)
        self.layout.addWidget(self.spells_per_day_extra_spells_lvl_8, 9, 3, 1, 1)
        self.layout.addWidget(self.spells_per_day_extra_spells_lvl_5, 6, 3, 1, 1)
        self.layout.addWidget(self.spells_per_day_dc_lvl_8, 9, 0, 1, 1)
        self.layout.addWidget(self.spells_per_day_dc_lvl_7, 8, 0, 1, 1)
        self.layout.addWidget(self.spells_per_day_extra_spells_lvl_7, 8, 3, 1, 1)
        self.layout.addWidget(self.spells_per_day_extra_spells_lvl_6, 7, 3, 1, 1)
        self.layout.addWidget(self.spells_per_day_spells_per_day_lvl_7, 8, 2, 1, 1)
        self.layout.addWidget(self.spells_per_day_spells_per_day_lvl_6, 7, 2, 1, 1)
        self.layout.addWidget(self.spells_per_day_spells_per_day_lvl_8, 9, 2, 1, 1)
        self.layout.addWidget(self.spells_per_day_base_spell_dc, 0, 0, 1, 1)
        self.layout.addWidget(self.spells_per_day_spells_per_day_lvl_9, 10, 2, 1, 1)
        self.layout.addWidget(self.spells_per_day_dc_lvl_9, 10, 0, 1, 1)
        self.layout.addWidget(self.spells_per_day_extra_spells_lvl_9, 10, 3, 1, 1)

    def translate(self):
        _translate = QtCore.QCoreApplication.translate
        self.root.setTitle(_translate("MainWindow", "Spells per day / Spells DC"))
        self.spells_per_day_dc_lvl_0.setText(_translate("MainWindow", "10"))
        self.spells_per_day_level_label.setText(_translate("MainWindow", "Level"))
        self.spells_per_day_spells_per_day_label.setText(_translate("MainWindow", "Spells/Day"))
        self.spells_per_day_extra_spells.setText(_translate("MainWindow", "Extra spells"))
        self.spells_per_day_spells_per_day_lvl_0.setText(_translate("MainWindow", "10"))
        self.spells_per_day_dc_lvl_1.setText(_translate("MainWindow", "10"))
        self.spells_per_day_extra_spells_lvl_0.setText(_translate("MainWindow", "10"))
        self._num_0.setText(_translate("MainWindow", "0"))
        self.spells_per_day_extra_spells_lvl_1.setText(_translate("MainWindow", "10"))
        self.spells_per_day_spells_per_day_lvl_2.setText(_translate("MainWindow", "10"))
        self.spells_per_day_dc_lvl_2.setText(_translate("MainWindow", "10"))
        self.spells_per_day_spells_per_day_lvl_1.setText(_translate("MainWindow", "10"))
        self.spells_per_day_spells_per_day_lvl_5.setText(_translate("MainWindow", "10"))
        self.spells_per_day_extra_spells_lvl_2.setText(_translate("MainWindow", "10"))
        self.spells_per_day_dc_lvl_3.setText(_translate("MainWindow", "10"))
        self.spells_per_day_spells_per_day_lvl_4.setText(_translate("MainWindow", "10"))
        self.spells_per_day_extra_spells_lvl_3.setText(_translate("MainWindow", "10"))
        self.spells_per_day_dc_lvl_6.setText(_translate("MainWindow", "10"))
        self.spells_per_day_extra_spells_lvl_4.setText(_translate("MainWindow", "10"))
        self.spells_per_day_dc_lvl_5.setText(_translate("MainWindow", "10"))
        self.spells_per_day_spells_per_day_lvl_3.setText(_translate("MainWindow", "10"))
        self.spells_per_day_dc_lvl_4.setText(_translate("MainWindow", "10"))
        self.spells_per_day_extra_spells_lvl_8.setText(_translate("MainWindow", "10"))
        self.spells_per_day_extra_spells_lvl_5.setText(_translate("MainWindow", "10"))
        self.spells_per_day_dc_lvl_8.setText(_translate("MainWindow", "10"))
        self.spells_per_day_dc_lvl_7.setText(_translate("MainWindow", "10"))
        self.spells_per_day_extra_spells_lvl_7.setText(_translate("MainWindow", "10"))
        self.spells_per_day_extra_spells_lvl_6.setText(_translate("MainWindow", "10"))
        self.spells_per_day_spells_per_day_lvl_7.setText(_translate("MainWindow", "10"))
        self.spells_per_day_spells_per_day_lvl_6.setText(_translate("MainWindow", "10"))
        self.spells_per_day_spells_per_day_lvl_8.setText(_translate("MainWindow", "10"))
        self.spells_per_day_base_spell_dc.setText(_translate("MainWindow", "Base Spell DC"))
        self.spells_per_day_dc_lvl_9.setText(_translate("MainWindow", "10"))
        self.spells_per_day_spells_per_day_lvl_9.setText(_translate("MainWindow", "10"))
        self.spells_per_day_extra_spells_lvl_9.setText(_translate("MainWindow", "10"))
        self._num_1.setText(_translate("MainWindow", "1"))
        self._num_2.setText(_translate("MainWindow", "2"))
        self._num_3.setText(_translate("MainWindow", "3"))
        self._num_4.setText(_translate("MainWindow", "4"))
        self._num_5.setText(_translate("MainWindow", "5"))
        self._num_6.setText(_translate("MainWindow", "6"))
        self._num_7.setText(_translate("MainWindow", "7"))
        self._num_8.setText(_translate("MainWindow", "8"))
        self._num_9.setText(_translate("MainWindow", "9"))