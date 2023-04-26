from SubstitutionListParser import SubstitutionListParser
from AhkScriptGenerator import AhkScriptGenerator
from Arguments import Arguments
from CompilerCaller import CompilerCaller

class Program:
    def __init__(self, args: Arguments):
        self._parser = SubstitutionListParser()
        self._scriptGenerator = AhkScriptGenerator()
        self._compilerCaller = CompilerCaller(args)
        self._arguments = args

    def run(self, inputFile: str, outputFile: str):
        substitutions = self._parser.parseFile(inputFile)

        for sub in substitutions.substitutions:
            sub.wrapperChar = self._arguments.wrapperCharacter

        self._scriptGenerator.generate(substitutions, outputFile)

        if self._arguments.compile:
            self._compilerCaller.compile(outputFile)
