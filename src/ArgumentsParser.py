import argparse
from Arguments import Arguments

class ArgumentsParser:
    def __init__(self):
        self._parser = argparse.ArgumentParser(
            description='Program, which generates AutoHotkey scripts from substitutions list'
        )

        self._parser.add_argument(
            '-s', '--subs-list',
            help='Substitutions list file name'
        )

        self._parser.add_argument(
            '-w', '-wrapper-char',
            help='Character to wrap substitution in'
        )

        self._parser.add_argument(
            '-o', '--output',
            help='Output file name'
        )

    def parse(self):
        args = self._parser.parse_args()

        config = Arguments()

        attributesMap = {
            'wrapper_char': 'wrapperChar',
            'subs_list': 'substitutionsFile',
            'output': 'outputFile'
        }

        for argName, attrName in attributesMap.items():
            if hasattr(args, argName):
                setattr(config, attrName, getattr(args, argName))

        return config
