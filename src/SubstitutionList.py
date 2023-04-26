from Substitution import Substitution

class SubstitutionList:
    def __init__(self):
        self.substitutions: list[Substitution] = []

    def add(self, substitution: Substitution):
        self.substitutions.append(substitution)

    def sort(self):
        self.substitutions.sort(key=lambda x: len(x.source), reverse=True)
