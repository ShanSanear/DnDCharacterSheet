from possible_exceptions import IncorrectCategory, NegativeCost, NegativeWeight

possible_categories = ("weapon", "food", "other", "armor", "jewelry")


class Item:
    def __init__(self, name="", weight=0, cost=0, category="other", description=''):
        if cost < 0:
            raise NegativeCost

        if weight < 0:
            raise NegativeWeight

        self.name = name
        self.weight = weight
        self.description = description
        if category not in possible_categories:
            raise IncorrectCategory("Invalid category: {}".format(category))
        self.category = category
        self.cost = cost
