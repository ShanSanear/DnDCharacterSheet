from abc import ABC, abstractmethod

from PyQt5 import QtCore

from gui.frames.qt_generic_functions import add_multiple_elements_to_layout_by_row, collect_editable_data, \
    get_general_dict_repr


class DefaultBox(ABC):
    @abstractmethod
    def add_to_layout(self, **kwargs):
        pass

    @abstractmethod
    def translate(self, **kwargs):
        pass

    def get_dict_repr(self):
        elements = self.__dict__.keys()
        elements = collect_editable_data(elements)
        return get_general_dict_repr(self, elements)


class ResizeableBox(ABC):

    def __init__(self, increase_width, increase_height):
        self.increase_width = increase_width
        self.increase_height = increase_height


    def update_size(self):
        new_root_width = self.root.width() + self.increase_width
        new_root_height = self.root.height() + self.increase_height
        new_container_width = self.container.width() + self.increase_width
        new_container_height = self.container.height() + self.increase_height
        self.root.setMinimumSize(QtCore.QSize(new_root_width, new_root_height))
        self.container.setMinimumSize(QtCore.QSize(new_container_width, new_container_height))
        if hasattr(self, "parent"):
            vertical_position = self.root.pos().y()
            lower_border = vertical_position + new_root_height
            print("Lower border: ", lower_border)
            print("Item:", self)
            if lower_border+self.increase_height > self.parent.tabs.height():
                self.parent.tabs.setMinimumHeight(lower_border + self.increase_height*2)

            #self.parent.setMinimumHeight(parent_height)
            #self.parent.tabs.setMinimumHeight(self.parent.tabs.height() + self.increase_height/2)


    def add_new_element(self, elements_list, layout, row_offset):
        element_idx = len(elements_list)
        new_element = self.create_new_element()

        if hasattr(self, "add_new"):
            self.layout.removeWidget(self.add_new)
        elements_list.append(new_element)
        values = [elements_list[-1].__dict__[element] for element in elements_list[-1].__dict__ if not element.startswith("_")]
        add_multiple_elements_to_layout_by_row(layout, values,
                                               row=row_offset+element_idx)
        if hasattr(self, "add_new"):
            self.layout.addWidget(self.add_new, len(elements_list)+1, 0, 1, 1)
        self.update_size()

    @abstractmethod
    def create_new_element(self):
        pass

    @abstractmethod
    def adding_missing_element(self):
        pass
