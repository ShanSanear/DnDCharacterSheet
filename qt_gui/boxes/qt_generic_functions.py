from PyQt5 import QtCore, QtWidgets


def resize_element(element, min_size, max_size):
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


def create_qlabel(name, parent, min_size=None, max_size=None, align=None):
    label = QtWidgets.QLabel(parent)
    label = resize_element(label, min_size, max_size)
    if align:
        label.setAlignment(align)
    label.setObjectName(name)
    return label


def create_qline_edit(name, parent, min_size=None, max_size=None, align=None, indent=None, text=None):
    qline = QtWidgets.QLineEdit(parent)
    qline = resize_element(qline, min_size, max_size)
    if align:
        qline.setAlignment(align)
    if indent:
        qline.setIndent(indent)
    if text:
        qline.setText(text)
    qline.setObjectName(name)
    return qline


def numeric_label(name, parent, align):
    return create_qlabel(name, parent, align=align)


def add_multiple_elements_to_layout_by_row(layout, elements_to_add, row=0, start_column=0, height=1, width=1):
    for column, element in enumerate(elements_to_add):
        layout.addWidget(element, row, start_column + column * width, height, width)


def add_multiple_elements_to_layout_by_column(layout, elements_to_add, column=0, start_row=0, height=1, width=1):
    for row, element in enumerate(elements_to_add):
        layout.addWidget(element, start_row + row * height, column, height, width)


def set_text_of_children(root_object, translate_reference):
    for name, translation in translate_reference.items():
        obj_ref = getattr(root_object, name)
        if isinstance(translation, dict):
            set_text_of_children(obj_ref, translation)
        else:
            if not isinstance(translation, str):
                raise AttributeError("Only strings can be passed to setText")
            obj_ref.setText(translation)
