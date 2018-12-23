import pytest

from Items.Jewelry.rings import Rings
from possible_exceptions import *

class TestRings:
    def test_name(self):
        ring = Rings(name='DUMMY NAME')
        assert ring.name == "DUMMY NAME"
    def test_ability(self):
        ring = Rings(special_ability="could_be_object_to_invoke")
        assert ring.special_ability == "could_be_object_to_invoke"
    def test_no_ability(self):
        ring = Rings(name="DUMMY NAME")
        with pytest.raises(AttributeError):
            print(ring.special_ability)