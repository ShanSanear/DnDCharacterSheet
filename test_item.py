import pytest

from item import *

class TestItem:
    def test_name(self):
        it = Item(name="Some_weapon")
        assert it.name == "Some_weapon"

    def test_weight(self):
        it = Item("", 2)
        assert it.weight == 2

    def test_category(self):
        it = Item(name="", weight=0, category="food")
        assert it.category == "food"

    def test_invalid_category(self):
        with pytest.raises(CategoryError):
            Item(name="", weight=0, category="Olaboga")

    def test_incorrect_item_cost(self):
        with pytest.raises(IncorrectCost):
            Item(cost=-1)

    def test_descritpion(self):
        it = Item(description="Desc")
        assert it.description == "Desc"
