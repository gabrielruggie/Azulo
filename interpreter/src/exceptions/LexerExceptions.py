class LexerSyntaxException (Exception):
    pass

# Exception for unknown and unreadable tokens
class UnexpectedTokenException(LexerSyntaxException):

    def __init__(self, line_num: int, unknown_token: str):
        self.message: str = f'Unexpected \'{unknown_token}\' on line {line_num}'
        super().__init__(self.message)

# Exception for incorrect library names/syntax
class IllegalOperatorException(LexerSyntaxException):
    
    def __init__ (self, type:str, operator: str, line_num:int):
        self.message = None
        if type == 'module':
            self.message = f'Illegal Operator in module declaration: \'{operator}\' near line {line_num}'
        elif type == 'detail':
            self.message = f'Illegal Operator in module attributes: \'{operator}\' near line {line_num}'
        
        super().__init__(self.message)

# Exception for incorrect library names/syntax
class MissingBracketException(LexerSyntaxException):
    
    def __init__ (self, type:str, word: str, line_num:int):
        self.message = f'Missing {type} bracket by word: \'{word}\' at line: {line_num}'
        super().__init__(self.message)

# Exception for incorrect library names/syntax
class MissingParameterException(LexerSyntaxException):
    
    def __init__ (self, line_num: int):
        self.message = f'Missing parameter or equals sign near line {line_num}'
        super().__init__(self.message)