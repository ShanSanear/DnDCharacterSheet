from possible_exceptions import NoSpellException, IncorrectSpellSchool

spell_schools = (
    "Abjuration", "Conjuration", "Divination", "Enchantment", "Evocation", "Illusion", "Necromancy", "Transmutation",
    "Universal")


class SpellBook:
    def __init__(self):
        self._spells_list = {}

    def add_spell(self, spell_name, spell_description, spell_level, casting_time='1 standard action',
                  spell_range='Long', spell_area='Touch', spell_duration='Instant', spell_saving_throw='Reflex',
                  spell_school='Evocation', spell_resistance=False):
        if spell_school not in spell_schools:
            raise IncorrectSpellSchool("No spell school named: {}".format(spell_school))
        self._spells_list[spell_name] = {
            "Description": spell_description, "level": spell_level,
            "Casting time": casting_time, "Range": spell_range, "Area": spell_area,
            "Duration": spell_duration, "Saving throw": spell_saving_throw, "School": spell_school,
            "Spell resistance": spell_resistance}

    def __getattr__(self, item):
        return self._spells_list[item]

    def __iter__(self):
        for key in self._spells_list:
            return self._spells_list[key]

    def remove_spell(self, spell_name):
        try:
            del self._spells_list[spell_name]

        except (AttributeError, KeyError):
            raise NoSpellException("No spell with name: {}".format(spell_name))

    def spells_list(self):
        return self._spells_list
