from typing import Iterable

from Substitution import Substitution
from SubstitutionList import SubstitutionList

class SubstitutionListParser:
    def __init__(self):
        pass

    def parseFile(self, filename: str):
        with open(filename, 'r', encoding='utf-8') as file:
            return self._parseLines(x.removesuffix('\n') for x in file)

    def _parseLines(self, lines: Iterable[str]) -> SubstitutionList:
        result = SubstitutionList()

        for line in lines:
            sources, sub = line.split('=')

            for source in sources.split(','):
                result.add(Substitution(source, sub))

        return result
