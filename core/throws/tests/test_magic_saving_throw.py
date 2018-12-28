from core.throws.magic_saving_throw import *

class TestMagicSavingThrow:

    def testBaseValues(self):
        mst = MagicSavingThrow()
        assert mst.fortitude == 0
        assert mst.reflex == 0
        assert mst.will == 0

    def testSetValue(self):
        mst = MagicSavingThrow()
        mst.will = 12
        assert mst.will == 12
        mst.fortitude = 12
        assert mst.fortitude == 12
        mst.reflex = 12
        assert mst.reflex == 12


