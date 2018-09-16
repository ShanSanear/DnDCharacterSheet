from Character.Spells.spells_dc import *
from Character.attributes import Attributes


class TestSpepllsDc:
    def test_init_spells_dc(self):
        attr = Attributes()
        sdc = SpellsDc(attr_cls=attr, mod='int')
        assert sdc.sdc == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_changing_spells_dc(self):
        attr = Attributes()
        sdc = SpellsDc(attr_cls=attr, mod='int')
        attr.int = 14
        assert sdc.sdc == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    def test_changing_spells_modd(self):
        attr = Attributes()
        sdc = SpellsDc(attr_cls=attr, mod='int')
        attr.cha = 14
        assert sdc.sdc == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        sdc.mod = 'cha'
        assert sdc.sdc == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
