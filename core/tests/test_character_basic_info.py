from core.character_basic_info import CharacterBasicInfo


class TestCharacterBasicInfo:

    def test_name(self):
        cbi = CharacterBasicInfo()
        cbi.name = "NEW_NAME"
        assert cbi.name == "NEW_NAME"

    def test_player(self):
        cbi = CharacterBasicInfo()
        cbi.player = "PLAYER_NAME"
        assert cbi.player == "PLAYER_NAME"

    def test_character_class(self):
        cbi = CharacterBasicInfo()
        cbi.character_class = "FIGHTER"
        assert cbi.character_class == "FIGHTER"

    def test_race(self):
        cbi = CharacterBasicInfo()
        cbi.race = "ELF"
        assert cbi.race == "ELF"

    def test_alignement(self):
        cbi = CharacterBasicInfo()
        cbi.alignement = "NE"
        assert cbi.alignement == "NE"

    def test_faith(self):
        cbi = CharacterBasicInfo()
        cbi.faith = "IMPERATOR"
        assert cbi.faith == "IMPERATOR"

    def test_level(self):
        cbi = CharacterBasicInfo()
        cbi.level = "1"
        assert cbi.level == "1"

    def test_age(self):
        cbi = CharacterBasicInfo()
        cbi.age = "8"
        assert cbi.age == "8"

    def test_weight(self):
        cbi = CharacterBasicInfo()
        cbi.weight = "120"
        assert cbi.weight == "120"

    def test_height(self):
        cbi = CharacterBasicInfo()
        cbi.height = "150"
        assert cbi.height == "150"

    def test_size(self):
        cbi = CharacterBasicInfo()
        cbi.size = "Medium"
        assert cbi.size == "Medium"

    def test_gender(self):
        cbi = CharacterBasicInfo()
        cbi.gender = "M"
        assert cbi.gender == "M"

    def test_eyes(self):
        cbi = CharacterBasicInfo()
        cbi.eyes = "Blue"
        assert cbi.eyes == "Blue"

    def test_hair(self):
        cbi = CharacterBasicInfo()
        cbi.hair = "Blonde"
        assert cbi.hair == "Blonde"
