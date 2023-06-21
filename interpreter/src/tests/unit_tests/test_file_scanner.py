from interpreter.src.scanners.FileScanner import FileScanner
import pytest
from loguru import logger

scanner = FileScanner("test01.azlp")

def view_output ():
    logger.debug(scanner.get_split_lines())
