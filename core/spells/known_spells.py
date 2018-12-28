class KnownSpells:
    def __init__(self):
        self._known_spells = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def get_known_spells(self):
        return self._known_spells

    def set_known_spells(self, val):
        self._known_spells = val

    known_spells = property(get_known_spells, set_known_spells)