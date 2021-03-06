import logging
from abc import ABC, abstractmethod

from PyQt5 import QtCore
from PyQt5.QtWidgets import QGroupBox, QWidget, QGridLayout, QScrollArea, QVBoxLayout

from gui.frames.qt_generic_functions import add_multiple_elements_to_layout_by_row, collect_editable_data, \
    get_general_dict_repr, get_int_from_widget, create_push_button


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
    parent: QWidget

    def __init__(self, parent, position, size):
        self.size = size
        self.position = position
        self.smaller_size = [size[0] - 20, size[1] - 40]
        self.parent = parent
        self.root = QGroupBox(parent)
        self.root.setGeometry(QtCore.QRect(*position, *size))
        self.root.setBaseSize(*size)

        self.main_widget = QWidget(self.parent)
        self.scrollarea = QScrollArea(self.main_widget)
        self.scrollarea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.main_widget.setGeometry(QtCore.QRect(*position, *size))
        self.scrollarea.setFixedHeight(self.smaller_size[1])
        self.scrollarea.setFixedWidth(self.smaller_size[0])
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
        self.add_new_button = create_push_button("add_new", self.container, min_size=[20, 20], max_size=[20, 20],
                                                 text="+")
        self.sort_button = create_push_button("sort_it", self.container, min_size=[20, 20], max_size=[20, 20],
                                              text="S", function_on_clicked=self.sort_elements)
        self.last_row = []

    def add_new_element(self):
        element_idx = len(self.elements_list)
        new_element = self.create_new_element()
        self.elements_list.append(new_element)
        values = self.elements_for_layout(new_element)
        self.adding_new_element_to_layout(element_idx, values)
        if hasattr(self, "set_values_from_attributes"):
            self.set_values_from_attributes()

    def adding_new_element_to_layout(self, element_idx, values):
        add_multiple_elements_to_layout_by_row(self.layout, values, row=self.row_offset + element_idx)
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
        self.add_last_row()
        self.reraise_widgets()

    def add_widgets_again(self):
        self.add_to_layout()
        self._add_all_elements_to_layout()

    def _add_all_elements_to_layout(self):
        for element_idx, element in enumerate(self.elements_list):
            values = self.elements_for_layout(element)
            self.adding_new_element_to_layout(element_idx, values)

    def reraise_widgets(self):
        self.add_new_button.raise_()

    def add_last_row(self):
        add_multiple_elements_to_layout_by_row(self.layout, self.last_row, row=len(self.elements_list) + 1,
                                               start_column=self.last_row_column, width=1, height=1)

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


class ScrollableBox(ResizeableBox):
    def __init__(self, parent, position, base_size, original_size, max_height, height_increment, row_offset,
                 last_row_column):
        ResizeableBox.__init__(self, parent=parent, position=position, size=base_size, row_offset=row_offset,
                               last_row_column=last_row_column)

        self.max_height = max_height
        self.height_increment = height_increment
        self.height_increments = 0
        self.exceed_height = False
        self.original_size = original_size
        self.original_smaller_size = [original_size[0] - 20, original_size[1] - 40]

    def increase_height(self):
        self.height_increments += 1
        base_root_height = self.size[1] + self.height_increment * self.height_increments
        if base_root_height > self.max_height:
            self.exceed_height = True
        else:
            self.exceed_height = False
        self._change_size_of_widgets()

    def decrease_height(self):
        self.height_increments -= 1
        base_root_height = self.size[1] + self.height_increment * self.height_increments
        if base_root_height > self.max_height:
            self.exceed_height = True
        else:
            self.exceed_height = False
        self._change_size_of_widgets()

    def _change_size_of_widgets(self):
        if not self.exceed_height:
            self.root.setGeometry(QtCore.QRect(*self.position, self.size[0],
                                               self.size[1] + (self.height_increments * self.height_increment)))

            self.main_widget.setGeometry(QtCore.QRect(*self.position, self.size[0],
                                                      self.size[1] + (self.height_increments * self.height_increment)))
            self.scrollarea.setFixedHeight(self.smaller_size[1] + (self.height_increments * self.height_increment))
            self.scrollarea.move(10, 10)
        else:
            self.root.setGeometry(QtCore.QRect(*self.position, *self.original_size))

            self.main_widget.setGeometry(QtCore.QRect(*self.position, *self.original_size))
            self.scrollarea.setFixedWidth(self.original_smaller_size[0])
            self.scrollarea.setFixedHeight(self.original_smaller_size[1])
            self.scrollarea.move(10, 20)

    def _remove_element(self, element):
        super(ScrollableBox, self)._remove_element(element)
        self.decrease_height()

    def delete_dynamic_widgets(self):
        for idx, item in reversed(list(enumerate(self.elements_list))):
            subwidgets = self.elements_for_layout(item)
            for widget in subwidgets:
                self.layout.removeWidget(widget)
                widget.deleteLater()

    def set_default_state(self):
        self.delete_dynamic_widgets()
        self.elements_list = []
        self.height_increments = 0
        self.add_new_element()
