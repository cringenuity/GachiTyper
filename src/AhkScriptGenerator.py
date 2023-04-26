import textwrap

from Substitution import Substitution
from SubstitutionList import SubstitutionList

class AhkScriptGenerator:
    _header = textwrap.dedent("""
        #SingleInstance Force
        #Hotstring * ? r z

    """)

    def generate(self, substitutions: SubstitutionList, outputFile: str):
        with open(outputFile, 'w', encoding='utf-8') as file:
            file.write(self._header)

            for sub in substitutions.substitutions:
                file.write(f'::{sub.source}::{sub.wrappedReplacement}\n')
