from possible_exceptions import NoSpellException


class SpellBook:
    def __init__(self):
        pass
    def add_spell(self, spell_name, spell_description, spell_level):
        setattr(self, spell_name, {"Description": spell_description, "level" : spell_level})

    def remove_spell(self, spell_name):
        try:
            delattr(self, spell_name)

        except (AttributeError, KeyError):
            raise NoSpellException("No spell with name: {}".format(spell_name))

    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield attr, value

    def spells_list(self):
        spells = {}
        for spell_name, description_and_level in self:
            spells[spell_name] = description_and_level
        return spells


