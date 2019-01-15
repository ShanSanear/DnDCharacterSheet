from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QScrollArea, QTabWidget

from qt_gui.boxes.armor_items import ArmorItems
from qt_gui.boxes.attacks import AttacksBox
from qt_gui.boxes.attributes import AttributesBox
from qt_gui.boxes.basic_info import BasicInfoBox
from qt_gui.boxes.feats import FeatsBox
from qt_gui.boxes.hp_ac import HpAcBox
from qt_gui.boxes.initiative_speed import InitiativeSpeedBox
from qt_gui.boxes.items import ItemsBox
from qt_gui.boxes.known_spells import KnownSpellsBox
from qt_gui.boxes.languages import LanguagesBox
from qt_gui.boxes.menu_bar import MenuBar
from qt_gui.boxes.notes import NotesBox
from qt_gui.boxes.number_of_spells import NumberOfSpellsBox
from qt_gui.boxes.saving_throws import SavingThrowsBox
from qt_gui.boxes.skills import SkillsBox
from qt_gui.boxes.spells_per_day import SpellsPerDayBox
from qt_gui.boxes.weapon_statistics import WeaponStatisticsBox
from qt_gui.boxes.weapons_box import WeaponsBox


class MyTabWidget(QtWidgets.QWidget):

    def __init__(self, parent):
        super(MyTabWidget, self).__init__(parent)
        self.tabs = QTabWidget()
        self.tab1 = QtWidgets.QWidget()
        self.tab2 = QtWidgets.QWidget()
        self.tab3 = QtWidgets.QWidget()
        self.tabs.addTab(self.tab1, "Tab 1")
        self.tabs.addTab(self.tab2, "Tab 2")
        self.tabs.addTab(self.tab3, "Tab 3")

        self.tab1.layout = QVBoxLayout(self)
        self.tab1.setLayout(self.tab1.layout)

        self.tab2.layout = QVBoxLayout(self)
        self.tab2.setLayout(self.tab2.layout)

        self.tab3.layout = QVBoxLayout(self)
        self.tab3.setLayout(self.tab3.layout)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.tabs)



# noinspection PyAttributeOutsideInit
class MainWindowUi:
    def setup_ui(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(1800, 1200)
        self.central_widget = MyTabWidget(main_window)
        self.central_widget.setObjectName("centralwidget")

        self.add_widgets_to_tab_1()
        self.add_widgets_to_tab_2()
        self.add_widgets_to_tab_3()

        self.central_widget.setLayout(self.central_widget.layout)
        self.retranslate_ui(main_window)
        main_window.setCentralWidget(self.central_widget)
        self.central_widget.tabs.setCurrentIndex(0)

        # main_window.setSizeIncrement(QtCore.QSize(1, 0))
        # main_window.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        # self.central_widget = QtWidgets.QWidget(main_window)
        # self.layout_v_box = QtWidgets.QVBoxLayout(self.central_widget)

        # self.scroll_area = QtWidgets.QScrollArea(self.central_widget)
        # self.layout_v_box.addWidget(self.scroll_area)

        # self.scrollAreaWidgetContents = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1800, 1500))
        # self.scroll_area.setWidget(self.scrollAreaWidgetContents)
        #
        # self.layout_h_box = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)

        # self.push_button = QtWidgets.QPushButton(self.central_widget)
        # self.push_button.setGeometry(QtCore.QRect(100, 20, 75, 23))
        # self.push_button.setObjectName("clickMeButton")
        # self.menu_bar = MenuBar(main_window)
        # main_window.setCentralWidget(self.central_widget)
        # Xself.scrollArea.setWidgetResizable(True)

    def add_widgets_to_tab_1(self):
        parent_for_boxes = self.central_widget.tab1
        self.basic_info_box = BasicInfoBox(parent_for_boxes, position=[10, 10], size=[850, 200])
        self.attributes_box = AttributesBox(parent_for_boxes, position=[10, 220], size=[320, 250])
        self.initiative_speed_box = InitiativeSpeedBox(parent_for_boxes, position=[10, 480], size=[271, 121])
        self.hp_ac_box = HpAcBox(parent_for_boxes, position=[350, 220], size=[350, 150])
        self.saving_throws_box = SavingThrowsBox(parent_for_boxes, position=[350, 380], size=[450, 150])
        self.attacks_box = AttacksBox(parent_for_boxes, position=[350, 550], size=[391, 121])
        self.weapons_statistics_box = WeaponStatisticsBox(parent_for_boxes, position=[870, 10], size=[261, 121])
        self.weapons_box = WeaponsBox(parent_for_boxes, position=[870, 220], size=[620, 450])
        return parent_for_boxes

    def add_widgets_to_tab_2(self):
        parent_for_boxes = self.central_widget.tab2
        self.skills_box = SkillsBox(parent_for_boxes, position=[10, 10], size=[600, 400])
        self.number_of_spells_box = NumberOfSpellsBox(parent_for_boxes, position=[10, 420], size=[600, 130])
        self.languages_box = LanguagesBox(parent_for_boxes, position=[650, 10], size=[270, 250])
        self.feats_box = FeatsBox(parent_for_boxes, position=[10, 580], size=[270, 80])
        self.spells_per_day_box = SpellsPerDayBox(parent_for_boxes, position=[950, 10], size=[300, 350])
        self.known_spells_box = KnownSpellsBox(parent_for_boxes, position=[650, 380], size=[600, 100])
        return parent_for_boxes

    def add_widgets_to_tab_3(self):
        parent_for_boxes = self.central_widget.tab3
        self.notes_box = NotesBox(parent_for_boxes, position=[10, 350], size=[510, 200])
        self.armor_items_box = ArmorItems(parent_for_boxes, position=[10, 10], size=[620, 331])
        self.items_box = ItemsBox(parent_for_boxes, position=[650, 10], size=[581, 291])

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "MainWindow"))
#        self.push_button.setText(_translate("MainWindow", "ClickMe"))
