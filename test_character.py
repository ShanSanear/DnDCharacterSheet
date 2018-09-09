from character import Character
import pytest


class TestCharacter:
    def test_name(self):

        pc = Character(name="Shan")
        assert pc.name == "Shan"

    def test_attributes(self):
        attributes = {"dex": 12}
        pc = Character(name="Shan", attributes=attributes)
        assert pc.attributes.dex == 12
        assert pc.attributes.dex_mod == 1
