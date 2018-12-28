class Attack:
    def __init__(self, attributes=None, size_bonus=0, misc_bonus=0, base_mod=0, attack_attribute='str'):
        self._attributes = attributes
        self._attack_attribute = attack_attribute
        self._size_bonus = size_bonus
        self._misc_bonus = misc_bonus
        self._base_mod = base_mod

    @property
    def _get_bonus_from_attribute(self):
        val = 0
        if self._attributes:
            val += getattr(self._attributes, self._attack_attribute)['mod']
        return val

    @property
    def _get_complete_modificator(self):
        complete = self.bonus_from_attribute + self._size_bonus + self._misc_bonus + self._base_mod
        return complete

    def _change_attack_attribute(self, new_attribute):
        self._attack_attribute = new_attribute

    def _get_attack_attribute(self):
        return self._attack_attribute

    def _get_size_bonus(self):
        return self._size_bonus

    def _get_misc_bonus(self):
        return self._misc_bonus

    def _get_base_mod(self):
        return self._base_mod

    def _set_size_bonus(self, val):
        self._size_bonus = val

    def _set_misc_bonus(self, val):
        self._misc_bonus = val

    def _set_base_mod(self, val):
        self._base_mod = val

    bonus_from_attribute = _get_bonus_from_attribute
    complete = _get_complete_modificator

    attack_attribute = property(_get_attack_attribute, _change_attack_attribute)
    size_bonus = property(_get_size_bonus, _set_size_bonus)
    misc_bonus = property(_get_misc_bonus, _set_misc_bonus)
    base_mod = property(_get_base_mod, _set_base_mod)
