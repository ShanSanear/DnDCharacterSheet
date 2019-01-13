from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QScrollArea

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


# noinspection PyAttributeOutsideInit
class MainWindowUi:
    def setup_ui(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(1748, 1267)
        main_window.setSizeIncrement(QtCore.QSize(1, 0))
        main_window.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("centralwidget")
        layout = QtWidgets.QVBoxLayout(self.central_widget)

        self.scrollArea = QtWidgets.QScrollArea(self.central_widget)
        layout.addWidget(self.scrollArea)

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1800, 1500))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        layout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        # add child widgets to this layout...

        self.push_button = QtWidgets.QPushButton(self.central_widget)
        self.push_button.setGeometry(QtCore.QRect(1540, 170, 75, 23))
        self.push_button.setObjectName("clickMeButton")
        self.menu_bar = MenuBar(main_window)
        self.weapons_statistics_box = WeaponStatisticsBox(None)
        self.skills_box = SkillsBox(None)
        self.number_of_spells_box = NumberOfSpellsBox(None)
        self.spells_per_day_box = SpellsPerDayBox(None)
        self.known_spells_box = KnownSpellsBox(None)
        self.armor_items_box = ArmorItems(None)
        self.weapons_box = WeaponsBox(None)
        self.notes_box = NotesBox(None)
        self.languages_box = LanguagesBox(None)
        self.items_box = ItemsBox(None)
        self.initiative_speed_box = InitiativeSpeedBox(None)
        self.feats_box = FeatsBox(None)
        self.saving_throws_box = SavingThrowsBox(None)
        self.attacks_box = AttacksBox(None)
        self.hp_ac_box = HpAcBox(None)
        self.attributes_box = AttributesBox(None)
        self.basic_info_box = BasicInfoBox(None)

        children = [self.weapons_statistics_box.root,
        self.skills_box.root,
        self.number_of_spells_box.root,
        self.spells_per_day_box.root,
        self.known_spells_box.root,
        self.armor_items_box.root,
        self.weapons_box.root,
        self.notes_box.root,
        self.languages_box.root,
        self.items_box.root,
        self.initiative_speed_box.root,
        self.feats_box.root,
        self.saving_throws_box.root,
        self.attacks_box.root,
        self.hp_ac_box.root,
        self.attributes_box.root,
        self.basic_info_box.root]
        for child in children:
            layout.addChildWidget(child)
        #main_window.setCentralWidget(self.central_widget)
        #Xself.scrollArea.setWidgetResizable(True)
        self.retranslate_ui(main_window)
        main_window.setCentralWidget(self.central_widget)

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.push_button.setText(_translate("MainWindow", "ClickMe"))
