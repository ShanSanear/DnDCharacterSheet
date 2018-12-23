from Character.Throws.basic_saving_throw import BasicSavingThrow
from Character.Throws.magic_saving_throw import MagicSavingThrow
from Character.Throws.temp_saving_throw import TempSavingThrow
from Character.Throws.misc_saving_throw import MiscSavingThrow

THROWS_KEYS = ('fortitude', 'reflex', 'will')
THROW_ATTRIBUTE = {"fortitude": 'con', "reflex": "dex", "will": "wis"}


class SavingThrows:
    def __init__(self, attr_cls, base_mods=None, misc_mods=None, magic_mods=None, temp_mods=None):
        self.attr = attr_cls

        if not base_mods:
            self.base_mods = BasicSavingThrow()
        else:
            self.base_mods = base_mods

        if not misc_mods:
            self.misc_mods = MiscSavingThrow()
        else:
            self.misc_mods = misc_mods

        if not magic_mods:
            self.magic_mods = MagicSavingThrow()
        else:
            self.magic_mods = magic_mods

        if not temp_mods:
            self.temp_mods = TempSavingThrow()
        else:
            self.temp_mods = temp_mods

    def _get_throw(self, throw):
        attr_of_throw = THROW_ATTRIBUTE[throw]
        val_of_throw = getattr(self.attr, attr_of_throw)['mod']
        val_of_throw += getattr(self.base_mods, throw)
        val_of_throw += getattr(self.misc_mods, throw)
        val_of_throw += getattr(self.magic_mods, throw)
        val_of_throw += getattr(self.temp_mods, throw)
        return val_of_throw

    @property
    def get_fortitude_throw(self):
        return self._get_throw("fortitude")

    @property
    def get_reflex_throw(self):
        return self._get_throw("reflex")

    @property
    def get_will_throw(self):
        return self._get_throw("will")

    reflex = get_reflex_throw
    fortitude = get_fortitude_throw
    will = get_will_throw
