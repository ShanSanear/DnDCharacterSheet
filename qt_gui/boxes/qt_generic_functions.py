from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QComboBox, QPlainTextEdit, QLineEdit


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


def create_qlabel(name: str, parent: QtWidgets.QLayout, min_size: (list, tuple) = None, max_size: (list, tuple) = None,
                  align=None):
    label = QtWidgets.QLabel(parent)
    label: QtWidgets.QLabel = resize_element(label, min_size, max_size)
    if align:
        label.setAlignment(align)
    label.setObjectName(name)
    return label


def create_qline_edit(name: str, parent: QtWidgets.QWidget, min_size: (list, tuple) = None,
                      max_size: (list, tuple) = None,
                      align=None, indent: int = None, text: str = None, enabled: bool = True):
    qline = QtWidgets.QLineEdit(parent)
    qline.setEnabled(enabled)

    qline: QtWidgets.QLineEdit = resize_element(qline, min_size, max_size)
    if align:
        qline.setAlignment(align)
    if indent:
        qline.setIndent(indent)
    if text:
        qline.setText(text)
    qline.setObjectName(name)

    return qline


def create_push_button(name: str, parent: QtWidgets.QWidget, min_size: (list, tuple) = None,
                       max_size: (list, tuple) = None,
                       text: str = None):
    button = QtWidgets.QPushButton(parent)
    button.setObjectName(name)
    button: QtWidgets.QPushButton = resize_element(button, min_size, max_size)
    button.setText(text)
    return button


def create_combo_box(name: str, parent: QtWidgets.QWidget, number_of_choices: int = 1,
                     choices_text: (list, tuple) = None,
                     min_size: (list, tuple) = None, max_size: (list, tuple) = None):
    combo_box: QComboBox = QtWidgets.QComboBox(parent)
    combo_box.setObjectName(name)
    for _ in range(number_of_choices):
        combo_box.addItem("")
    if choices_text:
        for idx, choice_text in enumerate(choices_text):
            combo_box.setItemText(idx, choice_text)
    if min_size or max_size:
        combo_box = resize_element(combo_box, min_size=min_size, max_size=max_size)
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
                set_text_of_children(obj_ref[idx], element_data)
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
    d = {}

    print(to_get)
    for element in to_get:
        obj_ref = getattr(root_object, element)
        if isinstance(obj_ref, QLineEdit):
            d[element] = obj_ref.text()
        elif isinstance(obj_ref, QPlainTextEdit):
            d[element] = obj_ref.document().toPlainText()
        elif isinstance(obj_ref, QComboBox):
            d[element] = obj_ref.currentIndex()
        elif isinstance(obj_ref, str):
            d[element] = obj_ref
        elif isinstance(obj_ref, list):
            tmp = []
            for obj in obj_ref:
                getting = collect_editable_data(obj.__dict__.keys())
                tmp.append(get_general_dict_repr(obj, getting))
            d[element] = list(tmp)
            pass

    return d
