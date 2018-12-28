import pytest

from possible_exceptions import *
from ..melee_weapon import *

class TestMeleeWeapon:
        def test_melee_weapon_name(self):
            melee_weapon = MeleeWeapon(name='DUMMY NAME')
            assert melee_weapon.name == "DUMMY NAME"

        def test_weight(self):
            melee_weapon = MeleeWeapon(weight=2)
            assert melee_weapon.weight == 2

        def test_description(self):
            melee_weapon = MeleeWeapon(description="DUMMY DESCRIPTION")
            assert melee_weapon.description == "DUMMY DESCRIPTION"

        def test_cost(self):
            melee_weapon = MeleeWeapon(cost=12)
            assert melee_weapon.cost == 12

        def test_negative_cost(self):
            with pytest.raises(NegativeCost):
                MeleeWeapon(cost=-2)

        def test_negative_weight(self):
            with pytest.raises(NegativeWeight):
                MeleeWeapon(weight=-1)

        def test_damage(self):
            melee_weapon = MeleeWeapon(damage='1k4')
            assert melee_weapon.damage == {'min' : 1, 'max' : 4}
            melee_weapon = MeleeWeapon(damage='1k4+1')
            assert melee_weapon.damage == {'min': 2, 'max': 5}
            melee_weapon = MeleeWeapon(damage='1D6')
            assert melee_weapon.damage == {'min': 1, 'max': 6}
            melee_weapon = MeleeWeapon(damage='1d8+2')
            assert melee_weapon.damage == {'min': 3, 'max': 10}

        def test_incorrect_damage(self):
            with pytest.raises(IncorrectDamage):
                MeleeWeapon(damage='1s8')
            with pytest.raises(IncorrectDamage):
                MeleeWeapon(damage='1k12+')

        def test_light_weapon(self):
            melee_weapon = MeleeWeapon(is_light_weapon=True, handling='1r')
            assert melee_weapon.is_light_weapon
            melee_weapon = MeleeWeapon(is_light_weapon=False)
            assert not melee_weapon.is_light_weapon

        def test_incorrect_argument_light_weapon(self):
            with pytest.raises(LightWeaponCheck):
                MeleeWeapon(is_light_weapon="omnomnomnom")

        def test_light_wepon_two_handed(self):
            with pytest.raises(LightWeaponCheck):
                MeleeWeapon(handling='2R', is_light_weapon=True)
            with pytest.raises(LightWeaponCheck):
                MeleeWeapon(handling='2h', is_light_weapon=True)

        def test_handling(self):
            melee_weapon = MeleeWeapon(handling='1h')
            melee_weapon.handling = '1h'
            melee_weapon = MeleeWeapon(handling='2h')
            melee_weapon.handling = '2h'
            melee_weapon = MeleeWeapon(handling='1R')
            melee_weapon.handling = '1h'
            melee_weapon = MeleeWeapon(handling='2r')
            melee_weapon.handling = '2h'

        def test_incorrect_handling(self):
            with pytest.raises(HandlingError):
                MeleeWeapon(handling='2k4')
