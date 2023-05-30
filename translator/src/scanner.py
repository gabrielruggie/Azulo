from typing import List
import os

# Put in a .env file
PATH = "/Users/gabrielruggie/Desktop/Coding Projects/Nube-Visualizer/translator/src/"

class FileScanner:

    def __init__(self, filepath: str) -> None:
        self.filepath = filepath

    # Opens file and returns a list of string lines
    def __get_lines (self) -> List[str]:
        lines = []

        with open(os.path.join(PATH, self.filepath)) as f:
            for line in f:
                lines.append(line)
        
        return lines

    # Returns a 2D list of a .nub file where each list contains key words 
    # delimited by spaces
    def get_split_lines (self) -> List[List[str]]:
        nube_file_lines = self.__get_lines()
        key_lines = []

        for string in nube_file_lines:
            key_lines.append(string.split(" "))
        
        return key_lines
