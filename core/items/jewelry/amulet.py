from core.items import Item

class Amulet(Item):
    def __init__(self, name='', weight=0, cost=0, special_ability=None):
        if special_ability:
            self.special_ability = special_ability
        super(Amulet, self).__init__(name=name, weight=weight, cost=cost)
