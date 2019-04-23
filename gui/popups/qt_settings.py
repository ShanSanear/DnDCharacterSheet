import logging
import sys

from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QDialog, QApplication, QSpinBox, QVBoxLayout, QHBoxLayout, QLabel, QWidget, \
    QDialogButtonBox, QCheckBox

from gui.constants import AUTOSAVE_INTERVAL, ASK_ABOUT_LOADING
from gui.qt_gui import config_logger


class SettingsWindow(QDialog):

    def __init__(self):
        super(SettingsWindow, self).__init__()
        self.settings = QSettings("settings.ini", QSettings.IniFormat, None)
        self.settings.setFallbacksEnabled(False)
        self.main_layout = QVBoxLayout(self)
        self.buttons_box = QDialogButtonBox(self)
        self.autosave_container = QWidget(self)
        self.autosave_label = QLabel(self.autosave_container)
        self.autosave_interval = QSpinBox(self.autosave_container)
        self.autosave_layout = QHBoxLayout(self.autosave_container)
        self.should_load_last_toggle = QCheckBox(self)
        self.setup_ui()
        self.retranslate()
        self.load_settings()

    def load_settings(self):
        logging.debug("Loading settings")
        self.autosave_interval.setValue(self.settings.value(AUTOSAVE_INTERVAL, 1, type=int))
        self.should_load_last_toggle.setChecked(self.settings.value(ASK_ABOUT_LOADING, False, type=bool))

    def setup_ui(self):
        self.setup_buttons()
        self.setup_layout()

    def setup_layout(self):
        self.autosave_layout.setContentsMargins(0, 0, 0, 0)
        self.autosave_layout.addWidget(self.autosave_label)
        self.autosave_layout.addWidget(self.autosave_interval)
        self.main_layout.addWidget(self.autosave_container)
        self.main_layout.addWidget(self.should_load_last_toggle)
        self.main_layout.addWidget(self.buttons_box)
        self.setLayout(self.main_layout)

    def setup_buttons(self):
        self.buttons_box.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.buttons_box.accepted.connect(self.save_settings)
        self.buttons_box.rejected.connect(self.cancel_changes)

    def cancel_changes(self):
        logging.debug("Cancel callback")
        self.close()

    def save_settings(self):
        logging.debug("Ok callback")
        self.settings.setValue(AUTOSAVE_INTERVAL, self.autosave_interval.value())
        self.settings.setValue(ASK_ABOUT_LOADING, self.should_load_last_toggle.isChecked())
        self.close()

    def retranslate(self):
        self.autosave_label.setText(QApplication.translate("SettingsDialog", "Autosave interval"))
        self.buttons_box.button(QDialogButtonBox.Cancel).setText(QApplication.translate("SettingsDialog", "Cancel"))
        self.should_load_last_toggle.setText(QApplication.translate("SettingsDialog", "Ask for loading last file"))
        self.setWindowTitle(QApplication.translate("SettingsDialog", "Settings"))

    def show(self) -> None:
        self.retranslate()
        super(SettingsWindow, self).show()


if __name__ == '__main__':
    config_logger(logging.DEBUG)
    logging.debug("Logger initialized")
    app = QApplication(sys.argv)
    mw = SettingsWindow()
    mw.show()
    sys.exit(app.exec())
