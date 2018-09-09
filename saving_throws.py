class SavingThrows:
    def __init__(self, modificators):
        self.fortitude = 0
        self.reflex = 0
        self.will = 0
        for throw, value in modificators.items():
            setattr(self, throw, value)


