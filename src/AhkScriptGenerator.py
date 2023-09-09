import textwrap
import os

from Substitution import Substitution
from SubstitutionList import SubstitutionList
from Arguments import Arguments

class AhkScriptGenerator:
    _header = textwrap.dedent("""
        #SingleInstance Force
        #Hotstring * ? r z

        #SuspendExempt True
        ::!!gachi off::
        ::!!гачи офф::
        {{
            Send "{{Raw}}{wrapper}Yes, Sir!{wrapper}"
            Suspend True
        }}

        ::!!gachi on::
        ::!!гачи он::
        {{
            Send "{{Raw}}{wrapper}that turns me on{wrapper}"
            Suspend False
        }}
        #SuspendExempt False

    """)

    def __init__(self, args: Arguments):
        self._args = args

    def generate(self, substitutions: SubstitutionList, outputFile: str):
        os.makedirs(os.path.dirname(outputFile), exist_ok=True)

        with open(outputFile, 'w', encoding='utf-8') as file:
            file.write(self._header.format(wrapper=self._args.wrapperCharacter))

            for sub in substitutions.substitutions:
                file.write(f'::{sub.source}::{sub.wrappedReplacement}\n')
