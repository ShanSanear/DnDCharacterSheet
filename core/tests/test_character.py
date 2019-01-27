import pytest

from core.character import Character


class TestCharacter:
    def test_name(self):
        pc = create_pc()
        assert pc.name == "Shan"

    def test_default_values(self):
        pc = create_pc()
        assert pc.name == "Shan"
        # assert pc.player == ""
        # assert pc.character_class == ""
        # assert pc.race == ""
        # assert pc.faith == ""
        # assert pc.level == ""
        # assert pc.alignement == ""
        # assert pc.size == ""
        # assert pc.age == ""
        # assert pc.gender == ""
        # assert pc.height == ""
        # assert pc.weight == ""
        # assert pc.eyes == ""
        # assert pc.hair == ""
        assert pc.attributes.str['value'] == 10

    def test_character_attributes(self):
        attributes = {"dex": 12}
        pc = create_pc()
        pc.attributes.set_attributes(attributes)
        assert pc.attributes.dex == {"value": 12, "mod": 1}

    def test_character_saving_throws(self):
        attributes = {"dex": 12}
        pc = create_pc()
        pc.attributes.set_attributes(attributes)
        assert pc.saving_throws.reflex == 1

    def test_character_saving_throws_with_changes(self):
        attributes = {"dex": 12}
        pc = create_pc()
        pc.attributes.set_attributes(attributes)
        pc.saving_throws.base_mods.reflex = 2
        assert pc.saving_throws.reflex == 3

    def test_melee_attack(self):
        attributes = {"str": 14, "dex": 12}
        pc = create_pc()
        pc.attributes.set_attributes(attributes)
        assert pc.melee_attack.complete == 2

    def test_melee_attack_with_changed_misc(self):
        attributes = {"str": 14, "dex": 12}
        pc = create_pc()
        pc.attributes.set_attributes(attributes)
        pc.melee_attack.misc_bonus = 2
        assert pc.melee_attack.complete == 4
        pc.melee_attack.base_mod = 3
        assert pc.melee_attack.complete == 7

    def test_adding_new_skill(self):
        pc = create_pc()
        pc.add_new_skill(name="Searching", related_attribute='int', rank=2, misc_rank=1)
        assert pc.skills[0].total == 3

    def test_adding_new_skill_with_different_attributes(self):
        attributes = {"str": 14, "dex": 12, "con" : 15, "int": 20, "wis": 14, "cha" : 18}
        pc = create_pc()
        pc.attributes.set_attributes(attributes)
        pc.add_new_skill(name="str_skill", related_attribute='str', rank=2, misc_rank=1)
        pc.add_new_skill(name="dex_skill", related_attribute='dex', rank=4, misc_rank=3)
        pc.add_new_skill(name="con_skill", related_attribute='con', rank=8, misc_rank=5)
        pc.add_new_skill(name="int_skill", related_attribute='int', rank=10, misc_rank=2)
        pc.add_new_skill(name="wis_skill", related_attribute='wis', rank=12, misc_rank=0)
        pc.add_new_skill(name="cha_skill", related_attribute='cha', rank=6, misc_rank=3)
        assert pc.skills[0].total == 5
        assert pc.skills[1].total == 8
        assert pc.skills[2].total == 15
        assert pc.skills[3].total == 17
        assert pc.skills[4].total == 14
        assert pc.skills[5].total == 13

    def test_changing_skill_attribute(self):
        attributes = {"str": 14, "dex": 12}
        pc = create_pc()
        pc.attributes.set_attributes(attributes)
        pc.add_new_skill(name="Searching", related_attribute='dex', rank=2, misc_rank=1)
        assert pc.skills[0].total == 4
        pc.attributes.dex = 14
        assert pc.skills[0].total == 5

    def test_negative_rank(self):
        attributes = {"str": 14, "dex": 12}
        pc = create_pc()
        pc.attributes.set_attributes(attributes)
        with pytest.raises(ValueError):
            pc.add_new_skill(name="Searching", related_attribute='dex', rank=-1, misc_rank=1)

    def test_negative_misc_rank(self):
        attributes = {"str": 14, "dex": 12}
        pc = create_pc()
        pc.attributes.set_attributes(attributes)
        with pytest.raises(ValueError):
            pc.add_new_skill(name="Searching", related_attribute='dex', rank=12, misc_rank=-31)




def create_pc():
    return Character(name="Shan")
