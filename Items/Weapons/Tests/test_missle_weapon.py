import pytest

from Items.Weapons.missle_weapon import *

class TestMissleWeapon:
    def test_name(self):
        missle_weapon = MissleWeapon(name='DUMMY NAME')
        assert missle_weapon.name == "DUMMY NAME"

    def test_damage(self):
        missle_weapon = MissleWeapon(damage='1k4')
        assert missle_weapon.damage == {"min" : 1, "max" : 4}

    def test_descritpion(self):
        missle_weapon = MissleWeapon(description='DUMMY DESCRIPTION')
        assert missle_weapon.description == "DUMMY DESCRIPTION"

    def test_critical(self):
        missle_weapon = MissleWeapon(critical='x3')
        assert missle_weapon.critical_multiplier == 3
        assert missle_weapon.critical_range == (20, 20)
        missle_weapon = MissleWeapon(critical='19-20/x3')
        assert missle_weapon.critical_multiplier == 3
        assert missle_weapon.critical_range == (19, 20)

    def test_attack_range(self):
        missle_weapon = MissleWeapon(attack_range=2)
        assert missle_weapon.range == 2
        missle_weapon = MissleWeapon(attack_range=4)
        assert missle_weapon.range == 4

    def test_incorrect_attack_range(self):
        with pytest.raises(IncorrectAttackRange):
            MissleWeapon(attack_range=0)
        with pytest.raises(IncorrectAttackRange):
            MissleWeapon(attack_range=-1)

    def test_weight(self):
        missle_weapon = MissleWeapon(weight=1)
        assert missle_weapon.weight == 1

    def test_cost(self):
        missle_weapon = MissleWeapon(cost=2)
        assert missle_weapon.cost == 2

    def test_ammo_type(self):
        missle_weapon = MissleWeapon(ammo_type='belt')
        assert missle_weapon.ammo_type == 'belt'
        missle_weapon = MissleWeapon(ammo_type='arrow')
        assert missle_weapon.ammo_type == 'arrow'

    def test_incorrect_ammo_type(self):
        with pytest.raises(IncorrectAmmoType):
            MissleWeapon(ammo_type='chickens')

    def test_ammo_count(self):
        missle_weapon = MissleWeapon(ammo_count=20)
        assert missle_weapon.ammo_count == 20
        missle_weapon = MissleWeapon(ammo_count=0)
        assert missle_weapon.ammo_count == 0

    def test_negative_ammo_count(self):
        with pytest.raises(NegativeAmmoCount):
            MissleWeapon(ammo_count=-1)

    def test_decrease_ammo_count(self):
        missle_weapon = MissleWeapon(ammo_count=20)
        missle_weapon.shot(1)
        assert missle_weapon.ammo_count == 19

    def test_handling(self):
        missle_weapon = MissleWeapon(name='Slingshot')
        assert missle_weapon.handling == '1h'
        missle_weapon = MissleWeapon(name='Bow')
        assert missle_weapon.handling == '2h'

