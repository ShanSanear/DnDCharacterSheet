class SpellsDc:
    def __init__(self, attr_cls, mod='int', other_attributes=None):
        self.mod = mod
        self._attr_cls = attr_cls
        self._sdc = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if not other_attributes:
            self._other_attributes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        else:
            self._other_attributes = other_attributes

    def _get_sdc(self):
        sdc = []
        attr_mod = getattr(self._attr_cls, self.mod)['mod']
        for level in range(0, 10):
            sdc_of_level = self._sdc[level] + self._other_attributes[level] + attr_mod
            sdc.append(sdc_of_level)
        return sdc

    def _set_sdc(self, val):
        self._sdc = val

    def _get_other_sdc(self):
        return self._other_attributes

    def _set_other_sdc(self, val):
        self._other_attributes = val

    sdc = property(_get_sdc, _set_sdc)
    other_attributes = property(_get_other_sdc, _set_other_sdc)
