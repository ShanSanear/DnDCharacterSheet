import pytest

from core.exceptions import *
from .. import Item

class TestItem:
    def test_name(self):
        it = Item(name="Some_weapon")
        assert it.name == "Some_weapon"

    def test_weight(self):
        it = Item(weight=2)
        assert it.weight == 2

    def test_negative_weight(self):
        with pytest.raises(NegativeWeight):
            Item(name="", weight=-1)

    def test_category(self):
        it = Item(category="food")
        assert it.category == "food"

    def test_invalid_category(self):
        with pytest.raises(IncorrectCategory):
            Item(category="Olaboga")

    def test_incorrect_item_cost(self):
        with pytest.raises(NegativeCost):
            Item(cost=-1)

    def test_descritpion(self):
        it = Item(description="Desc")
        assert it.description == "Desc"


