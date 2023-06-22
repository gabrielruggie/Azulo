from typing import List
import os

AZM_DIR = "/Users/gabrielruggie/Desktop/Coding Projects/Azulo/interpreter/azx_files/azm_files/"

class FileScanner:

    def __init__(self, file_name: str, filepath: str) -> None:
        self.file_name: str = file_name
        # Put in .env file
        self.filepath = filepath

    # Opens file and returns a list of string lines
    def get_lines (self) -> List[str]:
        lines: list = []

        with open(os.path.join(self.filepath, self.file_name)) as f:
            for line in f:
                stripped_line = line.strip("\n")
                if stripped_line != '':
                    lines.append(stripped_line)
        
        return lines

    # Returns a 2D list of a .nub file where each list contains key words 
    # delimited by spaces
    def get_split_lines (self) -> List[List[str]]:
        nube_file_lines: list = self.get_lines()
        key_lines: list = []

        for string in nube_file_lines:
            key_lines.append(string.strip().split(" "))
        
        return key_lines

    # Creates a new azm file based on the project name
    def write_azm_file (self, project_name: str, azm_line_list: list) -> None:

        with open(os.path.join(AZM_DIR, f'{project_name}.azm'), 'w') as f:    
            for line in azm_line_list:
                f.write(line)
        
