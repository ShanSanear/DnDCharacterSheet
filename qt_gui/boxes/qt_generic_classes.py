from abc import ABC, abstractmethod

from PyQt5 import QtCore

from qt_gui.boxes.qt_generic_functions import add_multiple_elements_to_layout_by_row


class DefaultBox(ABC):
    @abstractmethod
    def add_to_layout(self, **kwargs):
        pass

    @abstractmethod
    def translate(self, **kwargs):
        pass


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
        add_multiple_elements_to_layout_by_row(layout, elements_list[-1].__dict__.values(),
                                               row=row_offset+element_idx)
        self.update_size()

    @abstractmethod
    def create_new_element(self):
        pass
