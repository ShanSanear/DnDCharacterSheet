import logging

from PyQt5 import QtWidgets
from PyQt5.QtGui import QWheelEvent
from PyQt5.QtWidgets import QLineEdit


class NoWheelComboBox(QtWidgets.QComboBox):
    def __init__(self, *args, **kwargs):
        super(NoWheelComboBox, self).__init__(*args, **kwargs)

    def wheelEvent(self, e: QWheelEvent) -> None:
        pass


class MyQlineEdit(QLineEdit):
    def __init__(self, parent=None, function_on_unfocused=None, args_on_unfocused=None, str_format="{}",
                 is_float=False):
        self.function_on_unfocused = function_on_unfocused
        self.args_on_unfocused = args_on_unfocused
        self.str_format = str_format
        self.is_float = is_float
        super(MyQlineEdit, self).__init__(parent)

    def focusOutEvent(self, q_focus_event):
        if self.function_on_unfocused:
            if not self.args_on_unfocused:
                self.function_on_unfocused()
            else:
                self.function_on_unfocused(*self.args_on_unfocused)
        self.setCursorPosition(0)
        super(MyQlineEdit, self).focusOutEvent(q_focus_event)

    def setText(self, p_str):
        if self.str_format != "{}":
            try:
                if not self.is_float:
                    # Float in case of some kind of sum being with decimal point
                    text = self.str_format.format(int(float(p_str)))
                else:
                    text = self.str_format.format(float(p_str))
            except ValueError:
                text = p_str
                logging.warning("Couldnt work with text: %s", p_str)
        else:
            text = p_str
        super(MyQlineEdit, self).setText(text)
        self.setCursorPosition(0)
