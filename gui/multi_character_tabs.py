"""
Shamelessly copied from https://stackoverflow.com/a/44458561/10019761 with small tweaks.
Kudos to yurisnm (https://stackoverflow.com/users/6801746/yurisnm) for sharing this.
"""
import logging

from PyQt5.QtCore import QSize, pyqtSlot
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QTabBar
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QVBoxLayout


class TabBarPlus(QTabBar):
    """Tab bar that has a plus button floating to the right of the tabs."""

    add_new_tab_sig = pyqtSignal()

    def __init__(self, parent):
        super(TabBarPlus, self).__init__()
        self.setParent(parent)

        self.add_new_tab_button = QPushButton("+")
        self.add_new_tab_button.setParent(parent)
        self.add_new_tab_button.setFixedSize(23, 23)
        self.add_new_tab_button.clicked.connect(self.add_new_tab_sig.emit)
        self.move_add_new_tab_button()

    def sizeHint(self):
        """Return the size of the TabBar with increased width for the plus button."""
        size_hint = QTabBar.sizeHint(self)
        width = size_hint.width()
        height = size_hint.height()
        return QSize(width + 25, height)

    def resizeEvent(self, event):
        """Resize the widget and make sure the plus button is in the correct location."""
        super().resizeEvent(event)

        self.move_add_new_tab_button()

    def tabLayoutChange(self):
        """This virtual handler is called whenever the tab layout changes.
        If anything changes make sure the plus button is in the correct location.
        """
        super().tabLayoutChange()

        self.move_add_new_tab_button()

    def mouseDoubleClickEvent(self, event):
        if event.button() != Qt.LeftButton:
            super(TabBarPlus, self).mouseDoubleClickEvent(event)

        idx = self.currentIndex()
        new_tab_name, ok = QInputDialog.getText(self, 'New tab name', 'New tab name:')
        if ok:
            self.setTabText(idx, new_tab_name)

    def move_add_new_tab_button(self):
        """Move the plus button to the correct location."""
        size = 0
        for i in range(self.count()):
            size += self.tabRect(i).width() * 2

        h = self.geometry().top()
        w = self.width()
        logging.debug(f"Tab height: %d", h)
        logging.debug(f"Tab width: %d", w)
        if size > w:
            self.add_new_tab_button.move(w, h)
        else:
            self.add_new_tab_button.move(size + 10, h)


class MulticharacterTabWidget(QTabWidget):

    def __init__(self, parent, single_character_gui):
        super(MulticharacterTabWidget, self).__init__(parent)
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.single_character_gui = single_character_gui
        self.setLayout(self.layout)
        self.tab = TabBarPlus(self)
        self.setTabBar(self.tab)
        self.tab.add_new_tab_sig.connect(self.add_tab)
        self.tab.tabMoved.connect(self.tab.move_add_new_tab_button)
        self.tabCloseRequested.connect(self.removeTab)
        self._characters = []
        self.add_tab()

    def add_tab(self):
        if self.count() > 0:
            self.setTabsClosable(True)
        else:
            self.setTabsClosable(False)

        new_character = self.single_character_gui()
        self._characters.append(new_character)
        self.addTab(new_character.container, new_character.tab_name)

    def removeTab(self, p_int):
        del self._characters[p_int]
        try:
            self.chart.removeSeries(self.series[p_int])
            self.tables.remove(self.tables[p_int])
            self.models.remove(self.models[p_int])
            self.series.remove(self.series[p_int])
        except (TypeError, AttributeError):
            pass

        super(MulticharacterTabWidget, self).removeTab(p_int)

        if self.count() > 1:
            self.setTabsClosable(True)
        else:
            self.setTabsClosable(False)

    @pyqtSlot()
    def update_axes(self):

        for s in self.series:
            self.chart.removeSeries(s)
            self.chart.addSeries(s)
        self.chart.createDefaultAxes()

    def get_character(self, pos):
        return self._characters[pos]
