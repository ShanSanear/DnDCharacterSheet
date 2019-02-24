import logging
from types import SimpleNamespace


class InvalidAttribute(Exception):
    pass


class Attributes:
    def __init__(self, attributes=None, temp_attributes=None):
        # TODO Temporary attributes mods
        if not attributes:
            attributes = {}
        if not temp_attributes:
            temp_attributes = {}

        self._base_str = 10
        self._base_dex = 10
        self._base_con = 10
        self._base_wis = 10
        self._base_int = 10
        self._base_cha = 10
        self.temp = SimpleNamespace()
        self.temp.str = 0
        self.temp.dex = 0
        self.temp.con = 0
        self.temp.wis = 0
        self.temp.int = 0
        self.temp.cha = 0

        self.decreases = {}
        self.set_attributes(attributes)
        self.set_temp_attributes(temp_attributes)


    def temp_decrease(self, attr, decrease_value):
        current_value = getattr(self, attr)['value']
        if current_value - decrease_value < 1:
            raise InvalidAttribute("Can't decrease attribute value below 1. Tried attribute: {}".format(attr))
        self.decreases[attr] = decrease_value
        setattr(self, attr, current_value - decrease_value)

    def _get_str(self):
        if self.temp.str:
            return {"value": self.temp.str, "mod": (self.temp.str - 10) // 2}
        return {"value": self._base_str, "mod": (self._base_str - 10) // 2}

    def _get_dex(self):
        if self.temp.dex:
            return {"value": self.temp.dex, "mod": (self.temp.dex - 10) // 2}
        return {"value": self._base_dex, "mod": (self._base_dex - 10) // 2}

    def _get_con(self):
        if self.temp.con:
            return {"value": self.temp.con, "mod": (self.temp.con - 10) // 2}
        return {"value": self._base_con, "mod": (self._base_con - 10) // 2}

    def _get_wis(self):
        if self.temp.wis:
            return {"value": self.temp.wis, "mod": (self.temp.wis - 10) // 2}
        return {"value": self._base_wis, "mod": (self._base_wis - 10) // 2}

    def _get_int(self):
        if self.temp.int:
            return {"value": self.temp.int, "mod": (self.temp.int - 10) // 2}
        return {"value": self._base_int, "mod": (self._base_int - 10) // 2}

    def _get_cha(self):
        if self.temp.cha:
            return {"value": self.temp.cha, "mod": (self.temp.cha - 10) // 2}
        return {"value": self._base_cha, "mod": (self._base_cha - 10) // 2}

    def _set_str(self, val):
        self._base_str = val

    def _set_dex(self, val):
        self._base_dex = val

    def _set_con(self, val):
        self._base_con = val

    def _set_wis(self, val):
        self._base_wis = val

    def _set_int(self, val):
        self._base_int = val

    def _set_cha(self, val):
        self._base_cha = val

    def _get_base_str(self):
        return {"value": self._base_str, "mod": (self._base_str - 10) // 2}

    def _get_base_dex(self):
        return {"value": self._base_dex, "mod": (self._base_dex - 10) // 2}

    def _get_base_con(self):
        return {"value": self._base_con, "mod": (self._base_con - 10) // 2}

    def _get_base_wis(self):
        return {"value": self._base_wis, "mod": (self._base_wis - 10) // 2}

    def _get_base_int(self):
        return {"value": self._base_int, "mod": (self._base_int - 10) // 2}

    def _get_base_cha(self):
        return {"value": self._base_cha, "mod": (self._base_cha - 10) // 2}
    
    str = property(_get_str, _set_str)
    dex = property(_get_dex, _set_dex)
    con = property(_get_con, _set_con)
    wis = property(_get_wis, _set_wis)
    int = property(_get_int, _set_int)
    cha = property(_get_cha, _set_cha)

    base_str = property(_get_base_str, _set_str)
    base_dex = property(_get_base_dex, _set_dex)
    base_con = property(_get_base_con, _set_con)
    base_wis = property(_get_base_wis, _set_wis)
    base_int = property(_get_base_int, _set_int)
    base_cha = property(_get_base_cha, _set_cha)

    def set_attributes(self, attributes):
        for key, val in attributes.items():
            if val < 1:
                raise InvalidAttribute("{} is equal to : {}".format(key, val))
            setattr(self, key, val)

    def set_attribute(self, attribute, value):
        try:
            setattr(self, attribute, int(value))
        except ValueError:
            logging.debug("Empty or incorrect value passed as value to attribute, setting to 0")
            setattr(self, attribute, 0)

    def set_temp_attributes(self, temp_attributes):
        for key, val in temp_attributes.items():
            self.set_temp_attribute(self, attribute=key, value=val)

    def set_temp_attribute(self, attribute, value):
        try:
            setattr(self.temp, attribute, int(value))
        except ValueError:
            logging.debug("Empty or incorrect value passed as value to temp attribute")
            setattr(self.temp, attribute, 0)
