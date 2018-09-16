from Character.Attacks.ranged_attack import RangedAttack
from Character.attributes import Attributes


class TestAttack:

    def test_without_mods(self):
        attack = RangedAttack()
        assert attack.complete == 0
    
    def test_with_attributes(self):
        attr = Attributes({"dex": 14})
        attack = RangedAttack(attributes=attr)

        assert attack.complete == 2

    def test_with_base_mod(self):
        attack = RangedAttack(base_mod=2)
        assert attack.complete == 2

    def test_with_misc_mod(self):
        attack = RangedAttack(misc_bonus=4)
        assert attack.complete == 4

    def test_size_mod(self):
        attack = RangedAttack(size_bonus=3)
        assert attack.complete == 3

    def test_with_attributes_and_base_mod(self):
        attr = Attributes({"dex": 14})
        attack = RangedAttack(attributes=attr, base_mod=3)
        assert attack.complete == 5

    def test_with_misc_and_size_mod(self):
        attack = RangedAttack(misc_bonus=3, size_bonus=2)
        assert attack.complete == 5

    def test_attributes_value_changes(self):
        attr = Attributes({"dex": 14})
        attack = RangedAttack(attributes=attr, base_mod=3)
        assert attack.complete == 5
        attr.dex = 12
        assert attack.complete == 4

    def test_attributes_changes(self):
        attr = Attributes({"dex": 14})
        attack = RangedAttack(attributes=attr, base_mod=3)
        assert attack.complete == 5
        attack.attack_attribute = 'str'
        assert attack.complete == 3

    def test_all_at_once(self):
        attr = Attributes({"dex": 14})
        attack = RangedAttack(attributes=attr, base_mod=3, misc_bonus=2, size_bonus=1)
        assert attack.complete == 8
