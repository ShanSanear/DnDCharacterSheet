from PyQt5 import QtCore, QtWidgets


def create_qt_line_edit(minimum_size, maximum_size, widget_name):
    pass


def resize_element(element, min_size, max_size):
    if min_size:
        element.setMinimumSize(QtCore.QSize(*min_size))
    if max_size:
        element.setMaximumSize(QtCore.QSize(*max_size))
    return element


def create_qlabel(name, parent, min_size=None, max_size=None, align=None):
    label = QtWidgets.QLabel(parent)
    label = resize_element(label, min_size, max_size)
    if align:
        label.setAlignment(align)
    label.setObjectName(name)
    return label


def create_qline_edit(name, parent, min_size=None, max_size=None, align=None):
    qline = QtWidgets.QLineEdit(parent)
    qline = resize_element(qline, min_size, max_size)
    if align:
        qline.setAlignment(align)
    qline.setObjectName(name)
    return qline


def numeric_label(name, parent, align):
    return create_qlabel(name, parent, align=align)