from PyQt5 import QtGui
from PyQt5.QtCore import QSettings, QSize, QPoint, QTranslator
from PyQt5.QtWidgets import QMainWindow

from gui.constants import MAIN_WINDOW_SIZE, MAIN_WINDOW_POSITION
from gui.frames.qt_menu_bar import MenuBar
from gui.popups.qt_about_popup import AboutDialog
from gui.popups.qt_settings import SettingsWindow


class MainWindowWrapper(QMainWindow):
    def __init__(self, default_size):
        super(MainWindowWrapper, self).__init__()
        self.settings = QSettings("settings.ini", QSettings.IniFormat, None)
        self.settings.setFallbacksEnabled(False)
        self.default_size = QSize(*default_size)
        self.trans = QTranslator(self)
        self.about_popup = AboutDialog("About", self)
        self.settings_window = SettingsWindow()
        self.menu_bar = MenuBar(self)
        self.menu_bar.retranslate()

    def common_connect_menu_bar(self):
        self.menu_bar.about.triggered.connect(self.about_popup.show)
        self.menu_bar.open_settings.triggered.connect(self.settings_window.show)

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

    def restore_window_settings(self):
        self._load_size()
        self._load_position()

    def change_main_window_title(self, new_title):
        self.setWindowTitle(new_title)
