from Character.Spells.spells_per_day import *
from Character.attributes import Attributes


class TestSpellsPerDay:
    def test_max_spells_per_day(self):
        attr = Attributes()
        spd = SpellsPerDay(attr_cls=attr, mod='int')
        assert spd.max_spells_per_day == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def test_modify_spells_per_day(self):
        attr = Attributes()
        spd = SpellsPerDay(attr_cls=attr, mod='int')
        spd.max_spells_per_day[0] = 2
        assert spd.max_spells_per_day == [2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        spd.max_spells_per_day[2] = 3
        assert spd.max_spells_per_day == [2, 0, 3, 0, 0, 0, 0, 0, 0, 0]
        spd.max_spells_per_day = [2, 0, 3, 0, 0, 0, 0, 2, 2, 0]
        assert spd.max_spells_per_day == [2, 0, 3, 0, 0, 0, 0, 2, 2, 0]

    def test_bonus_spells_spells_per_day(self):
        attr = Attributes()
        spd = SpellsPerDay(attr_cls=attr, mod='int')
        assert spd.bonus_spells_per_day == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
