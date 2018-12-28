import pytest

from possible_exceptions import *
from .. import Armor

class TestArmor:
    def test_armor_name(self):
        ar = Armor(name="DUMMY_NAME")
        assert ar.name == "DUMMY_NAME"

    def test_armor_description(self):
        ar = Armor(description="DUMMY_DESCRIPTION")
        assert ar.description == "DUMMY_DESCRIPTION"

    def test_armor_weight(self):
        ar = Armor(weight=1)
        assert ar.weight == 1

    def test_armor_bonus_ac(self):
        ar = Armor(bonus=4)
        assert ar.bonus == 4

    def test_armor_magical_bonus_ac(self):
        ar = Armor(bonus=4, magic_bonus=1)
        assert ar.raw_bonus == 4
        assert ar.bonus == 5
        assert ar.magic_bonus == 1

    def test_negative_ac(self):
        with pytest.raises(NegativeArmorBonus):
            Armor(bonus=-1)

    def test_armor_test_penalty(self):
        ar = Armor(test_penalty=3)
        assert ar.test_penalty == 3

    def test_armor_magic_penalty(self):
        ar = Armor(magic_penalty=10)
        assert ar.magic_penalty == 10

    def test_max_dex_bonus(self):
        ar = Armor(max_dex_bonus=4)
        assert ar.max_dex_bonus == 4

    def test_negative_max_dex_bonus(self):
        with pytest.raises(NegativeDexBonus):
            Armor(max_dex_bonus=-1)
