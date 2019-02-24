import pytest

from core.attributes import *


class TestAttributes:
    def test_str(self):
        attr = Attributes({"str": 12})
        assert attr.str == {"value": 12, "mod": 1}

    def test_dex(self):
        attr = Attributes({"dex": 8})
        assert attr.dex == {"value": 8, "mod": -1}

    def test_con(self):
        with pytest.raises(InvalidAttribute):
            Attributes({"con": -4})

    def test_temp_value(self):
        attr = Attributes({"str": 12})
        attr.temp.str = 10
        assert attr.str["value"] == 10

    def test_temp_value_returned(self):
        attr = Attributes({"str": 12})
        attr.temp.str = 10
        assert attr.str["value"] == 10
        attr.temp.str = 0
        assert attr.str["value"] == 12

    def test_all_attributes(self):
        attributes = dict(str=10, dex=10, con=10, wis=10, int=10, cha=10)
        attr = Attributes(attributes)
        assert attr.str == {"value": 10, "mod": 0}
        assert attr.dex == {"value": 10, "mod": 0}
        assert attr.con == {"value": 10, "mod": 0}
        assert attr.wis == {"value": 10, "mod": 0}
        assert attr.int == {"value": 10, "mod": 0}
        assert attr.cha == {"value": 10, "mod": 0}


if __name__ == '__main__':
    TestAttributes().test_all_attributes()
