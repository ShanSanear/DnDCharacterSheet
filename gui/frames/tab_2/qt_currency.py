from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication

from gui.frames.qt_generic_classes import BoxType, DefaultBox
from gui.frames.qt_generic_functions import create_qlabel, add_multiple_elements_to_layout_by_column, create_qline_edit


class CurrencyBox(BoxType, DefaultBox):
    def __init__(self, parent, position, size):
        BoxType.__init__(self, parent=parent, position=position, size=size)
        qlabel_dict = dict(parent=self.container, align=QtCore.Qt.AlignRight)
        qline_dict = dict(parent=self.container, max_size=[40, None])
        self.copper_label = create_qlabel(**qlabel_dict)
        self.silver_label = create_qlabel(**qlabel_dict)
        self.gold_label = create_qlabel(**qlabel_dict)
        self.platinum_label = create_qlabel(**qlabel_dict)
        self.copper_value = create_qline_edit(**qline_dict)
        self.silver_value = create_qline_edit(**qline_dict)
        self.gold_value = create_qline_edit(**qline_dict)
        self.platinum_value = create_qline_edit(**qline_dict)

        self.add_to_layout()

    def add_to_layout(self, **kwargs):
        labels = [self.copper_label, self.silver_label, self.gold_label, self.platinum_label]
        add_multiple_elements_to_layout_by_column(layout=self.layout, elements_to_add=labels, column=0)
        values = [self.copper_value, self.silver_value, self.gold_value, self.platinum_value]
        add_multiple_elements_to_layout_by_column(layout=self.layout, elements_to_add=values, column=1)

    def retranslate(self):
        self.root.setTitle(QApplication.translate("MoneyBox", "Currency"))
        self.copper_label.setText(QApplication.translate("MoneyBox", "Copper (cp)"))
        self.silver_label.setText(QApplication.translate("MoneyBox", "Silver (sp)"))
        self.gold_label.setText(QApplication.translate("MoneyBox", "Gold (gp)"))
        self.platinum_label.setText(QApplication.translate("MoneyBox", "Platinum (pp)"))
