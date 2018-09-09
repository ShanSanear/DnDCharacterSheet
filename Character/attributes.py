class InvalidAttribute(Exception):
    pass


class Attributes:
    def __init__(self, attributes):
        self._str = 10
        self._dex = 10
        self._con = 10
        self._wis = 10
        self._int = 10
        self._cha = 10
        self.decreases = {}

        for key, val in attributes.items():
            if val < 1:
                raise InvalidAttribute("{} is equal to : {}".format(key, val))
            setattr(self, key, val)

    def temp_decrease(self, attr, decrease_value):
        current_value = getattr(self, attr)['value']
        if current_value - decrease_value < 1:
            raise InvalidAttribute("Can't decrease attribute value below 1. Tried attribute: {}".format(attr))
        self.decreases[attr] = decrease_value
        setattr(self, attr, current_value - decrease_value)

    def get_str(self):
        return {"value": self._str, "mod": (self._str - 10) // 2}

    def get_dex(self):
        return {"value": self._dex, "mod": (self._dex - 10) // 2}

    def get_con(self):
        return {"value": self._con, "mod": (self._con - 10) // 2}

    def get_wis(self):
        return {"value": self._wis, "mod": (self._wis - 10) // 2}

    def get_int(self):
        return {"value": self._int, "mod": (self._int - 10) // 2}

    def get_cha(self):
        return {"value": self._cha, "mod": (self._cha - 10) // 2}

    def set_str(self, val):
        self._str = val

    def set_dex(self, val):
        self._dex = val

    def set_con(self, val):
        self._con = val

    def set_wis(self, val):
        self._wis = val

    def set_int(self, val):
        self._int = val

    def set_cha(self, val):
        self._cha = val

    str = property(get_str, set_str)
    dex = property(get_dex, set_dex)
    con = property(get_con, set_con)
    wis = property(get_wis, set_wis)
    int = property(get_int, set_int)
    cha = property(get_cha, set_cha)
