import pytest

from item_exceptions import *

from chest_armor import *


class TestChestArmor:
    def test_chest_armor_name(self):
        chest_ar = ChestArmor(name='DUMMY_NAME')
        assert chest_ar.name == "DUMMY_NAME"

    def test_chest_armor_description(self):
        chest_ar = ChestArmor(description="DUMMY_DESCRIPTION")
        assert chest_ar.description == "DUMMY_DESCRIPTION"

    def test_chest_armor_weight(self):
        chest_ar = ChestArmor(weight=10)
        assert chest_ar.weight == 10

    def test_cost(self):
        chest_ar = ChestArmor(cost=10)
        assert chest_ar.cost == 10

    def test_negative_cost(self):
        with pytest.raises(NegativeCost):
            ChestArmor(cost=-1)

    def test_chest_armor_type(self):
        chest_ar = ChestArmor(armor_type='light')
        assert chest_ar.armor_type == 'light'
        chest_ar = ChestArmor(armor_type='heavy')
        assert chest_ar.armor_type == 'heavy'
        chest_ar = ChestArmor(armor_type='medium')
        assert chest_ar.armor_type == 'medium'

    def test_incorrect_chest_armor_type(self):
        with pytest.raises(IncorrectArmorType):
            ChestArmor(armor_type='olaboga')

    def test_armor_bonus(self):
        chest_ar = ChestArmor(armor_bonus=10)
        assert chest_ar.armor_bonus == 10

    def test_test_penalty(self):
        chest_ar = ChestArmor(test_penalty=10)
        assert chest_ar.test_penalty == 10

    def test_magic_test_penalty(self):
        chest_ar = ChestArmor(magic_penalty=10)
        assert chest_ar.magic_penalty == 10

    def test_negative_penalties(self):
        with pytest.raises(NegativePenalty):
            ChestArmor(test_penalty=-1)
        with pytest.raises(NegativePenalty):
            ChestArmor(magic_penalty=-1)
