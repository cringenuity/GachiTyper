class Substitution:
    def __init__(self, source: str, replacement: str):
        self.source = source
        self.replacement = replacement

    @property
    def wrappedReplacement(self):
        return f'♂{self.replacement}♂'
