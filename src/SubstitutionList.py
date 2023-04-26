from Substitution import Substitution

class SubstitutionList:
    def __init__(self):
        self.substitutions: list[Substitution] = []

    def add(self, substitution: Substitution):
        self.substitutions.append(substitution)
