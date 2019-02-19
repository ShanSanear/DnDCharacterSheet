from core.exceptions import SpellNotInSpellBook, SpellNotRemembered


class RememberedSpells:
    def __init__(self, spell_book):
        self._spell_book = spell_book

    def __iter__(self):
        for attr, value in self.__dict__.items():
            if not attr.startswith('_'):
                yield attr, value
            else:
                continue

    def remember(self, name_to_remember):
        try:
            found_spell = getattr(self._spell_book, name_to_remember)
        except KeyError:
            raise SpellNotInSpellBook("There is no spell named {} in spellbook.".format(name_to_remember))

        setattr(self, name_to_remember, found_spell)

    def forget(self, name_to_forget):
        try:
            delattr(self, name_to_forget)
        except (AttributeError, KeyError):
            raise SpellNotRemembered("No spell named: {} in remembered spells.".format(name_to_forget))

    def _get_remembered_spells(self):
        remembered = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
        for spell, description in self:
            remembered[description['level']][spell] = description
        return remembered

    def _set_remembered_spells(self, val):
        pass

    remembered = property(_get_remembered_spells, _set_remembered_spells)
