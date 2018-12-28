from core.items import Item

class Rings(Item):
    def __init__(self, name='', weight=0, cost=0, special_ability=None):
        super(Rings, self).__init__(name=name, weight=weight, cost=cost, category='jewelry')
        if special_ability:
            self.special_ability = special_ability

