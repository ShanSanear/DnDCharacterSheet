from possible_exceptions import NoAttributesInstance


class Skill:
    def __init__(self, name='', attr_cls=None, related_attribute='str', rank=0, misc_rank=0, description=''):

        self.name = name
        if not attr_cls:
            raise NoAttributesInstance("No attributes class instance was passed as parameter.")
        else:
            self.attrs = attr_cls

        self.related_attribute = related_attribute
        self._base_rank = rank
        self.misc_rank = misc_rank
        self._attr_rank = getattr(self.attrs, self.related_attribute)['mod']
        self.description = description

    def get_rank(self):
        self._attr_rank = getattr(self.attrs, self.related_attribute)['mod']
        _rank = self._base_rank + self._attr_rank + self.misc_rank
        return _rank

    def change_skill_rank(self, val):
        self._base_rank = val

    rank = property(get_rank, change_skill_rank)

