import pytest

from weapons import *


class TestWeapons:
    def test_weapon_name(self):
        weapon = Weapon(name="Test_name")
        assert weapon.name == "Test_name"

    def test_weapon_category(self):
        weapon = Weapon(weight=0, )
        assert weapon.category == 'weapon'

    def test_ranged_weapon_type(self):
        weapon = Weapon(weapon_type='ranged', attack_range=1)
        assert weapon.type == 'ranged'

    def test_incorrect_weapon_type(self):
        with pytest.raises(IncorrectWeaponType):
            Weapon(name='', weapon_type='omnomnomnom')

    def test_ranged_weapon_without_range(self):
        with pytest.raises(IncorrectAttackRange):
            Weapon(name='', weapon_type='ranged', attack_range=0)

    def test_weapon_damage(self):
        weapon = Weapon(damage='1d6')
        assert weapon.damage == {"min": 1, "max": 6}
        weapon = Weapon(damage='2d6')
        assert weapon.damage == {"min": 2, "max": 12}
        weapon = Weapon(damage='3K4')
        assert weapon.damage == {"min": 3, "max": 12}

    def test_inccorect_weapon_damage(self):
        with pytest.raises(IncorrectDamage):
            Weapon(damage='1s6')

    def test_cant_change_damage(self):
        with pytest.raises(AttributeError):
            weapon = Weapon(damage='1d6')
            weapon.damage = {'min': 3, 'max': 8}

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

