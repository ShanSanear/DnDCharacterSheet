class SpellsPerDay:
    def __init__(self, attr_cls, mod='int'):
        self.attr_cls = attr_cls
        self.mod = mod
        self._max_spells_per_day = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def _get_max_spells_per_day(self):
        return self._max_spells_per_day

    def _set_max_spells_per_day(self, val):
        self._max_spells_per_day = val


    @property
    def _get_bonus_spelss_per_day(self):
        mod_value = getattr(self.attr_cls, self.mod)['mod']

        bonus_spells_per_day = [0]

        for val in range(3, -6, -1):
            bonus_spells = (mod_value + val) // 4
            if bonus_spells < 0:
                bonus_spells = 0
            bonus_spells_per_day.append(bonus_spells)

        return bonus_spells_per_day

    bonus_spells_per_day = _get_bonus_spelss_per_day
    max_spells_per_day = property(_get_max_spells_per_day, _set_max_spells_per_day)
