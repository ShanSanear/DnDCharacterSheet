from PyQt5 import QtCore, QtWidgets

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


# noinspection PyAttributeOutsideInit,PyArgumentList
class MainWindowUi:
    def setup_ui(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(1748, 1267)
        main_window.setSizeIncrement(QtCore.QSize(1, 0))
        main_window.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("centralwidget")

        self.push_button = QtWidgets.QPushButton(self.central_widget)
        self.push_button.setGeometry(QtCore.QRect(1540, 170, 75, 23))
        self.push_button.setObjectName("clickMeButton")
        self.menu_bar = MenuBar(main_window)
        self.weapons_statistics_box = WeaponStatisticsBox(self.central_widget)
        self.skills_box = SkillsBox(self.central_widget)
        self.number_of_spells_box = NumberOfSpellsBox(self.central_widget)
        self.spells_per_day_box = SpellsPerDayBox(self.central_widget)
        self.known_spells_box = KnownSpellsBox(self.central_widget)
        self.armor_items_box = ArmorItems(self.central_widget)
        self.weapons_box = WeaponsBox(self.central_widget)
        self.notes_box = NotesBox(self.central_widget)
        self.languages_box = LanguagesBox(self.central_widget)
        self.items_box = ItemsBox(self.central_widget)
        self.initiative_speed_box = InitiativeSpeedBox(self.central_widget)
        self.feats_box = FeatsBox(self.central_widget)
        self.saving_throws_box = SavingThrowsBox(self.central_widget)
        self.attacks_box = AttacksBox(self.central_widget)
        self.hp_ac_box = HpAcBox(self.central_widget)
        self.attributes_box = AttributesBox(self.central_widget)
        self.basic_info_box = BasicInfoBox(self.central_widget)
        main_window.setCentralWidget(self.central_widget)
        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.push_button.setText(_translate("MainWindow", "ClickMe"))
