from functools import partial

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QComboBox, QPlainTextEdit, QLineEdit, QCheckBox


def resize_element(element: QtWidgets.QWidget, min_size: (list, tuple), max_size: (list, tuple)):
    if min_size:
        if min_size[0]:
            element.setMinimumWidth(min_size[0])
        if min_size[1]:
            element.setMinimumHeight(min_size[1])
    if max_size:
        if max_size[0]:
            element.setMaximumWidth(max_size[0])
        if max_size[1]:
            element.setMaximumHeight(max_size[1])
    return element


def create_checkbox(parent: QtWidgets.QWidget, name: str, function_on_toggle=None, args_on_toggle=None):
    checkbox = QtWidgets.QCheckBox(parent)
    checkbox.setObjectName(name)
    if function_on_toggle:
        if not args_on_toggle:
            checkbox.toggled.connect(function_on_toggle)
        else:
            checkbox.toggled.connect(partial(function_on_toggle, args_on_toggle))
    return checkbox


def create_qlabel(name: str, parent: QtWidgets.QWidget, min_size: (list, tuple) = None, max_size: (list, tuple) = None,
                  align=None):
    label = QtWidgets.QLabel(parent)
    label: QtWidgets.QLabel = resize_element(label, min_size, max_size)
    if align:
        label.setAlignment(align)
    label.setObjectName(name)
    return label


def create_qline_edit(name: str, parent: QtWidgets.QWidget, min_size: (list, tuple) = None,
                      max_size: (list, tuple) = None,
                      align=None, indent: int = None, text: str = None, enabled: bool = True,
                      function_on_text_changed=None, args_on_text_changed=None, function_on_unfocused=None,
                      args_on_unfocused=None):
    qline = MyQlineEdit(parent, function_on_unfocused=function_on_unfocused, args_on_unfocused=args_on_unfocused)
    qline.setEnabled(enabled)

    qline: QtWidgets.QLineEdit = resize_element(qline, min_size, max_size)
    if align:
        qline.setAlignment(align)
    if indent:
        qline.setIndent(indent)
    if text:
        qline.setText(text)
    if function_on_text_changed:
        if not args_on_text_changed:
            qline.textChanged.connect(function_on_text_changed)
        else:
            qline.textChanged.connect(partial(function_on_text_changed, *args_on_text_changed))
    qline.setObjectName(name)

    return qline


def create_push_button(name: str, parent: QtWidgets.QWidget, min_size: (list, tuple) = None,
                       max_size: (list, tuple) = None, text: str = None, function_on_clicked=None,
                       args_on_clicked=None):
    button = QtWidgets.QPushButton(parent)
    button.setObjectName(name)
    button: QtWidgets.QPushButton = resize_element(button, min_size, max_size)
    button.setText(text)
    if function_on_clicked:
        if not args_on_clicked:
            button.clicked.connect(function_on_clicked)
        else:
            button.clicked.connect(partial(function_on_clicked, args_on_clicked))
    return button


def create_combo_box(name: str, parent: QtWidgets.QWidget, number_of_choices: int = 1,
                     choices_text: (list, tuple) = None,
                     min_size: (list, tuple) = None, max_size: (list, tuple) = None, function_on_index_changed=None,
                     args_on_index_changed=None):
    combo_box: QComboBox = QtWidgets.QComboBox(parent)
    combo_box.setObjectName(name)
    for _ in range(number_of_choices):
        combo_box.addItem("")
    if choices_text:
        for idx, choice_text in enumerate(choices_text):
            combo_box.setItemText(idx, choice_text)
    if min_size or max_size:
        combo_box = resize_element(combo_box, min_size=min_size, max_size=max_size)
    if function_on_index_changed:
        if not args_on_index_changed:
            combo_box.currentIndexChanged.connect(function_on_index_changed)
        else:
            combo_box.currentIndexChanged.connect(partial(function_on_index_changed, *args_on_index_changed))
    return combo_box


def numeric_label(name, parent, align):
    return create_qlabel(name, parent, align=align)


def add_multiple_elements_to_layout_by_row(layout: QtWidgets.QLayout, elements_to_add: (list, tuple), row: int = 0,
                                           start_column: int = 0, height: int = 1, width: int = 1):
    for column, element in enumerate(elements_to_add):
        add_element_to_layout(layout, element, row, start_column + column * width, height, width)


def add_multiple_elements_to_layout_by_column(layout: QtWidgets.QLayout, elements_to_add: (list, tuple),
                                              column: int = 0, start_row: int = 0, height: int = 1, width: int = 1):
    for row, element in enumerate(elements_to_add):
        add_element_to_layout(layout, element, start_row + row * height, column, height, width)


def add_element_to_layout(layout: QtWidgets.QLayout, element_to_add: QtWidgets.QWidget, row: int, column: int,
                          height: int, width: int):
    layout.addWidget(element_to_add, row, column, height, width)


def set_combo_box_choices(root_object, choices):
    for idx, choice_text in enumerate(choices):
        root_object.setItemText(idx, choice_text)


def set_text_of_children(root_object, to_set: dict):
    for name, data_to_set in to_set.items():
        if name == "title":
            root_object.setTitle(data_to_set)
            continue
        if name == "choices":
            set_combo_box_choices(root_object, data_to_set)
        obj_ref = getattr(root_object, name)
        if isinstance(data_to_set, dict):
            set_text_of_children(obj_ref, data_to_set)
        elif isinstance(data_to_set, list):
            for idx, element_data in enumerate(data_to_set):
                # obj_ref in such case is self.items, self.spells etc.
                try:
                    set_text_of_children(obj_ref[idx], element_data)
                except IndexError:
                    # TODO - Maybe call adding missing elements multiple times, THEN adding objects?
                    root_object.add_new_element()
                    set_text_of_children(obj_ref[idx], element_data)
        elif isinstance(obj_ref, QComboBox):
            obj_ref.setCurrentIndex(data_to_set)

        elif isinstance(obj_ref, QCheckBox):
            obj_ref.setChecked(data_to_set)
        else:
            if not isinstance(data_to_set, str):
                raise AttributeError("Only strings can be passed to setText")
            if isinstance(obj_ref, QPlainTextEdit):
                obj_ref.setPlainText(data_to_set)
            elif isinstance(obj_ref, str):
                setattr(root_object, name, data_to_set)
            else:
                obj_ref.setText(data_to_set)


def collect_editable_data(elements_to_clean_up):
    tmp = {element for element in elements_to_clean_up if "label" not in element}
    commons = ["root", "container", "layout", "translate_reference"]
    for common in commons:
        try:
            tmp.remove(common)
        except KeyError:
            pass
    return tmp


def get_general_dict_repr(root_object, to_get):
    data = {}

    print(to_get)
    for element in to_get:
        obj_ref = getattr(root_object, element)
        if isinstance(obj_ref, QLineEdit):
            if not obj_ref.isEnabled():
                print(obj_ref, "is read only, skipping")
            else:
                data[element] = obj_ref.text()
        elif isinstance(obj_ref, QPlainTextEdit):
            data[element] = obj_ref.document().toPlainText()
        elif isinstance(obj_ref, QComboBox):
            data[element] = obj_ref.currentIndex()
        elif isinstance(obj_ref, QCheckBox):
            data[element] = obj_ref.isChecked()
        elif isinstance(obj_ref, str):
            data[element] = obj_ref
        elif isinstance(obj_ref, list):
            tmp = []
            for obj in obj_ref:
                getting = collect_editable_data(obj.__dict__.keys())
                tmp.append(get_general_dict_repr(obj, getting))
            data[element] = list(tmp)
            pass

    return data


def get_sum_of_elements(skill, to_get_from):
    tmp = 0
    for element in to_get_from:
        try:
            tmp += int(getattr(skill, element).text())
        except ValueError:
            pass
    return tmp


def update_texts(root_object, to_set, to_get_from):
    obj_to_set = getattr(root_object, to_set)
    obj_to_set.setText(str(get_sum_of_elements(root_object, to_get_from)))


class MyQlineEdit(QLineEdit):
    def __init__(self, parent=None, function_on_unfocused=None, args_on_unfocused=None):
        self.function_on_unfocused = function_on_unfocused
        self.args_on_unfocused = args_on_unfocused
        super(MyQlineEdit, self).__init__(parent)

    def focusOutEvent(self, q_focus_event):
        if self.function_on_unfocused:
            if not self.args_on_unfocused:
                self.function_on_unfocused()
            else:
                self.function_on_unfocused(*self.args_on_unfocused)
        self.setCursorPosition(0)
        super(MyQlineEdit, self).focusOutEvent(q_focus_event)
