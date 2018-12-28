from possible_exceptions import IncorrectAlignementError


class Alignement:
    def __init__(self):
        self.alignement = "NN"

    def set_alignement(self, provided_alignement):
        self.check_provided_alignement(provided_alignement)
        self.alignement = provided_alignement

    def check_provided_alignement(self, provided_alignement):
        if provided_alignement not in ["LG", "NG", "CG", "LN", "NN", "CN", "LE", "NE", "CE"]:
            raise IncorrectAlignementError
