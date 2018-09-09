class InvalidAttribute(Exception):
    pass


class Attributes:
    def __init__(self, attributes):
        self.str = 10
        self.dex = 10
        self.con = 10
        self.wis = 10
        self.int = 10
        self.cha = 10
        self.decreases = {}

        for key, val in attributes.items():
            if val < 1:
                raise InvalidAttribute("{} is equal to : {}".format(key, val))
            setattr(self, key, val)

    def temp_decrease(self, attr, decrease_value):
        current_value = getattr(self, attr)
        if current_value - decrease_value < 1:
            raise InvalidAttribute("Can't decrease attribute value below 1. Tried attribute: {}".format(attr))
        self.decreases[attr] = decrease_value
        setattr(self, attr, current_value - decrease_value)

    @property
    def get_str_mod(self):
        return (self.str - 10) // 2
    @property
    def get_dex_mod(self):
        return (self.dex - 10) //2
    @property
    def get_con_mod(self):
        return (self.con - 10)//2
    @property
    def get_wis_mod(self):
        return (self.wis - 10) //2
    @property
    def get_int_mod(self):
        return (self.int - 10) //2
    @property
    def get_cha_mod(self):
        return (self.cha - 10) //2


    str_mod = get_str_mod
    dex_mod = get_dex_mod
    con_mod = get_con_mod
    wis_mod = get_wis_mod
    int_mod = get_int_mod
    cha_mod = get_cha_mod
