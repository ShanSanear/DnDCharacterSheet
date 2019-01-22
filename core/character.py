from core.attacks.melee_attack import MeleeAttack
from core.attributes import Attributes
from core.character_basic_info import CharacterBasicInfo
from core.saving_throws import SavingThrows


class Character(CharacterBasicInfo):

    def __init__(self, name):
        CharacterBasicInfo.__init__(self)
        self.name = name


    def provide_attributes(self, attributes):
        self.attributes = Attributes(attributes)

    def get_saving_throws(self):
        self.saving_throws = SavingThrows(self.attributes)

    def get_melee_attack(self):
        self.melee_attack = MeleeAttack(self.attributes)

    @property
    def get_melee_attack_value(self):
        return self.melee_attack.complete

    melee_attack_value = get_melee_attack_value
