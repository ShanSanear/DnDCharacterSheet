from PyQt5 import QtWidgets


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


def create_qline_edit(name, parent, min_size=None, max_size=None, align=None, indent=None, text=None, enabled=True):
    qline = QtWidgets.QLineEdit(parent)
    qline.setEnabled(enabled)

    qline = resize_element(qline, min_size, max_size)
    if align:
        qline.setAlignment(align)
    if indent:
        qline.setIndent(indent)
    if text:
        qline.setText(text)
    qline.setObjectName(name)

    return qline


def create_push_button(name, parent, min_size=None, max_size=None, text=None):
    button = QtWidgets.QPushButton(parent)
    button.setObjectName(name)
    button = resize_element(button, min_size, max_size)
    button.setText(text)
    return button


def create_combo_box(name, parent, number_of_choices=1, choices_text=None, min_size=None, max_size=None):
    combo_box = QtWidgets.QComboBox(parent)
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


def add_multiple_elements_to_layout_by_row(layout, elements_to_add, row=0, start_column=0, height=1, width=1):
    for column, element in enumerate(elements_to_add):
        add_element_to_layout(layout, element, row, start_column + column * width, height, width)


def add_multiple_elements_to_layout_by_column(layout, elements_to_add, column=0, start_row=0, height=1, width=1):
    for row, element in enumerate(elements_to_add):
        add_element_to_layout(layout, element, start_row + row * height, column, height, width)


def add_element_to_layout(layout, element_to_add, row, column, height, width):
    layout.addWidget(element_to_add, row, column, height, width)

def set_combo_box_choices(root_object, choices):
    for idx, choice_text in enumerate(choices):
        root_object.setItemText(idx, choice_text)


def set_text_of_children(root_object, translate_reference):
    for name, translation in translate_reference.items():
        if name == "title":
            root_object.setTitle(translation)
            continue
        if name == "choices":
            set_combo_box_choices(root_object, translation)
        obj_ref = getattr(root_object, name)
        if isinstance(translation, dict):
            set_text_of_children(obj_ref, translation)
        else:
            if not isinstance(translation, str):
                raise AttributeError("Only strings can be passed to setText")
            obj_ref.setText(translation)
