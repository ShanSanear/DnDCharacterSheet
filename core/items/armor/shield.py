from core.items.armor import Armor


class Shield(Armor):
    def __init__(self, name='', shield_bonus=0, magic_shield_bonus=0, max_dex_bonus=0,
                 test_penalty=0, magic_penalty=0, weight=0, description=''):
        super(Shield, self).__init__(name=name, bonus=shield_bonus, magic_penalty=magic_penalty,
                                     magic_bonus=magic_shield_bonus, max_dex_bonus=max_dex_bonus,
                                     test_penalty=test_penalty, weight=weight, description=description)

        self.shield_bonus = self.bonus
        self.magic_shield_bonus = self.magic_bonus
