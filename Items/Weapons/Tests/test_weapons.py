import pytest

from Items.Weapons.weapons import *

from possible_exceptions import *


class TestWeapons:
    def test_weapon_name(self):
        weapon = Weapon(name="Test_name")
        assert weapon.name == "Test_name"

    def test_weapon_category(self):
        weapon = Weapon(weight=0)
        assert weapon.category == 'weapon'

    def test_weapon_damage(self):
        weapon = Weapon(damage='1d6')
        assert weapon.damage == {"min": 1, "max": 6}
        weapon = Weapon(damage='2d6')
        assert weapon.damage == {"min": 2, "max": 12}
        weapon = Weapon(damage='3K4')
        assert weapon.damage == {"min": 3, "max": 12}
        weapon = Weapon(damage='2D6')
        assert weapon.damage == {"min": 2, "max": 12}
        weapon = Weapon(damage='2k4+1')
        assert weapon.damage == {'min': 3, "max": 9}

    def test_inccorect_weapon_damage(self):
        with pytest.raises(IncorrectDamage):
            Weapon(damage='1s6')

        with pytest.raises(IncorrectDamage):
            Weapon(damage='1k4+')

        with pytest.raises(IncorrectDamage):
            Weapon(damage='4w8+')

    def test_change_weapon_damage(self):
        wep = Weapon(damage='1k8')
        assert wep.damage == {'min': 1, 'max': 8}
        wep.damage = '1k12+1'
        assert wep.damage == {'min': 2, 'max': 13}

    def test_wrong_change_weapon_damage(self):
        wep = Weapon(damage="1k12")
        with pytest.raises(IncorrectDamage):
            wep.damage = '1k8x'

    def test_critical_range(self):
        weapon = Weapon(critical='x3')
        assert weapon.critical_multiplier == 3
        assert weapon.critical_range == (20, 20)
        weapon = Weapon(critical='18-20/X2')
        assert weapon.critical_multiplier == 2
        assert weapon.critical_range == (18, 20)
        weapon = Weapon(critical='19-20/x3')
        assert weapon.critical_multiplier == 3
        assert weapon.critical_range == (19, 20)
        weapon = Weapon(critical='17-20x2')
        assert weapon.critical_multiplier == 2
        assert weapon.critical_range == (17, 20)

    def test_incorrect_critical_range(self):
        with pytest.raises(IncorrectCritical):
            Weapon(critical='1-10x12')
        with pytest.raises(IncorrectCritical):
            Weapon(critical='x12')

    def test_weapon_description(self):
        weapon = Weapon(description="DESC")
        assert weapon.description == "DESC"

    def test_weapon_cost(self):
        weapon = Weapon(cost=1)
        assert weapon.cost == 1
