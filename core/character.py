from core.attacks.melee_attack import MeleeAttack
from core.attacks.ranged_attack import RangedAttack
from core.attributes import Attributes
from core.character_basic_info import CharacterBasicInfo
from core.items import Equipment
from core.saving_throws import SavingThrows
from core.spells.known_spells import KnownSpells
from core.spells.remembered_spells import RememberedSpells
from core.spells.spell_book import SpellBook
from core.spells.spells_dc import SpellsDc
from core.spells.spells_per_day import SpellsPerDay


class Character(CharacterBasicInfo):

    def __init__(self, name):
        CharacterBasicInfo.__init__(self)
        self.name = name
        self.attributes = Attributes()
        self.saving_throws = SavingThrows(self.attributes)
        self.melee_attack = MeleeAttack(self.attributes)
        self.ranged_attack = RangedAttack(self.attributes)
        self.equipement = Equipment()
        self.spell_book = SpellBook()
        self.spells_dc = SpellsDc()
        self.spells_per_day = SpellsPerDay()
        self.remembered_spells = RememberedSpells()
        self.known_spells = KnownSpells()

