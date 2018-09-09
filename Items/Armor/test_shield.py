import pytest

from Items.Armor.shield import *
from possible_exceptions import *


class TestShield:
    def test_shield_name(self):
        sh = Shield(name="DUMMY_NAME")
        assert sh.name == "DUMMY_NAME"

    def test_shield_bonus(self):
        sh = Shield(shield_bonus=10)
        assert sh.shield_bonus == 10

    def test_magic_shield_bonus(self):
        sh = Shield(magic_shield_bonus=10)
        assert sh.magic_shield_bonus == 10

    def test_test_penalty(self):
        sh = Shield(test_penalty=2)
        assert sh.test_penalty == 2

    def test_incorrect_test_penalty(self):
        with pytest.raises(NegativePenalty):
            Shield(test_penalty=-1)
        with pytest.raises(NegativePenalty):
            Shield(magic_penalty=-1)
