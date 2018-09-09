from Items.Weapons.weapons import Weapon
from possible_exceptions import *

possible_ammo = ('belt', 'arrow', 'rock', 'bullets')


class MissleWeapon(Weapon):
    def __init__(self, name='', damage='1d4', critical='x2', attack_range=1, weight=0, description='', cost=0,
                 ammo_type='belt', ammo_count=10):

        if "slingshot" in name or "Slingshot" in name:
            self.handling = '1h'
        else:
            self.handling = '2h'

        if ammo_type not in possible_ammo:
            raise IncorrectAmmoType("Incorrect ammo type. Passed ammo type: {}".format(ammo_type))
        else:
            self.ammo_type = ammo_type

        if attack_range <= 0:
            raise IncorrectAttackRange("Negative attack range for ranged weapon. "
                                       "Weapon range passed: {}".format(attack_range))

        if ammo_count < 0:
            raise NegativeAmmoCount("Negative ammo count. Ammo count passed: {}".format(ammo_count))
        else:
            self.ammo_count = ammo_count

        super(MissleWeapon, self).__init__(name=name, damage=damage, critical=critical, attack_range=attack_range,
                                           weight=weight, description=description, cost=cost)

    def shot(self, shots):
        self.ammo_count -= shots
