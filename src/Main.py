import os
from glob import iglob
from Program import Program
from ArgumentsParser import ArgumentsParser
from Arguments import Arguments

def main():
    parser = ArgumentsParser()
    args = parser.parse()

    if args.substitutionsFile is not None:
        outputFile = args.outputFile

        if outputFile is None:
            outputFile = 'GachiTyper.ahk'

        Program(args).run(args.substitutionsFile, outputFile)

if __name__ == '__main__':
    main()
