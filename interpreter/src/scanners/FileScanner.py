from typing import List
import os

# Put in a .env file
PATH = "/Users/gabrielruggie/Desktop/Coding Projects/Azulo/interpreter/azlx_files/test_files"

class FileScanner:

    def __init__(self, filepath: str) -> None:
        self.filepath = filepath

    # Opens file and returns a list of string lines
    def get_lines (self) -> List[str]:
        lines = []

        with open(os.path.join(PATH, self.filepath)) as f:
            for line in f:
                stripped_line = line.strip("\n")
                if stripped_line != '':
                    lines.append(stripped_line)
        
        return lines

    # Returns a 2D list of a .nub file where each list contains key words 
    # delimited by spaces
    def get_split_lines (self) -> List[List[str]]:
        nube_file_lines = self.get_lines()
        key_lines = []

        for string in nube_file_lines:
            key_lines.append(string.strip().split(" "))
        
        return key_lines
