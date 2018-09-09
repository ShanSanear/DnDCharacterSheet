from Character.saving_throws import *
from Character.attributes import Attributes

class TestSavingThrows:

    def test_fortitude_saving_throw(self):
        attr = Attributes({"con": 16})
        st = SavingThrows(attr_cls=attr)
        assert st.fortitude == 3

    def test_multiple_types(self):
        base_mods = {"fortitude": 0, "reflex": 0, "will": 0}
        misc_mods = {"fortitude": 0, "reflex": 0, "will": 0}
        magic_mods = {"fortitude": 0, "reflex": 0, "will": 0}
        temp_mods = {"fortitude": 0, "reflex": 0, "will": 0}
        pass