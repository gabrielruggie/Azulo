from interpreter.src.scanners.FileScanner import FileScanner
import pytest
from loguru import logger

TEST_PATH = "/Users/gabrielruggie/Desktop/Coding Projects/Azulo/interpreter/azx_files/test_files"
scanner = FileScanner("test01.azlp", TEST_PATH)

def view_output ():
    logger.debug(scanner.get_split_lines())
