from attributes import Attributes

class Character:
    def __init__(self, name, attributes = None):
        if not attributes:
            attributes = {}
        self.name = name
        self.attributes = Attributes(attributes)
