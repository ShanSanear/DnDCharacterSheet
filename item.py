possible_categories = ("weapon", "food", "other", "armor")


class CategoryError(Exception):
    pass


class IncorrectCost(Exception):
    pass



class Item:
    def __init__(self, name="", weight=0, cost=0, category="other", description=''):
        if cost < 0:
            raise IncorrectCost

        self.name = name
        self.weight = weight
        self.description = description
        if category not in possible_categories:
            raise CategoryError("Invalid category: {}".format(category))
        self.category = category
