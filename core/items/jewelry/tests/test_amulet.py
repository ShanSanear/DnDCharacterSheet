import pytest

from .. import Amulet

class TestAmulet:
    def test_name(self):
        am = Amulet(name="DUMMY NAME")
        assert am.name == "DUMMY NAME"

    def test_ability(self):
        am = Amulet(special_ability="could_be_object_to_invoke")
        assert am.special_ability == "could_be_object_to_invoke"
    def test_no_ability(self):
        am = Amulet(name="DUMMY NAME")
        with pytest.raises(AttributeError):
            print(am.special_ability)
