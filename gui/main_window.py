from PyQt5.QtWidgets import QTabWidget, QMainWindow, QScrollArea, QWidget, QSizePolicy

import core
from gui.frames.qt_menu_bar import MenuBar
from gui.frames.tab_1.qt_attributes import AttributesBox
from gui.frames.tab_1.qt_basic_info import BasicInfoBox
from gui.frames.tab_1.qt_combat import CombatBox
from gui.frames.tab_1.qt_feats import FeatsBox
from gui.frames.tab_1.qt_hp_ac import HpAcBox
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


class CoreWindow(QMainWindow):

    def __init__(self):
        super(CoreWindow, self).__init__()
        self.char_core = core.character.Character("Shan")
        attrs = dict(str=12, dex=12, con=12, int=12, wis=12, cha=16)
        self.char_core.attributes.set_attributes(attrs)

        self.tabs = QTabWidget(self)
        self.tabs.setMinimumSize(1340, 800)
        self.resize(1360, 860)
        self.tabs.setCurrentIndex(0)
        size_policy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        size_policy.setHeightForWidth(True)
        self.tabs.setSizePolicy(size_policy)

        scroll = QScrollArea()
        scroll.setEnabled(True)
        scroll.setWidget(self.tabs)
        scroll.setWidgetResizable(True)
        self.setCentralWidget(scroll)

        self.menu_bar = MenuBar(self)


class Tab1(CoreWindow):

    def __init__(self):
        super(Tab1, self).__init__()
        self.tab1 = QWidget(self.tabs)
        self.basic_info_box = BasicInfoBox(self.tab1, position=[10, 10], size=[500, 200])
        self.skills_box = SkillsBox(self.tab1, position=[830, 10], size=[500, 780], char_core=self.char_core)

        self.attributes_box = AttributesBox(self.tab1, position=[10, 220], size=[240, 240],
                                            char_core=self.char_core)

        self.weapons_statistics_box = WeaponStatisticsBox(self.tab1, position=[10, 520],
                                                          size=[500, 120], char_core=self.char_core)

        self.combat_box = CombatBox(self.tab1, position=[520, 10], size=[300, 200], char_core=self.char_core)
        self.saving_throws_box = SavingThrowsBox(self.tab1, position=[260, 360], size=[250, 150],
                                                 char_core=self.char_core)
        self.hp_ac_box = HpAcBox(self.tab1, position=[260, 220], size=[250, 130], char_core=self.char_core)
        self.feats_box = FeatsBox(self.tab1, position=[520, 220], size=[300, 570])
        self.tabs.addTab(self.tab1, "Basic information / Combat / Skills / Feats")


class Tab2(Tab1):

    def __init__(self):
        super(Tab2, self).__init__()
        self.tab2 = QWidget(self.tabs)
        self.items_box = ItemsBox(self.tab2, position=[10, 10], size=[500, 780], char_core=self.char_core)
        self.number_of_spells_box = NumberOfSpellsBox(self.tab2, position=[520, 10], size=[450, 100])
        self.languages_box = LanguagesBox(self.tab2, position=[1090, 380], size=[150, 250])
        self.spells_per_day_box = SpellsPerDayBox(self.tab2, position=[1090, 10], size=[150, 350])
        self.known_spells_box = KnownSpellsBox(self.tab2, position=[520, 120], size=[550, 670])
        self.tabs.addTab(self.tab2, "Items / Spells / Languages")


class Tab3(Tab2):

    def __init__(self):
        super(Tab3, self).__init__()
        self.tab3 = QWidget(self.tabs)
        self.notes_box = NotesBox(self.tab3, position=[650, 470], size=[620, 290])
        self.armor_items_box = ArmorItems(self.tab3, position=[10, 10], size=[620, 51], items_box=self.items_box,
                                          hp_ac_box=self.hp_ac_box)
        self.weapons_box = WeaponsBox(self.tab3, position=[650, 10], size=[620, 450],
                                      weapons_statistics_box=self.weapons_statistics_box, items_box=self.items_box)
        self.tabs.addTab(self.tab3, "Weapons / Armor / Notes")


class MainWindowUi(Tab3):

    def __init__(self):
        super(MainWindowUi, self).__init__()
        self.tabs.setCurrentIndex(0)
