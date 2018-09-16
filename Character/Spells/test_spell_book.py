import pytest

from Character.Spells.spell_book import *


class TestSpellBook:
    def test_init_values(self):
        sb = SpellBook()
        sb.add_spell("Blizzard", "Blizzard description", 3)
        assert getattr(sb, "Blizzard") == {"Description": "Blizzard description", "level": 3}

    def test_multiple_spells(self):
        sb = SpellBook()

        sb.add_spell("Fireball", "Fireball description", 3)
        sb.add_spell("Magic missle", "MM description", 1)

        assert sb.spells_list() == {"Fireball": {"Description": "Fireball description", "level": 3},
                                    "Magic missle": {"Description": "MM description", "level": 1}}

    def test_remove_speells(self):
        sb = SpellBook()

        sb.add_spell("Fireball", "Fireball description", 3)
        assert sb.spells_list() == {"Fireball": {"Description": "Fireball description", "level": 3}}
        sb.remove_spell("Fireball")
        assert sb.spells_list() == {}
        with pytest.raises(NoSpellException):
            sb.remove_spell("Fireball")
