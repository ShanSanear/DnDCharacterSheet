class InvalidAttribute(Exception):
    pass


class Attributes:
    def __init__(self, attributes=None):
        if not attributes:
            attributes = {}

        self._str = 10
        self._dex = 10
        self._con = 10
        self._wis = 10
        self._int = 10
        self._cha = 10

        self.decreases = {}
        self.set_attributes(attributes)


    def temp_decrease(self, attr, decrease_value):
        current_value = getattr(self, attr)['value']
        if current_value - decrease_value < 1:
            raise InvalidAttribute("Can't decrease attribute value below 1. Tried attribute: {}".format(attr))
        self.decreases[attr] = decrease_value
        setattr(self, attr, current_value - decrease_value)

    def _get_str(self):
        return {"value": self._str, "mod": (self._str - 10) // 2}

    def _get_dex(self):
        return {"value": self._dex, "mod": (self._dex - 10) // 2}

    def _get_con(self):
        return {"value": self._con, "mod": (self._con - 10) // 2}

    def _get_wis(self):
        return {"value": self._wis, "mod": (self._wis - 10) // 2}

    def _get_int(self):
        return {"value": self._int, "mod": (self._int - 10) // 2}

    def _get_cha(self):
        return {"value": self._cha, "mod": (self._cha - 10) // 2}

    def _set_str(self, val):
        self._str = val

    def _set_dex(self, val):
        self._dex = val

    def _set_con(self, val):
        self._con = val

    def _set_wis(self, val):
        self._wis = val

    def _set_int(self, val):
        self._int = val

    def _set_cha(self, val):
        self._cha = val

    str = property(_get_str, _set_str)
    dex = property(_get_dex, _set_dex)
    con = property(_get_con, _set_con)
    wis = property(_get_wis, _set_wis)
    int = property(_get_int, _set_int)
    cha = property(_get_cha, _set_cha)

    def set_attributes(self, attributes):
        for key, val in attributes.items():
            if val < 1:
                raise InvalidAttribute("{} is equal to : {}".format(key, val))
            setattr(self, key, val)
