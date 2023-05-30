from constant_classes.NubeLibraryConstants import NubeLibraryConstants
from exception_classes.Exceptions import InvalidLibraryException, UnknownKeywordException, IllegalOperatorException, MissiongBracketException, MissingParameterException
from Scanner import FileScanner
from typing import List, Dict, Any

class NubeFileParser:

    def __init__ (self):
        # A new open bracket sets this to True. A closed bracket sets this to False
        # If we find an open bracket and this is True, we have a problem
        self.__bracket_flag = False
        self.__nube_library = ""
        self.__new_module = False
        self.__new_module_info = {}

        scanner = FileScanner(filepath="blah.nub")
        self.__file_line_list = scanner.get_split_lines()

    # Sets the library being used in current nube file
    def __setattr__(self, __lib: str) -> None:
        vld = NubeLibraryConstants.validate_library(__lib)

        if vld:
            self.__nube_library = __lib
            # Turn off once library is found and validated
            self.__fresh_file = False
        else:
            raise InvalidLibraryException(__lib)
    
    # Gets library of file for translator
    def __getattribute__(self) -> str:
        return self.__nube_library

    # Remember to remove newline characters!!
    def __keyword_controller (self, word: str, word_idx: int, line: List) -> None:

        match(word):
            # Set file library with word immediately after `lib` keyword
            case "lib:": self.__setattr__(line[word_idx+1])

            # Most likley going to leave this like this. 
            # We don't care about new line characters
            case "\n": pass

            case "module": 
                self.__new_module = True
                # Clear list before creating a new one
                self.__new_module_info = []
                # Module name should be the first thing in the list
                self.__new_module_info["name"] = line[word_idx+1]

            case "//": pass

            case other:
                raise UnknownKeywordException(word)
    
    # Remember to remove newline characters!!
    def __new_module_controller (self, word: str, word_idx: int, line: List) -> None:

        match(word):
            # Add the type of module as second data field
            case "type": self.__new_module_info["type"] = line[word_idx+1]

            case "{": self.__bracket_flag = True

            case other: IllegalOperatorException(word=word)

    # Remember to remove newline characters!!
    def __bracket_controller (self, word: str, word_idx: int, line: List) -> None:

        # May want to switch to if else here instead to ensure regex
        match(word):

            case "}": 
                self.__bracket_controller = False
                self.__new_module = False
                # Create a new node once done with current block
                self.__create_new_module_node()

            # Use regex to find all tabbed in data fields. All values within a module 
            # block must be indented. Otherwise, error
            case "\t*": # << Put regex here
                if line[word_idx+2] == None:
                    raise MissingParameterException(word=word, mod_name=self.__new_module_info["name"])
                else:
                    # +2 because of equal sign
                    self.__new_module_info["name"] = line[word_idx+2]

            case other: raise MissiongBracketException(word=word)

    def __create_new_module_node (self) -> object:
        return ModuleNode(
            name=self.__new_module_info["name"],
            mod_type=self.__new_module_info["type"],
            data=self.__new_module_info["data"]
            )
    
    def process (self):

        for string_list in self.__file_line_list:

            for string in string_list:

                string_idx = string_list.index(string)
                # First thing in a file should be the `lib` because we need to use the library
                # to valid the subclasses such as Lambda Vs CloudFunction ==> Done by Lexer

                if self.__new_module:
                    
                    if self.__bracket_flag:
                        self.__bracket_controller(word=string, word_idx=string_idx, line=string_list)
                    else:
                        self.__new_module_controller(word=string, word_idx=string_idx, line=string_list)

                else:
                    self.__keyword_controller(word=string, word_idx=string_idx, line=string_list)


class ModuleNode:

    def __init__ (self, name: str, mod_type: str, data: Dict):
        self.name = name
        self.mod_type = mod_type
        self.data = data

