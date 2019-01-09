# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from qt_gui.boxes.armor_items import ArmorItems
from qt_gui.boxes.attacks import AttacksBox
from qt_gui.boxes.feats import FeatsBox
from qt_gui.boxes.hp_ac import HpAcBox
from qt_gui.boxes.initiative_speed import InitiativeSpeedBox
from qt_gui.boxes.items import ItemsBox
from qt_gui.boxes.known_spells import KnownSpellsBox
from qt_gui.boxes.languages import LanguagesBox
from qt_gui.boxes.notes import NotesBox
from qt_gui.boxes.number_of_spells import NumberOfSpellsBox
from qt_gui.boxes.saving_throws import SavingThrowsBox
from qt_gui.boxes.skills import SkillsBox
from qt_gui.boxes.spells_per_day import SpellsPerDayBox
from qt_gui.boxes.weapon_statistics import WeaponStatisticsBox
from qt_gui.boxes.weapons_box import WeaponsBox



#translator
#_translate = QtCore.QCoreApplication.translate


# noinspection PyAttributeOutsideInit,PyArgumentList


class MainWindowUi(object):
    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1748, 1267)
        MainWindow.setSizeIncrement(QtCore.QSize(1, 0))
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        palette = self.create_palette()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1540, 170, 75, 23))
        self.pushButton.setObjectName("clickMeButton")

        self.create_basic_info_box(palette)
        self.create_attributes_box()
        self.create_hp_ac_box()
        self.create_attacks_box()
        self.create_saving_throws_box()
        self.create_feats_box()
        self.create_initiative_speed_box()
        self.create_items_box()
        self.create_languages_box()
        self.create_notes_box()
        self.create_weapons_box()
        self.create_armor_box()
        self.create_known_spells_layout()
        self.create_spells_per_day_box()
        self.create_number_of_spells_box()
        self.create_skills_layout()
        self.create_weapon_statistics_box()
        self.create_menu_bar(MainWindow)

        MainWindow.setCentralWidget(self.centralwidget)
        self.character_class_label.setBuddy(self.character_class)
        self.character_race_label.setBuddy(self.character_race)
        self.character_name_label.setBuddy(self.character_name)
        self.player_name_label.setBuddy(self.player_name)

        self.retranslate_ui(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def create_menu_bar(self, MainWindow):
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1748, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menuBar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menuBar)
        self.actionNew_character = QtWidgets.QAction(MainWindow)
        self.actionNew_character.setObjectName("actionNew_character")
        self.actionOpen_character = QtWidgets.QAction(MainWindow)
        self.actionOpen_character.setObjectName("actionOpen_character")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionNew_character)
        self.menuFile.addAction(self.actionOpen_character)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())

    def create_weapon_statistics_box(self):
        self.WeaponStatisticsBox = WeaponStatisticsBox(self.centralwidget)

    def create_skills_layout(self):
        self.SkillsBox = SkillsBox(self.centralwidget)

    def create_number_of_spells_box(self):
        self.NumberOfSpellsBox = NumberOfSpellsBox(self.centralwidget)

    def create_spells_per_day_box(self):
        self.SpellsPerDayBox = SpellsPerDayBox(self.centralwidget)

    def create_known_spells_layout(self):
        self.KnownSpellsBox = KnownSpellsBox(self.centralwidget)

    def create_armor_box(self):
        self.ArmorItems = ArmorItems(self.centralwidget)

    def create_weapons_box(self):
        self.WeaponsBox = WeaponsBox(self.centralwidget)

    def create_notes_box(self):
        self.NotesBox = NotesBox(self.centralwidget)

    def create_languages_box(self):
        self.LanguagesBox = LanguagesBox(self.centralwidget)

    def create_items_box(self):
        self.ItemsBox = ItemsBox(self.centralwidget)

    def create_initiative_speed_box(self):
        self.InitiativeSpeedBox = InitiativeSpeedBox(self.centralwidget)

    def create_feats_box(self):
        self.FeatsBox = FeatsBox(self.centralwidget)

    def create_saving_throws_box(self):
        self.SavingThrowsBox = SavingThrowsBox(self.centralwidget)

    def create_attacks_box(self):
        self.AttacksBox = AttacksBox(self.centralwidget)

    def create_hp_ac_box(self):
        self.HpAcBox = HpAcBox(self.centralwidget)

    def create_attributes_box(self):
        self.AttributesBox = QtWidgets.QGroupBox(self.centralwidget)
        self.AttributesBox.setGeometry(QtCore.QRect(10, 200, 311, 231))
        self.AttributesBox.setObjectName("AttributesBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.AttributesBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 285, 201))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.AttributesLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.AttributesLayout.setContentsMargins(9, 9, 9, 9)
        self.AttributesLayout.setSpacing(6)
        self.AttributesLayout.setObjectName("AttributesLayout")
        self.attr_str_val = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.attr_str_val.setMinimumSize(QtCore.QSize(0, 23))
        self.attr_str_val.setObjectName("attr_str_val")
        self.attr_head_name = QtWidgets.QLabel(self.gridLayoutWidget)
        self.attr_head_name.setMinimumSize(QtCore.QSize(0, 0))
        self.attr_head_name.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.attr_head_name.setBaseSize(QtCore.QSize(10, 0))
        self.attr_head_name.setAlignment(QtCore.Qt.AlignCenter)
        self.attr_head_name.setObjectName("attr_head_name")
        self.attr_int_label = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.attr_int_label.sizePolicy().hasHeightForWidth())
        self.attr_int_label.setSizePolicy(sizePolicy)
        self.attr_int_label.setMinimumSize(QtCore.QSize(40, 0))
        self.attr_int_label.setBaseSize(QtCore.QSize(10, 0))
        self.attr_int_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.attr_int_label.setObjectName("attr_int_label")
        self.attr_con_mod = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.attr_con_mod.setMinimumSize(QtCore.QSize(0, 23))
        self.attr_con_mod.setObjectName("attr_con_mod")
        self.Attr_head_mod = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Attr_head_mod.setAlignment(QtCore.Qt.AlignCenter)
        self.Attr_head_mod.setObjectName("Attr_head_mod")
        self.attr_dex_val = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.attr_dex_val.setMinimumSize(QtCore.QSize(0, 23))
        self.attr_dex_val.setObjectName("attr_dex_val")
        self.attr_head_temp_mod = QtWidgets.QLabel(self.gridLayoutWidget)
        self.attr_head_temp_mod.setMinimumSize(QtCore.QSize(0, 20))
        self.attr_head_temp_mod.setMaximumSize(QtCore.QSize(16777215, 20))
        self.attr_head_temp_mod.setAlignment(QtCore.Qt.AlignCenter)
        self.attr_head_temp_mod.setWordWrap(True)
        self.attr_head_temp_mod.setObjectName("attr_head_temp_mod")
        self.attr_dex_label = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.attr_dex_label.sizePolicy().hasHeightForWidth())
        self.attr_dex_label.setSizePolicy(sizePolicy)
        self.attr_dex_label.setMinimumSize(QtCore.QSize(40, 0))
        self.attr_dex_label.setBaseSize(QtCore.QSize(10, 0))
        self.attr_dex_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.attr_dex_label.setObjectName("attr_dex_label")
        self.attr_head_temp_val = QtWidgets.QLabel(self.gridLayoutWidget)
        self.attr_head_temp_val.setAlignment(QtCore.Qt.AlignCenter)
        self.attr_head_temp_val.setObjectName("attr_head_temp_val")
        self.attr_con_temp_mod = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.attr_con_temp_mod.setMinimumSize(QtCore.QSize(0, 23))
        self.attr_con_temp_mod.setObjectName("attr_con_temp_mod")
        self.attr_int_temp_mod = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.attr_int_temp_mod.setMinimumSize(QtCore.QSize(0, 23))
        self.attr_int_temp_mod.setObjectName("attr_int_temp_mod")
        self.attr_con_val = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.attr_con_val.setMinimumSize(QtCore.QSize(0, 23))
        self.attr_con_val.setObjectName("attr_con_val")
        self.attr_con_temp_val = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.attr_con_temp_val.setMinimumSize(QtCore.QSize(0, 23))
        self.attr_con_temp_val.setObjectName("attr_con_temp_val")
        self.attr_wis_mod = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.attr_wis_mod.setMinimumSize(QtCore.QSize(0, 23))
        self.attr_wis_mod.setObjectName("attr_wis_mod")
        self.attr_wis_temp_mod = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.attr_wis_temp_mod.setMinimumSize(QtCore.QSize(0, 23))
        self.attr_wis_temp_mod.setObjectName("attr_wis_temp_mod")
        self.attr_wis_temp_val = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.attr_wis_temp_val.setMinimumSize(QtCore.QSize(0, 23))
        self.attr_wis_temp_val.setObjectName("attr_wis_temp_val")
        self.attr_dex_mod = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.attr_dex_mod.setMinimumSize(QtCore.QSize(0, 23))
        self.attr_dex_mod.setObjectName("attr_dex_mod")
        self.attr_dex_temp_val = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.attr_dex_temp_val.setMinimumSize(QtCore.QSize(0, 23))
        self.attr_dex_temp_val.setObjectName("attr_dex_temp_val")
        self.attr_con_label = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.attr_con_label.sizePolicy().hasHeightForWidth())
        self.attr_con_label.setSizePolicy(sizePolicy)
        self.attr_con_label.setMinimumSize(QtCore.QSize(40, 0))
        self.attr_con_label.setBaseSize(QtCore.QSize(10, 0))
        self.attr_con_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.attr_con_label.setObjectName("attr_con_label")
        self.attr_dex_temp_mod = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.attr_dex_temp_mod.setMinimumSize(QtCore.QSize(0, 23))
        self.attr_dex_temp_mod.setObjectName("attr_dex_temp_mod")
        self.attr_wis_val = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.attr_wis_val.setMinimumSize(QtCore.QSize(0, 23))
        self.attr_wis_val.setObjectName("attr_wis_val")
        self.attr_head_val = QtWidgets.QLabel(self.gridLayoutWidget)
        self.attr_head_val.setAlignment(QtCore.Qt.AlignCenter)
        self.attr_head_val.setObjectName("attr_head_val")
        self.attr_int_temp_val = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.attr_int_temp_val.setMinimumSize(QtCore.QSize(0, 23))
        self.attr_int_temp_val.setObjectName("attr_int_temp_val")
        self.attr_int_mod = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.attr_int_mod.setMinimumSize(QtCore.QSize(0, 23))
        self.attr_int_mod.setObjectName("attr_int_mod")
        self.attr_int_val = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.attr_int_val.setMinimumSize(QtCore.QSize(0, 23))
        self.attr_int_val.setObjectName("attr_int_val")
        self.attr_wis_label = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.attr_wis_label.sizePolicy().hasHeightForWidth())
        self.attr_wis_label.setSizePolicy(sizePolicy)
        self.attr_wis_label.setMinimumSize(QtCore.QSize(40, 0))
        self.attr_wis_label.setBaseSize(QtCore.QSize(10, 0))
        self.attr_wis_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.attr_wis_label.setObjectName("attr_wis_label")
        self.attr_str_temp_mod = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.attr_str_temp_mod.setObjectName("attr_str_temp_mod")
        self.AttributesLayout.addWidget(self.attr_str_temp_mod, 1, 4, 1, 1)
        self.attr_str_label = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.attr_str_label.sizePolicy().hasHeightForWidth())
        self.attr_str_label.setSizePolicy(sizePolicy)
        self.attr_str_label.setMinimumSize(QtCore.QSize(40, 0))
        self.attr_str_label.setBaseSize(QtCore.QSize(10, 0))
        self.attr_str_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.attr_str_label.setObjectName("attr_str_label")
        self.attr_str_mod = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.attr_str_mod.setMinimumSize(QtCore.QSize(0, 23))
        self.attr_str_mod.setObjectName("attr_str_mod")
        self.attr_str_temp_val = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.attr_str_temp_val.setMinimumSize(QtCore.QSize(0, 23))
        self.attr_str_temp_val.setObjectName("attr_str_temp_val")
        self.attr_cha_label = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.attr_cha_label.sizePolicy().hasHeightForWidth())
        self.attr_cha_label.setSizePolicy(sizePolicy)
        self.attr_cha_label.setMinimumSize(QtCore.QSize(40, 0))
        self.attr_cha_label.setBaseSize(QtCore.QSize(10, 0))
        self.attr_cha_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.attr_cha_label.setObjectName("attr_cha_label")
        self.attr_cha_val = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.attr_cha_val.setMinimumSize(QtCore.QSize(0, 23))
        self.attr_cha_val.setObjectName("attr_cha_val")
        self.attr_cha_mod = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.attr_cha_mod.setMinimumSize(QtCore.QSize(0, 23))
        self.attr_cha_mod.setObjectName("attr_cha_mod")
        self.attr_cha_temp_val = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.attr_cha_temp_val.setMinimumSize(QtCore.QSize(0, 23))
        self.attr_cha_temp_val.setObjectName("attr_cha_temp_val")
        self.attr_cha_temp_mod = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.attr_cha_temp_mod.setMinimumSize(QtCore.QSize(0, 23))
        self.attr_cha_temp_mod.setObjectName("attr_cha_temp_mod")

        self.AttributesLayout.addWidget(self.attr_str_val, 1, 1, 1, 1)
        self.AttributesLayout.addWidget(self.attr_head_name, 0, 0, 1, 1)
        self.AttributesLayout.addWidget(self.attr_int_label, 4, 0, 1, 1)
        self.AttributesLayout.addWidget(self.attr_con_mod, 3, 2, 1, 1)
        self.AttributesLayout.addWidget(self.Attr_head_mod, 0, 2, 1, 1)
        self.AttributesLayout.addWidget(self.attr_dex_val, 2, 1, 1, 1)
        self.AttributesLayout.addWidget(self.attr_head_temp_mod, 0, 4, 1, 1)
        self.AttributesLayout.addWidget(self.attr_dex_label, 2, 0, 1, 1)
        self.AttributesLayout.addWidget(self.attr_head_temp_val, 0, 3, 1, 1)
        self.AttributesLayout.addWidget(self.attr_con_temp_mod, 3, 4, 1, 1)
        self.AttributesLayout.addWidget(self.attr_int_temp_mod, 4, 4, 1, 1)
        self.AttributesLayout.addWidget(self.attr_con_val, 3, 1, 1, 1)
        self.AttributesLayout.addWidget(self.attr_con_temp_val, 3, 3, 1, 1)
        self.AttributesLayout.addWidget(self.attr_wis_mod, 5, 2, 1, 1)
        self.AttributesLayout.addWidget(self.attr_wis_temp_mod, 5, 4, 1, 1)
        self.AttributesLayout.addWidget(self.attr_wis_temp_val, 5, 3, 1, 1)
        self.AttributesLayout.addWidget(self.attr_dex_mod, 2, 2, 1, 1)
        self.AttributesLayout.addWidget(self.attr_dex_temp_val, 2, 3, 1, 1)
        self.AttributesLayout.addWidget(self.attr_con_label, 3, 0, 1, 1)
        self.AttributesLayout.addWidget(self.attr_dex_temp_mod, 2, 4, 1, 1)
        self.AttributesLayout.addWidget(self.attr_wis_val, 5, 1, 1, 1)
        self.AttributesLayout.addWidget(self.attr_head_val, 0, 1, 1, 1)
        self.AttributesLayout.addWidget(self.attr_int_temp_val, 4, 3, 1, 1)
        self.AttributesLayout.addWidget(self.attr_int_mod, 4, 2, 1, 1)
        self.AttributesLayout.addWidget(self.attr_int_val, 4, 1, 1, 1)
        self.AttributesLayout.addWidget(self.attr_wis_label, 5, 0, 1, 1)
        self.AttributesLayout.addWidget(self.attr_str_label, 1, 0, 1, 1)
        self.AttributesLayout.addWidget(self.attr_str_mod, 1, 2, 1, 1)
        self.AttributesLayout.addWidget(self.attr_str_temp_val, 1, 3, 1, 1)
        self.AttributesLayout.addWidget(self.attr_cha_label, 6, 0, 1, 1)
        self.AttributesLayout.addWidget(self.attr_cha_val, 6, 1, 1, 1)
        self.AttributesLayout.addWidget(self.attr_cha_mod, 6, 2, 1, 1)
        self.AttributesLayout.addWidget(self.attr_cha_temp_val, 6, 3, 1, 1)
        self.AttributesLayout.addWidget(self.attr_cha_temp_mod, 6, 4, 1, 1)

    def create_basic_info_box(self, palette):
        self.BasicInfoBox = QtWidgets.QGroupBox(self.centralwidget)
        self.BasicInfoBox.setGeometry(QtCore.QRect(10, 0, 811, 201))
        self.BasicInfoBox.setObjectName("BasicInfoBox")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.BasicInfoBox)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 791, 162))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.BasicInfoLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.BasicInfoLayout.setContentsMargins(9, 9, 9, 9)
        self.BasicInfoLayout.setSpacing(6)
        self.BasicInfoLayout.setObjectName("BasicInfoLayout")
        self.character_class_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.character_class_label.setMinimumSize(QtCore.QSize(178, 16))
        self.character_class_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.character_class_label.setIndent(-1)
        self.character_class_label.setObjectName("character_class_label")
        self.character_faith_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.character_faith_label.setMinimumSize(QtCore.QSize(178, 16))
        self.character_faith_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.character_faith_label.setIndent(-1)
        self.character_faith_label.setObjectName("character_faith_label")
        self.character_race_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.character_race_label.setMinimumSize(QtCore.QSize(177, 16))
        self.character_race_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.character_race_label.setIndent(-1)
        self.character_race_label.setObjectName("character_race_label")
        self.character_alignement_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.character_alignement_label.setMinimumSize(QtCore.QSize(178, 16))
        self.character_alignement_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.character_alignement_label.setIndent(-1)
        self.character_alignement_label.setObjectName("character_alignement_label")
        self.character_race = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.character_race.setMinimumSize(QtCore.QSize(177, 23))
        self.character_race.setPalette(palette)
        self.character_race.setAlignment(QtCore.Qt.AlignCenter)
        self.character_race.setObjectName("character_race")
        self.character_alignement = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.character_alignement.setMinimumSize(QtCore.QSize(178, 23))
        self.character_alignement.setPalette(palette)
        self.character_alignement.setAlignment(QtCore.Qt.AlignCenter)
        self.character_alignement.setObjectName("character_alignement")
        self.character_class = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.character_class.setMinimumSize(QtCore.QSize(178, 23))
        self.character_class.setPalette(palette)
        self.character_class.setAlignment(QtCore.Qt.AlignCenter)
        self.character_class.setObjectName("character_class")
        self.character_faith = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.character_faith.setMinimumSize(QtCore.QSize(178, 23))
        self.character_faith.setPalette(palette)
        self.character_faith.setAlignment(QtCore.Qt.AlignCenter)
        self.character_faith.setObjectName("character_faith")
        self.character_name_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.character_name_label.setIndent(-1)
        self.character_name_label.setObjectName("character_name_label")
        self.character_name = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.character_name.setMinimumSize(QtCore.QSize(0, 23))
        self.character_name.setPalette(palette)
        self.character_name.setObjectName("character_name")
        self.player_name_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.player_name_label.setIndent(-1)
        self.player_name_label.setObjectName("player_name_label")
        self.character_height_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.character_height_label.setMinimumSize(QtCore.QSize(86, 15))
        self.character_height_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.character_height_label.setIndent(-1)
        self.character_height_label.setObjectName("character_height_label")
        self.character_height = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.character_height.setMinimumSize(QtCore.QSize(86, 23))
        self.character_height.setPalette(palette)
        self.character_height.setAlignment(QtCore.Qt.AlignCenter)
        self.character_height.setObjectName("character_height")
        self.character_weight_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.character_weight_label.setMinimumSize(QtCore.QSize(86, 15))
        self.character_weight_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.character_weight_label.setIndent(-1)
        self.character_weight_label.setObjectName("character_weight_label")
        self.character_weight = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.character_weight.setMinimumSize(QtCore.QSize(86, 23))
        self.character_weight.setPalette(palette)
        self.character_weight.setAlignment(QtCore.Qt.AlignCenter)
        self.character_weight.setObjectName("character_weight")
        self.character_eyes_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.character_eyes_label.setMinimumSize(QtCore.QSize(86, 15))
        self.character_eyes_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.character_eyes_label.setIndent(-1)
        self.character_eyes_label.setObjectName("character_eyes_label")
        self.character_hair = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.character_hair.setMinimumSize(QtCore.QSize(86, 23))
        self.character_hair.setPalette(palette)
        self.character_hair.setAlignment(QtCore.Qt.AlignCenter)
        self.character_hair.setObjectName("character_hair")
        self.player_name = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.player_name.setMinimumSize(QtCore.QSize(0, 23))
        self.player_name.setPalette(palette)
        self.player_name.setObjectName("player_name")
        self.character_eyes = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.character_eyes.setMinimumSize(QtCore.QSize(86, 23))
        self.character_eyes.setPalette(palette)
        self.character_eyes.setAlignment(QtCore.Qt.AlignCenter)
        self.character_eyes.setObjectName("character_eyes")
        self.character_hair_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.character_hair_label.setMinimumSize(QtCore.QSize(86, 15))
        self.character_hair_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.character_hair_label.setIndent(-1)
        self.character_hair_label.setObjectName("character_hair_label")
        self.character_gender = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.character_gender.setMinimumSize(QtCore.QSize(85, 23))
        self.character_gender.setPalette(palette)
        self.character_gender.setAlignment(QtCore.Qt.AlignCenter)
        self.character_gender.setObjectName("character_gender")
        self.character_age = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.character_age.setMinimumSize(QtCore.QSize(86, 23))
        self.character_age.setPalette(palette)
        self.character_age.setAlignment(QtCore.Qt.AlignCenter)
        self.character_age.setObjectName("character_age")
        self.character_size_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.character_size_label.setMinimumSize(QtCore.QSize(86, 15))
        self.character_size_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.character_size_label.setIndent(-1)
        self.character_size_label.setObjectName("character_size_label")
        self.character_size = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.character_size.setMinimumSize(QtCore.QSize(86, 23))
        self.character_size.setPalette(palette)
        self.character_size.setAlignment(QtCore.Qt.AlignCenter)
        self.character_size.setObjectName("character_size")
        self.character_age_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.character_age_label.setMinimumSize(QtCore.QSize(86, 15))
        self.character_age_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.character_age_label.setIndent(-1)
        self.character_age_label.setObjectName("character_age_label")
        self.character_gender_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.character_gender_label.setMinimumSize(QtCore.QSize(85, 15))
        self.character_gender_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.character_gender_label.setIndent(-1)
        self.character_gender_label.setObjectName("character_gender_label")
        self.character_level = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.character_level.setMinimumSize(QtCore.QSize(86, 23))
        self.character_level.setPalette(palette)
        self.character_level.setAlignment(QtCore.Qt.AlignCenter)
        self.character_level.setObjectName("character_level")
        self.character_level_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.character_level_label.setMinimumSize(QtCore.QSize(86, 15))
        self.character_level_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.character_level_label.setIndent(-1)
        self.character_level_label.setObjectName("character_level_label")

        self.BasicInfoLayout.addWidget(self.character_class_label, 2, 0, 1, 2)
        self.BasicInfoLayout.addWidget(self.character_faith_label, 2, 6, 1, 2)
        self.BasicInfoLayout.addWidget(self.character_race_label, 2, 2, 1, 2)
        self.BasicInfoLayout.addWidget(self.character_alignement_label, 2, 4, 1, 2)
        self.BasicInfoLayout.addWidget(self.character_race, 3, 2, 1, 2)
        self.BasicInfoLayout.addWidget(self.character_alignement, 3, 4, 1, 2)
        self.BasicInfoLayout.addWidget(self.character_class, 3, 0, 1, 2)
        self.BasicInfoLayout.addWidget(self.character_faith, 3, 6, 1, 2)
        self.BasicInfoLayout.addWidget(self.character_name_label, 0, 0, 1, 4)
        self.BasicInfoLayout.addWidget(self.character_name, 1, 0, 1, 4)
        self.BasicInfoLayout.addWidget(self.player_name_label, 0, 4, 1, 4)
        self.BasicInfoLayout.addWidget(self.character_height_label, 4, 4, 1, 1)
        self.BasicInfoLayout.addWidget(self.character_height, 5, 4, 1, 1)
        self.BasicInfoLayout.addWidget(self.character_weight_label, 4, 5, 1, 1)
        self.BasicInfoLayout.addWidget(self.character_weight, 5, 5, 1, 1)
        self.BasicInfoLayout.addWidget(self.character_eyes_label, 4, 6, 1, 1)
        self.BasicInfoLayout.addWidget(self.character_hair, 5, 7, 1, 1)
        self.BasicInfoLayout.addWidget(self.player_name, 1, 4, 1, 4)
        self.BasicInfoLayout.addWidget(self.character_eyes, 5, 6, 1, 1)
        self.BasicInfoLayout.addWidget(self.character_hair_label, 4, 7, 1, 1)
        self.BasicInfoLayout.addWidget(self.character_gender, 5, 3, 1, 1)
        self.BasicInfoLayout.addWidget(self.character_age, 5, 2, 1, 1)
        self.BasicInfoLayout.addWidget(self.character_size_label, 4, 1, 1, 1)
        self.BasicInfoLayout.addWidget(self.character_size, 5, 1, 1, 1)
        self.BasicInfoLayout.addWidget(self.character_age_label, 4, 2, 1, 1)
        self.BasicInfoLayout.addWidget(self.character_gender_label, 4, 3, 1, 1)
        self.BasicInfoLayout.addWidget(self.character_level, 5, 0, 1, 1)
        self.BasicInfoLayout.addWidget(self.character_level_label, 4, 0, 1, 1)

    def retranslate_ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "ClickMe"))

        self.translate_basic_info_box(_translate)
        self.translate_attributes_box(_translate)
        self.translate_menu_bar(_translate)

    def translate_menu_bar(self, _translate):
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionNew_character.setText(_translate("MainWindow", "New character..."))
        self.actionOpen_character.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

    def translate_basic_info_box(self, _translate):
        self.BasicInfoBox.setTitle(_translate("MainWindow", "Basic Info"))
        self.character_class_label.setText(_translate("MainWindow", "Class"))
        self.character_faith_label.setText(_translate("MainWindow", "Faith"))
        self.character_race_label.setText(_translate("MainWindow", "Race"))
        self.character_alignement_label.setText(_translate("MainWindow", "Alignement"))
        self.character_race.setText(_translate("MainWindow", "Lorem ipsum"))
        self.character_alignement.setText(_translate("MainWindow", "Lorem ipsum"))
        self.character_class.setText(_translate("MainWindow", "Lorem ipsum"))
        self.character_faith.setText(_translate("MainWindow", "Lorem ipsum"))
        self.character_name_label.setText(_translate("MainWindow", "Character name"))
        self.character_name.setText(_translate("MainWindow", "Lorem ipsum"))
        self.player_name_label.setText(_translate("MainWindow", "Player name"))
        self.character_height_label.setText(_translate("MainWindow", "Height"))
        self.character_height.setText(_translate("MainWindow", "10"))
        self.character_weight_label.setText(_translate("MainWindow", "Weight"))
        self.character_weight.setText(_translate("MainWindow", "10"))
        self.character_eyes_label.setText(_translate("MainWindow", "Eyes"))
        self.character_hair.setText(_translate("MainWindow", "Lorem ipsum"))
        self.player_name.setText(_translate("MainWindow", "Lorem ipsum"))
        self.character_eyes.setText(_translate("MainWindow", "Lorem ipsum"))
        self.character_hair_label.setText(_translate("MainWindow", "Hair"))
        self.character_gender.setText(_translate("MainWindow", "Lorem ipsum"))
        self.character_age.setText(_translate("MainWindow", "10"))
        self.character_size_label.setText(_translate("MainWindow", "Size"))
        self.character_size.setText(_translate("MainWindow", "Lorem ipsum"))
        self.character_age_label.setText(_translate("MainWindow", "Age"))
        self.character_gender_label.setText(_translate("MainWindow", "Gender"))
        self.character_level.setText(_translate("MainWindow", "10"))
        self.character_level_label.setText(_translate("MainWindow", "Level"))

    def translate_attributes_box(self, _translate):
        self.AttributesBox.setTitle(_translate("MainWindow", "Attributes"))
        self.attr_str_val.setText(_translate("MainWindow", "10"))
        self.attr_head_name.setText(_translate("MainWindow", "Atrribute"))
        self.attr_int_label.setText(_translate("MainWindow", "INT"))
        self.attr_con_mod.setText(_translate("MainWindow", "10"))
        self.Attr_head_mod.setText(_translate("MainWindow", "Mod"))
        self.attr_dex_val.setText(_translate("MainWindow", "10"))
        self.attr_head_temp_mod.setText(_translate("MainWindow", "Temp mod"))
        self.attr_dex_label.setText(_translate("MainWindow", "DEX"))
        self.attr_head_temp_val.setText(_translate("MainWindow", "Temp val"))
        self.attr_con_temp_mod.setText(_translate("MainWindow", "10"))
        self.attr_int_temp_mod.setText(_translate("MainWindow", "10"))
        self.attr_con_val.setText(_translate("MainWindow", "10"))
        self.attr_con_temp_val.setText(_translate("MainWindow", "10"))
        self.attr_wis_mod.setText(_translate("MainWindow", "10"))
        self.attr_wis_temp_mod.setText(_translate("MainWindow", "10"))
        self.attr_wis_temp_val.setText(_translate("MainWindow", "10"))
        self.attr_dex_mod.setText(_translate("MainWindow", "10"))
        self.attr_dex_temp_val.setText(_translate("MainWindow", "10"))
        self.attr_con_label.setText(_translate("MainWindow", "CON"))
        self.attr_dex_temp_mod.setText(_translate("MainWindow", "10"))
        self.attr_wis_val.setText(_translate("MainWindow", "10"))
        self.attr_head_val.setText(_translate("MainWindow", "Value"))
        self.attr_int_temp_val.setText(_translate("MainWindow", "10"))
        self.attr_int_mod.setText(_translate("MainWindow", "10"))
        self.attr_int_val.setText(_translate("MainWindow", "10"))
        self.attr_wis_label.setText(_translate("MainWindow", "WIS"))
        self.attr_str_temp_mod.setText(_translate("MainWindow", "10"))
        self.attr_str_label.setText(_translate("MainWindow", "STR"))
        self.attr_str_mod.setText(_translate("MainWindow", "10"))
        self.attr_str_temp_val.setText(_translate("MainWindow", "10"))
        self.attr_cha_label.setText(_translate("MainWindow", "CHA"))
        self.attr_cha_val.setText(_translate("MainWindow", "10"))
        self.attr_cha_mod.setText(_translate("MainWindow", "10"))
        self.attr_cha_temp_val.setText(_translate("MainWindow", "10"))
        self.attr_cha_temp_mod.setText(_translate("MainWindow", "10"))


    def create_palette(self):
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        return palette
