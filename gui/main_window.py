from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QTabWidget

from gui.frames.qt_armor_items import ArmorItems
from gui.frames.qt_attacks import AttacksBox
from gui.frames.qt_attributes import AttributesBox
from gui.frames.qt_basic_info import BasicInfoBox
from gui.frames.qt_feats import FeatsBox
from gui.frames.qt_hp_ac import HpAcBox
from gui.frames.qt_initiative_speed import InitiativeSpeedBox
from gui.frames.qt_items import ItemsBox
from gui.frames.qt_known_spells import KnownSpellsBox
from gui.frames.qt_languages import LanguagesBox
from gui.frames.qt_menu_bar import MenuBar
from gui.frames.qt_notes import NotesBox
from gui.frames.qt_number_of_spells import NumberOfSpellsBox
from gui.frames.qt_saving_throws import SavingThrowsBox
from gui.frames.qt_skills import SkillsBox
from gui.frames.qt_spells_per_day import SpellsPerDayBox
from gui.frames.qt_weapon_statistics import WeaponStatisticsBox
from gui.frames.qt_weapons import WeaponsBox


class TabWidget(QtWidgets.QWidget):

    def __init__(self, parent):
        super(TabWidget, self).__init__(parent)
        self.tabs = QTabWidget()
        self.tab1 = QtWidgets.QWidget()
        self.tab2 = QtWidgets.QWidget()
        self.tab3 = QtWidgets.QWidget()
        self.tabs.addTab(self.tab1, "Basic information")
        self.tabs.addTab(self.tab2, "Items / Spells / Languages")
        self.tabs.addTab(self.tab3, "Weapons / Armor / Notes")

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
        main_window.resize(1300, 850)
        self.central_widget = TabWidget(main_window)
        self.central_widget.setObjectName("centralwidget")

        self.add_widgets_to_tab_1()
        self.add_widgets_to_tab_2()
        self.add_widgets_to_tab_3()

        self.central_widget.setLayout(self.central_widget.layout)
        self.retranslate_ui(main_window)
        self.menu_bar = MenuBar(main_window)
        main_window.setCentralWidget(self.central_widget)
        main_window.setMenuBar(self.menu_bar.root)
        #self.push_button = create_push_button("ClickMe", self.central_widget)
        #self.push_button.move(200, 30)

        self.central_widget.tabs.setCurrentIndex(0)

    def add_widgets_to_tab_1(self):
        parent_for_boxes = self.central_widget.tab1
        self.basic_info_box = BasicInfoBox(parent_for_boxes, position=[10, 10], size=[500, 220])
        self.skills_box = SkillsBox(parent_for_boxes, position=[10, 245], size=[500, 40])

        self.attributes_box = AttributesBox(parent_for_boxes, position=[540, 10], size=[270, 250])
        self.hp_ac_box = HpAcBox(parent_for_boxes, position=[540, 290], size=[340, 150])
        self.feats_box = FeatsBox(parent_for_boxes, position=[540, 480], size=[340, 100])

        self.weapons_statistics_box = WeaponStatisticsBox(parent_for_boxes, position=[840, 10], size=[180, 110])
        self.attacks_box = AttacksBox(parent_for_boxes, position=[840, 140], size=[340, 120])

        self.saving_throws_box = SavingThrowsBox(parent_for_boxes, position=[910, 290], size=[320, 150])
        self.feats_box_2 = FeatsBox(parent_for_boxes, position=[910, 480], size=[340, 100])

        self.initiative_speed_box = InitiativeSpeedBox(parent_for_boxes, position=[1050, 10], size=[200, 80])

        return parent_for_boxes

    def add_widgets_to_tab_2(self):
        parent_for_boxes = self.central_widget.tab2
        self.items_box = ItemsBox(parent_for_boxes, position=[10, 10], size=[500, 80])
        self.number_of_spells_box = NumberOfSpellsBox(parent_for_boxes, position=[520, 10], size=[450, 100])
        self.languages_box = LanguagesBox(parent_for_boxes, position=[1090, 380], size=[150, 250])
        self.spells_per_day_box = SpellsPerDayBox(parent_for_boxes, position=[1090, 10], size=[150, 350])
        self.known_spells_box = KnownSpellsBox(parent_for_boxes, position=[520, 120], size=[550, 60])
        return parent_for_boxes

    def add_widgets_to_tab_3(self):
        parent_for_boxes = self.central_widget.tab3
        self.notes_box = NotesBox(parent_for_boxes, position=[650, 470], size=[620, 290])
        self.armor_items_box = ArmorItems(parent_for_boxes, position=[10, 10], size=[620, 51])
        self.weapons_box = WeaponsBox(parent_for_boxes, position=[650, 10], size=[620, 450])

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "MainWindow"))
