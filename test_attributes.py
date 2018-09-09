import pytest
from attributes import *

class TestAttributes:
    def test_str(self):
        attr = Attributes({"str" : 12})
        assert attr.str == 12
        assert attr.str_mod == 1
    def test_dex(self):
        attr = Attributes({"dex" : 8})
        assert attr.dex == 8
        assert attr.dex_mod == -1
    def test_con(self):
        with pytest.raises(InvalidAttribute):
            attr = Attributes({"con" : -4})

    def test_temp_decrease(self):
        attr = Attributes({"str": 12})
        attr.temp_decrease("str", 2)
        assert attr.str == 10

    def test_invalid_temp_decrease(self):
        attr = Attributes({"dex": 14})
        with pytest.raises(InvalidAttribute):
            attr.temp_decrease("dex", 14)


    def test_all_attributes(self):
        attributes = dict(str=10, dex=10, con=10, wis=10, int=10, cha=10)
        attr = Attributes(attributes)
        assert attr.str == 10
        assert attr.dex == 10
        assert attr.con == 10
        assert attr.wis == 10
        assert attr.int == 10
        assert attr.cha == 10

        assert attr.str_mod == 0
        assert attr.dex_mod == 0
        assert attr.con_mod == 0
        assert attr.wis_mod == 0
        assert attr.int_mod == 0
        assert attr.cha_mod == 0


if __name__ == '__main__':
    TestAttributes().test_all_attributes()