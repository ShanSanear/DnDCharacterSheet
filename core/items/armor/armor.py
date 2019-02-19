from core.items import Item
from core.exceptions import NegativeArmorBonus, NegativeDexBonus, NegativePenalty

class Armor(Item):
    def __init__(self, name='', bonus=0, magic_bonus=0, max_dex_bonus=0,
                 test_penalty=0, magic_penalty=0, weight=0, description='', cost=0):
        if bonus < 0:
            raise NegativeArmorBonus

        if max_dex_bonus < 0:
            raise NegativeDexBonus

        if test_penalty < 0 or magic_penalty < 0:
            raise NegativePenalty
        super(Armor, self).__init__(name=name, weight=weight, description=description, cost=cost)
        self.max_dex_bonus = max_dex_bonus
        self.raw_bonus = bonus
        self.bonus = bonus + magic_bonus
        self.magic_bonus = magic_bonus
        self.test_penalty = test_penalty
        self.magic_penalty = magic_penalty
