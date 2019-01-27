from core.attacks.melee_attack import MeleeAttack
from core.attacks.ranged_attack import RangedAttack
from core.attributes import Attributes
from core.saving_throws import SavingThrows
from core.skills import Skill


class Character:

    def __init__(self, name):
        self.name = name
        self.attributes = Attributes()
        self.saving_throws = SavingThrows(self.attributes)
        self.melee_attack = MeleeAttack(self.attributes)
        self.ranged_attack = RangedAttack(self.attributes)
        self.skills = []
        #self.equipement = Equipment()
        #self.spell_book = SpellBook()
        #self.spells_dc = SpellsDc(attr_cls=self.attributes)
        #self.spells_per_day = SpellsPerDay(attr_cls=self.attributes)
        #self.remembered_spells = RememberedSpells(spell_book=self.spell_book)
        #self.known_spells = KnownSpells()
        # TODO - those elements above COULD be based on backend api - in the long run, not now

    def add_new_skill(self, **kwargs):
        self.skills.append(Skill(attr_cls=self.attributes, **kwargs))



