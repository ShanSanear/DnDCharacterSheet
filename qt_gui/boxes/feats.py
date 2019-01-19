from types import SimpleNamespace

from PyQt5 import QtWidgets, QtCore

from qt_gui.boxes.qt_generic_classes import DefaultBox, ResizeableBox
from qt_gui.boxes.qt_generic_functions import create_qline_edit, create_push_button, create_qlabel, \
    add_multiple_elements_to_layout_by_row, set_text_of_children


class FeatsBox(DefaultBox, ResizeableBox):
    def __init__(self, parent, position, size):
        ResizeableBox.__init__(self, increase_width=0, increase_height=25)
        self.root = QtWidgets.QGroupBox(parent)
        self.root.setGeometry(QtCore.QRect(*position, *size))
        self.root.setObjectName("FeatsBox")
        self.container = QtWidgets.QWidget(self.root)
        self.container.setObjectName("FeatsQwidget")
        self.layout = QtWidgets.QGridLayout(self.container)
        self.layout.setObjectName("FeatsLayout")
        self.name_label = create_qlabel("feat_name_label", self.container)
        self.description_field_label = create_qlabel("feat_name_label", self.container)
        self.description_label = create_qlabel("feat_description_label", self.container)
        self.feats = []
        self.translate_reference = {
            "EN":
                {
                    "description_label": "Desc",
                    "description_field_label": "Desc",
                    "name_label": "Feat name",
                }
        }
        self.translate_reference_new_element = {
            "EN": {
                "description_buttn" : "..."
            }
        }

        for _ in range(5):
            self.add_feat()

        self.add_to_layout()
        self.translate("EN")
        self.root.setLayout(self.layout)

    def add_feat(self):
        self.add_new_element(elements_list=self.feats, layout=self.layout, row_offset=1)

    def translate(self, language):
        set_text_of_children(self, self.translate_reference[language])

    def create_new_element(self):
        return self.create_feat()

    def add_to_layout(self):
        add_multiple_elements_to_layout_by_row(self.layout, [self.name_label, self.description_label,
                                                             self.description_field_label])

    def create_feat(self):
        new_feat = SimpleNamespace()
        idx = len(self.feats)
        new_feat.name = create_qline_edit(f"feat{idx}_name", self.container, max_size=(150, None))

        new_feat.description_edit = create_qline_edit(f"feat_{idx}_description_edit", self.container)
        new_feat.description_button = create_push_button(f"feat_{idx}_description_button",
                                                         self.container, max_size=[20, None],)
        set_text_of_children(new_feat, self.translate_reference_new_element["EN"])
        return new_feat
