from core.feats import *

class TestFeats:
    def test_name(self):
        feat = Feat(name="DUMMY_NAME")
        assert feat.name == "DUMMY_NAME"
    def test_description(self):
        feat = Feat(description='DUMMY DESCRIPTION')
        assert feat.description == "DUMMY DESCRIPTION"