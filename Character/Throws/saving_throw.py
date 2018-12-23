class SavingThrow:
    def __init__(self):
        self._fortitude = 0
        self._reflex = 0
        self._will = 0

    def _set_value(self, throw, value):
        setattr(self, throw, value)

    def set_value(self, throw, value):
        self._set_value(throw, value)

    def _get_fortitude(self):
        return self._fortitude

    def _set_fortitude(self, val):
        self._fortitude = val

    fortitude = property(_get_fortitude, _set_fortitude)

    def _get_reflex(self):
        return self._reflex

    def _set_reflex(self, val):
        self._reflex = val

    reflex = property(_get_reflex, _set_reflex)

    def _get_will(self):
        return self._will

    def _set_will(self, val):
        self._will = val

    will = property(_get_will, _set_will)
