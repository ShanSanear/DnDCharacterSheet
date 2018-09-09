from item import Item
from item_exceptions import IncorrectWeaponType, IncorrectAttackRange, IncorrectDamage, IncorrectCritical
import re

DICE_RE = re.compile(r'(?P<count>\d{1,2})([kK]|[dD])(?P<dice>\d{1,3})$')
CRITICAL_RE = re.compile(r'((?P<low_range>\d{2})-(?P<high_range>\d{2}))?/?([xX](?P<multiplier>\d))$')
weapon_types = ('ranged', 'melee')



class Weapon(Item):
    def __init__(self, name='', weapon_type='melee', damage='1d4',
                 critical='x2', attack_range=0, weight=0, description=''):
        super().__init__(name=name, weight=weight, category='weapon', description=description)

        self.min_damage = 0
        self.max_damage = 0
        damage_match = re.match(DICE_RE, damage)
        if not damage_match:
            raise IncorrectDamage("Incorrect damage passed: {}".format(damage))
        else:
            self.fill_damage_range(damage_match)

        if attack_range < 0 or (attack_range == 0 and weapon_type == 'ranged'):
            raise IncorrectAttackRange("Incorrect range: {} for weapon type: {}".format(attack_range, weapon_type))

        if weapon_type not in weapon_types:
            raise IncorrectWeaponType("Invalid weapon type: {}".format(weapon_type))

        self.critical_multiplier = 0
        self.critical_range = (20, 20)

        crit_match = re.match(CRITICAL_RE, critical)
        if crit_match:
            self.fill_critical_range(crit_match)
        else:
            raise IncorrectCritical("Incorrect critical value passed: {}".format(critical))

        self.type = weapon_type
        self.range = attack_range

    def fill_damage_range(self, match):
        self.min_damage = int(match['count'])
        self.max_damage = int(match['dice']) * int(match['count'])

    @property
    def get_weapon_damage(self):
        return {"min": self.min_damage, "max": self.max_damage}

    def fill_critical_range(self, match):
        self.critical_multiplier = int(match['multiplier'])
        try:
            self.critical_range = (int(match['low_range']), int(match['high_range']))
        except TypeError:
            pass

    damage = get_weapon_damage
