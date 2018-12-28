import pytest

from core.spells.known_spells import *


class TestKnownSpells:
    def test_init_values(self):
        ks = KnownSpells()
        assert ks.known_spells == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def test_set_1st_lvl(self):
        ks = KnownSpells()
        ks.known_spells[1] = 2
        assert ks.known_spells == [0, 2, 0, 0, 0, 0, 0, 0, 0, 0]

    def test_set_9th_lvl(self):
        ks = KnownSpells()
        ks.known_spells[9] = 5
        assert ks.known_spells == [0, 0, 0, 0, 0, 0, 0, 0, 0, 5]

    def test_error_set_10th_lvl(self):
        ks = KnownSpells()
        with pytest.raises(IndexError):
            ks.known_spells[10] = 5
