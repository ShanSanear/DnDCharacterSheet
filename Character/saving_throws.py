throws_keys = ('fortitude', 'reflex', 'will')
throw_attribute = {"fortitude": 'con', "reflex": "dex", "will": "wis"}


class SavingThrows:
    def __init__(self, attr_cls, base_mods=None, misc_mods=None, magic_mods=None, temp_mods=None):
        for var in [base_mods, misc_mods, magic_mods, temp_mods]:
            if var is None:
                var = {"fortitude": 0, "reflex": 0, "will": 0}
        self.attr = attr_cls
        self.base_mods = base_mods
        self.misc_mods = misc_mods
        self.magic_mods = magic_mods
        self.temp_mods = temp_mods

    def _get_throw(self, throw):
        attr_of_throw = throw_attribute[throw]
        attr_mod = getattr(self.attr, attr_of_throw)['mod']
        val_of_throw = attr_mod
        val_of_throw += self.base_mods[throw]
        val_of_throw += self.misc_mods[throw]
        val_of_throw += self.magic_mods[throw]
        val_of_throw += self.temp_mods[throw]
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
