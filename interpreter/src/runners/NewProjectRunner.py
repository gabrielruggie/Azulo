from interpreter.src.Lexer import Lexer
from interpreter.src.scanners.FileScanner import FileScanner
from interpreter.src.Validator import Validator
from interpreter.src.exceptions.LexerExceptions import *
from interpreter.src.exceptions.ValidatorExceptions import *

# Lets always have a user write a file to a specific directory ==> azlp_files
# This will get run anytime a new project is created
# 1. Read in file and create 2D list
# 2. Create dict objects
# 3. Validate dict objects
# 4. Write azm file

NEW_PROJECT_DIR = "/Users/gabrielruggie/Desktop/Coding Projects/Azulo/interpreter/azx_files/azlp_files/"

# Get Filename from CLI
file_name = input()

# Instances
scanner = FileScanner(file_name=file_name, filepath=NEW_PROJECT_DIR)
lexer = Lexer()
validator = Validator()




