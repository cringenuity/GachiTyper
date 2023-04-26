import textwrap

from Substitution import Substitution
from SubstitutionList import SubstitutionList

class AhkScriptGenerator:
    _header = textwrap.dedent("""
        #SingleInstance Force
        #Hotstring * ? r z

        #SuspendExempt True
        ::!!gachi off::
        ::!!гачи офф::
        {
            Send "{Raw}Yes, Sir!"
            Suspend True
        }

        ::!!gachi on::
        ::!!гачи он::
        {
            Send "{Raw}Yes, Sir!"
            Suspend False
        }
        #SuspendExempt False

    """)

    def generate(self, substitutions: SubstitutionList, outputFile: str):
        with open(outputFile, 'w', encoding='utf-8') as file:
            file.write(self._header)

            for sub in substitutions.substitutions:
                file.write(f'::{sub.source}::{sub.wrappedReplacement}\n')
