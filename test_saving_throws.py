from saving_throws import *

class TestSavingThrows:

    def test_fortitude_saving_throw(self):
        modificators = {"fortitude" : 3}

        st = SavingThrows(modificators)
        assert  st.fortitude == 3