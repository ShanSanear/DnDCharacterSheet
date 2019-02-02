from functools import partial
from types import SimpleNamespace

from PyQt5 import QtWidgets, QtCore

from gui.frames.qt_generic_classes import DefaultBox, ResizeableBox
from gui.frames.qt_generic_functions import create_qline_edit, create_push_button, create_qlabel, \
    add_multiple_elements_to_layout_by_row, set_text_of_children
from gui.popups.qt_full_description import DescriptionDialog


class FeatsBox(DefaultBox, ResizeableBox):
    def __init__(self, parent, position, size):
        # TODO remove button
        # TODO - scrollbar after achieving certain height
        self.parent = parent

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
        self.labels = [self.name_label, self.description_field_label, self.description_label]
        self.add_new = create_push_button("add_new_feat", self.container, min_size=[20, 20], max_size=[20, 20], text="+")
        self.feats = []
        self.translate_reference = {
            "EN":
                {
                    "root": {
                        "title": "Feats"
                    },
                    "description_label": "Desc",
                    "description_field_label": "Desc",
                    "name_label": "Feat name",
                }
        }
        self.translate_reference_new_element = {
            "EN": {
                "description_button": "..."
            }
        }

        ResizeableBox.__init__(self, elements_list=self.feats, row_offset=1, increase_width=0, increase_height=28,
                               add_new_column=3)
        self.add_to_layout()
        self.add_feat = self.add_new_element
        self.add_new.clicked.connect(self.add_feat)

        for _ in range(1):
            self.add_feat()

        self.translate("EN")
        self.root.setLayout(self.layout)



    def translate(self, language):
        set_text_of_children(self, self.translate_reference[language])

    def create_new_element(self):
        return self.create_feat()

    def add_to_layout(self):
        add_multiple_elements_to_layout_by_row(self.layout, [self.name_label, self.description_label,
                                                             self.description_field_label])
        self.place_add_button()

    def show_description(self, feat):
        dialog = DescriptionDialog("Feat description", self.root, feat)
        dialog.show()


    def create_feat(self):
        new_feat = SimpleNamespace()
        idx = len(self.feats)
        new_feat.name = create_qline_edit(f"feat{idx}_name", self.container, max_size=(150, None))

        new_feat.description_edit = create_qline_edit(f"feat_{idx}_description_edit", self.container)
        new_feat.description_button = create_push_button(f"feat_{idx}_description_button",
                                                         self.container, min_size=[20, 20], max_size=[20, 20], )
        new_feat.description_button.clicked.connect(partial(self.show_description, new_feat))
        new_feat._full_description = "ABCD"
        new_feat.delete_feat = create_push_button("item_delete", self.container,min_size=[20, 20], max_size=[20, 20], text="-",
                                                  function_on_clicked=self._remove_element, args_on_clicked=new_feat)
        set_text_of_children(new_feat, self.translate_reference_new_element["EN"])


        return new_feat
