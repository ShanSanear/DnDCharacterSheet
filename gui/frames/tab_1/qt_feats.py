from functools import partial
from types import SimpleNamespace

from PyQt5.QtWidgets import QApplication

from gui.frames.qt_generic_classes import ScrollableBox
from gui.frames.qt_generic_functions import create_qline_edit, create_push_button, create_qlabel, \
    add_multiple_elements_to_layout_by_row
from gui.popups.qt_full_description import DescriptionDialog


class FeatsBox(ScrollableBox):
    def __init__(self, parent, position, size):
        base_size = [size[0], 100]
        height_increment = 26
        max_height = size[1]
        ScrollableBox.__init__(self, parent=parent, position=position, base_size=base_size, max_height=max_height,
                               original_size=size,
                               height_increment=height_increment, row_offset=1, last_row_column=1)
        self.name_label = create_qlabel(self.container)
        self.description_field_label = create_qlabel(self.container)
        self.description_label = create_qlabel(self.container)
        self.labels = [self.name_label, self.description_field_label, self.description_label]
        self.add_to_layout()
        self.add_feat = self.add_new_element
        self.add_new.clicked.connect(self.add_feat)

        self.add_feat()

    def update_size(self):
        pass

    def create_new_element(self):
        self.increase_height()
        return self.create_feat()

    def add_to_layout(self):
        add_multiple_elements_to_layout_by_row(self.layout, [self.name_label, self.description_label])
        self.add_last_row()

    def show_description(self, feat):
        dialog = DescriptionDialog(QApplication.translate("Feats", "Feat description"), self.root, feat)
        dialog.show()

    def create_feat(self):
        new_feat = SimpleNamespace()
        idx = len(self.elements_list)
        new_feat.name = create_qline_edit(self.container, max_size=(150, None),
                                          function_on_unfocused=self.sort_elements)

        new_feat.description_button = create_push_button(f"feat_{idx}_description_button",
                                                         self.container, min_size=[20, 20], max_size=[20, 20],
                                                         text="...")
        new_feat.description_button.clicked.connect(partial(self.show_description, new_feat))
        new_feat._full_description = ""
        new_feat.delete_feat = create_push_button("item_delete", self.container, min_size=[20, 20], max_size=[20, 20],
                                                  text="-",
                                                  function_on_clicked=self._remove_element, args_on_clicked=new_feat)

        return new_feat

    def retranslate(self):
        self.root.setTitle(QApplication.translate("Feats", "Feats / Special abilities"))
        self.description_label.setText(QApplication.translate("Feats", "Desc"))
        self.name_label.setText(QApplication.translate("Feats", "Feat name"))
