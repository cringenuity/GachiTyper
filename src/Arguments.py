from dataclasses import dataclass

@dataclass
class Arguments:
    wrapperCharacter: str = '♂'
    substitutionsFile: str | None = None
    outputFile: str | None = None
    compile: bool = False
    compilerPath: str = r'C:\Program Files\AutoHotkey\Compiler\Ahk2Exe.exe'
