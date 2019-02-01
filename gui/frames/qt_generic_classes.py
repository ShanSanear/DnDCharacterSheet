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

    def __init__(self, elements_list, row_offset, increase_width, increase_height):
        self.elements_list = elements_list
        self.row_offset = row_offset
        self.increase_width = increase_width
        self.increase_height = increase_height
        self.root_initial_height = self.root.height()
        self.container_initial_height = self.container.height()


    def update_size(self):
        new_root_height = self.root_initial_height + self.increase_height * len(self.elements_list)
        new_container_height = self.container_initial_height + self.increase_height * len(self.elements_list)
        self.root.setMinimumHeight(new_root_height)
        self.container.setMinimumHeight(new_container_height)
        self.root.setMaximumHeight(new_root_height)
        self.container.setMaximumHeight(new_container_height)
        if hasattr(self, "parent"):
            vertical_position = self.root.pos().y()
            lower_border = vertical_position + new_root_height
            print("Lower border: ", lower_border)
            print("Item:", self)
            self.parent.tabs.setMinimumHeight(lower_border + self.increase_height*2)

            #self.parent.setMinimumHeight(parent_height)
            #self.parent.tabs.setMinimumHeight(self.parent.tabs.height() + self.increase_height/2)


    def add_new_element(self):
        element_idx = len(self.elements_list)
        new_element = self.create_new_element()

        if hasattr(self, "add_new"):
            self.layout.removeWidget(self.add_new)
        self.elements_list.append(new_element)
        values = self.elements_for_layout(self.elements_list)
        add_multiple_elements_to_layout_by_row(self.layout, values,
                                               row=self.row_offset+element_idx)
        if hasattr(self, "add_new"):
            self.layout.addWidget(self.add_new, len(self.elements_list)+1, 0, 1, 1)
        self.update_size()
        if hasattr(self, "set_values_from_attributes"):
            self.set_values_from_attributes()

    def elements_for_layout(self, elements_list, idx=-1):
        return [elements_list[idx].__dict__[element] for element in elements_list[-1].__dict__ if
                not element.startswith("_")]

    @abstractmethod
    def create_new_element(self):
        pass

    @abstractmethod
    def adding_missing_element(self):
        pass
