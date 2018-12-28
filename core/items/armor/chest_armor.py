from core.items.armor import Armor
from possible_exceptions import IncorrectArmorType

possible_armor_types = ('light', 'medium', 'heavy')


class ChestArmor(Armor):
    def __init__(self, name='', armor_bonus=0, magic_armor_bonus=0, max_dex_bonus=0, armor_type='light', test_penalty=0, cost=0,
                 magic_penalty=0, weight=0, description=''):
        super(ChestArmor, self).__init__(name=name, cost=cost, bonus=armor_bonus, magic_penalty=magic_penalty,
                                         magic_bonus=magic_armor_bonus, max_dex_bonus=max_dex_bonus,
                                         test_penalty=test_penalty, weight=weight, description=description)
        self.armor_bonus = self.bonus
        self.magic_armor_bonus = self.magic_bonus
        if armor_type not in possible_armor_types:
            raise IncorrectArmorType("Incorrect armor type: {}".format(armor_type))
        else:
            self.armor_type = armor_type
