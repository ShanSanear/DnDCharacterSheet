from functools import partial
from types import SimpleNamespace

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QScrollArea, QVBoxLayout

from gui.frames.qt_generic_classes import DefaultBox, ResizeableBox
from gui.frames.qt_generic_functions import create_qline_edit, create_push_button, create_qlabel, \
    add_multiple_elements_to_layout_by_row, set_text_of_children
from gui.popups.qt_full_description import DescriptionDialog


class FeatsBox(DefaultBox, ResizeableBox):
    def __init__(self, parent, position, size):
        # TODO - scrollbar after achieving certain height
        self.parent = parent

        self.root = QtWidgets.QGroupBox(parent)
        self.root.setGeometry(QtCore.QRect(*position, *size))
        self.root.setObjectName("FeatsBox")
        smaller_size = [size[0] * 0.90, size[1] * 0.90]
        self.main_widget = QtWidgets.QWidget(self.parent)
        self.scrollarea = QScrollArea(self.main_widget)
        # self.scrollarea.setStyleSheet("QScrollArea {background-color: #D8D8D8}")
        # self.scrollarea.setStyleSheet("QScrollArea {background-color:white;}")
        # self.main_widget.setStyleSheet("background-color:transparent;")

        self.scrollarea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.main_widget.setGeometry(QtCore.QRect(*position, *size))
        self.scrollarea.setFixedHeight(smaller_size[1])
        self.scrollarea.setFixedWidth(smaller_size[0])
        self.scrollarea.setWidgetResizable(True)
        self.scrollarea.move(10, 10)
        self.container = QtWidgets.QWidget(self.main_widget)
        self.container.setObjectName("FeatsQwidget")
        self.layout = QtWidgets.QGridLayout(self.container)
        self.layout.setObjectName("FeatsLayout")
        self.name_label = create_qlabel("feat_name_label", self.container)
        self.description_field_label = create_qlabel("feat_name_label", self.container)
        self.description_label = create_qlabel("feat_description_label", self.container)
        self.labels = [self.name_label, self.description_field_label, self.description_label]
        self.add_new = create_push_button("add_new_feat", self.container, min_size=[20, 20], max_size=[20, 20],
                                          text="+")
        self.last_row = [self.add_new]
        self.feats = []
        self.translate_reference = {
            "EN":
                {
                    "root": {
                        "title": "Feats / Special abilities"
                    },
                    "description_label": "Desc",
                    "name_label": "Feat name",
                }
        }
        self.translate_reference_new_element = {
            "EN": {
                "description_button": "..."
            }
        }

        ResizeableBox.__init__(self, elements_list=self.feats, row_offset=1, increase_width=0, increase_height=28,
                               last_row_column=2)
        self.add_to_layout()
        self.add_feat = self.add_new_element
        self.add_new.clicked.connect(self.add_feat)

        for _ in range(25):
            self.add_feat()

        self.translate("EN")
        self.scrollarea.setWidget(self.container)
        self.layout_All = QVBoxLayout(self.main_widget)
        self.layout_All.addWidget(self.scrollarea)

    def translate(self, language):
        set_text_of_children(self, self.translate_reference[language])

    def update_size(self):
        pass

    def create_new_element(self):
        return self.create_feat()

    def add_to_layout(self):
        add_multiple_elements_to_layout_by_row(self.layout, [self.name_label, self.description_label])
        self.add_last_row()

    def show_description(self, feat):
        dialog = DescriptionDialog("Feat description", self.root, feat)
        dialog.show()

    def create_feat(self):
        new_feat = SimpleNamespace()
        idx = len(self.feats)
        new_feat.name = create_qline_edit(f"feat{idx}_name", self.container, max_size=(150, None),
                                          function_on_unfocused=self.sort_elements)

        #new_feat.description_edit = create_qline_edit(f"feat_{idx}_description_edit", self.container)
        new_feat.description_button = create_push_button(f"feat_{idx}_description_button",
                                                         self.container, min_size=[20, 20], max_size=[20, 20], )
        new_feat.description_button.clicked.connect(partial(self.show_description, new_feat))
        new_feat._full_description = "ABCD"
        new_feat.delete_feat = create_push_button("item_delete", self.container, min_size=[20, 20], max_size=[20, 20],
                                                  text="-",
                                                  function_on_clicked=self._remove_element, args_on_clicked=new_feat)
        set_text_of_children(new_feat, self.translate_reference_new_element["EN"])

        return new_feat
