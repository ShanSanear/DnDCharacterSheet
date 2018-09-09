from armor import *


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

    def test_armor_type(self):
        ar = Armor(armor_type='light')
        assert ar.armor_type == 'light'
        ar = Armor(armor_type='heavy')
        assert ar.armor_type == 'heavy'
        ar = Armor(armor_type='medium')
        assert ar.armor_type == 'medium'
        ar = Armor(armor_type='')

    def test_armor_bonus_ac(self):
        ar = Armor(ac=4)
        assert ar.ac == 4

    def test_armor_magical_bonus_ac(self):
        ar = Armor(ac=4, mac=1)
        assert ar.raw_ac == 4
        assert ar.ac == 5
        assert ar.mac == 1

    def test_armor_test_penalty(self):
        ar = Armor(test_penalty=3)
        assert ar.test_penalty == 3

    def test_armor_magic_penalty(self):
        ar = Armor(magic_penalty=10)
        ar.magic_penalty == 10
