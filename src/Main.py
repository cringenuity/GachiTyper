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

        Program().run(args.substitutionsFile, outputFile)
    else:
        generateAllScripts(args)

def generateAllScripts(args: Arguments):
    for subsListName in iglob('*SubsList.txt'):
        outputFileName = subsListName.replace('SubsList.txt', '.ahk')

        outputFileName = os.path.join('out', outputFileName)

        Program(args).run(subsListName, outputFileName)

if __name__ == '__main__':
    main()
