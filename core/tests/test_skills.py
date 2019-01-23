from core.attributes import Attributes
from core.skills import *


class TestSkills:
    def test_name(self):
        attr = Attributes({"str": 14})
        sk = Skill(name="DUMMY NAME", attr_cls=attr)
        assert sk.name == "DUMMY NAME"

    def test_output_skill_rank(self):
        attr = Attributes({"str": 14})
        sk = Skill(name='', attr_cls=attr, related_attribute='str', rank=4, misc_rank=0)
        assert sk.total == 6
        attr.str = 16
        assert sk.total == 7

    def test_change_rank(self):
        attr = Attributes({"str": 14})
        sk = Skill(name='', attr_cls=attr, related_attribute='str', rank=4, misc_rank=0)
        assert sk.total == 6
        sk.total = 5
        assert sk.total == 7
        sk.total = 1
        assert sk.total == 3

    def test_change_related_attribute(self):
        attr = Attributes({"str": 12, "int": 16})
        sk = Skill(name='', attr_cls=attr, related_attribute='str', rank=3, misc_rank=0)
        assert sk.total == 4
        sk.related_attribute = 'int'
        assert sk.total == 6

    def test_change_misc_rank(self):
        attr = Attributes({"str": 14})
        sk = Skill(name='', attr_cls=attr, related_attribute='str', rank=4, misc_rank=0)
        assert sk.total == 6
        sk.misc_rank = 4
        assert sk.total == 10
