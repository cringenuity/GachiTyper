import argparse
from Arguments import Arguments

class ArgumentsParser:
    def __init__(self):
        self._parser = argparse.ArgumentParser(
            description='Program, which generates AutoHotkey scripts from substitutions list'
        )

        self._parser.add_argument(
            'filename',
            metavar='FILENAME',
            help='Substitutions list file name'
        )

        self._parser.add_argument(
            '-w', '--wrapper-char',
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
            'wrapper_char': 'wrapperCharacter',
            'filename': 'substitutionsFile',
            'output': 'outputFile'
        }

        for argName, attrName in attributesMap.items():
            if (value := getattr(args, argName)) is not None:
                setattr(
                    config,
                    attrName,
                    value
                        .encode('utf-8', 'surrogateescape')
                        .decode('unicode-escape'))

        return config
