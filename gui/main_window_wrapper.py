from PyQt5 import QtGui
from PyQt5.QtCore import QSettings, QSize, QPoint
from PyQt5.QtWidgets import QMainWindow

from gui.constants import MAIN_WINDOW_SIZE, MAIN_WINDOW_POSITION


class MainWindowWrapper(QMainWindow):
    def __init__(self, default_size):
        super(MainWindowWrapper, self).__init__()
        self.settings = QSettings("settings.ini", QSettings.IniFormat, None)
        self.settings.setFallbacksEnabled(False)
        self.default_size = QSize(*default_size)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        size = self.size()
        self.settings.setValue(MAIN_WINDOW_SIZE, size)
        qpos: QPoint = self.pos()
        self.settings.setValue(MAIN_WINDOW_POSITION, qpos)
        self.settings.sync()
        super(MainWindowWrapper, self).closeEvent(a0)

    def _load_size(self):
        size = self.settings.value(MAIN_WINDOW_SIZE, self.default_size, type=QSize)
        self.resize(size)

    def _load_position(self):
        base_position = self.settings.value(MAIN_WINDOW_POSITION, None, type=QPoint)
        if base_position:
            self.move(base_position)
