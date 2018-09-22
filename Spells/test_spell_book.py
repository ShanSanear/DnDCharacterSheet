import pytest

from Spells.spell_book import *


class TestSpellBook:
    """
    Default spell dict:
    ["Dummy spell"] = {
            "Description": "Dummy spell description",
            "level": 3,
            "Casting time": "1 standard action",
            "Range": "Long",
            "Area": "Touch",
            "Duration": "Instant",
            "Saving throw": "Reflex",
            "School": "Evocation",
            "Spell resistance": False
        }
    """
    def test_init_values(self):
        sb = SpellBook()
        sb.add_spell("Dummy spell", "Dummy spell description", 3)
        assert getattr(sb, "Dummy spell")["Description"] == "Dummy spell description"
        assert getattr(sb, "Dummy spell")["level"] == 3
        assert getattr(sb, "Dummy spell")["Casting time"] == '1 standard action'
        assert getattr(sb, "Dummy spell")["Range"] == "Long"
        assert getattr(sb, "Dummy spell")["Area"] == "Touch"
        assert getattr(sb, "Dummy spell")["Duration"] == "Instant"
        assert getattr(sb, "Dummy spell")["Saving throw"] == "Reflex"
        assert getattr(sb, "Dummy spell")["School"] == "Evocation"
        assert not getattr(sb, "Dummy spell")["Spell resistance"]

    def test_custom_spell(self):
        sb = SpellBook()
        sb.add_spell(spell_name="Fireball", spell_level=3, spell_school="Evocation", casting_time="1 standard action",
                     spell_area="20-ft.-radius", spell_duration="Instantaneous", spell_range="Long",
                     spell_saving_throw='Reflex, half', spell_resistance=True, spell_description="Fireball description")

        assert sb.spells_list() == {
            "Fireball": {"level": 3, "School": "Evocation", "Area": "20-ft.-radius", "Duration": "Instantaneous",
                         "Casting time": "1 standard action", "Range": "Long", "Saving throw": "Reflex, half",
                         "Spell resistance": True, "Description": "Fireball description"}}

    def test_remove_speells(self):
        sb = SpellBook()

        sb.add_spell(spell_name="Fireball", spell_level=3, spell_school="Evocation", casting_time="1 standard action",
                     spell_area="20-ft.-radius", spell_duration="Instantaneous", spell_range="Long",
                     spell_saving_throw='Reflex, half', spell_resistance=True, spell_description="Fireball description")
        assert sb.spells_list() == {
            "Fireball": {"level": 3, "School": "Evocation", "Area": "20-ft.-radius", "Duration": "Instantaneous",
                         "Casting time": "1 standard action", "Range": "Long", "Saving throw": "Reflex, half",
                         "Spell resistance": True, "Description": "Fireball description"}}
        sb.remove_spell("Fireball")
        assert sb.spells_list() == {}
        with pytest.raises(NoSpellException):
            sb.remove_spell("Fireball")

    def test_incorect_spell_school(self):
        sb = SpellBook()
        with pytest.raises(IncorrectSpellSchool):
            sb.add_spell(spell_name="TEST NAME", spell_description="TEST DESC", spell_level=2,
                         spell_school="Incorrect spell school")
