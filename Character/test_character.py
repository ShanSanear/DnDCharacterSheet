from Character.character import Character


class TestCharacter:
    def test_name(self):

        pc = Character(name="Shan")
        assert pc.name == "Shan"

    def test_attributes(self):
        attributes = {"dex": 12}
        pc = Character(name="Shan", attributes=attributes)
        assert pc.attributes.dex == {"value" : 12, "mod" : 1}