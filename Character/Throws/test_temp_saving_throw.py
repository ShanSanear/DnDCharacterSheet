from Character.Throws.temp_saving_throw import *

class TestTempSavingThrow:

    def testBaseValues(self):
        tst = TempSavingThrow()
        assert tst.fortitude == 0
        assert tst.reflex == 0
        assert tst.will == 0

    def testSetValue(self):
        tst = TempSavingThrow()
        tst.will = 12
        assert tst.will == 12
        tst.fortitude = 12
        assert tst.fortitude == 12
        tst.reflex = 12
        assert tst.reflex == 12


