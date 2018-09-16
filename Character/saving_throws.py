throws_keys = ('fortitude', 'reflex', 'will')
throw_attribute = {"fortitude": 'con', "reflex": "dex", "will": "wis"}


class SavingThrows:
    def __init__(self, attr_cls, base_mods=None, misc_mods=None, magic_mods=None, temp_mods=None):
        self.attr = attr_cls
        self.__base_mods = base_mods
        self.__misc_mods = misc_mods
        self.__magic_mods = magic_mods
        self.__temp_mods = temp_mods

    def _get_throw(self, throw):
        attr_of_throw = throw_attribute[throw]
        val_of_throw = getattr(self.attr, attr_of_throw)['mod']
        val_of_throw += getattr(self.__base_mods, throw)
        val_of_throw += getattr(self.__misc_mods, throw)
        val_of_throw += getattr(self.__magic_mods, throw)
        val_of_throw += getattr(self.__temp_mods, throw)
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
