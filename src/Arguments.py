from dataclasses import dataclass

@dataclass
class Arguments:
    wrapperCharacter: str = '♂'
    substitutionsFile: str | None = None
    outputFile: str | None = None
