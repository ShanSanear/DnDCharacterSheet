from core.exceptions import NoAttributesInstance


class Skill:
    def __init__(self, name='', attr_cls=None, related_attribute='str', rank=0, misc_rank=0):

        self.name = name
        if not attr_cls:
            raise NoAttributesInstance("No attributes class instance was passed as parameter.")
        else:
            self.attrs = attr_cls

        if rank < 0 or misc_rank < 0:
            raise ValueError(f"Either skill rank: ({rank}) misc rank ({misc_rank}) is negative, couldn't create skill.")

        self.related_attribute = related_attribute
        self._base_rank = rank
        self.misc_rank = misc_rank
        self._attr_rank = getattr(self.attrs, self.related_attribute)['mod']

    def get_rank(self):
        self._attr_rank = getattr(self.attrs, self.related_attribute)['mod']
        _rank = self._base_rank + self._attr_rank + self.misc_rank
        return _rank

    def change_skill_rank(self, val):
        self._base_rank = val

    total = property(get_rank, change_skill_rank)

