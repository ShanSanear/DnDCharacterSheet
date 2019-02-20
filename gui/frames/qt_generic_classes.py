import logging
from abc import ABC, abstractmethod

from PyQt5 import QtCore
from PyQt5.QtWidgets import QGroupBox, QWidget, QGridLayout

from gui.frames.qt_generic_functions import add_multiple_elements_to_layout_by_row, collect_editable_data, \
    get_general_dict_repr, get_int_from_widget


class BoxType:
    def __init__(self, parent, position, size, spacing=10, margins=(20, 10, 10, 20), defaults=False):
        self.parent = parent
        self.root = QGroupBox(parent)
        self.root.setGeometry(QtCore.QRect(*position, *size))
        self.container = QWidget(self.root)
        self.layout = QGridLayout(self.container)
        if not defaults:
            self.layout.setSpacing(spacing)
            self.layout.setContentsMargins(*margins)
        self.root.setLayout(self.layout)


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

    def __init__(self, elements_list, row_offset, increase_width, increase_height, last_row_column=4):
        self.elements_list = elements_list
        self.row_offset = row_offset
        self.increase_width = increase_width
        self.increase_height = increase_height
        self.root_initial_height = self.root.height()
        self.container_initial_height = self.container.height()
        if hasattr(self, "parent"):
            self.initial_tab_height = self.parent.tabs.height()
        self.last_row_column = last_row_column
        self.end_scroll = False
        self.scrollarea.verticalScrollBar().rangeChanged.connect(self._max_scroll)
        self.scrollarea.verticalScrollBar().valueChanged.connect(lambda value: self.scrolled(value))

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
            logging.debug("Lower border: %s", lower_border)
            logging.debug("Item: %s", self)
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
            self.add_last_row()

    def elements_for_layout(self, new_element):
        return [new_element.__dict__[element] for element in new_element.__dict__ if
                not element.startswith("_")]

    def _remove_element(self, element):
        idx = self._get_element_index(element)
        logging.debug("Index of element to remove: %d", idx)
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
        widgets = self.labels + self.last_row
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

    def add_last_row(self):
        self.layout.addWidget(self.add_new, len(self.elements_list) + 1, self.last_row_column, 1, 1)
        # add_multiple_elements_to_layout_by_row(self.layout, self.last_row, row=len(self.elements_list) + 1,
        #                                        start_column=self.add_new_column)

    def sort_elements(self):
        self.elements_list = sorted(self.elements_list, key=self._sort_element)
        self.update_layout()

    def _sort_element(self, element):
        if hasattr(element, 'lvl'):
            lvl = get_int_from_widget(element.lvl, 0)
            return element.name.text() == "", lvl, element.name.text()
        else:
            return element.name.text() == "", element.name.text()

    def _max_scroll(self, min_scroll, max_scroll):
        logging.debug("Max scroll in _max_scroll: %s", max_scroll)
        logging.debug("Min scroll in _max_scroll: %s", min_scroll)
        if self.end_scroll:
            self.scrollarea.verticalScrollBar().setSliderPosition(max_scroll)

    def scrolled(self, value):
        logging.debug("Scrolled to: %s", value)
        maximum_scroll = self.scrollarea.verticalScrollBar().maximum()
        if value == maximum_scroll:
            self.end_scroll = True
        else:
            self.end_scroll = False
        logging.debug("Is at the end scroll: %s", self.end_scroll)

    @abstractmethod
    def create_new_element(self):
        pass
