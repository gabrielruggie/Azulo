from interpreter.src.Lexer import Lexer
from interpreter.src.scanners.FileScanner import FileScanner
from interpreter.src.Validator import Validator
from interpreter.src.exceptions.LexerExceptions import *
from interpreter.src.exceptions.ValidatorExceptions import *
from interpreter.src.exceptions.LexerExceptions import *
from interpreter.src.exceptions.ValidatorExceptions import *

from typing import List

# Lets always have a user write a file to a specific directory ==> azlp_files
# This will get run anytime a new project is created
# 1. Read in file and create 2D list
# 2. Create dict objects
# 3. Validate dict objects
# 4. Write azm file

NEW_PROJECT_DIR = "/Users/gabrielruggie/Desktop/Coding Projects/Azulo/interpreter/azx_files/azlp_files/"

# Get Filename from CLI
file_name: str = input()

# Instances
scanner = FileScanner(file_name=file_name, filepath=NEW_PROJECT_DIR)
lexer = Lexer()
validator = Validator()

try:

    new_project_file_lines: List[List[str]] = scanner.get_split_lines()

    lexer.set_azlp_lines(azlp_lines=new_project_file_lines)
    module_dict_items: List[dict] = lexer.process()

    validator.set_module_dict_objects(module_dict_objects=module_dict_items)
    valid_azm_lines: List[str] = validator.validate()

    period_idx: int = file_name.index('.')
    scanner.write_azm_file(project_name=file_name[0:period_idx], azm_line_list=valid_azm_lines)

except LexerSyntaxException as ex:
    pass

except ValidationError as ex:
    pass

# Done

