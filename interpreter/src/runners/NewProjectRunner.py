from interpreter.src.Lexer import Lexer
from interpreter.src.scanners.FileScanner import FileScanner
from interpreter.src.Validator import Validator
from interpreter.src.exceptions.LexerExceptions import *
from interpreter.src.exceptions.ValidatorExceptions import *
from interpreter.src.exceptions.LexerExceptions import *
from interpreter.src.exceptions.ValidatorExceptions import *

from typing import List
from loguru import logger

# Lets always have a user write a file to a specific directory ==> azlp_files
# This will get run anytime a new project is created
# 1. Read in file and create 2D list
# 2. Create dict objects
# 3. Validate dict objects
# 4. Write azm file

def main (file_name: str):
    # Instances
    scanner = FileScanner(file_name=file_name)
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

        logger.info("New project created!")

    except LexerSyntaxException as ex:
        logger.debug("There was a syntax error in one of the module instantiations: ", ex)

    except ValidationError as ex:
        logger.debug("At least one module does not follow contract: ", ex)

    except Exception as ex:
        logger.debug("An unexpected issue occurred during new project runner run time", ex)

    # Done

if __name__ == '__main__':
    file_name: str = input()
    main(file_name=file_name)
