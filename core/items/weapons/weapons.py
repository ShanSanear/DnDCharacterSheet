from core.items import Item
from core.exceptions import IncorrectDamage, IncorrectCritical
from core.patterns import CRITICAL_RE, DICE_RE

import re


class Weapon(Item):
    def __init__(self, name='', damage='1d4',
                 critical='x2', attack_range=0, weight=0, description='', cost=0):
        super().__init__(name=name, weight=weight, category='weapon', description=description, cost=cost)

        self.min_damage = 0
        self.max_damage = 0
        damage_match = re.match(DICE_RE, damage)
        if not damage_match:
            raise IncorrectDamage("Incorrect damage passed: {}".format(damage))
        else:
            self._fill_damage_range(damage_match)

        self.critical_multiplier = 2
        self.critical_range = (20, 20)

        crit_match = re.match(CRITICAL_RE, critical)
        if crit_match:
            self._fill_critical_range(crit_match)
        else:
            raise IncorrectCritical("Incorrect critical value passed: {}".format(critical))

        self.range = attack_range

    def _fill_damage_range(self, match):
        count = int(match['count'])
        dice = int(match['dice'])
        try:
            bonus = int(match['bonus'])
        except TypeError:
            bonus = 0
        self.min_damage = count + bonus
        self.max_damage = dice * count + bonus

    def _get_weapon_damage(self):
        return {"min": self.min_damage, "max": self.max_damage}

    def _set_weapon_damage(self, damage):
        damage_match = re.match(DICE_RE, damage)
        if damage_match:
            self._fill_damage_range(damage_match)
        else:
            raise IncorrectDamage("Incorrect damage passed: {}".format(damage))

    def _fill_critical_range(self, match):
        self.critical_multiplier = int(match['multiplier'])
        try:
            self.critical_range = (int(match['low_range']), int(match['high_range']))
        except TypeError:
            pass

    damage = property(_get_weapon_damage, _set_weapon_damage)
