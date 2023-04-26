class Substitution:
    def __init__(self, source: str, replacement: str, wrapperChar: str | None = None):
        self.source = source
        self.replacement = replacement
        self.wrapperChar = wrapperChar

    @property
    def wrappedReplacement(self):
        return f'{self.wrapperChar}{self.replacement}{self.wrapperChar}'

    def __str__(self):
        return f'{self.source} -> {self.wrappedReplacement}'
