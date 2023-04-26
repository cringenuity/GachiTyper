from SubstitutionListParser import SubstitutionListParser
from AhkScriptGenerator import AhkScriptGenerator
from Arguments import Arguments
from CompilerCaller import CompilerCaller
from ConflictSearcher import ConflictSearcher

class Program:
    def __init__(self, args: Arguments):
        self._parser = SubstitutionListParser()
        self._scriptGenerator = AhkScriptGenerator()
        self._compilerCaller = CompilerCaller(args)
        self._conflictSearcher = ConflictSearcher()
        self._arguments = args

    def run(self, inputFile: str, outputFile: str):
        substitutions = self._parser.parseFile(inputFile)

        for sub in substitutions.substitutions:
            sub.wrapperChar = self._arguments.wrapperCharacter

        conflicts = self._conflictSearcher.search_conflicts(substitutions)

        if len(conflicts) != 0:
            print(f'Found conflicts in file {inputFile}:')
            for sub1, sub2 in conflicts:
                print(f'    "{sub1}" and "{sub2}"')

        self._scriptGenerator.generate(substitutions, outputFile)

        if self._arguments.compile:
            self._compilerCaller.compile(outputFile)
