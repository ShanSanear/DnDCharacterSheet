from PyQt5.QtWidgets import QTabWidget, QMainWindow, QScrollArea, QWidget, QSizePolicy

from gui.frames.qt_menu_bar import MenuBar
from gui.frames.tab_1.qt_attacks import AttacksBox
from gui.frames.tab_1.qt_attributes import AttributesBox
from gui.frames.tab_1.qt_basic_info import BasicInfoBox
from gui.frames.tab_1.qt_feats import FeatsBox
from gui.frames.tab_1.qt_hp_ac import HpAcBox
from gui.frames.tab_1.qt_initiative_speed import InitiativeSpeedBox
from gui.frames.tab_1.qt_saving_throws import SavingThrowsBox
from gui.frames.tab_1.qt_skills import SkillsBox
from gui.frames.tab_1.qt_weapon_statistics import WeaponStatisticsBox
from gui.frames.tab_2.qt_items import ItemsBox
from gui.frames.tab_2.qt_known_spells import KnownSpellsBox
from gui.frames.tab_2.qt_languages import LanguagesBox
from gui.frames.tab_2.qt_number_of_spells import NumberOfSpellsBox
from gui.frames.tab_2.qt_spells_per_day import SpellsPerDayBox
from gui.frames.tab_3.qt_armor_items import ArmorItems
from gui.frames.tab_3.qt_notes import NotesBox
from gui.frames.tab_3.qt_weapons import WeaponsBox


class MainWindowUi(QMainWindow):
    def __init__(self, char_core):
        super(MainWindowUi, self).__init__()
        self.char_core = char_core

    def setup_ui(self):
        self.setObjectName("MainWindow")
        self.resize(1400, 830)
        self.tabs = QTabWidget(self)
        self.tabs.setMinimumSize(1300, 780)
        size_policy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        size_policy.setHeightForWidth(True)
        self.tabs.setSizePolicy(size_policy)
        self.tab1 = QWidget(self.tabs)
        self.tab1.tabs = self.tabs
        self.tab2 = QWidget(self.tabs)
        self.tab2.tabs = self.tabs
        self.tab3 = QWidget(self.tabs)
        self.tabs.addTab(self.tab1, "Basic information")
        self.tabs.addTab(self.tab2, "Items / Spells / Languages")
        self.tabs.addTab(self.tab3, "Weapons / Armor / Notes")
        self.create_tab_1()
        self.create_tab_2()
        self.create_tab_3()
        self.menu_bar = MenuBar(self)

        scroll = QScrollArea()
        scroll.setEnabled(True)
        scroll.setWidget(self.tabs)
        scroll.setWidgetResizable(True)
        self.setCentralWidget(scroll)
        self.add_base_elements()
        self.tabs.setCurrentIndex(0)

    def create_tab_1(self):
        parent_for_boxes = self.tab1
        print(self.tab1.parent())
        print(self.tabs.parent())
        self.basic_info_box = BasicInfoBox(parent_for_boxes, position=[10, 10], size=[500, 220])
        self.skills_box = SkillsBox(parent_for_boxes, position=[10, 245], size=[500, 90], char_core=self.char_core)

        self.attributes_box = AttributesBox(parent_for_boxes, position=[540, 10], size=[270, 250],
                                            char_core=self.char_core)
        self.hp_ac_box = HpAcBox(parent_for_boxes, position=[540, 290], size=[340, 150], char_core=self.char_core)
        self.feats_box = FeatsBox(parent_for_boxes, position=[540, 480], size=[340, 100])

        self.weapons_statistics_box = WeaponStatisticsBox(parent_for_boxes, position=[840, 10],
                                                          size=[420, 110], char_core=self.char_core)
        self.attacks_box = AttacksBox(parent_for_boxes, position=[840, 140], size=[340, 120], char_core=self.char_core)

        self.saving_throws_box = SavingThrowsBox(parent_for_boxes, position=[910, 290], size=[320, 150],
                                                 char_core=self.char_core)
        self.feats_box_2 = FeatsBox(parent_for_boxes, position=[910, 480], size=[340, 100])

        self.initiative_speed_box = InitiativeSpeedBox(parent_for_boxes, position=[1200, 140], size=[200, 80], char_core=self.char_core)

        return parent_for_boxes

    def create_tab_2(self):
        parent_for_boxes = self.tab2
        self.items_box = ItemsBox(parent_for_boxes, position=[10, 10], size=[500, 80])
        self.number_of_spells_box = NumberOfSpellsBox(parent_for_boxes, position=[520, 10], size=[450, 100])
        self.languages_box = LanguagesBox(parent_for_boxes, position=[1090, 380], size=[150, 250])
        self.spells_per_day_box = SpellsPerDayBox(parent_for_boxes, position=[1090, 10], size=[150, 350])
        self.known_spells_box = KnownSpellsBox(parent_for_boxes, position=[520, 120], size=[550, 60])
        return parent_for_boxes

    def create_tab_3(self):
        parent_for_boxes = self.tab3
        self.notes_box = NotesBox(parent_for_boxes, position=[650, 470], size=[620, 290])
        self.armor_items_box = ArmorItems(parent_for_boxes, position=[10, 10], size=[620, 51])
        self.weapons_box = WeaponsBox(parent_for_boxes, position=[650, 10], size=[620, 450],
                                      weapons_statistics_box=self.weapons_statistics_box)

    def add_base_elements(self):
        pass
        #for _ in range(20):
        #    self.skills_box.add_skill()
        # for _ in range(20):
        #      self.feats_box.add_feat()
        #      self.feats_box_2.add_feat()
        # for _ in range(30):
        #     self.items_box.add_item()
