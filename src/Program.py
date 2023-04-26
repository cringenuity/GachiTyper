from SubstitutionListParser import SubstitutionListParser
from AhkScriptGenerator import AhkScriptGenerator

class Program:
    def __init__(self):
        self._parser = SubstitutionListParser()
        self._scriptGenerator = AhkScriptGenerator()

    def run(self, inputFile: str, outputFile: str):
        substitutions = self._parser.parseFile(inputFile)
        self._scriptGenerator.generate(substitutions, outputFile)
