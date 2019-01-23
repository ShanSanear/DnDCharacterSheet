from core.attacks.melee_attack import MeleeAttack
from core.attacks.ranged_attack import RangedAttack
from core.attributes import Attributes
from core.character_basic_info import CharacterBasicInfo
from core.items import Equipment
from core.saving_throws import SavingThrows


class Character(CharacterBasicInfo):

    def __init__(self, name):
        CharacterBasicInfo.__init__(self)
        self.name = name
        self.attributes = Attributes()
        self.saving_throws = SavingThrows(self.attributes)
        self.melee_attack = MeleeAttack(self.attributes)

