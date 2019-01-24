from abc import ABC, abstractmethod

from PyQt5 import QtCore

from qt_gui.boxes.qt_generic_functions import add_multiple_elements_to_layout_by_row, collect_editable_data


class DefaultBox(ABC):
    @abstractmethod
    def add_to_layout(self, **kwargs):
        pass

    @abstractmethod
    def translate(self, **kwargs):
        pass

    def get_dict_repr(self):
        d = {}
        elements = self.__dict__.keys()
        elements = collect_editable_data(elements)
        print(elements)
        for element in elements:
            d[element] = getattr(self, element).text()
        print(d)
        return d


# noinspection PyUnresolvedReferences
class ResizeableBox(ABC):


    def __init__(self, increase_width, increase_height):
        self.increase_width = increase_width
        self.increase_height = increase_height


    def update_size(self):
        root_width = self.root.width()
        root_height = self.root.height()
        container_width = self.container.width()
        container_height = self.container.height()
        self.root.setMinimumSize(QtCore.QSize(root_width + self.increase_width, root_height + self.increase_height))
        self.container.setMinimumSize(QtCore.QSize(container_width + self.increase_width,
                                                   container_height + self.increase_height))

    def add_new_element(self, elements_list, layout, row_offset):
        element_idx = len(elements_list)
        new_element = self.create_new_element()
        elements_list.append(new_element)
        values = [elements_list[-1].__dict__[element] for element in elements_list[-1].__dict__ if not element.startswith("_")]
        add_multiple_elements_to_layout_by_row(layout, values,
                                               row=row_offset+element_idx)
        self.update_size()

    @abstractmethod
    def create_new_element(self):
        pass
