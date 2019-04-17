from gui.frames.qt_menu_bar import MenuBar
from gui.popups.qt_about_popup import AboutDialog
from gui.popups.qt_settings import SettingsWindow


class CommonWindow:
    def __init__(self):
        self.about_popup = AboutDialog("About", self)
        self.settings_window = SettingsWindow()
        self.menu_bar = MenuBar(self)
        self.menu_bar.retranslate()

    def common_connect_menu_bar(self):
        self.menu_bar.about.triggered.connect(self.about_popup.show)
        self.menu_bar.open_settings.triggered.connect(self.settings_window.show)
