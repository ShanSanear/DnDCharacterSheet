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

    def __init__(self, elements_list, row_offset, increase_width, increase_height, add_new_column=4):
        self.elements_list = elements_list
        self.row_offset = row_offset
        self.increase_width = increase_width
        self.increase_height = increase_height
        self.root_initial_height = self.root.height()
        self.container_initial_height = self.container.height()
        if hasattr(self, "parent"):
            self.initial_tab_height = self.parent.tabs.height()
        self.add_new_column = add_new_column

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
            if self.initial_tab_height < lower_border:
                self.parent.tabs.setMinimumHeight(lower_border + self.increase_height * 2)
            else:
                self.parent.tabs.setMinimumHeight(self.initial_tab_height)

            # self.parent.setMinimumHeight(parent_height)
            # self.parent.tabs.setMinimumHeight(self.parent.tabs.height() + self.increase_height/2)

    def add_new_element(self):
        element_idx = len(self.elements_list)
        new_element = self.create_new_element()
        self.elements_list.append(new_element)
        values = self.elements_for_layout(new_element)

        self.adding_new_element_to_layout(element_idx, values)
        if hasattr(self, "set_values_from_attributes"):
            self.set_values_from_attributes()
        self.update_size()

    def adding_new_element_to_layout(self, element_idx, values):
        if hasattr(self, "add_new"):
            self.layout.removeWidget(self.add_new)
        add_multiple_elements_to_layout_by_row(self.layout, values,
                                               row=self.row_offset + element_idx)
        if hasattr(self, "add_new"):
            self.place_add_button()

    def elements_for_layout(self, new_element):
        return [new_element.__dict__[element] for element in new_element.__dict__ if
                not element.startswith("_")]

    def _remove_element(self, element):
        idx = self._get_element_index(element)
        print(idx)
        self._delete_from_layout(element)
        del self.elements_list[idx]
        self.update_layout()
        self.update_size()

    def update_layout(self):
        self.remove_widgets_from_layout()
        self.add_widgets_again()

    def _get_element_index(self, element):
        for idx, searched_for in enumerate(self.elements_list):
            if element == searched_for:
                return idx

    def _delete_from_layout(self, element):
        elements = self.elements_for_layout(element)
        for element in elements:
            element.setParent(None)

    def remove_widgets_from_layout(self):
        widgets = self.labels + [self.add_new]
        for widget in widgets:
            self.layout.removeWidget(widget)
        for idx, item in reversed(list(enumerate(self.elements_list))):
            subwidgets = self.elements_for_layout(item)
            for widget in subwidgets:
                self.layout.removeWidget(widget)

    def add_widgets_again(self):
        self.add_to_layout()
        self._add_all_elements_to_layout()

    def _add_all_elements_to_layout(self):
        for element_idx, element in enumerate(self.elements_list):
            values = self.elements_for_layout(element)
            self.adding_new_element_to_layout(element_idx, values)

    def place_add_button(self):
        self.layout.addWidget(self.add_new, len(self.elements_list) + 1, self.add_new_column, 1, 1)

    @abstractmethod
    def create_new_element(self):
        pass
