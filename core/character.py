from core.attacks.melee_attack import MeleeAttack
from core.attributes import Attributes
from core.saving_throws import SavingThrows


class Character:

    def __init__(self, name, player=None, character_class="Fighter", race="Human", faith="", level=1, alignement="NN",
                 size="Medium", age=18, gender="M", height=180, weight=80, eyes="Blue", hair_color="Bronze"):
        self.name = name
        self.player = player
        self.character_class = character_class
        self.race = race
        self.faith = faith
        self.level = level
        self.alignement = alignement
        self.size = size
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.eyes = eyes
        self.hair_color = hair_color

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
