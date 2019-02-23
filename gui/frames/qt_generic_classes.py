import logging
from abc import ABC, abstractmethod

from PyQt5 import QtCore
from PyQt5.QtWidgets import QGroupBox, QWidget, QGridLayout, QScrollArea, QVBoxLayout

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


class ResizeType:
    def __init__(self, parent, position, size):
        self.parent = parent
        self.root = QGroupBox(parent)
        self.root.setGeometry(QtCore.QRect(*position, *size))
        smaller_size = [size[0] - 20, size[1] - 40]
        self.main_widget = QWidget(self.parent)
        self.scrollarea = QScrollArea(self.main_widget)
        self.scrollarea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.main_widget.setGeometry(QtCore.QRect(*position, *size))
        self.scrollarea.setFixedHeight(smaller_size[1])
        self.scrollarea.setFixedWidth(smaller_size[0])
        self.scrollarea.setWidgetResizable(True)
        self.scrollarea.move(10, 10)

        self.container = QWidget(self.main_widget)
        self.layout = QGridLayout(self.container)
        self.scrollarea.setWidget(self.container)
        self.layout_All = QVBoxLayout(self.main_widget)
        self.layout_All.addWidget(self.scrollarea)


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


class ResizeableBox(DefaultBox, ResizeType):

    def __init__(self, parent, position, size, row_offset, last_row_column=4):
        ResizeType.__init__(self, parent=parent, position=position, size=size)
        self.elements_list = []
        self.row_offset = row_offset
        self.last_row_column = last_row_column
        self.end_scroll = False
        self.scrollarea.verticalScrollBar().rangeChanged.connect(self._max_scroll)
        self.scrollarea.verticalScrollBar().valueChanged.connect(lambda value: self.scrolled(value))

    def add_new_element(self):
        element_idx = len(self.elements_list)
        new_element = self.create_new_element()
        self.elements_list.append(new_element)
        values = self.elements_for_layout(new_element)

        self.adding_new_element_to_layout(element_idx, values)
        if hasattr(self, "set_values_from_attributes"):
            self.set_values_from_attributes()

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

    def update_layout(self):
        self.remove_widgets_from_layout()
        self.add_widgets_again()

    def add_widgets_again(self):
        self.add_to_layout()
        self._add_all_elements_to_layout()

    def _add_all_elements_to_layout(self):
        for element_idx, element in enumerate(self.elements_list):
            values = self.elements_for_layout(element)
            self.adding_new_element_to_layout(element_idx, values)

    def add_last_row(self):
        self.layout.addWidget(self.add_new, len(self.elements_list) + 1, self.last_row_column, 1, 1)

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

    # @abstractmethod
    # def add_to_layout(self):
    #     pass

    @abstractmethod
    def create_new_element(self):
        pass
