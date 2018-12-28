from core.throws.misc_saving_throw import *

class TestMiscSavingThrow:

    def testBaseValues(self):
        mst = MiscSavingThrow()
        assert mst.fortitude == 0
        assert mst.reflex == 0
        assert mst.will == 0

    def testSetValue(self):
        mst = MiscSavingThrow()
        mst.will = 12
        assert mst.will == 12
        mst.fortitude = 12
        assert mst.fortitude == 12
        mst.reflex = 12
        assert mst.reflex == 12
