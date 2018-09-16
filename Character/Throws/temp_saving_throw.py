class TempSavingThrow:
    def __init__(self):
        self.__fortitude = 0
        self.__reflex = 0
        self.__will = 0

    def _set_value(self, throw, value):
        setattr(self, throw, value)

    def set_value(self, throw, value):
        self._set_value(throw, value)

    def _get_fortitude(self):
        return self.__fortitude
    
    def _set_fortitude(self, val):
        self.__fortitude = val
        
    fortitude = property(_get_fortitude, _set_fortitude)

    def _get_reflex(self):
        return self.__reflex

    def _set_reflex(self, val):
        self.__reflex = val

    reflex = property(_get_reflex, _set_reflex)
    
    def _get_will(self):
        return self.__will

    def _set_will(self, val):
        self.__will = val

    will = property(_get_will, _set_will)