from core.items.weapons.weapons import Weapon
from core.exceptions import LightWeaponCheck, HandlingError
import re
from core.patterns import HANDLING_RE


class MeleeWeapon(Weapon):
    def __init__(self, name='', damage='1d4',
                 critical='x2', attack_range=0, weight=0, description='', cost=0, is_light_weapon=False, handling='2h'):

        super(MeleeWeapon, self).__init__(name=name, damage=damage, critical=critical, attack_range=attack_range,
                                          weight=weight, description=description, cost=cost)
        handling_match = re.match(HANDLING_RE, handling)
        if handling_match:
            self.handling = handling_match['hand'] + 'h'
        else:
            raise HandlingError(
                "Incorrect parameter for handling of the weapon. "
                "Should be [12][rRhH] pattern. Passed handling: {}".format(handling))

        if is_light_weapon not in (True, False):
            raise LightWeaponCheck(
                "is_light_weapon can be either True or False, passed parameter: {}".format(is_light_weapon))
        if self.handling == '2h' and is_light_weapon:
                raise LightWeaponCheck("Light weapons cannot be 2-handed.")
        self.is_light_weapon = is_light_weapon
