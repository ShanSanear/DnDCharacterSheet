from core.skills import *
from core.attributes import Attributes


class TestSkills:
    def test_name(self):
        attr = Attributes({"str": 14})
        sk = Skill(name="DUMMY NAME", attr_cls=attr)
        assert sk.name == "DUMMY NAME"

    def test_output_skill_rank(self):
        attr = Attributes({"str": 14})
        sk = Skill(name='', attr_cls=attr, related_attribute='str', rank=4, misc_rank=0)
        assert sk.rank == 6
        attr.str = 16
        assert sk.rank == 7

    def test_change_rank(self):
        attr = Attributes({"str": 14})
        sk = Skill(name='', attr_cls=attr, related_attribute='str', rank=4, misc_rank=0)
        assert sk.rank == 6
        sk.rank = 5
        assert sk.rank == 7
        sk.rank = 1
        assert sk.rank == 3

    def test_change_related_attribute(self):
        attr = Attributes({"str": 12, "int": 16})
        sk = Skill(name='', attr_cls=attr, related_attribute='str', rank=3, misc_rank=0)
        assert sk.rank == 4
        sk.related_attribute = 'int'
        assert sk.rank == 6

    def test_change_misc_rank(self):
        attr = Attributes({"str": 14})
        sk = Skill(name='', attr_cls=attr, related_attribute='str', rank=4, misc_rank=0)
        assert sk.rank == 6
        sk.misc_rank = 4
        assert sk.rank == 10

    def test_description(self):
        attr = Attributes({"str": 14})
        sk = Skill(name='', attr_cls=attr, related_attribute='str', rank=4, misc_rank=0, description="DUMMY DESCRIPTION")
        assert sk.description == "DUMMY DESCRIPTION"