class CharacterBasicInfo:
    def __init__(self):
        self._name = ""
        self._player = ""
        self._character_class = ""
        self._race = ""
        self._alignement = ""
        self._faith = ""
        self._level = ""
        self._age = ""
        self._weight = ""
        self._height = ""
        self._size = ""
        self._gender = ""
        self._eyes = ""
        self._hair = ""

    def _set_name(self, name):
        self._name = name

    def _get_name(self):
        return self._name


    def _set_player(self, player):
        self._player = player

    def _get_player(self):
        return self._player


    def _set_character_class(self, character_class):
        self._character_class = character_class

    def _get_character_class(self):
        return self._character_class


    def _set_race(self, race):
        self._race = race

    def _get_race(self):
        return self._race


    def _set_alignement(self, alignement):
        self._alignement = alignement

    def _get_alignement(self):
        return self._alignement


    def _set_faith(self, faith):
        self._faith = faith

    def _get_faith(self):
        return self._faith


    def _set_level(self, level):
        self._level = level

    def _get_level(self):
        return self._level


    def _set_age(self, age):
        self._age = age

    def _get_age(self):
        return self._age


    def _set_weight(self, weight):
        self._weight = weight

    def _get_weight(self):
        return self._weight


    def _set_height(self, height):
        self._height = height

    def _get_height(self):
        return self._height


    def _set_size(self, size):
        self._size = size

    def _get_size(self):
        return self._size


    def _set_gender(self, gender):
        self._gender = gender

    def _get_gender(self):
        return self._gender


    def _set_eyes(self, eyes):
        self._eyes = eyes

    def _get_eyes(self):
        return self._eyes


    def _set_hair(self, hair):
        self._hair = hair

    def _get_hair(self):
        return self._hair

    name = property(_get_name, _set_name)
    player = property(_get_player, _set_player)
    character_class = property(_get_character_class, _set_character_class)
    race = property(_get_race, _set_race)
    alignement = property(_get_alignement, _set_alignement)
    faith = property(_get_faith, _set_faith)
    level = property(_get_level, _set_level)
    age = property(_get_age, _set_age)
    weight = property(_get_weight, _set_weight)
    height = property(_get_height, _set_height)
    size = property(_get_size, _set_size)
    gender = property(_get_gender, _set_gender)
    eyes = property(_get_eyes, _set_eyes)
    hair = property(_get_hair, _set_hair)
