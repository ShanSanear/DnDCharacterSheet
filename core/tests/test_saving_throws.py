from core.attributes import Attributes
from core.saving_throws import *
from core.throws.basic_saving_throw import BasicSavingThrow
from core.throws.magic_saving_throw import MagicSavingThrow
from core.throws.misc_saving_throw import MiscSavingThrow
from core.throws.temp_saving_throw import TempSavingThrow


class TestSavingThrows:
    def test_fortitude_from_attribute(self):
        attr = Attributes({"con": 16})
        base_mods = BasicSavingThrow()
        misc_mods = MiscSavingThrow()
        magic_mods = MagicSavingThrow()
        temp_mods = TempSavingThrow()

        st = SavingThrows(attr_cls=attr, base_mods=base_mods, misc_mods=misc_mods, magic_mods=magic_mods, temp_mods=temp_mods)
        assert st.fortitude == 3

    def test_fortitude_from_base_and_attr(self):
        attr = Attributes({"con": 20})
        base_mods = BasicSavingThrow()
        misc_mods = MiscSavingThrow()
        magic_mods = MagicSavingThrow()
        temp_mods = TempSavingThrow()
        base_mods.fortitude = 3

        st = SavingThrows(attr_cls=attr, base_mods=base_mods, misc_mods=misc_mods, magic_mods=magic_mods,
                          temp_mods=temp_mods)
        assert st.fortitude == 8

    def test_reflex_from_temp_and_misc(self):
        attr = Attributes()
        base_mods = BasicSavingThrow()
        misc_mods = MiscSavingThrow()
        magic_mods = MagicSavingThrow()
        temp_mods = TempSavingThrow()
        temp_mods.fortitude = 3
        misc_mods.fortitude = 7

        st = SavingThrows(attr_cls=attr, base_mods=base_mods, misc_mods=misc_mods, magic_mods=magic_mods,
                          temp_mods=temp_mods)
        assert st.fortitude == 10