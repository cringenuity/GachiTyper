import os
import subprocess as sp

from Arguments import Arguments

class CompilerCaller:
    def __init__(self, args: Arguments):
        self._arguments = args

    def compile(self, inputFile: str, outputFile: str | None = None):
        if outputFile is None:
            outputFile = os.path.splitext(inputFile)[0] + '.exe'

        sp.run([
            self._arguments.compilerPath,
            '/in', inputFile,
            '/out', outputFile,
            '/silent'
        ])
