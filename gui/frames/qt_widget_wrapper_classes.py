from PyQt5 import QtWidgets
from PyQt5.QtGui import QWheelEvent


class NoWheelComboBox(QtWidgets.QComboBox):
    def __init__(self, *args, **kwargs):
        super(NoWheelComboBox, self).__init__(*args, **kwargs)

    def wheelEvent(self, e: QWheelEvent) -> None:
        pass
