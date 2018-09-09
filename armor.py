from item import Item


class Armor(Item):
    def __init__(self, name='', armor_type='light', ac=0, mac=0,
                 test_penalty=0, magic_penalty=0, weight=0, description=''):
        super(Armor, self).__init__(name=name, weight=weight, description=description)
        self.armor_type = armor_type
        self.raw_ac = ac
        self.ac = ac + mac
        self.mac = mac
        self.test_penalty = test_penalty
        self.magic_penalty = magic_penalty
