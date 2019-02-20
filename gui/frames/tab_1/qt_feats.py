from functools import partial
from types import SimpleNamespace

from gui.frames.qt_generic_classes import DefaultBox, ResizeableBox
from gui.frames.qt_generic_functions import create_qline_edit, create_push_button, create_qlabel, \
    add_multiple_elements_to_layout_by_row, set_text_of_children
from gui.popups.qt_full_description import DescriptionDialog


class FeatsBox(DefaultBox, ResizeableBox):
    def __init__(self, parent, position, size):
        # TODO - scrollbar after achieving certain height
        self.feats = []
        ResizeableBox.__init__(self, parent=parent, position=position, size=size,
                               elements_list=self.feats, row_offset=1, increase_width=0, increase_height=28,
                               last_row_column=2)
        self.name_label = create_qlabel(self.container)
        self.description_field_label = create_qlabel(self.container)
        self.description_label = create_qlabel(self.container)
        self.labels = [self.name_label, self.description_field_label, self.description_label]
        self.add_new = create_push_button("add_new_feat", self.container, min_size=[20, 20], max_size=[20, 20],
                                          text="+")
        self.last_row = [self.add_new]
        self.translate_reference = {"EN":
            {"root":
                {
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

        self.add_to_layout()
        self.add_feat = self.add_new_element
        self.add_new.clicked.connect(self.add_feat)

        for _ in range(17):
            self.add_feat()
        self.translate("EN")

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
        new_feat.name = create_qline_edit(self.container, max_size=(150, None),
                                          function_on_unfocused=self.sort_elements)

        # new_feat.description_edit = create_qline_edit(self.container)
        new_feat.description_button = create_push_button(f"feat_{idx}_description_button",
                                                         self.container, min_size=[20, 20], max_size=[20, 20], )
        new_feat.description_button.clicked.connect(partial(self.show_description, new_feat))
        new_feat._full_description = "ABCD"
        new_feat.delete_feat = create_push_button("item_delete", self.container, min_size=[20, 20], max_size=[20, 20],
                                                  text="-",
                                                  function_on_clicked=self._remove_element, args_on_clicked=new_feat)
        set_text_of_children(new_feat, self.translate_reference_new_element["EN"])

        return new_feat
