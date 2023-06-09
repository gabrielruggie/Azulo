import typing
# Exception for incorrect library names/syntax
class InvalidLibraryException(Exception):
    
    def __init__ (self, user_library: str):
        self.user_library = user_library
        super().__init__(f' \'{self.user_library}\' is not a valid library')

# Exception for incorrect library names/syntax
class UnknownKeywordException(Exception):
    
    def __init__ (self, unknown_word: str):
        self.unknown_word = unknown_word
        super().__init__(f'Unknown keyword: \'{self.unknown_word}\'')

# Exception for incorrect library names/syntax
class IllegalOperatorException(Exception):
    
    def __init__ (self, operator: str):
        self.operator = operator
        super().__init__(f'Illegal Operator in Module declaration: \'{self.unknown_word}\'')

# Exception for incorrect library names/syntax
class MissiongBracketException(Exception):
    
    def __init__ (self, word: str):
        self.word = word
        super().__init__(f'Missing bracket by word: \'{self.unknown_word}\'')

# Exception for incorrect library names/syntax
class MissingParameterException(Exception):
    
    def __init__ (self, word: str, mod_name: str):
        self.word = word
        self.mod_name = mod_name
        super().__init__(f'Missing parameter or equals sign by \'{self.unknown_word}\' in module {self.mod_name}')