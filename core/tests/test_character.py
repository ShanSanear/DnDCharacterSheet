from core.character import Character


class TestCharacter:
    def test_name(self):
        pc = Character(name="Shan")
        assert pc._name == "Shan"

    def test_default_values(self):
        pc = Character(name="Shan")
        assert pc.name == "Shan"
        assert pc.player == ""
        assert pc.character_class == ""
        assert pc.race == ""
        assert pc.faith == ""
        assert pc.level == ""
        assert pc.alignement == ""
        assert pc.size == ""
        assert pc.age == ""
        assert pc.gender == ""
        assert pc.height == ""
        assert pc.weight == ""
        assert pc.eyes == ""
        assert pc.hair == ""

    def test_character_attributes(self):
        attributes = {"dex": 12}
        pc = Character(name="Shan")
        pc.provide_attributes(attributes=attributes)
        assert pc.attributes.dex == {"value": 12, "mod": 1}

    def test_character_saving_throws(self):
        attributes = {"dex": 12}
        pc = Character(name="Shan")
        pc.provide_attributes(attributes)
        pc.get_saving_throws()
        assert pc.saving_throws.reflex == 1

    def test_character_saving_throws_with_changes(self):
        attributes = {"dex": 12}
        pc = Character(name="Shan")
        pc.provide_attributes(attributes)
        pc.get_saving_throws()
        pc.saving_throws.base_mods.reflex = 2
        assert pc.saving_throws.reflex == 3

    def test_melee_attack(self):
        attributes = {"str": 14, "dex": 12}
        pc = Character(name="Shan")
        pc.provide_attributes(attributes)
        pc.get_melee_attack()
        assert pc.melee_attack_value == 2

    def test_melee_attack_with_changed_misc(self):
        attributes = {"str": 14, "dex": 12}
        pc = Character(name="Shan")
        pc.provide_attributes(attributes)
        pc.get_melee_attack()
        pc.melee_attack.misc_bonus = 2
        assert pc.melee_attack_value == 4
        pc.melee_attack.base_mod = 3
        assert pc.melee_attack_value == 7
