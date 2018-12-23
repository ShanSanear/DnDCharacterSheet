from Character.Throws.basic_saving_throw import *


class TestBasicSavingThrow:

    def testBaseValues(self):
        bst = BasicSavingThrow()
        assert bst.fortitude == 0
        assert bst.reflex == 0
        assert bst.will == 0

    def testSetValue(self):
        bst = BasicSavingThrow()
        bst.will = 12
        assert bst.will == 12
        bst.fortitude = 12
        assert bst.fortitude == 12
        bst.reflex = 12
        assert bst.reflex == 12


